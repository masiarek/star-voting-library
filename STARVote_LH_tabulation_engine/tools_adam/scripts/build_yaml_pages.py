#!/usr/bin/env python3
"""
build_yaml_pages.py — generate a browsable, EDUCATIONAL Markdown page for every
election YAML, the same way `_tabulated` mirrors and the YAML index are
generated. One page per YAML, written to `<folder>/<folder>_pages/<stem>.md`
(nested beside the source, like the `_tabulated` mirrors).

Each page carries: title · method (linked to its concept docs) · the file's own
scenario description · the ballots (with a how-to-read line and a marker legend
when markers appear) · the expected winner · the full engine report (pulled
from the `_tabulated` mirror — machine-specific file:// lines stripped) · and
auto cross-references: the folder README, topic hubs matched from the content,
the divergence-review case when methods disagree on this election, sibling
cases in the same set, the glossary, and the by-method index.

A case may also have a HAND-AUTHORED companion at `<set>/<stem>.md`, alongside
the generated `<set>/cases/cases_pages/<stem>.md`. Those stay the author's, with
one exception: a small `case-meta` block under the H1 — method, seats, expected
winners, and a link to the full generated count — which this script owns and
rebuilds from the YAML. Prose outside the markers is never touched.

Pages are GENERATED — do not edit by hand. `tests/test_yaml_pages_current.py`
fails if a page (or a companion's `case-meta` block) drifts from its
YAML/mirror. Regenerate with:

    python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py
"""
import glob
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

def _find_repo(start):
    p = os.path.dirname(os.path.abspath(start))
    while p != os.path.dirname(p):
        if os.path.isdir(os.path.join(p, "01_STAR")) and os.path.isdir(os.path.join(p, "STARVote_LH_tabulation_engine")):
            return p
        p = os.path.dirname(p)
    return os.path.dirname(os.path.abspath(start))
REPO = _find_repo(__file__)  # robust: search upward for the repo root

ROOTS = ["01_STAR", "02_STAR_Bloc", "03_STAR_PR", "04_Approval",
         "05_Ranked_Robin", "method_comparisons", "06_Other"]

GENERATED_SUFFIXES = ("_tabulated", "_generated", "_pages")

# --- method → (display name, concept-docs path relative to repo root) --------
METHOD_DOCS = {
    "star":        ("STAR (single winner)", "01_STAR/01_Learn"),
    "approval":    ("Approval Voting", "04_Approval/01_Learn"),
    "rankedrobin": ("Ranked Robin (RCV-RR / Copeland)", "05_Ranked_Robin/01_Learn"),
    "rcv_irv":     ("RCV-IRV (Instant Runoff)", "06_Other/RCV_IRV/concepts"),
    "bloc":        ("Bloc STAR (multi-winner, majoritarian)", "03_STAR_PR/01_Learn"),
    "sss":         ("Sequentially Spent Score (proportional STAR)", "03_STAR_PR/01_Learn"),
    "rrv":         ("Reweighted Range Voting (proportional STAR)", "03_STAR_PR/01_Learn"),
    "allocated":   ("Allocated Score (proportional STAR)", "03_STAR_PR/01_Learn"),
    "stv":         ("STV (proportional, ranked ballots)", "03_STAR_PR/01_Learn"),
}
METHOD_ALIASES = {
    "rcv_rr": "rankedrobin", "copeland": "rankedrobin", "consensus": "rankedrobin",
    "rr": "rankedrobin", "rcv": "rcv_irv", "irv": "rcv_irv",
    "approve": "approval", "av": "approval", "approval_voting": "approval",
    "approval_single_winner": "approval", "approval_multi_winner": "approval",
}

