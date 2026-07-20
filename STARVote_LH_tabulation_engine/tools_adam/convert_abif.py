#!/usr/bin/env python3
"""
convert_abif.py — convert between ABIF and this library's YAML ballot grid.

ABIF (Aggregated Ballot Interchange Format, by Rob Lanphier / electorama) is the
election-methods community's interchange format: one grammar for ranked AND
rated ballots. This library authors in a spreadsheet-style YAML grid instead.
The two correspond at the *ballot* layer — ABIF votelines ↔ our `ballots:` block
— so this tool bridges exactly that layer, in both directions. See the explainer:
00_start_here/scores_and_ranks/abif_format.md

    # ABIF -> tabulatable YAML (direction inferred from the .abif extension)
    python convert_abif.py testfiles/test003.abif -o test003.yaml
    python convert_abif.py test003.abif --method STAR        # -> stdout

    # YAML grid -> ABIF
    python convert_abif.py my_case.yaml -o my_case.abif
    python convert_abif.py my_case.yaml --operators          # A/5 > B/4 form

What it handles
---------------
* ABIF -> grid:
    - rated votelines (`Allie/5`)  -> a 0-5 score grid (`voting_method: STAR`)
    - ranked votelines (`A>B=C`)   -> ranked lines (`voting_method: RankedRobin`)
    - hybrid (`Allie/5 =Billy/5 >Candace/4`): the SCORES are authoritative (they
      carry the order too); `>`/`=` operators are validated and a contradiction
      (`A/5 > B/6`) is reported, not silently resolved.
    - count prefixes (`12:` / `12*`) -> weighted rows (`12 × …`).
    - ratings > 5: kept as-is with a warning (the 0-5 CLI will reject them);
      pass --rescale to linearly map the ballot set to 0-5.
* grid -> ABIF:
    - a score grid       -> rated votelines (comma form by default; `--operators`
      for the sorted `A/5 > B/4 = C/4` form).
    - ranked lines       -> ranked votelines.
    - identical ballots are aggregated into `count:` lines ("Aggregated" in ABIF).

Round-trips are stable modulo canonical formatting; `--check` tabulates the YAML
side with the LH engine so you can confirm the winner survives the conversion.

Not a full ABIF parser: it reads the ballot layer (comments `#`, metadata `{…}`
titles, counts, `>`/`=`/`,`, `/rating`, bare/`[bracketed]`/`"quoted"` names) —
enough for the electorama test corpus and everyday interchange, not the exotic
edges of the spec.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENGINE = HERE.parent / "starvote_larry_hastings.py"

_COUNT = re.compile(r"^\s*(\d+)\s*[:*]\s*(.*)$")        # ABIF count prefix: 12:  12*
_GRIDW = re.compile(r"^\s*(\d+)\s*[×xX:]\s*(.*)$")      # our grid weight: 12 ×  12:


# --------------------------------------------------------------------------- #
# ABIF parsing
# --------------------------------------------------------------------------- #
class ABIFError(ValueError):
    pass


def _tokenize_voteline(body):
    """('A/5 =B/5 >C/4') -> ([(name, rating|None), …], [op, …]) with one fewer op
    than tokens. Operators are '>', '=', ',' between consecutive candidates."""
    tokens, ops, i, n = [], [], 0, len(body)
    expect_op = False
    while i < n:
        ch = body[i]
        if ch.isspace():
            i += 1
            continue
        if expect_op:
            if ch in ">=,":
                ops.append(ch)
                expect_op = False
                i += 1
                continue
            raise ABIFError(f"expected an operator (>, =, ,) near: {body[i:][:20]!r}")
        # read a candidate token
        if ch == "[":
            j = body.find("]", i)
            if j < 0:
                raise ABIFError(f"unclosed '[' in: {body!r}")
            name, i = body[i + 1:j], j + 1
        elif ch == '"':
            j = body.find('"', i + 1)
            if j < 0:
                raise ABIFError(f"unclosed '\"' in: {body!r}")
            name, i = body[i + 1:j], j + 1
        else:
            j = i
            while j < n and body[j] not in ">=,/" and not body[j].isspace():
                j += 1
            name, i = body[i:j], j
        rating = None
        if i < n and body[i] == "/":                    # optional /rating
            j = i + 1
            while j < n and (body[j].isdigit() or body[j] == "."):
                j += 1
            raw = body[i + 1:j]
            if not raw:
                raise ABIFError(f"'/' with no rating after {name!r}")
            rating = float(raw) if "." in raw else int(raw)
            i = j
        tokens.append((name.strip(), rating))
        expect_op = True
    return tokens, ops


def parse_abif(text):
    """Return dict(kind='rated'|'ranked', candidates=[…], ballots=[…], title=str|None).
    A rated ballot is (weight, {name: rating}); a ranked ballot is (weight,
    [level, …]) where each level is a list of tied names (most preferred first)."""
    title, order, ballots = None, [], []
    kinds = set()
    for raw in text.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("{"):                    # metadata block (single line)
            m = re.search(r'"?title"?\s*[:=]\s*"([^"]*)"', stripped)
            if m:
                title = m.group(1)
            continue
        body = line.split("#", 1)[0].strip()            # trailing comment
        if not body:
            continue
        m = _COUNT.match(body)
        weight, rest = (int(m.group(1)), m.group(2).strip()) if m else (1, body)
        if not rest:
            continue
        toks, ops = _tokenize_voteline(rest)
        for name, _ in toks:
            if name and name not in order:
                order.append(name)
        rated = any(r is not None for _, r in toks)
        if rated:
            if any(r is None for _, r in toks):
                raise ABIFError(f"mixed rated/unrated candidates on one line: {rest!r}")
            # consistency check: operators must not contradict the scores
            for (na, ra), op, (nb, rb) in zip(toks, ops, toks[1:]):
                if op == ">" and not ra > rb:
                    raise ABIFError(f"'{na}/{ra} > {nb}/{rb}' contradicts the scores")
                if op == "=" and ra != rb:
                    raise ABIFError(f"'{na}/{ra} = {nb}/{rb}' contradicts the scores")
            kinds.add("rated")
            ballots.append((weight, {na: ra for na, ra in toks}))
        else:
            kinds.add("ranked")
            levels, cur = [], [toks[0][0]]
            for op, (nb, _) in zip(ops, toks[1:]):
                if op == ">":
                    levels.append(cur)
                    cur = [nb]
                else:                                   # '=' or ',' -> same level
                    cur.append(nb)
            levels.append(cur)
            ballots.append((weight, levels))
    if not ballots:
        raise ABIFError("no vote lines found")
    if len(kinds) > 1:
        raise ABIFError("file mixes rated and ranked ballots — not convertible to one grid")
    return {"kind": kinds.pop(), "candidates": order, "ballots": ballots, "title": title}


# --------------------------------------------------------------------------- #
# ABIF -> our YAML grid
# --------------------------------------------------------------------------- #
def _bracket(name):
    return f"[{name}]" if re.search(r"[\s>=,/]", name) else name


def abif_to_grid(text, method=None, rescale=False, num_winners=1):
    p = parse_abif(text)
    cands, kind = p["candidates"], p["kind"]
    lines, notes = [], []
    if kind == "rated":
        maxr = max((r for _, b in p["ballots"] for r in b.values()), default=0)
        scale = None
        if maxr > 5:
            if rescale:
                scale = maxr
                notes.append(f"rescaled 0–{int(maxr)} ratings to 0–5 (÷{maxr}×5).")
            else:
                notes.append(f"WARNING: max rating {int(maxr)} > 5 — the 0-5 CLI will "
                             "reject this file; re-run with --rescale to map to 0–5.")

        def cell(v):
            if scale:
                return str(round(v * 5 / scale))
            return str(int(v)) if float(v).is_integer() else str(v)

        lines.append(", ".join(cands))
        for w, b in p["ballots"]:
            row = ", ".join(cell(b.get(c, 0)) for c in cands)
            lines.append(f"{w} × {row}" if w != 1 else row)
        default_method = "STAR"
    else:                                               # ranked
        for w, levels in p["ballots"]:
            body = " > ".join("=".join(_bracket(c) for c in lvl) for lvl in levels)
            lines.append(f"{w} × {body}" if w != 1 else body)
        default_method = "RankedRobin"

    method = method or default_method
    out = []
    if p["title"]:
        out.append(f'election_title: "{p["title"]}"')
    out.append("# converted from ABIF by tools_adam/convert_abif.py")
    for note in notes:
        out.append(f"# {note}")
    out.append(f"voting_method: {method}")
    out.append(f"num_winners: {num_winners}")
    out.append("ballots: |-")
    out.extend(f"  {ln}" for ln in lines)
    out.append("")
    return "\n".join(out), notes


# --------------------------------------------------------------------------- #
# our YAML grid -> ABIF
# --------------------------------------------------------------------------- #
def _load_ballots_block(yaml_text):
    """Pull the raw `ballots:` block out of a YAML file without needing PyYAML
    (the block is a literal scalar we parse ourselves), plus an optional title."""
    title = None
    mt = re.search(r'^\s*election_title\s*:\s*"?([^"\n]+)"?\s*$', yaml_text, re.M)
    if mt:
        title = mt.group(1).strip().strip('"')
    m = re.search(r"^\s*ballots\s*:\s*\|.*\n((?:(?: {2,}|\t).*\n?)+)", yaml_text, re.M)
    if not m:
        raise ABIFError("no `ballots:` literal block found")
    block = m.group(1)
    indent = min(len(ln) - len(ln.lstrip())
                 for ln in block.splitlines() if ln.strip())
    return [ln[indent:] for ln in block.splitlines()], title


_MARKERS = set("-~&?%")


def grid_to_abif(yaml_text, operators=False):
    rows, title = _load_ballots_block(yaml_text)
    rows = [r.split("#", 1)[0].rstrip() for r in rows]
    rows = [r for r in rows if r.strip()]
    ranked = any(">" in r for r in rows)
    out = []
    if title:
        out.append(f'{{title: "{title}"}}')
    out.append("# converted from the YAML grid by tools_adam/convert_abif.py")

    if ranked:
        for r in rows:
            m = _GRIDW.match(r)
            w, body = (int(m.group(1)), m.group(2)) if m else (1, r)
            levels = [[c.strip() for c in lvl.split("=") if c.strip()]
                      for lvl in body.split(">")]
            abif = " > ".join("=".join(_bracket(c) for c in lvl) for lvl in levels)
            out.append(f"{w}: {abif}" if w != 1 else abif)
        return "\n".join(out) + "\n"

    # score grid: first content row is the header
    header = [c.strip() for c in rows[0].split(",")]

    def score(cell):
        cell = cell.strip()
        return 0 if (cell == "" or cell in _MARKERS) else int(cell)

    # aggregate identical ballots
    agg = {}
    order = []
    for r in rows[1:]:
        m = _GRIDW.match(r)
        w, body = (int(m.group(1)), m.group(2)) if m else (1, r)
        cells = [score(c) for c in body.split(",")]
        if len(cells) != len(header):
            raise ABIFError(f"row has {len(cells)} cells, header has {len(header)}: {r!r}")
        key = tuple(cells)
        if key not in agg:
            agg[key] = 0
            order.append(key)
        agg[key] += w

    for key in order:
        pairs = list(zip(header, key))
        if operators:                                   # sorted A/5 > B/4 = C/4
            pairs.sort(key=lambda p: -p[1])
            body = _bracket(pairs[0][0]) + f"/{pairs[0][1]}"
            for (na, sa), (nb, sb) in zip(pairs, pairs[1:]):
                body += f" {'=' if sb == sa else '>'} {_bracket(nb)}/{sb}"
        else:                                           # comma rated form
            body = ", ".join(f"{_bracket(nm)}/{sc}" for nm, sc in pairs)
        w = agg[key]
        out.append(f"{w}: {body}" if w != 1 else body)
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def _tabulate(yaml_text):
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as fh:
        fh.write(yaml_text)
        path = fh.name
    try:
        r = subprocess.run([sys.executable, str(ENGINE), path],
                           capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr
    finally:
        Path(path).unlink(missing_ok=True)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Convert between ABIF and the YAML ballot grid.")
    ap.add_argument("input", help="a .abif or .yaml/.yml file")
    ap.add_argument("-o", "--out", help="output file (default: stdout)")
    ap.add_argument("--to", choices=["abif", "yaml"],
                    help="force direction (default: inferred from the input extension)")
    ap.add_argument("--method", help="ABIF->YAML: voting_method (default: STAR for "
                    "rated, RankedRobin for ranked)")
    ap.add_argument("--num-winners", type=int, default=1)
    ap.add_argument("--rescale", action="store_true",
                    help="ABIF->YAML: linearly map ratings >5 down to 0–5")
    ap.add_argument("--operators", action="store_true",
                    help="YAML->ABIF: emit the sorted `A/5 > B/4` form instead of commas")
    ap.add_argument("--check", action="store_true",
                    help="also tabulate the YAML side with the LH engine and print the winner")
    args = ap.parse_args(argv)

    src = Path(args.input)
    text = src.read_text(encoding="utf-8")
    direction = args.to or ("yaml" if src.suffix.lower() == ".abif" else "abif")

    try:
        if direction == "yaml":                         # ABIF -> YAML
            result, notes = abif_to_grid(text, method=args.method,
                                         rescale=args.rescale, num_winners=args.num_winners)
            yaml_for_check = result
        else:                                           # YAML -> ABIF
            result = grid_to_abif(text, operators=args.operators)
            notes, yaml_for_check = [], text
    except ABIFError as e:
        print(f"convert_abif: {e}", file=sys.stderr)
        return 1

    if args.out:
        Path(args.out).write_text(result, encoding="utf-8")
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(result)
    for note in notes:
        print(f"convert_abif: {note}", file=sys.stderr)

    if args.check:
        rc, out = _tabulate(yaml_for_check)
        win = [ln for ln in out.splitlines() if "=" in ln and ("STAR" in ln or "Winner" in ln)]
        tail = "\n".join(out.strip().splitlines()[-3:])
        print(f"\nconvert_abif --check: engine exit {rc}\n{tail}", file=sys.stderr)
        return rc
    return 0


if __name__ == "__main__":
    sys.exit(main())
