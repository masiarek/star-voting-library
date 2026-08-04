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
             "_notes",  # personal working notes — site-excluded, not content
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
# Relative-link checker: every relative path in a tracked .md must resolve —
# markdown `[text](path)`, AND raw HTML `<img src=…>` / `<a href=…>` (plus
# other src-bearing tags), which the repo uses for sized images and anchors.
# Folder reorganizations silently break these; this catches them. (External
# http(s)/mailto/data links and pure #anchors are not checked.)
# --------------------------------------------------------------------------- #
MD_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
# href on <a>, src on <img>/<source>/<video>/<audio>/<embed>/<iframe>
_HTML_PATH = re.compile(
    r"""(?ix) < (?: a | img | source | video | audio | embed | iframe ) \b
        [^>]*? \b (?: href | src ) \s* = \s* (["']) (.+?) \1""")
_EXTERNAL = re.compile(r"(?i)^\s*(https?:|mailto:|data:|tel:|//|#)")
_FENCED = re.compile(r"```.*?```", re.S)
_INLINE_CODE = re.compile(r"`[^`\n]*`")


def check_links():
    """Return sorted [(md_file, raw_link)] for every relative link — markdown
    or HTML src/href — that does not resolve to an existing file or directory."""
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
            raws = [m.group(1).strip() for m in MD_LINK.finditer(text)]
            raws += [m.group(2).strip() for m in _HTML_PATH.finditer(text)]
            for raw in raws:
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
                elif os.path.isdir(p) and not (
                    os.path.exists(os.path.join(p, "README.md"))
                    or os.path.exists(os.path.join(p, "index.md"))
                ):
                    # Fine on GitHub (tree view), but the published site emits
                    # no index.html for a README-less folder → the link 404s.
                    broken.append((rel, raw + "  [folder link, but the folder "
                                              "has no README.md — 404s on the "
                                              "published site]"))
    return sorted(set(broken))


# --------------------------------------------------------------------------- #
# Anchor checker: a link like `page.md#some-heading` must point at a heading
# that actually exists on the *rendered* page. The classic breakage: a heading
# with " — ", " & ", " / " or ":" renders (in MkDocs / Python-Markdown's `toc`)
# with the gap collapsed to a SINGLE hyphen, but the link was written with the
# DOUBLE hyphen GitHub would produce (`#properties--criteria` vs the site's
# `#properties-criteria`). The site is the canonical surface, so the site's slug
# wins. check_links() only verifies the FILE resolves; this verifies the #anchor.
# --------------------------------------------------------------------------- #
import unicodedata

_ATX = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
_EXPLICIT_ID = re.compile(r"\{#([\w-]+)\}|\{:\s*#([\w-]+)")  # {#id} / {: #id }


def _slugify(value, sep="-"):
    """Python-Markdown's default `toc` slugify — what MkDocs uses to mint ids."""
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    return re.sub(r"[%s\s]+" % re.escape(sep), sep, value)


_ANCHOR_CACHE = {}


def _page_anchors(path):
    """The set of anchor slugs a rendered .md page exposes (heading ids), with
    Python-Markdown's duplicate-heading suffixing (`slug`, `slug_1`, `slug_2`…)."""
    if path in _ANCHOR_CACHE:
        return _ANCHOR_CACHE[path]
    anchors, counts = set(), {}
    try:
        text = open(path, encoding="utf-8").read()
    except OSError:
        _ANCHOR_CACHE[path] = anchors
        return anchors
    for line in _FENCED.sub("", text).splitlines():
        m = _ATX.match(line)
        if not m:
            continue
        htext = m.group(2)
        exp = _EXPLICIT_ID.search(htext)
        if exp:
            slug = exp.group(1) or exp.group(2)
        else:
            t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", htext)  # [txt](url) -> txt
            slug = _slugify(re.sub(r"[`*_]", "", t))
        if slug in counts:
            counts[slug] += 1
            anchors.add(f"{slug}_{counts[slug]}")
        else:
            counts[slug] = 0
            anchors.add(slug)
    _ANCHOR_CACHE[path] = anchors
    return anchors