# --- keyword → topic hub / concept page (relative to repo root) --------------
TOPIC_LINKS = [
    (r"center[ _-]?squeeze", "Center squeeze (topic hub)", "07_Concepts/topics/center_squeeze/README.md"),
    (r"monotonic",           "Monotonicity (topic hub)", "07_Concepts/topics/monotonicity/README.md"),
    (r"summab",              "Summability (topic hub)", "07_Concepts/topics/summability/README.md"),
    (r"condorcet|cycle",     "Condorcet efficiency (topic hub)", "07_Concepts/topics/condorcet/README.md"),
    (r"\btie|lot[ _]order|lot[ _]number|dead[ _]rung|tiebreak", "Ties & tie-breaking (topic hub)", "07_Concepts/topics/ties/README.md"),
    (r"tie[ _-]?break|dead[ _]rung", "The tie-breaking ladder (full chain)", "01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md"),
    (r"quorum",              "Quorum", "07_Concepts/topics/quorum.md"),
    (r"split|spoiler",       "Vote splitting (worked set)", "method_comparisons/split_voting/README.md"),
    (r"runoff",              "Runoff reversal (worked set)", "01_STAR/02_Examples/runoff_overturns_leader/README.md"),
    (r"abstention|marker|blank|spoiled", "Ballot & terminology basics", "07_Concepts/topics/ballot_and_terminology_basics.md"),
    (r"black[ _]curtain",    "The Black Curtain (worked set)", "method_comparisons/black_curtain/README.md"),
    (r"exhaust",             "Exhausted ballots (conversation)", "06_Other/RCV_IRV/concepts/exhausted_ballots_301.md"),
]

GLOSSARY = "07_Concepts/GLOSSARY.md"
INDEX = "07_Concepts/YAML_test_case_index/README.md"

MARKER_LEGEND = ("`-` blank · `~` race abstention · `&` candidate abstention · "
                 "`?` spoiled · `%` spoiled+reissued — all tabulate as 0 "
                 "(reported honestly)")

# Widest parameter line we'll allow before falling back to block style.
PARAM_LINE_WIDTH = 88


def _dump_param(key, value):
    """One `key: value` chunk, written the way the cases themselves write it.

    A scalar-only list stays inline (`lot_numbers: [A, B, C]`) — one dash per
    line was noise the source files never had. Two guards: scalars are dumped
    on their own so a params block with no collection in it can't collapse into
    a flow map (`{bv_election_id: g3f7r2, ...}`), and a chunk too wide for the
    fence falls back to block style, which beats a flow list wrapped mid-list.
    """
    def _dump(flow_style):
        return yaml.safe_dump({key: value}, sort_keys=False, allow_unicode=True,
                              default_flow_style=flow_style, width=10 ** 6).rstrip()

    if not isinstance(value, (list, tuple, dict)):
        return _dump(False)
    inline = _dump(None)
    if any(len(line) > PARAM_LINE_WIDTH for line in inline.splitlines()):
        return _dump(False)
    return inline


# --------------------------------------------------------------------------- #
# Extraction helpers (schema-tolerant: flat files and nested BV imports)
# --------------------------------------------------------------------------- #
def _find_first(node, keys):
    """Depth-first search for the first value under any of `keys`."""
    if isinstance(node, dict):
        for k in keys:
            if k in node and node[k] is not None:
                return node[k]
        for v in node.values():
            found = _find_first(v, keys)
            if found is not None:
                return found
    elif isinstance(node, list):
        for v in node:
            found = _find_first(v, keys)
            if found is not None:
                return found
    return None


def _norm_method(raw):
    m = re.split(r"[#\s]", str(raw or "STAR").strip())[0].strip().lower()
    return METHOD_ALIASES.get(m, m)


def _ballot_kind(ballots_text, method):
    clean = "\n".join(ln.split("#")[0] for ln in str(ballots_text).splitlines())
    if ">" in clean:
        return "ranked"
    if method == "approval":
        return "approval"
    return "score"

HOW_TO_READ = {
    "score":    "Row 1 = candidate names; each later row is one voter's 0–5 scores "
                "(a `N ×` prefix = N identical ballots).",
    "approval": "Row 1 = candidate names; each later row is one voter's approvals "
                "(`1` = approve, `0`/blank = not approved).",
    "ranked":   "Each row is one voter's ranking, most-preferred first "
                "(`N:` prefix = N identical ballots).",
}


