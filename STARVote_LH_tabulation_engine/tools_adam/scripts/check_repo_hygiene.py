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
# An HTML comment is inert on every surface — GitHub, MkDocs and a local
# viewer all render nothing — so a path inside one is not a link. The house
# convention leans on this: the BV workflow says to comment out a screenshot
# slot you have not captured yet rather than leave a REPLACE_ placeholder. Not
# stripping it reported those inert slots as broken links, which reddened the
# docs build on a commented-out `<img src=…>` (2026-08-06).
# ORDER IS LOAD-BEARING: strip fences FIRST. A code sample that *shows* an HTML
# comment leaves an unbalanced `<!--`, and stripping comments first eats across the
# closing ``` — the fence then no longer matches, every example link inside it gets
# checked as real, and the count jumps (1 -> 56 when tried the wrong way round).
_HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
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
            text = _INLINE_CODE.sub("", _HTML_COMMENT.sub("", _FENCED.sub("", text)))
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
# Folder-link checker: `[label](some_folder/)` must be written
# `[label](some_folder/README.md)`.
#
# The bare form resolves on GitHub (the tree view renders the folder's README)
# and on the built site (the server serves the folder's index.html), so it looks
# fine from two of the three surfaces people actually use — which is how ~1,000
# of them accumulated. The two places it fails:
#
#   1. MkDocs does NOT rewrite it. The build log says "contains an unrecognized
#      relative link '../../06_Other/RCV_IRV/concepts', it was LEFT AS IS", and
#      the raw href ships to the published page. 635 links were landing dead on
#      the site before the 2026-08 sweep.
#   2. A plain local Markdown viewer opens it as a file and reports it missing.
#
# check_links() above covers the *other* half of this — a folder link whose
# folder has no README.md at all. This one covers folders that DO have one, so
# between them every folder link is either rewritten or reported.
# --------------------------------------------------------------------------- #