def check_anchors():
    """Return sorted [(md_file, raw_link, suggestion)] for every relative link
    whose #anchor matches no heading on the (existing) target page. `suggestion`
    is the hyphen-collapsed anchor when that one *would* resolve, else None."""
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
            text = _INLINE_CODE.sub("", _FENCED.sub("", text))
            for m in MD_LINK.finditer(text):
                raw = m.group(1).strip()
                tgt = raw.split()[0].strip("<>")
                if re.match(r"(?i)^(https?:|mailto:)", tgt) or "#" not in tgt:
                    continue
                filepart, _, anchor = tgt.partition("#")
                if not anchor:
                    continue
                if filepart == "":
                    target_path = full                       # same-page anchor
                elif filepart.endswith(".md"):
                    target_path = os.path.normpath(os.path.join(
                        dirpath, unquote(filepart).replace("/", os.sep)))
                else:
                    continue                                 # anchors only in .md
                if not os.path.isfile(target_path):
                    continue                                 # missing file = check_links' job
                have = _page_anchors(target_path)
                if unquote(anchor) in have:
                    continue
                collapsed = re.sub(r"-{2,}", "-", unquote(anchor))
                suggestion = collapsed if collapsed in have else None
                broken.append((rel, raw, suggestion))
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


# The documented top-level schema for election YAMLs (field reference:
# 07_Concepts/about_this_repo/YAML_authoring_template.md). A key outside this
# set is almost always a typo — and a typo in a load-bearing key (say
# `expected_winers:`) silently removes the file from test discovery, which is
# exactly the failure class this check exists to catch.
ELECTION_KEYS = {
    "election_title",
    # scenario_description = the teaching text; election_description = the
    # BetterVoting election's own live blurb (only meaningful in BV-backed
    # cases, where both may appear). The old use of election_description as a
    # synonym for the teaching text was normalized away 2026-08-01.
    "scenario_description", "election_description",
    "voting_method", "num_winners", "ballots",
    "expected_winners", "expected_results",
    "options", "lot_numbers", "eligible_voters", "quorum", "blocs",
    "paradoxes", "video_script",
    "election",  # the nested BetterVoting export schema
    "bv_election_id", "bv_results_url", "bv_test_id", "bv_github_issue",
    "lh_only_reason",
}


def unknown_top_level_keys(data):
    """The keys of `data` outside the documented election schema, each paired
    with a did-you-mean suggestion (or None)."""
    import difflib
    out = []
    for k in data:
        if k in ELECTION_KEYS:
            continue
        hint = difflib.get_close_matches(str(k), sorted(ELECTION_KEYS), n=1)
        out.append((str(k), hint[0] if hint else None))
    return out


def check_top_level_keys():
    """Return [(file, problem)] for election YAMLs carrying unrecognized
    top-level keys."""
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
        if not isinstance(data, dict):
            continue
        if "ballots" not in data and "election" not in data:
            continue        # not an election file
        for key, hint in unknown_top_level_keys(data):
            msg = f"unknown top-level key `{key}:`"
            if hint:
                msg += f" — did you mean `{hint}:`?"
            bad.append((rel, msg))
    return sorted(bad)


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
# **Level:** tags — one shape, so the audience token stays pickable-from and the
# voice rule in CLAUDE.md is enforceable rather than remembered. Canonical:
#     **Level: <rung> · <audience>**
# rung = 101|201|301|401, an arrow range (201 → 301), or `reference`
# audience = for voters | for presenters | for debaters | deep dive
# Untagged pages are fine (the 101 spine mostly is); a *malformed* tag is not.
# Elaboration goes AFTER the closing `**`, never inside the token.
# --------------------------------------------------------------------------- #
_LEVEL_TOKEN = re.compile(r"\*\*Level:.*?\*\*|\*\*Level:\*\*")
_LEVEL_RUNG = r"(?:101|201|301|401)(?:\s*→\s*(?:101|201|301|401))?|reference"
_LEVEL_AUD = r"for voters|for presenters|for debaters|deep dive"
_LEVEL_OK = re.compile(rf"^\*\*Level: (?:{_LEVEL_RUNG}) · (?:{_LEVEL_AUD})\*\*$")