def _mirror_path(yaml_path):
    d = os.path.dirname(yaml_path)
    stem = os.path.splitext(os.path.basename(yaml_path))[0]
    mirror_dir = os.path.join(d, os.path.basename(d) + "_tabulated")
    primary = os.path.join(mirror_dir, stem + "_tabulated.txt")
    if os.path.exists(primary):
        return primary
    # Non-STAR engines write method-tagged mirrors (<stem>_RANGE_tabulated.txt,
    # <stem>_321_tabulated.txt, ...) so they never collide with a STAR mirror.
    # When no primary exists, the tagged mirror IS the engine report.
    tagged = sorted(
        glob.glob(os.path.join(glob.escape(mirror_dir), glob.escape(stem) + "_*_tabulated.txt"))
    )
    return tagged[0] if tagged else primary


def _mirror_report(yaml_path):
    """The engine report from the _tabulated mirror: the section after the
    TABULATION RESULTS divider (composed mirrors) or the whole file (plain
    mirrors). Machine-specific file:// lines are stripped."""
    mp = _mirror_path(yaml_path)
    if not os.path.exists(mp):
        return None
    text = open(mp, encoding="utf-8").read()
    if "TABULATION RESULTS" in text:
        text = text.split("TABULATION RESULTS", 1)[1]
        text = text.split("\n", 2)[2] if text.count("\n") >= 2 else text
    lines = [ln for ln in text.splitlines() if "file:///" not in ln]
    # The full render opens with the title banner and the (indented) scenario
    # description — the page already shows both, so trim that echo: drop the
    # leading "=== title ===" line plus any indented/blank lines that follow.
    out, started = [], False
    for i, ln in enumerate(lines):
        if not started:
            if re.match(r"^=== .* ===\s*$", ln):
                continue
            if not ln.strip() or ln.startswith("  "):
                continue
            started = True
        out.append(ln)
    return "\n".join(out).strip("\n")


# Report sections that are audit detail, not the first-read lesson: the abstract
# preference matrix, the Condorcet line that references it, and the score-count
# table. For a newcomer these ambush the page (the matrix leads the raw report);
# we fold them so the count — scoring round → automatic runoff → winner — leads.
_SECTION_BOUNDARY = re.compile(r"^(?:---\s+.+?\s+---\s*$|\[[^\]]+\])")
_FOLD_SECTION = re.compile(r"Preference\)?\s*Matrix|Condorcet|Score Distribution", re.I)


def _split_report(report):
    """Split the engine report into (lead, audit): the beginner-facing count
    (scoring round, automatic runoff, winner) vs the folded detail (preference
    matrix, Condorcet, score distribution). `audit` is "" when none of those
    sections appear — non-STAR reports (IRV rounds, RR pairwise, …) pass through
    unfolded."""
    segments, header, block = [], None, []
    for ln in report.split("\n"):
        if _SECTION_BOUNDARY.match(ln):
            if block or header is not None:
                segments.append((header, block))
            header, block = ln, [ln]
        else:
            block.append(ln)
    if block or header is not None:
        segments.append((header, block))

    lead, audit = [], []
    for hdr, blk in segments:
        (audit if hdr and _FOLD_SECTION.search(hdr) else lead).append(blk)

    def _join(blocks):
        return "\n\n".join("\n".join(b).strip("\n") for b in blocks).strip("\n")

    if not audit:
        return report.strip("\n"), ""
    return _join(lead), _join(audit)


def _rel(target_repo_relative, page_dir):
    return os.path.relpath(os.path.join(REPO, target_repo_relative),
                           page_dir).replace(os.sep, "/")


def _folder_readme(folder):
    for fn in sorted(os.listdir(folder)):
        if fn.lower().startswith("readme") and fn.lower().endswith(".md"):
            return fn
    return None


def _divergence_case(stem):
    root = os.path.join(REPO, "method_comparisons", "divergence_review", "cases")
    if not os.path.isdir(root):
        return None
    for dirpath, _dirs, files in os.walk(root):
        if stem + ".md" in files:
            return os.path.relpath(os.path.join(dirpath, stem + ".md"), REPO)
    return None


