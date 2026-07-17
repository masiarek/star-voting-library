#!/usr/bin/env python3
"""
check_repo_hygiene.py — warn about misplaced / junk files.

The recurring problem: pasting screenshots or BetterVoting exports lands generic
names in the wrong place (PyCharm drops `img_5.png` into a folder root; BV exports
arrive as `Ballot Data ... .json`). `.gitignore` keeps those out of commits, but
silent ignoring is risky — a *real* screenshot pasted as `img_3.png` would vanish
unnoticed. So this script scans the working tree (ignored files included) and
**warns** with where each file should actually go.

It does NOT delete or move anything — it just tells you. Run it directly, or let
the pre-commit hook run it (warn-only; it never blocks a commit).

    python STARVote_LH_tabulation_engine/tools_adam/scripts/check_repo_hygiene.py
"""
import os
import re
import sys

def _find_repo(start):
    p = os.path.dirname(os.path.abspath(start))
    while p != os.path.dirname(p):
        if os.path.isdir(os.path.join(p, "01_STAR")) and os.path.isdir(os.path.join(p, "STARVote_LH_tabulation_engine")):
            return p
        p = os.path.dirname(p)
    return os.path.dirname(os.path.abspath(start))
REPO = _find_repo(__file__)  # robust: search upward for the repo root

# Directories we never police (raw staging, generated, vendored, caches).
SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__",
             "_demo_dropbox", ".idea", ".claude", ".junie",
             "site"}  # mkdocs build output (mirrors the whole repo)


def _skip(rel):
    parts = rel.split(os.sep)
    return any(p in SKIP_DIRS for p in parts) or "_tabulated" in rel or "_generated" in rel or "_tabulation_engine" in rel


# Each rule: (compiled regex on the basename, human message with where it belongs).
RULES = [
    (re.compile(r"(?i)^(img|image)[ _-]?\d+\.png$"),
     "generic paste image — BV screenshots belong in an `img/` subfolder, renamed "
     "`<bv_id>_<what>.png` (e.g. img/r2pvc9_result_bars.png)."),
    (re.compile(r"(?i)^screen ?shot.*\.png$"),
     "raw screenshot name — move into the case's `img/` subfolder and rename "
     "`<bv_id>_<what>.png`."),
    (re.compile(r"(?i)^ballot data.*\.json$"),
     "raw BetterVoting export drop — convert/rename to the case's "
     "`<descriptor>_<bvid>_bv_export.json`, or delete if it's a stray."),
    (re.compile(r"(?i).* - copy.*"),
     "looks like a duplicated file (\" - Copy\") — rename or delete."),
    (re.compile(r"(?i)^untitled.*"),
     "placeholder name (\"Untitled…\") — rename to something meaningful or delete."),
]


def scan():
    hits = []
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        rel_dir = os.path.relpath(dirpath, REPO)
        if rel_dir != "." and _skip(rel_dir):
            continue
        for fn in filenames:
            for rx, msg in RULES:
                if rx.match(fn):
                    rel = os.path.normpath(os.path.join(rel_dir, fn))
                    hits.append((rel, msg))
                    break
    hits.sort()
    return hits


# --------------------------------------------------------------------------- #
# Relative-link checker: every [text](relative/path) in a tracked .md must
# resolve. Folder reorganizations silently break these; this catches them.
# (External http(s)/mailto links and pure #anchors are not checked.)
# --------------------------------------------------------------------------- #
MD_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
_EXTERNAL = re.compile(r"(?i)^\s*(https?:|mailto:|#)")
_FENCED = re.compile(r"```.*?```", re.S)
_INLINE_CODE = re.compile(r"`[^`\n]*`")