def check_levels():
    """Return [(file, lineno, found)] for malformed **Level:** tags."""
    hits = []
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, REPO)
            if _skip(rel) or rel == "CLAUDE.md":   # CLAUDE.md documents the shape
                continue
            try:
                lines = open(path, encoding="utf-8").read().splitlines()
            except OSError:
                continue
            for i, ln in enumerate(lines, 1):
                for m in _LEVEL_TOKEN.finditer(ln):
                    if not _LEVEL_OK.match(m.group(0)):
                        hits.append((rel, i, m.group(0)))
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
# door). A new case added to the folder but forgotten in that README goes
# silently missing — the exact bug that dropped bv2184_fyy886_lunch_vote from
# 01_STAR/02_Examples, rr_blank_is_last_c4_b3 from 05_Ranked_Robin/02_Examples, and
# bv2130_bvhchj_party_plurality from 03_STAR_PR/02_Examples. This gate makes that
# impossible: for each listed folder, every generated page must be referenced
# (by href) somewhere in its index README.
#
# An ALLOWLIST, and near-total: a 2026-08-02 survey of all 89 folders carrying
# generated pages found 81 whose README already indexes every case, so they are
# all enrolled here. Enrolling turns "complete today" into "must stay complete",
# which is the point — but it means a README that later wants to link only a
# representative subset must be dropped from this dict, deliberately, rather
# than drifting. Paths are repo-relative POSIX.
#
# The nine NOT enrolled, and why (re-check before adding):
#   summability_demo, tie_break_dead_rung  — name their cases in `inline code`,
#       not links; enrolling means converting those spans to real links first
#       (worth doing on its own merits — those filenames aren't clickable today)
#   pet_real_bv_election  — two-tier: the README is a narrative walkthrough that
#       links its lesson write-ups, and those link the cases. Reachable, but not
#       from the README, and flattening that into the walkthrough would cost more
#       than the gate is worth here
#   symmetric_centrist_all_methods  — two-tier, but the write-up stem
#       (bv2171_h93tm4_all_methods) doesn't match the page stem
#       (bv2171_h93tm4_star), so no artifact rule bridges it; needs 2 explicit links
#   split_voting/_main  — has generated pages and NO README at all
#   the four `<folder>/cases` dirs  — an artifact of _cases_pages_dir's legacy
#       branch matching `cases/cases_pages`; the same pages as the parent folder
#
# Value = the README that indexes the folder, when that is NOT the folder's own
# README.md. 02_STAR_Bloc/02_Examples is the standing example: its own page says the
# index "lives one level up … That's the single source of truth", so the gate has
# to read the parent's table or it would police the wrong file.
# --------------------------------------------------------------------------- #
INDEX_COMPLETE_DIRS = {
    # --- 01_STAR
    "01_STAR/09_Parked/Flat_scores_ties": None,
    "01_STAR/02_Examples": None,
    "01_STAR/04_Real_Elections/abstain_bugs": None,
    "01_STAR/03_Criteria/equal_and_opposite": None,
    "01_STAR/05_Practice": None,
    "01_STAR/03_Criteria/favorite_betrayal": None,
    "01_STAR/03_Criteria/iia_cycle_spoiler": None,
    "01_STAR/03_Criteria/majority_criterion": None,
    "01_STAR/03_Criteria/none_of_the_above": None,
    "01_STAR/02_Examples/runoff_overturns_leader": None,
    "01_STAR/04_Real_Elections/runoff_reversal_bv_cases": None,
    "01_STAR/09_Parked/silly_two_cand_STAR": None,
    "01_STAR/03_Criteria/tie_break_ladder": None,
    # --- 02_STAR_Bloc
    "02_STAR_Bloc/02_Examples": "02_STAR_Bloc/README.md",   # index lives in the parent table
    # --- 03_STAR_PR
    "03_STAR_PR/02_Examples": None,
    # --- 04_Approval
    "04_Approval/02_Examples": None,
    "04_Approval/02_Examples/multiwinner": None,
    # --- 05_Ranked_Robin
    "05_Ranked_Robin/02_Examples": None,
    "05_Ranked_Robin/03_Criteria/burial": None,
    "05_Ranked_Robin/03_Criteria/clone_independence": None,
    "05_Ranked_Robin/02_Examples/condorcet_vs_ranked_robin": None,
    "05_Ranked_Robin/02_Examples/consensus_choice_divergence": None,
    "05_Ranked_Robin/02_Examples/copeland_score": None,
    "05_Ranked_Robin/02_Examples/most_wins_vs_condorcet": None,
    "05_Ranked_Robin/03_Criteria/rr_tiebreaks": None,
    "05_Ranked_Robin/02_Examples/rr_vs_irv_plurality": None,
    "05_Ranked_Robin/02_Examples/star_vs_rr_divergence": None,
    # --- 06_Other
    "06_Other/Plurality": None,
    "06_Other/RCV_IRV": None,
    "06_Other/RCV_IRV/equal_vote_balance": None,
    "06_Other/Range": None,
    "06_Other/STV": None,
    "06_Other/STV/bv_stv_sole_survivor_crash": None,
    "06_Other/ballot_style_lab": None,
    "06_Other/three_two_one": None,
    # --- method_comparisons
    "method_comparisons/BV_Library": None,
    "method_comparisons/_main": None,
    "method_comparisons/alaska_2022": None,
    "method_comparisons/alaska_2022_general": None,
    "method_comparisons/approval_majority_criterion": None,
    "method_comparisons/black_curtain": None,
    "method_comparisons/borda_condorcet_1788": None,
    "method_comparisons/brams_grading_paradox": None,
    "method_comparisons/burlington_2009": None,
    "method_comparisons/center_squeeze": None,
    "method_comparisons/center_squeeze_bv2137": None,
    "method_comparisons/chicken_dilemma": None,
    "method_comparisons/condorcet_burial_alaska": None,
    "method_comparisons/copeland_vs_borda_margins": None,
    "method_comparisons/cycle_resolution": None,
    "method_comparisons/dark_horse_borda": None,
    "method_comparisons/edelman_condorcet_myth": None,
    "method_comparisons/fairvote_condorcet_claims": None,
    "method_comparisons/fairvote_star_whitepaper": None,
    "method_comparisons/favorite_betrayal_irv": None,
    "method_comparisons/felsenthal_paradoxes": None,   # 2-tier: rows are elections, each linking every method yaml
    "method_comparisons/food_truck_row": None,   # indexes via _tabulated.txt links
    "method_comparisons/manipulability_p3": None,
    "method_comparisons/minimal_tilted_cycle": None,
    "method_comparisons/minority_winner": None,
    "method_comparisons/minority_winner_progression": None,
    "method_comparisons/monotonicity": None,
    "method_comparisons/multi_member_plurality": None,
    "method_comparisons/no_condorcet_bv2138": None,
    "method_comparisons/ordered_majority_rule": None,
    "method_comparisons/paradoxes_and_whoops": None,
    "method_comparisons/participation_no_show": None,
    "method_comparisons/pet_poll_four_methods": None,
    "method_comparisons/pet_poll_four_winners": None,
    "method_comparisons/pets_governance": None,
    "method_comparisons/postit_rcv_example": None,
    "method_comparisons/preference_vs_support": None,
    "method_comparisons/reinforcement_paradox": None,
    "method_comparisons/reversal_symmetry": None,
    "method_comparisons/same_matrix_different_plurality": None,
    "method_comparisons/sntv_village_council": None,
    "method_comparisons/split_cycle": None,
    "method_comparisons/star_5_1_0_challenge": None,
    "method_comparisons/symmetric_centrist_bv2170": None,
    "method_comparisons/tournament_solutions": None,
    "method_comparisons/valuable_condorcet_loser": None,
    "method_comparisons/weak_condorcet_loser": None,
}