# --------------------------------------------------------------------------- #
# Case facts — one source of truth for the metadata line
# --------------------------------------------------------------------------- #
# Both the generated page and the managed block on its hand-authored companion
# print the same "Method · seats · expected winners" line, so it is built once
# here. Deriving it twice is exactly how the companion pages drifted in the
# first place.
def _case_facts(data):
    """(display name, docs path, seats, winners|None, expected_winners|None, lot)."""
    method = _norm_method(_find_first(data, ["voting_method"]))
    seats = _find_first(data, ["num_winners", "seats"]) or 1
    winners = None
    ew = data.get("expected_winners") if isinstance(data, dict) else None
    if isinstance(ew, list) and ew:
        winners = [str(w) for w in ew]
    else:
        er = _find_first(data, ["expected_results"])
        w = _find_first(er, ["winners", "elected"]) if er is not None else None
        if isinstance(w, list) and w:
            winners = [str(x) for x in w]
    lot = data.get("lot_numbers") if isinstance(data, dict) else None
    disp, docs = METHOD_DOCS.get(method, (str(method), "07_Concepts"))
    return disp, docs, seats, winners, ew, lot


def _meta_line(disp, docs, seats, winners, from_dir):
    seat_txt = "1 seat" if str(seats) == "1" else f"{seats} seats"
    return (f"**Method:** [{disp}]({_rel(docs, from_dir)}) · **{seat_txt}**"
            + (f" · **Expected winner{'s' if winners and len(winners) > 1 else ''}:** "
               + ", ".join(winners) if winners else ""))