# Three spellings, all equivalent to a reader and all equally unrewritten:
#   [x](foo/)   [x](foo)   [x](foo/#anchor)
_FOLDER_LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+?)(#[^)\s]*)?\)")


def check_folder_links():
    """Return sorted [(md_file, raw_link, suggestion)] for every relative link
    pointing at a directory that has a README.md, written without naming it."""
    from urllib.parse import unquote
    bare = []
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        rel_dir = os.path.relpath(dirpath, REPO)
        if rel_dir != "." and _skip(rel_dir):
            continue
        for fn in filenames:
            if not fn.lower().endswith(".md"):
                continue
            rel = os.path.normpath(os.path.join(rel_dir, fn))
            try:
                text = open(os.path.join(dirpath, fn), encoding="utf-8").read()
            except OSError:
                continue
            # Links inside code blocks / inline code are examples, not links —
            # and this page documents the bad form on purpose.
            text = _INLINE_CODE.sub("", _HTML_COMMENT.sub("", _FENCED.sub("", text)))
            for m in _FOLDER_LINK.finditer(text):
                target, frag = m.group(1), m.group(2) or ""
                if _EXTERNAL.match(target) or target.startswith("/"):
                    continue
                p = os.path.normpath(
                    os.path.join(dirpath, unquote(target).replace("/", os.sep)))
                if not (os.path.isdir(p)
                        and os.path.exists(os.path.join(p, "README.md"))):
                    continue
                fixed = target.rstrip("/") + "/README.md" + frag
                bare.append((rel, target + frag, fixed))
    return sorted(set(bare))


# --------------------------------------------------------------------------- #
# Uncommitted-target checker: a link on an ALREADY-COMMITTED page must point at
# a file that is also committed.
#
# check_links() above resolves every link against the WORKING TREE, where a
# not-yet-committed file — yours, or a concurrent session's — is sitting right
# there. So the link looks fine locally and the pre-commit hook passes. CI then
# builds the COMMITTED tree, the target isn't in it, and `mkdocs build --strict`
# turns that missing target into a WARNING, which in strict mode fails the whole
# docs deploy. Nothing in the local gate can see it, because locally it is true.
#
# This is not hypothetical: on 2026-08-05 the docs build went red five times in
# about twenty minutes in a checkout shared by two sessions, every time because
# a committed page referenced a file that had not been committed yet.
#
# Only TRACKED pages are scanned. A brand-new page linking to a brand-new case
# is fine — both get committed together, and warning about it would fire on
# every draft in progress. The break is specifically an *already-published* page
# pointing at something that isn't published, which is why the page's own
# tracked-ness is the trigger.
# --------------------------------------------------------------------------- #
_MAX_LISTED = 10   # per-check cap on printed findings before summarizing


def _git_tracked_paths():
    """Repo-relative paths that the next commit's tree will contain: the union
    of the INDEX (`ls-files`) and the HEAD tree. Separators normalized.
    Returns None (check no-ops) if git isn't available or this isn't a repo.

    Why the union rather than `ls-files` alone. `ls-files` reads only the index,
    and this repo is routinely open in two sessions at once — while one of them
    is mid-`git commit` the index.lock is held and the index is transiently
    inconsistent, so a file that is comfortably committed in HEAD reads back as
    untracked. Testing that on 2026-08-05 produced six false positives in one
    run, every one of them present in both HEAD and origin/master. A guard that
    cries wolf during a normal concurrent commit would be turned off within a
    day, so HEAD is consulted too and anything in either set counts as present.

    The trade: a target that is committed but deliberately `git rm`-ed in the
    index reads as present and is not flagged. That is the deletion commit's
    problem to notice, and it is far rarer than concurrent index churn.
    """
    import subprocess

    def _run(args):
        return subprocess.run(["git", "-C", REPO] + args, capture_output=True,
                              text=True, check=True, timeout=60).stdout

    paths = set()
    ok = False
    for args, sep in (
        (["ls-files", "-z"], "\0"),
        (["ls-tree", "-r", "--name-only", "-z", "HEAD"], "\0"),
    ):
        try:
            paths |= {os.path.normpath(p) for p in _run(args).split(sep) if p}
            ok = True
        except Exception:
            continue        # e.g. no HEAD yet in a fresh repo, or a held lock
    return paths if ok else None


def _iter_relative_links():
    """Yield (rel_md, dirpath, raw_link, resolved_fs_path) for every relative
    link in every scanned .md file — the extraction check_links() does, factored
    out so a new check need not re-implement it. check_links() is left as-is."""
    from urllib.parse import unquote
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
            text = _INLINE_CODE.sub("", _HTML_COMMENT.sub("", _FENCED.sub("", text)))
            raws = [m.group(1).strip() for m in MD_LINK.finditer(text)]
            raws += [m.group(2).strip() for m in _HTML_PATH.finditer(text)]
            for raw in raws:
                if _EXTERNAL.match(raw):
                    continue
                target = raw.split()[0].strip("<>").split("#")[0]
                if not target or os.path.basename(target).startswith("REPLACE_"):
                    continue
                p = os.path.normpath(
                    os.path.join(dirpath, unquote(target).replace("/", os.sep)))
                yield rel, dirpath, raw, p


def format_untracked_report(hits, max_listed=_MAX_LISTED):
    """Render check_untracked_link_targets() findings as report lines, capped.

    Capped because the usual trigger is a concurrent session mid-rename, where a
    single uncommitted case is linked from a dozen generated pages: one run here
    produced 48 findings naming the same handful of files, burying the other
    eleven hygiene checks. The DISTINCT TARGETS are what you act on — the
    per-page hits only say where they were spotted — so the overflow summarizes
    by target ("commit these 3 files") instead of an unhelpful "and 38 more".
    """
    lines = [f"   • {rel}  →  ({raw})   [not tracked: {trel}]"
             for rel, raw, trel in hits[:max_listed]]
    extra = len(hits) - len(lines)
    if extra:
        targets = sorted({t for _rel, _raw, t in hits})
        pages = len({r for r, _raw, _t in hits})
        lines.append(f"   … and {extra} more, from {pages} page(s) in total.")
        lines.append(f"   Commit these {len(targets)} file(s) and every one of "
                     "them clears:")
        lines += [f"       - {t}" for t in targets[:max_listed]]
        if len(targets) > max_listed:
            lines.append(f"       - … and {len(targets) - max_listed} more")
    return lines


def check_untracked_link_targets():
    """Return sorted [(md_file, raw_link, target_rel)] for links on a tracked
    page whose target exists on disk but is NOT tracked by git."""
    tracked = _git_tracked_paths()
    if tracked is None:
        return []
    hits = []
    for rel, _dirpath, raw, p in _iter_relative_links():
        if rel not in tracked:
            continue                      # page not committed yet — see docstring
        if not os.path.exists(p):
            continue                      # check_links() already reports these
        if os.path.isdir(p):
            idx = next((os.path.join(p, n) for n in ("README.md", "index.md")
                        if os.path.exists(os.path.join(p, n))), None)
            if idx is None:
                continue                  # README-less folder — check_links()' job
            p = idx
        trel = os.path.normpath(os.path.relpath(p, REPO))
        if trel.startswith(".."):
            continue                      # outside the repo — not ours to judge
        if trel not in tracked:
            hits.append((rel, raw, trel))
    return sorted(set(hits))


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
            text = _INLINE_CODE.sub("", _HTML_COMMENT.sub("", _FENCED.sub("", text)))
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
# YAML_library/YAML_authoring_template.md). A key outside this
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

    An untracked page is SKIPPED. This checkout is routinely open in several
    sessions at once, and a case that is still being built — its page drawn but
    its README row not written yet — is not an index the repo has committed.
    Flagging it failed the pre-commit suite for every OTHER session too, which
    is how one half-finished case blocked the whole repo's commits. Staging the
    case (`git add`) brings it straight back under the gate, so the case you are
    actually committing is still checked. See _git_tracked_paths().
    """
    missing = []
    tracked = _git_tracked_paths()
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
        text = _INLINE_CODE.sub("", _HTML_COMMENT.sub("", _FENCED.sub("", text)))
        linked = {os.path.basename(m.group(1).split("#")[0].strip())
                  for m in MD_LINK.finditer(text)}
        for fn in sorted(os.listdir(pages_dir)):
            if not fn.endswith(".md"):
                continue
            stem = fn[:-3]
            if linked & {fn, stem + ".yaml", stem + ".yml",
                         stem + "_tabulated.txt"}:
                continue
            if tracked is not None and os.path.normpath(
                    os.path.relpath(os.path.join(pages_dir, fn), REPO)
            ) not in tracked:
                continue        # still being built — not the committed index yet
            missing.append((rel_readme, f"{fn} — case in {rel_folder} is not "
                                        "linked from the index (not its page, "
                                        "its .yaml, or its _tabulated.txt)"))
    return sorted(missing)


# --------------------------------------------------------------------------- #
# Pasted engine reports on hand-authored pages
# --------------------------------------------------------------------------- #
# CLAUDE.md already says it ("a pasted long report would go stale"), and it did:
# the BV1815 companion page sat for months showing a pre-`[Bloc STAR: …]` report
# the engine no longer emits. A pasted report has no test behind it, so nothing
# notices. This gate makes the choice explicit — a long engine-shaped block on a
# hand-authored page is either a `:report` include of the case's generated page,
# which tracks the engine for free, or it is labelled as an abridgement, which
# many pages legitimately are (bv750's `a 15 ; b 15 ; c 15  ← three-way tie` is
# Adam's compression for the lesson, not output, and must not be "fixed" into
# one). Two exemptions, both deliberate: GENERATED pages are rebuilt from their
# sources and cannot drift, and a page showing a *generic illustration* has no
# case to include — CLAUDE.md exempts those, so the gate only fires when the
# page itself names the case whose report it is showing.
#
# ANNOTATED fences are never convertible. A block carrying `←` margin notes is a
# rendition the author built for the lesson, and replacing it with an include
# deletes the annotation that was the point. Nine were lost that way before this
# was understood; they are restored and labelled. Annotation ⇒ abridged, always.
_REPORT_FENCE = re.compile(r"^([ \t]*)(```+|~~~+)([^\n]*)\n(.*?)^\1\2\s*$", re.S | re.M)
_REPORT_SIGNS = [r"Scoring Round", r"Automatic Runoff Round", r"\[Score Distribution\]",
                 r"^---.*Voting Method", r"^\s*Winners?\s*[—-]", r"Tabulating \d+ ballots",
                 r"Runoff \(Preference\) Matrix", r"Condorcet Winner\]", r"tiebreaker"]
_REPORT_MIN_LINES = 8
_ABRIDGED = re.compile(r"abridged", re.I)
# Engine output is only ever an unlabelled or ```text fence. A ```yaml block is a
# case file, not a report — and `options.md` / `YAML_authoring_template.md` do
# document keys like `show_condorcet:  # hide the [Condorcet Winner] line`, whose
# COMMENTS trip the signature list. Fence language settles it before content does.
_NOT_A_REPORT_LANG = {"yaml", "yml", "json", "python", "py", "bash", "sh",
                      "shell", "console", "csv", "toml", "ini", "diff", "js"}

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


_GENERATED_MARK = re.compile(r"do not hand-edit|do not edit by hand|Generated by |"
                             r"Generated from ", re.I)
_ANNOTATED = re.compile(r"←|⟵")

# A fence inside `<!-- report:<stem> --> … <!-- /report -->` is not hand-pasted:
# build_yaml_pages.py wrote it from that case's generated page and
# test_report_blocks_are_current fails when it drifts. That block replaced the
# bare `--8<--` include, which rendered on the MkDocs site but printed as
# literal text on GitHub — so the gate has to recognise both.
_REPORT_BLOCK = re.compile(r"<!-- report:[A-Za-z0-9_.\-]+ -->.*?<!-- /report -->", re.S)


def _case_pages():
    """{stem: repo-relative generated page} for every case that has one."""
    out = {}
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and d != "site"]
        if os.path.basename(dirpath) != "cases_pages":
            continue
        for fn in filenames:
            if fn.endswith(".md"):
                out[fn[:-3]] = os.path.relpath(os.path.join(dirpath, fn),
                                               REPO).replace(os.sep, "/")
    return out


def _hand_authored_pages():
    """Every .md a human maintains — generated trees and generated pages excluded."""
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and d != "site"
                       and not d.endswith("_pages")]
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dirpath, fn)
            try:
                text = open(p, encoding="utf-8").read()
            except OSError:
                continue
            if _GENERATED_MARK.search(text[:600]):
                continue
            yield os.path.relpath(p, REPO).replace(os.sep, "/"), text


def check_pasted_reports():
    """Return [(rel, problem)] for un-included, unlabelled engine reports.

    Fires only when the page NAMES the case whose report it shows: that is what
    separates a stale copy (fixable by including the case's generated page) from
    a generic illustration with no case behind it, which CLAUDE.md exempts.
    """
    bad = []
    case_pages = _case_pages()
    for rel, text in sorted(_hand_authored_pages()):
        if rel in PASTED_REPORT_GRANDFATHERED:
            continue
        named = [s for s in case_pages if s in text]
        if not named:
            continue
        managed = [m.span() for m in _REPORT_BLOCK.finditer(text)]
        for m in _REPORT_FENCE.finditer(text):
            info, body = m.group(3), m.group(4)
            if "--8<--" in body or _ABRIDGED.search(info):
                continue
            if any(a <= m.start() < b for a, b in managed):
                continue          # generated block, regenerated and drift-tested
            lang = info.strip().split()[0].lower() if info.strip() else ""
            if lang in _NOT_A_REPORT_LANG:
                continue
            lines = [l for l in body.splitlines() if l.strip()]
            if len(lines) < _REPORT_MIN_LINES:
                continue          # short teaching snippets are fine (CLAUDE.md)
            if sum(1 for s in _REPORT_SIGNS if re.search(s, body, re.M)) < 2:
                continue
            line_no = text[:m.start()].count("\n") + 1
            if _ANNOTATED.search(body):
                fix = ('carries `←` notes, so it is a rendition, not a copy — '
                       'label the fence title="Abridged for the lesson — not '
                       'verbatim engine output". Do NOT replace it with an '
                       'include; that deletes the annotation.')
            else:
                best = max(named, key=len)
                fix = (f'let the generator embed it instead — mark the spot with '
                       f'<!-- report:{best} --> / <!-- /report --> and run '
                       f'build_yaml_pages.py, or label it abridged if the '
                       f'compression is deliberate')
            bad.append((f"{rel}:{line_no}",
                        f"{len(lines)}-line engine report pasted by hand — {fix}"))
            break                 # one finding per page is enough to act on
    return bad


_CODE_SPAN_PATH = re.compile(
    r"`([A-Za-z0-9_][A-Za-z0-9_./-]*\.(?:md|yaml|py|sh|json|toml|txt))`")

_BY_BASENAME = None


def _repo_files_named(basename):
    """Repo-relative paths of every file with this basename (cached, one walk).

    Deliberately does NOT use `_skip()`: that excludes `_tabulation_engine`,
    which is precisely where the truncated `tests/…` and `tools_adam/…` paths
    resolve to.  SKIP_DIRS alone is right here — it still drops `.claude`, so
    the worktree copies under `.claude/worktrees/` cannot turn a real finding
    into an "ambiguous" one and silence it.
    """
    global _BY_BASENAME
    if _BY_BASENAME is None:
        _BY_BASENAME = {}
        for dirpath, dirnames, filenames in os.walk(REPO):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for f in filenames:
                rel = os.path.relpath(os.path.join(dirpath, f), REPO)
                _BY_BASENAME.setdefault(f, []).append(rel)
    return _BY_BASENAME.get(basename, [])


def check_code_span_paths():
    """Return [(rel:line, msg)] for repo-root paths written as bare code text.

    A page that says ``07_Concepts/tips/TIPS_terminology.md`` in backticks reads
    as "go look at this file," but the path is root-relative while every reader
    resolves it from the page's own folder — so the desktop app and any local
    Markdown viewer open `<this folder>/07_Concepts/tips/…` and 404.  On GitHub
    and the built site it is inert code text, which is why this class survived
    every existing check: `check_links` only sees real links.

    That invisibility is the real cost.  Because these are not links, the
    2026-08-02 reorganization's `migrate_concept_links.py` could not rewrite
    them either, so several silently kept pointing at pre-reorg paths
    (`07_Concepts/residual_vote_splitting.md`, `split_voting/*.yaml`) long after
    the files moved.

    Fires only when the path resolves from the repo root but NOT from the
    containing file — i.e. it is provably a real repo file written the wrong way
    round.  A path that resolves from neither is left alone: it is usually a
    reference to some *other* codebase (BetterVoting's
    `packages/frontend/src/i18n/en.yaml`), which is exactly what code text is for.

    Scripts count too (2026-08-07).  The extension list was `md|yaml` at first,
    on the theory that this was a docs-link problem — but "go look at this file"
    is said just as often about a *simulation or tool* as about a page, and nine
    of those were hiding behind the narrower regex (`06_Other/simulations/
    fbc_simulation.py` on the FBC 301 page, the JSON→YAML converter on two
    pages, `build_yaml_pages.py` in ORGANIZATION.md, and so on).

    TRUNCATED paths are caught too, since the 2026-08-07 sweep.  Engine-dir
    shorthand like ``tests/test_sim_star_model.py`` names a file that really
    lives at `STARVote_LH_tabulation_engine/tests/…`, so it resolves from
    neither the page nor the root and used to fall through the other-codebase
    escape hatch above — invisible to every check in the repo.  It is the same
    defect wearing a shorter name: 19 of them across 15 reader-facing pages, on
    lines that read "the guard test is X" with no way to reach X.  They are
    identified by a *basename* search, and only a unique hit whose tail matches
    on a path boundary counts, so an other-codebase path still has to coincide
    exactly with one repo file to be claimed — and if it somehow does, linking
    it is not the wrong answer anyway.

    `CLAUDE.md` is exempt, and that exemption is the whole reason this rung can
    be a gate.  It holds 16 of these and they are idiomatic there: it tells the
    reader to run pytest *from the engine dir*, so `tests/…` is the correct
    thing to type, not a broken link.  A working-instruction file addresses
    someone with a shell open; a teaching page addresses someone with a mouse.
    """
    bad = []
    for rel, text in sorted(_hand_authored_pages()):
        exempt = os.path.basename(rel) == "CLAUDE.md"
        here = os.path.dirname(os.path.join(REPO, rel))
        for i, line in enumerate(text.splitlines(), 1):
            for m in _CODE_SPAN_PATH.finditer(line):
                path = m.group(1)
                if "/" not in path:
                    continue
                if line[m.end():m.end() + 2] == "](":
                    continue          # already the label of a real link
                if os.path.exists(os.path.join(here, path)):
                    continue          # resolves from the page — correct as written
                if os.path.exists(os.path.join(REPO, path)):
                    fixed = os.path.relpath(os.path.join(REPO, path), here or REPO)
                    bad.append((f"{rel}:{i}",
                                f"`{path}` is a repo-root path in code text — readers "
                                f"resolve it from this page's folder and get a 404. "
                                f"Link it: [`{os.path.basename(path)}`]({fixed})"))
                    continue
                if exempt:
                    continue          # engine-dir shorthand, addressed to a shell
                hits = _repo_files_named(os.path.basename(path))
                hits = [h for h in hits if h.endswith("/" + path)]
                if len(hits) != 1:
                    continue          # ambiguous, or not a repo file (other codebase)
                fixed = os.path.relpath(os.path.join(REPO, hits[0]), here or REPO)
                bad.append((f"{rel}:{i}",
                            f"`{path}` is a truncated repo path in code text — the "
                            f"file is at {hits[0]}, so it resolves from neither this "
                            f"page nor the repo root. Link it: [`{path}`]({fixed})"))
    return bad


# Paths in CLAUDE.md that are deliberately unresolvable.  Both are QUOTATIONS
# inside its own writeup of the bare-code-text bug, not references to anything:
# the first is its worked example of a path that rotted through the 2026-08-02
# reorganization, the second its example of a legitimate reference to ANOTHER
# codebase (BetterVoting's).  Each has to stay broken to keep being an example
# — "fixing" either one deletes the point the sentence is making.
_CLAUDE_MD_ILLUSTRATIVE = {
    "07_Concepts/residual_vote_splitting.md",
    "packages/frontend/src/i18n/en.yaml",
}


# A ballot row as this repo writes one: single-character cells (a 0–5 score or a
# blank/abstention marker) joined by commas.  Two cells minimum, so an ordinary
# "5, 4" in prose needs the comma run to look like a ballot before we look further.
_BALLOT_ROW = re.compile(
    r"^\s*(?P<row>[-~&?%0-5](?:\s*,\s*[-~&?%0-5])+)\s*(?P<rest>\S.*)$")

# The multiplier written on the WRONG side.  Two shapes, both deliberately tight:
# the rest of the line *opens* with it (`× 5   Andre`, `×3`), or a real `×` glyph
# turns up later in an annotation (`← the 3-voter majority (×3)`).  Bare `x`/`X`
# is only honoured in the first position — anywhere else it matches prose.
_WEIGHT_AFTER_ROW = re.compile(r"^[xX×]\s?\d+\b|[(\s]×\s?\d+\b")


def check_ballot_weight_side():
    """Return [(rel:line, msg)] for ballot rows whose weight trails the scores.

    One election is written one way everywhere else in the repo: the count comes
    FIRST.  That is the YAML schema (`Count:Ada,Ben,Cara` / `15:5,2,0` — the
    engine's parser only ever matches a *leading* weight, so a source file
    physically cannot drift), and it is what the engine echoes back
    (`Count × Memphis,…` / `42 × 5,4,3,2`).  Hand-authored Markdown is the one
    surface with no parser and no generator holding the line, so that is exactly
    where `0,4,5   ×3` accumulates — and a reader who meets both forms has to
    work out, per page, which number is the ballot and which is the bloc size.

    Scans hand-authored pages and the election YAMLs.  A YAML's `ballots:` block
    is already safe by construction, so a hit there is in a comment or a
    `scenario_description` — prose that teaches the wrong form just as loudly.
    """
    bad = []

    def _scan(rel, text):
        for i, line in enumerate(text.splitlines(), 1):
            m = _BALLOT_ROW.match(line)
            if not m:
                continue
            if not _WEIGHT_AFTER_ROW.search(m.group("rest")):
                continue
            row = re.sub(r"\s+", "", m.group("row"))
            bad.append((f"{rel}:{i}",
                        f"ballot row `{row}` carries its weight AFTER the scores — "
                        f"put the count first (`N × {row}`, under a `Count × …` "
                        f"header), the way the YAML schema and the engine's own "
                        f"echo write it"))

    for rel, text in sorted(_hand_authored_pages()):
        _scan(rel, text)

    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and d != "site"]
        for fn in sorted(filenames):
            if not fn.endswith((".yaml", ".yml")):
                continue
            p = os.path.join(dirpath, fn)
            rel = os.path.relpath(p, REPO).replace(os.sep, "/")
            if "_tabulated" in rel:
                continue          # generated mirror — it echoes the source
            try:
                text = open(p, encoding="utf-8").read()
            except OSError:
                continue
            if "ballots:" not in text and "grades:" not in text:
                continue          # not an election file
            _scan(rel, text)

    return bad


def check_claude_md_paths(source=None):
    """Return [(rel:line, msg)] for CLAUDE.md path references that no longer resolve.

    CLAUDE.md is the one file where a root-relative path in code text is already
    correct: it sits AT the repo root, so root-relative is page-relative, and
    `check_code_span_paths` rightly has nothing to say about its ~41 paths.  It
    is also deliberately not a wall of links — it loads into context every
    session, and the reader who needs a clickable href least is the one reading
    it there.

    But "correct today" and "checked" are different things, and nothing checked
    these.  They are inert text, so a folder move rots them **silently**, in the
    file that both the contributor docs and every agent session take their
    instructions from.  That is not hypothetical: it is exactly how the
    2026-08-02 reorganization left four pages naming pre-reorg paths, which is
    the story CLAUDE.md itself tells a few lines above one of them.

    So this rung checks *reachability, not form* — the complement of
    check_code_span_paths, which checks form and ignores this file.  A path
    passes if it resolves from the repo root, or if its tail uniquely matches
    one repo file (the `tests/…` engine-dir shorthand, correct to type from the
    engine dir and exempted there for that reason).  Bare filenames with no
    slash are not checked: `README.md` appears 11 times meaning "a folder's
    README", and `_bv_export.json` / `_tabulated.txt` / `_201.md` are naming
    conventions and suffixes rather than files.

    `source` overrides the file read, for the non-vacuity test.  It exists so
    that test never has to write to the real CLAUDE.md: this checkout is often
    open in two sessions at once, and a probe left behind by a crashed run
    would corrupt the operating contract both of them are following.  Paths are
    still resolved against the repo root either way — that root-relative
    reading is the whole premise, not a property of where the file sits.
    """
    bad = []
    if source is None:
        path_ = os.path.join(REPO, "CLAUDE.md")
        if not os.path.exists(path_):
            return bad
        with open(path_, encoding="utf-8") as fh:
            text = fh.read()
    else:
        text = source
    for i, line in enumerate(text.splitlines(), 1):
        for m in _CODE_SPAN_PATH.finditer(line):
            path = m.group(1)
            if "/" not in path:
                continue          # a file's NAME, not a location — see docstring
            if path in _CLAUDE_MD_ILLUSTRATIVE:
                continue          # deliberately broken; it IS the example
            if os.path.exists(os.path.join(REPO, path)):
                continue          # resolves from the root, where CLAUDE.md lives
            hits = [h for h in _repo_files_named(os.path.basename(path))
                    if h.endswith("/" + path)]
            if len(hits) == 1:
                continue          # engine-dir shorthand, still reachable
            near = _repo_files_named(os.path.basename(path))
            where = f" (basename now at: {', '.join(near[:3])})" if near else \
                    " (basename found nowhere in the repo)"
            bad.append((f"CLAUDE.md:{i}",
                        f"`{path}` no longer resolves{where}. CLAUDE.md's paths "
                        f"are inert code text, so nothing else catches this — "
                        f"repoint it, or add it to _CLAUDE_MD_ILLUSTRATIVE if it "
                        f"is a deliberate example."))
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
    folder_links = check_folder_links()
    if not folder_links:
        print("repo-hygiene: ✓ every folder link names its README.md.")
    else:
        rc = 1
        print(f"repo-hygiene: ⚠️  bare folder links ({len(folder_links)}) — these "
              "resolve on GitHub and on the site, but MkDocs leaves the href")
        print("              UNREWRITTEN (\"left as is\" in the build log) so the "
              "published page 404s, and a local viewer can't open them either.")
        print("              Name the README.md explicitly:")
        for rel, raw, fixed in folder_links:
            print(f"   • {rel}  →  ({raw})  → use ({fixed})")
    untracked_targets = check_untracked_link_targets()
    if not untracked_targets:
        print("repo-hygiene: ✓ every link target on a committed page is itself committed.")
    else:
        rc = 1
        print(f"repo-hygiene: ⚠️  committed pages linking to UNCOMMITTED files "
              f"({len(untracked_targets)}) — these resolve in your working")
        print("              tree, so the link check above passes, but CI builds the "
              "COMMITTED tree, where the target is")
        print("              missing, and `mkdocs build --strict` fails the docs deploy "
              "on it. Commit the target alongside")
        print("              the page, or drop the link until it lands:")
        for line in format_untracked_report(untracked_targets):
            print(line)
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
        print("repo-hygiene: ✓ no hand-pasted engine reports on hand-authored pages"
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
    span_paths = check_code_span_paths()
    if not span_paths:
        print("repo-hygiene: ✓ no repo-root paths written as bare code text.")
    else:
        rc = 1
        print(f"repo-hygiene: ⚠️  repo-root paths in code text ({len(span_paths)}) — "
              "inert on GitHub and the site, but the desktop app and any local")
        print("              Markdown viewer resolve them from the page's own folder "
              "and 404. They are also invisible to check_links and to")
        print("              migrate_concept_links.py, so they rot silently through "
              "a folder move — make them links:")
        for rel, msg in span_paths:
            print(f"   • {rel}\n       {msg}")
    weight_side = check_ballot_weight_side()
    if not weight_side:
        print("repo-hygiene: ✓ every ballot row puts its weight before the scores.")
    else:
        rc = 1
        print(f"repo-hygiene: ⚠️  ballot weights written after the scores "
              f"({len(weight_side)}) — the YAML schema and the engine's echo both")
        print("              put the count FIRST (`Count × Ada,Ben,Cara` / "
              "`3 × 5,2,0`), and a source file cannot drift because the parser")
        print("              only matches a leading weight. Hand-authored Markdown "
              "is the one surface with nothing holding the line, so mixing")
        print("              the two forms makes a reader decide per page which "
              "number is the ballot and which is the bloc size:")
        for rel, msg in weight_side:
            print(f"   • {rel}\n       {msg}")
    claude_paths = check_claude_md_paths()
    if not claude_paths:
        print("repo-hygiene: ✓ every path CLAUDE.md names still resolves.")
    else:
        rc = 1
        print(f"repo-hygiene: ⚠️  stale paths in CLAUDE.md ({len(claude_paths)}) — "
              "these are inert code text, correct as written from the repo")
        print("              root, and therefore invisible to every other check "
              "here. CLAUDE.md is what both contributors and each agent")
        print("              session take their instructions from, so a path that "
              "rots there is followed for weeks before anyone notices:")
        for rel, msg in claude_paths:
            print(f"   • {rel}\n       {msg}")
    # exit non-zero so a caller *can* gate on it; the pre-commit hook runs it
    # warn-only, and tests/test_md_links.py gates on the link half.
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