def _cases_pages_dir(folder):
    """The folder's generated-pages directory, or None. Two layouts exist: the
    current house one (`<folder>/cases/cases_pages/`) and an older sibling form
    (`<folder>/<basename>_pages/`) still used by a handful of folders."""
    for cand in (os.path.join(folder, "cases", "cases_pages"),
                 os.path.join(folder, os.path.basename(folder) + "_pages")):
        if os.path.isdir(cand):
            return cand
    return None


def check_pages_indexed():
    """Return [(readme_rel, problem)] for cases under an INDEX_COMPLETE_DIRS
    folder that its indexing README never links.

    A case counts as indexed if the README links ANY of its three artifacts:
    the generated page (`<stem>.md`), the source (`<stem>.yaml`), or the audit
    mirror (`<stem>_tabulated.txt`). All three are legitimate index styles in
    this repo — 02_STAR_Bloc's table links the yaml for its teaching rows and
    the page for its BV rows; food_truck_row links the tabulated mirror — and
    the question this gate asks is "did you forget the case exists?", not
    "which artifact did you link?".

    An allowlisted folder whose README or pages directory cannot be resolved is
    reported as a FAILURE, never skipped: this check spent its whole life inert
    because it looked for `01_STAR/02_Examples/_main_pages/` while the actual layout
    is `01_STAR/02_Examples/cases/cases_pages/`, so a missing directory silently meant
    "✓ nothing to check". A gate that cannot find its target is broken, not clean.
    """
    missing = []
    for rel_folder, rel_index in sorted(INDEX_COMPLETE_DIRS.items()):
        folder = os.path.join(REPO, rel_folder.replace("/", os.sep))
        readme = (os.path.join(REPO, rel_index.replace("/", os.sep)) if rel_index
                  else os.path.join(folder, "README.md"))
        rel_readme = os.path.relpath(readme, REPO)
        pages_dir = _cases_pages_dir(folder)
        if pages_dir is None:
            missing.append((rel_folder, "no generated-pages directory found "
                                        "(looked for cases/cases_pages/ and "
                                        f"{os.path.basename(folder)}_pages/) — "
                                        "drop it from INDEX_COMPLETE_DIRS or fix "
                                        "the path"))
            continue
        try:
            text = open(readme, encoding="utf-8").read()
        except OSError:
            missing.append((rel_folder, f"indexing README {rel_readme} is "
                                        "unreadable or missing"))
            continue
        text = _INLINE_CODE.sub("", _FENCED.sub("", text))
        linked = {os.path.basename(m.group(1).split("#")[0].strip())
                  for m in MD_LINK.finditer(text)}
        for fn in sorted(os.listdir(pages_dir)):
            if not fn.endswith(".md"):
                continue
            stem = fn[:-3]
            if linked & {fn, stem + ".yaml", stem + ".yml",
                         stem + "_tabulated.txt"}:
                continue
            missing.append((rel_readme, f"{fn} — case in {rel_folder} is not "
                                        "linked from the index (not its page, "
                                        "its .yaml, or its _tabulated.txt)"))
    return sorted(missing)