# --------------------------------------------------------------------------- #
# Page rendering
# --------------------------------------------------------------------------- #
def render(yaml_path, siblings):
    rel_src = os.path.relpath(yaml_path, REPO).replace(os.sep, "/")
    folder = os.path.dirname(yaml_path)
    stem = os.path.splitext(os.path.basename(yaml_path))[0]
    page_dir = os.path.join(folder, os.path.basename(folder) + "_pages")

    data = yaml.safe_load(open(yaml_path, encoding="utf-8").read())
    if not isinstance(data, (dict, list)):
        return None
    ballots = _find_first(data, ["ballots"])
    if ballots is None:
        return None
    title = _find_first(data, ["election_title", "title"]) or stem
    desc = _find_first(data, ["scenario_description", "election_description",
                              "race_description"])
    disp, docs, seats, winners, ew, lot = _case_facts(data)
    kind = _ballot_kind(ballots, _norm_method(_find_first(data, ["voting_method"])))
    ballots_text = str(ballots).rstrip("\n")
    has_markers = bool(re.search(r"[~&?%]|(^|,)\s*-\s*(,|$)", ballots_text, re.M))

    L = []
    # Keep generated case dumps out of the site's search index: they were 44%
    # of a 9 MB search_index.json and crowded the teaching pages out of
    # results. The pages stay fully published and linkable — just unindexed.
    # (Material for MkDocs reads this front matter; GitHub renders it as a
    # small metadata box, which is acceptable on a generated page.)
    L.append("---")
    L.append("search:")
    L.append("  exclude: true")
    L.append("---")
    L.append("")
    L.append(f"# {title}")
    L.append("")
    L.append(f"*Generated from [`{os.path.basename(yaml_path)}`](../{os.path.basename(yaml_path)}) "
             f"— do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*")
    L.append("")
    L.append(_meta_line(disp, docs, seats, winners, page_dir))
    # BV-backed case -> the house live-results lead line (CLAUDE.md rule).
    bv_id = data.get("bv_election_id") if isinstance(data, dict) else None
    if not bv_id and isinstance(data, dict):
        m = re.match(r"^bv\w+_([a-z0-9]{6})_", os.path.basename(yaml_path))
        bv_id = m.group(1) if m else None
    # The test id rides along in the same parenthetical: it identifies this case
    # in the BV tracker, and a section of its own for one machine id was thin.
    bv_test = data.get("bv_test_id") if isinstance(data, dict) else None
    if bv_id:
        ids = f"election `{bv_id}`" + (f" · test `{bv_test}`" if bv_test else "")
        L.append("")
        L.append(f"**▶ Live on BetterVoting:** [vote](https://bettervoting.com/{bv_id}) · "
                 f"**[results ↗](https://bettervoting.com/{bv_id}/results)** ({ids}).")
    if lot:
        L.append("")
        L.append(f"**Official tie-break (lot) order:** {' > '.join(str(c) for c in lot)} "
                 f"— consulted only if every deterministic tiebreaker stays tied "
                 f"([how the ladder works]({_rel('01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md', page_dir)})).")
    L.append("")
    if desc:
        L.append("## Scenario")
        L.append("")
        L.append(str(desc).strip())
        L.append("")
    # Machine-readable parameters, verbatim from the YAML — but only the keys the
    # page hasn't already said in prose. Method, seats and the expected winners
    # are in the metadata line under the title; the lot order and the BV election
    # id each have their own bolded line. Re-printing those as YAML was pure
    # restatement — on 43% of the cases it was the *entire* block — and the echo
    # is what made the page read as two halves rather than one file. What's left
    # here is the part no sentence above covers (blocs, eligible_voters, quorum,
    # and a test id whose BV line never fired); the raw `.yaml` is one click away
    # in the byline. Each key is dropped only when the line that would carry it
    # actually rendered, so a case that lacks the BV line keeps its ids here.
    said_in_prose = {"voting_method", "num_winners"}
    if isinstance(ew, list) and ew:      # the metadata line is showing this list
        said_in_prose.add("expected_winners")
    if lot:
        said_in_prose.add("lot_numbers")
    if bv_id:
        said_in_prose.add("bv_election_id")
        if bv_test:
            said_in_prose.add("bv_test_id")
    params = {}
    if isinstance(data, dict):
        for key in ("voting_method", "num_winners", "expected_winners",
                    "lot_numbers", "eligible_voters", "quorum", "blocs",
                    "bv_election_id", "bv_test_id"):
            if key in data and key not in said_in_prose:
                params[key] = data[key]
    if params:
        L.append("## Parameters (from the YAML)")
        L.append("")
        L.append("```yaml")
        L.append("\n".join(_dump_param(k, v) for k, v in params.items()))
        L.append("```")
        L.append("")
    L.append("## Ballots")
    L.append("")
    L.append(HOW_TO_READ[kind])
    if has_markers:
        L.append("")
        L.append(f"Markers on these ballots: {MARKER_LEGEND}.")
    L.append("")
    L.append("```text")
    L.append(ballots_text)
    L.append("```")
    L.append("")
    report = _mirror_report(yaml_path)
    L.append("## What the engine says")
    L.append("")
    if report:
        mirror_rel = os.path.relpath(_mirror_path(yaml_path), page_dir).replace(os.sep, "/")
        lead, audit = _split_report(report)
        if audit:
            # Lead with the count; then the full audit inline (no collapsing — a
            # teaching page reads better with nothing hidden).
            L.append("The count, step by step — the rounds and how the winner is "
                     "reached:")
            L.append("")
            L.append("```text")
            L.append(lead)
            L.append("```")
            L.append("")
            L.append("### Full audit — preference matrix, Condorcet, and score distribution")
            L.append("")
            L.append("```text")
            L.append(audit)
            L.append("```")
            L.append("")
            L.append(f"Everything in one file: the [`_tabulated` mirror]({mirror_rel}) "
                     f"(regenerated on every run; every analysis forced on).")
        else:
            L.append(f"Full report from the [`_tabulated` mirror]({mirror_rel}) "
                     f"(regenerated on every run; every analysis forced on):")
            L.append("")
            L.append("```text")
            L.append(report)
            L.append("```")
    else:
        L.append("*(No `_tabulated` mirror found — run the file once to generate it.)*")
    L.append("")
    L.append("Run it yourself:")
    L.append("")
    L.append("```bash")
    L.append(f"python STARVote_LH_tabulation_engine/starvote_larry_hastings.py {rel_src}")
    L.append("```")
    L.append("")

    # --- cross-references ---------------------------------------------------
    refs = []
    readme = _folder_readme(folder)
    if readme:
        refs.append(f"[This set's lesson (README)](../{readme}) — the hand-written "
                    f"teaching context for every case in this folder")
    div = _divergence_case(stem)
    if div:
        refs.append(f"[Methods disagree on this election]({_rel(div, page_dir)}) — "
                    f"its entry in the divergence review ledger")
    hay = " ".join([stem, str(title), str(desc or "")]).lower()
    seen = set()
    for pat, label, target in TOPIC_LINKS:
        if re.search(pat, hay) and target not in seen and os.path.exists(os.path.join(REPO, target)):
            seen.add(target)
            refs.append(f"[{label}]({_rel(target, page_dir)})")
    refs.append(f"[Glossary]({_rel(GLOSSARY, page_dir)}) · "
                f"[all cases by method]({_rel(INDEX, page_dir)})")
    L.append("## See also")
    L.append("")
    for r in refs:
        L.append(f"- {r}")
    others = [s for s in siblings if s != os.path.basename(yaml_path)]
    if others:
        L.append("")
        L.append("More cases in this set: "
                 + " · ".join(f"[{os.path.splitext(s)[0]}]({os.path.splitext(s)[0]}.md)"
                              for s in others))
    L.append("")
    return "\n".join(L)