def check_links():
    """Return sorted [(md_file, raw_link)] for every relative link that does
    not resolve to an existing file or directory."""
    from urllib.parse import unquote
    broken = []
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        rel_dir = os.path.relpath(dirpath, REPO)
        if rel_dir != "." and _skip(rel_dir):
            continue
        for fn in filenames:
            if not fn.lower().endswith(".md"):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.normpath(os.path.join(rel_dir, fn))
            try:
                text = open(full, encoding="utf-8").read()
            except OSError:
                continue
            # Links inside code blocks / inline code are examples, not links.
            text = _INLINE_CODE.sub("", _FENCED.sub("", text))
            for m in MD_LINK.finditer(text):
                raw = m.group(1).strip()
                if _EXTERNAL.match(raw):
                    continue
                target = raw.split()[0].strip("<>")     # drop optional "title"
                target = target.split("#")[0]           # drop #fragment
                if not target:
                    continue
                # 'REPLACE_*' basenames are deliberate placeholders (e.g. a
                # screenshot not yet captured) — skip, don't report.
                if os.path.basename(target).startswith("REPLACE_"):
                    continue
                p = os.path.normpath(
                    os.path.join(dirpath, unquote(target).replace("/", os.sep)))
                if not os.path.exists(p):
                    broken.append((rel, raw))
    return sorted(set(broken))


# --------------------------------------------------------------------------- #
# Description quality gate: every teaching YAML must carry a real
# scenario_description — it is the educational prose on that file's generated
# page. Missing, placeholder ("tbd"), or one-liner-thin descriptions are the
# difference between a lesson and a bare data file.
# --------------------------------------------------------------------------- #
TEACHING_ROOTS = ["01_STAR", "02_STAR_Bloc", "03_STAR_PR", "04_Approval",
                  "05_Ranked_Robin", "method_comparisons", "06_Other"]
MIN_DESCRIPTION_CHARS = 80
PLACEHOLDER = re.compile(r"^\s*(tbd|todo|fixme|xxx|\?+|self-explanatory\b.*)\s*$",
                         re.I | re.S)


def _yaml_teaching_files():
    for root in TEACHING_ROOTS:
        base = os.path.join(REPO, root)
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames
                           if d not in SKIP_DIRS
                           and not d.endswith(("_tabulated", "_generated", "_pages", "_tabulation_engine"))]
            for fn in sorted(filenames):
                if fn.endswith((".yaml", ".yml")):
                    yield os.path.join(dirpath, fn)


def _find_key(node, keys):
    if isinstance(node, dict):
        for k in keys:
            if node.get(k):
                return node[k]
        for v in node.values():
            r = _find_key(v, keys)
            if r:
                return r
    elif isinstance(node, list):
        for v in node:
            r = _find_key(v, keys)
            if r:
                return r
    return None


def check_descriptions():
    """Return [(file, problem)] for teaching YAMLs with weak/no descriptions."""
    try:
        import yaml as _yaml
    except ImportError:  # pragma: no cover
        return []
    bad = []
    for path in _yaml_teaching_files():
        rel = os.path.relpath(path, REPO)
        try:
            data = _yaml.safe_load(open(path, encoding="utf-8").read())
        except Exception:
            continue        # malformed YAML is the negative suite's business
        if not isinstance(data, (dict, list)):
            continue
        if _find_key(data, ["ballots"]) is None:
            continue        # not an election file
        desc = _find_key(data, ["scenario_description", "election_description",
                                "race_description"])
        text = str(desc).strip() if desc else ""
        if not text:
            bad.append((rel, "no scenario_description — the generated page has no lesson"))
        elif PLACEHOLDER.match(text):
            bad.append((rel, f"placeholder description ({text[:20]!r})"))
        elif len(text) < MIN_DESCRIPTION_CHARS:
            bad.append((rel, f"description too thin ({len(text)} chars < "
                             f"{MIN_DESCRIPTION_CHARS}) — say what it shows and "
                             f"what to look for"))
        if not _find_key(data, ["election_title", "title"]):
            bad.append((rel, "no election_title"))
    return sorted(bad)


# --------------------------------------------------------------------------- #
# Terminology linter: mechanical enforcement of the house canon (CLAUDE.md).
# Precision over recall — every rule here should be a near-certain mistake.
# --------------------------------------------------------------------------- #
TERM_RULES = [
    (re.compile(r"\bBuckling\b"),
     "misspelling: the method is 'Bucklin'"),
    (re.compile(r"\bCond(?:ercet|orect|orcert)\b", re.I),
     "misspelling: 'Condorcet'"),
    (re.compile(r"\bEqual Preference\b"),
     "house canon: the runoff bucket is 'Equal Support' (the aka is documented "
     "once in GLOSSARY.md, not used as a lead term)"),
    (re.compile(r"\bRCV\b(?!-IRV|-RR)(?=.*(?:eliminat|exhaust|non-?monoton|center[ -]squeez|squeez))", re.I),
     "precision: center squeeze / exhausted ballots / non-monotonicity are "
     "IRV-specific — say 'RCV-IRV' or 'IRV', not bare 'RCV'"),
]
# Files that DISCUSS or QUOTE the wrong usage on purpose (the canon statement
# itself, the naming debate, verbatim false claims). Everything else can
# suppress a single deliberate line with the marker: terminology-ok
TERM_SKIP_FILES = {"GLOSSARY.md", "TIPS_terminology.md", "CLAUDE.md", "AGENTS.md",
                   "rcv_irv_false_claims.md", "RCV_or_IRV_whats_the_right_word.md",
                   "RCV-IRV-confusing-name.md"}