# --------------------------------------------------------------------------- #
# Pasted engine reports on companion pages
# --------------------------------------------------------------------------- #
# CLAUDE.md already says it ("a pasted long report would go stale"), and it did:
# the BV1815 companion page sat for months showing a pre-`[Bloc STAR: …]` report
# the engine no longer emits. A pasted report has no test behind it, so nothing
# notices. This gate makes the choice explicit — a long engine-shaped block on a
# companion page is either an embed of the `_tabulated` mirror, which tracks the
# engine for free, or it is labelled as an abridgement, which several pages
# legitimately are (bv750's `a 15 ; b 15 ; c 15  ← three-way tie` is Adam's
# compression for the lesson, not output, and should not be "fixed" into one).
_REPORT_FENCE = re.compile(r"^([ \t]*)(```+|~~~+)([^\n]*)\n(.*?)^\1\2\s*$", re.S | re.M)
_REPORT_SIGNS = [r"Scoring Round", r"Automatic Runoff Round", r"\[Score Distribution\]",
                 r"^---.*Voting Method", r"^\s*Winners?\s*[—-]", r"Tabulating \d+ ballots",
                 r"Runoff \(Preference\) Matrix", r"Condorcet Winner\]", r"tiebreaker"]
_REPORT_MIN_LINES = 8
_ABRIDGED = re.compile(r"abridged", re.I)

# Empty, and meant to stay that way. It briefly held the 34 pages that predated
# this gate — 28 of them showing output the engine had stopped emitting, mostly
# from the switch to bracketed `[STAR Voting: Scoring Round]` headers. All 34
# were converted (30 to `:report` includes, 6 relabelled as the deliberate
# abridgements they always were), so no page exists that this rule can't be
# applied to. Adding an entry is not the fix — embed the report, or say abridged.
PASTED_REPORT_GRANDFATHERED = set()


def _companion_pages():
    """Hand-authored pages that shadow a generated case page: {path: mirror dir}."""
    found = {}
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and d != "site"]
        if os.path.basename(dirpath) != "cases_pages":
            continue
        ydir = os.path.dirname(dirpath)
        parent = os.path.dirname(ydir)
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            comp = os.path.join(parent, fn)
            if os.path.isfile(comp):
                found[comp] = os.path.join(ydir, "cases_tabulated",
                                           fn[:-3] + "_tabulated.txt")
    return found