# --------------------------------------------------------------------------- #
# Build
# --------------------------------------------------------------------------- #
def expected_pages():
    """Return {absolute page path: content} for every election YAML."""
    pages = {}
    for root in ROOTS:
        base = os.path.join(REPO, root)
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames
                           if not d.endswith(GENERATED_SUFFIXES) and d != "img"
                           and not d.endswith("_tabulation_engine")]
            ymls = sorted(f for f in filenames if f.endswith((".yaml", ".yml")))
            for fn in ymls:
                path = os.path.join(dirpath, fn)
                try:
                    content = render(path, ymls)
                except Exception as e:      # unparsable file: skip, warn
                    print(f"  ! skipped {os.path.relpath(path, REPO)}: {e}")
                    continue
                if content is None:
                    continue
                page_dir = os.path.join(dirpath, os.path.basename(dirpath) + "_pages")
                pages[os.path.join(page_dir, os.path.splitext(fn)[0] + ".md")] = content
    return pages


def existing_pages():
    found = {}
    for root in ROOTS:
        base = os.path.join(REPO, root)
        for dirpath, _dirs, filenames in os.walk(base):
            if os.path.basename(dirpath).endswith("_pages"):
                for fn in filenames:
                    if fn.endswith(".md"):
                        p = os.path.join(dirpath, fn)
                        found[p] = open(p, encoding="utf-8").read()
    return found


def check():
    """Return (stale_or_missing, orphans) page paths."""
    want, have = expected_pages(), existing_pages()
    stale = [p for p, c in want.items() if have.get(p) != c]
    orphans = [p for p in have if p not in want]
    return stale, orphans


# --------------------------------------------------------------------------- #
# Companion pages — the managed metadata block
# --------------------------------------------------------------------------- #
# A case may have TWO pages: the generated one under `<set>/cases/cases_pages/`,
# and a hand-authored narrative page at `<set>/<stem>.md`. Only the generated one
# ever carried the method/seats/winners line, so a reader who landed on the
# companion saw prose and no parameters — and had no link to the page that had
# them. Rather than retype the facts into 50 hand-authored files (where they go
# stale the first time a YAML changes), the companion gets a small block that
# this script owns, delimited by HTML comments. Everything outside the markers
# is the author's; everything inside is regenerated from the YAML.
COMPANION_START = ("<!-- case-meta:start — managed by build_yaml_pages.py; "
                   "edit the YAML, not these lines -->")