def check_terminology():
    """Return [(file, lineno, message)] for house-canon violations in
    hand-written .md files and YAML descriptions."""
    hits = []
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS
                       and not d.endswith(("_tabulated", "_generated", "_pages"))
                       and d not in ("divergence_review", "YAML_test_case_index")]
        for fn in filenames:
            if not fn.endswith((".md", ".yaml", ".yml")) or fn in TERM_SKIP_FILES:
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, REPO)
            try:
                lines = open(path, encoding="utf-8").read().splitlines()
            except OSError:
                continue
            for i, ln in enumerate(lines, 1):
                if "terminology-ok" in ln:      # deliberate, reviewed usage
                    continue
                # Quoted 'RCV' / "RCV" is someone's usage under discussion,
                # not our own claim — exempt it from the precision rule.
                scrubbed = re.sub(r"[\"'“”‘’]RCV[.,]?[\"'“”‘’]", "QUOTEDRCV", ln)
                for rx, msg in TERM_RULES:
                    if rx.search(scrubbed):
                        hits.append((rel, i, msg))
    return sorted(hits)


# --------------------------------------------------------------------------- #
# BV-case completeness: every BV-backed election YAML should have a sibling .md
# (its write-up page). The registry TRACKS the md path but leaves it blank when
# absent — this gate makes that self-verifying, so a promoted case can't ship
# without its page. "BV-backed" mirrors build_bv_registry.py's qualification:
# a `bv_test_id`/`bv_election_id` field, a `bv…` filename, or a frozen
# `_bv_export.json` sibling.
# --------------------------------------------------------------------------- #
_BV_FN = re.compile(r"^bv\d", re.I)


def check_bv_case_md():
    """Return [(yaml_rel, why)] for BV-backed YAMLs missing their sibling .md."""
    try:
        import yaml as _yaml
    except ImportError:  # pragma: no cover
        return []
    missing = []
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        rel_dir = os.path.relpath(dirpath, REPO)
        if rel_dir != "." and _skip(rel_dir):
            continue
        if "2_negative" in rel_dir or "negative" in rel_dir:
            continue                       # negative fixtures aren't cases
        for fn in filenames:
            if not fn.endswith((".yaml", ".yml")):
                continue
            stem = os.path.join(dirpath, fn.rsplit(".", 1)[0])
            has_field = False
            try:
                data = _yaml.safe_load(open(os.path.join(dirpath, fn), encoding="utf-8"))
                has_field = isinstance(data, dict) and bool(
                    data.get("bv_test_id") or data.get("bv_election_id"))
            except Exception:
                pass
            bv_backed = (has_field or _BV_FN.match(fn)
                         or os.path.exists(stem + "_bv_export.json"))
            if not bv_backed:
                continue
            # A case is documented by a same-stem sibling `<stem>.md`, OR the
            # folder's generated page `<folder>_pages/<stem>.md`.
            base = fn.rsplit(".", 1)[0]
            pages_md = os.path.join(dirpath,
                                    os.path.basename(dirpath) + "_pages", base + ".md")
            if not (os.path.exists(stem + ".md") or os.path.exists(pages_md)):
                rel = os.path.relpath(os.path.join(dirpath, fn), REPO)
                missing.append((rel, "BV-backed case has no write-up page "
                                     f"(neither {base}.md nor {os.path.basename(dirpath)}"
                                     f"_pages/{base}.md)"))
    return sorted(missing)