def check_pasted_reports():
    """Return [(rel, problem)] for un-embedded, unlabelled engine reports."""
    bad = []
    for comp, mirror in sorted(_companion_pages().items()):
        rel = os.path.relpath(comp, REPO).replace(os.sep, "/")
        if rel in PASTED_REPORT_GRANDFATHERED:
            continue
        try:
            text = open(comp, encoding="utf-8").read()
        except OSError:
            continue
        for m in _REPORT_FENCE.finditer(text):
            info, body = m.group(3), m.group(4)
            if "--8<--" in body or _ABRIDGED.search(info):
                continue
            lines = [l for l in body.splitlines() if l.strip()]
            if len(lines) < _REPORT_MIN_LINES:
                continue          # short teaching snippets are fine (CLAUDE.md)
            if sum(1 for s in _REPORT_SIGNS if re.search(s, body, re.M)) < 2:
                continue
            line_no = text[:m.start()].count("\n") + 1
            how = (f"embed it — ```text\\n--8<-- \"{os.path.relpath(mirror, REPO)}\"\\n```"
                   if os.path.isfile(mirror)
                   else "embed the case's _tabulated mirror")
            bad.append((f"{rel}:{line_no}",
                        f"{len(lines)}-line engine report pasted by hand — {how}, "
                        "or mark the fence ```text abridged if the compression is "
                        "deliberate"))
            break                 # one finding per page is enough to act on
    return bad


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
        print(f"repo-hygiene: ⚠️  broken relative links ({len(dead)}) — markdown or "
              "HTML src/href; a folder move probably left these behind:")
        for rel, raw in dead:
            print(f"   • {rel}  →  ({raw})")
    bad_anchors = check_anchors()
    if not bad_anchors:
        print("repo-hygiene: ✓ every #anchor link points at a real heading.")
    else:
        rc = 1
        print(f"repo-hygiene: ⚠️  links to nonexistent #anchors ({len(bad_anchors)}) — "
              "the heading's rendered slug differs (MkDocs collapses ` — `/`&`/`/` "
              "gaps to ONE hyphen):")
        for rel, raw, suggestion in bad_anchors:
            fix = f"  → did you mean #{suggestion}?" if suggestion else ""
            print(f"   • {rel}  →  ({raw}){fix}")
    bad_keys = check_top_level_keys()
    if not bad_keys:
        print("repo-hygiene: ✓ every election YAML uses only documented top-level keys.")
    else:
        rc = 1
        print(f"repo-hygiene: ⚠️  unknown top-level YAML keys ({len(bad_keys)}) — "
              "a typo here silently un-tests the case:")
        for rel, msg in bad_keys:
            print(f"   • {rel}\n       {msg}")
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
    bad_levels = check_levels()
    if not bad_levels:
        print("repo-hygiene: ✓ every **Level:** tag uses the canonical shape.")
    else:
        rc = 1
        print(f"repo-hygiene: ⚠️  malformed **Level:** tags ({len(bad_levels)}) — "
              "want `**Level: <101|201|301|401|range|reference> · "
              "<for voters|for presenters|for debaters|deep dive>**`, with any")
        print("              elaboration AFTER the closing `**` (see CLAUDE.md, "
              "'Voice' + 'Level'):")
        for rel, ln, found in bad_levels:
            print(f"   • {rel}:{ln}  {found}")
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
        print(f"repo-hygiene: ✓ all {len(INDEX_COMPLETE_DIRS)} index-complete "
              "READMEs list every case in their folder.")
    else:
        rc = 1
        print(f"repo-hygiene: ⚠️  cases missing from an index README ({len(unlisted)}) — "
              "add them to the README (or move the folder off INDEX_COMPLETE_DIRS):")
        for rel, msg in unlisted:
            print(f"   • {rel}\n       {msg}")
    pasted = check_pasted_reports()
    grandfathered = len(PASTED_REPORT_GRANDFATHERED)
    if not pasted:
        print("repo-hygiene: ✓ no hand-pasted engine reports on companion pages"
              + (f" ({grandfathered} grandfathered — burn the list down)."
                 if grandfathered else "."))
    else:
        rc = 1
        print(f"repo-hygiene: ⚠️  hand-pasted engine reports ({len(pasted)}) — nothing "
              "tests a pasted report, so it goes stale the next time the engine's")
        print("              output format changes (see CLAUDE.md, 'Route the short "
              "snippet to the full report'):")
        for rel, msg in pasted:
            print(f"   • {rel}\n       {msg}")
    # exit non-zero so a caller *can* gate on it; the pre-commit hook runs it
    # warn-only, and tests/test_md_links.py gates on the link half.
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