COMPANION_END = "<!-- case-meta:end -->"
_COMPANION_RE = re.compile(re.escape("<!-- case-meta:start") + r".*?"
                           + re.escape(COMPANION_END) + r"\n?", re.S)


def _companion_path(yaml_path):
    """The hand-authored page shadowing this case (`<set>/<stem>.md`), if any."""
    folder = os.path.dirname(yaml_path)
    stem = os.path.splitext(os.path.basename(yaml_path))[0]
    p = os.path.join(os.path.dirname(folder), stem + ".md")
    return p if os.path.isfile(p) else None


def companion_block(yaml_path):
    """(companion path, managed block) for a case with a companion, else None."""
    comp = _companion_path(yaml_path)
    if not comp:
        return None
    data = yaml.safe_load(open(yaml_path, encoding="utf-8").read())
    if not isinstance(data, (dict, list)) or _find_first(data, ["ballots"]) is None:
        return None
    disp, docs, seats, winners, _ew, _lot = _case_facts(data)
    folder = os.path.dirname(yaml_path)
    stem = os.path.splitext(os.path.basename(yaml_path))[0]
    comp_dir = os.path.dirname(comp)
    page = os.path.relpath(os.path.join(folder, os.path.basename(folder) + "_pages",
                                        stem + ".md"), comp_dir).replace(os.sep, "/")
    line = _meta_line(disp, docs, seats, winners, comp_dir) + f" · [full count →]({page})"
    return comp, "\n".join([COMPANION_START, line, COMPANION_END])


def apply_companion_block(text, block):
    """Insert or refresh the managed block directly under the page's H1."""
    if _COMPANION_RE.search(text):
        return _COMPANION_RE.sub(lambda _m: block + "\n", text, count=1)
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("# "):
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            return "\n".join(lines[:i + 1] + ["", block, ""] + lines[j:])
    return block + "\n\n" + text          # no H1: put it up top rather than skip


def expected_companions():
    """{absolute companion path: managed block} for every case that has one."""
    blocks, seen = {}, {}
    for root in ROOTS:
        base = os.path.join(REPO, root)
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames
                           if not d.endswith(GENERATED_SUFFIXES) and d != "img"
                           and not d.endswith("_tabulation_engine")]
            for fn in sorted(filenames):
                if not fn.endswith((".yaml", ".yml")):
                    continue
                path = os.path.join(dirpath, fn)
                try:
                    got = companion_block(path)
                except Exception as e:                     # unparsable: skip, warn
                    print(f"  ! skipped companion for {os.path.relpath(path, REPO)}: {e}")
                    continue
                if not got:
                    continue
                comp, block = got
                if comp in seen:                           # two cases, one companion
                    print(f"  ! {os.path.relpath(comp, REPO)} is claimed by both "
                          f"{os.path.basename(seen[comp])} and {fn}; left alone")
                    blocks.pop(comp, None)
                    continue
                seen[comp] = path
                blocks[comp] = block
    return blocks


def check_companions():
    """Companion pages whose managed block is missing or out of date."""
    return [p for p, block in expected_companions().items()
            if apply_companion_block(open(p, encoding="utf-8").read(), block)
            != open(p, encoding="utf-8").read()]


def main():
    want = expected_pages()
    written = 0
    for p, content in sorted(want.items()):
        os.makedirs(os.path.dirname(p), exist_ok=True)
        if not os.path.exists(p) or open(p, encoding="utf-8").read() != content:
            open(p, "w", encoding="utf-8").write(content)
            written += 1
    removed = 0
    for p in existing_pages():
        if p not in want:
            os.remove(p)
            removed += 1
    print(f"yaml-pages: {len(want)} pages ({written} written/updated, {removed} orphan(s) removed)")

    companions = expected_companions()
    touched = 0
    for p, block in sorted(companions.items()):
        cur = open(p, encoding="utf-8").read()
        new = apply_companion_block(cur, block)
        if new != cur:
            open(p, "w", encoding="utf-8").write(new)
            touched += 1
    print(f"case-meta blocks: {len(companions)} companion page(s) ({touched} updated)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