# --------------------------------------------------------------------------- #
# Index completeness: some folders keep a README that is meant to be an
# EXHAUSTIVE index of their generated pages (the teaching progression's front
# door). A new page added to `<folder>_pages/` but forgotten in that README goes
# silently missing — the exact bug that dropped bv2184_fyy886_lunch_vote from
# 01_STAR/_main. This gate makes that impossible: for each listed folder, every
# `<folder>_pages/*.md` must be referenced (by href) somewhere in its README.md.
#
# Deliberately an ALLOWLIST, not every folder: most READMEs are narrative and
# link a representative subset by design. Add a folder here only when its README
# is a complete index. Paths are repo-relative POSIX.
# --------------------------------------------------------------------------- #
INDEX_COMPLETE_DIRS = [
    "01_STAR/_main",
]


def check_pages_indexed():
    """Return [(readme_rel, unlisted_page)] for pages under an INDEX_COMPLETE_DIRS
    folder's `<folder>_pages/` that its README.md never links."""
    missing = []
    for rel_folder in INDEX_COMPLETE_DIRS:
        folder = os.path.join(REPO, rel_folder.replace("/", os.sep))
        readme = os.path.join(folder, "README.md")
        pages_dir = os.path.join(folder, os.path.basename(folder) + "_pages")
        if not (os.path.isfile(readme) and os.path.isdir(pages_dir)):
            continue
        try:
            text = open(readme, encoding="utf-8").read()
        except OSError:
            continue
        text = _INLINE_CODE.sub("", _FENCED.sub("", text))
        linked = {os.path.basename(m.group(1).split("#")[0].strip())
                  for m in MD_LINK.finditer(text)}
        for fn in sorted(os.listdir(pages_dir)):
            if fn.endswith(".md") and fn not in linked:
                missing.append((os.path.relpath(readme, REPO), fn))
    return sorted(missing)


def main(argv):
    rc = 0
    hits = scan()
    if not hits:
        print("repo-hygiene: ✓ no misplaced/junk files found.")
    else:
        rc = 1
        print("repo-hygiene: ⚠️  misplaced or junk files detected "
              f"({len(hits)}). These are ignored by git, but check each — a *real*")
        print("              file pasted with the wrong name/place would otherwise be lost:")
        for rel, msg in hits:
            print(f"   • {rel}\n       {msg}")
        print("\n  (House rules: BV screenshots → img/<bv_id>_*.png; BV exports → "
              "<descriptor>_<bvid>_bv_export.json. See CLAUDE.md.)")
    dead = check_links()
    if not dead:
        print("repo-hygiene: ✓ all relative Markdown links resolve.")
    else:
        rc = 1
        print(f"repo-hygiene: ⚠️  broken relative links ({len(dead)}) — a folder "
              "move probably left these behind:")
        for rel, raw in dead:
            print(f"   • {rel}  →  ({raw})")
    weak = check_descriptions()
    if not weak:
        print("repo-hygiene: ✓ every teaching YAML has a real description.")
    else:
        rc = 1
        print(f"repo-hygiene: ⚠️  weak/missing descriptions ({len(weak)}):")
        for rel, msg in weak:
            print(f"   • {rel}\n       {msg}")
    terms = check_terminology()
    if not terms:
        print("repo-hygiene: ✓ no house-terminology violations.")
    else:
        rc = 1
        print(f"repo-hygiene: ⚠️  terminology violations ({len(terms)}):")
        for rel, ln, msg in terms:
            print(f"   • {rel}:{ln}  {msg}")
    no_md = check_bv_case_md()
    if not no_md:
        print("repo-hygiene: ✓ every BV-backed case has a sibling .md page.")
    else:
        rc = 1
        print(f"repo-hygiene: ⚠️  BV cases missing their .md page ({len(no_md)}):")
        for rel, msg in no_md:
            print(f"   • {rel}\n       {msg}")
    unlisted = check_pages_indexed()
    if not unlisted:
        print("repo-hygiene: ✓ every index-complete README lists all its pages.")
    else:
        rc = 1
        print(f"repo-hygiene: ⚠️  pages missing from an index README ({len(unlisted)}) — "
              "add them to the README (or move the folder off INDEX_COMPLETE_DIRS):")
        for rel, page in unlisted:
            print(f"   • {rel}  ←  {page} not linked")
    # exit non-zero so a caller *can* gate on it; the pre-commit hook runs it
    # warn-only, and tests/test_md_links.py gates on the link half.
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
