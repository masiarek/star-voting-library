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

# Sibling script: it owns the ballot-art geometry AND the ballot-row parsing, so
# the alt text under an image is derived from the same read of the YAML that
# drew it. (Path-inserted rather than package-imported because the tests load
# this file by path, which leaves the script's own directory off sys.path.)
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPT_DIR not in sys.path:
    sys.path.insert(0, _SCRIPT_DIR)
import build_style_ballot_images as ballot_art  # noqa: E402

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
    "star":        ("STAR (single winner)", "01_STAR/01_Learn/README.md"),
    "approval":    ("Approval Voting", "04_Approval/01_Learn/README.md"),
    "rankedrobin": ("Ranked Robin (RCV-RR / Copeland)", "05_Ranked_Robin/01_Learn/README.md"),
    "rcv_irv":     ("RCV-IRV (Instant Runoff)", "06_Other/RCV_IRV/concepts/README.md"),
    "bloc":        ("Bloc STAR (multi-winner, majoritarian)", "03_STAR_PR/01_Learn/README.md"),
    "sss":         ("Sequentially Spent Score (proportional STAR)", "03_STAR_PR/01_Learn/README.md"),
    "rrv":         ("Reweighted Range Voting (proportional STAR)", "03_STAR_PR/01_Learn/README.md"),
    "allocated":   ("Allocated Score (proportional STAR)", "03_STAR_PR/01_Learn/README.md"),
    "stv":         ("STV (proportional, ranked ballots)", "03_STAR_PR/01_Learn/README.md"),
    "cav":         ("Combined Approval Voting (CAV)", "06_Other/Combined_Approval/README.md"),
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
    # Range/Score voters are handed a different piece of paper from STAR's — no
    # stars, and the scale is the election's rather than a fixed 0–5. Calling it
    # "score" here is what once put a star ballot on the Range page.
    if method in ballot_art.RANGE_BALLOT_METHODS:
        return "range"
    return "score"

HOW_TO_READ = {
    "score":    "Row 1 = candidate names; each later row is one voter's 0–5 scores "
                "(a `N ×` prefix = N identical ballots).",
    "range":    "Row 1 = candidate names; each later row is one voter's scores on "
                "this election's scale, 0 = worst "
                "(a `N ×` prefix = N identical ballots).",
    "approval": "Row 1 = candidate names; each later row is one voter's approvals "
                "(`1` = approve, `0`/blank = not approved).",
    "ranked":   "Each row is one voter's ranking, most-preferred first "
                "(`N:` prefix = N identical ballots).",
}


# --------------------------------------------------------------------------- #
# Ballot art — the picture of the ballot, when a case has one
# --------------------------------------------------------------------------- #
# Convention, not configuration: if `<yaml dir>/img/<stem>_ballot_<n>.png` exists
# it goes on the page. Draw it with
#
#     python STARVote_LH_tabulation_engine/tools_adam/scripts/build_style_ballot_images.py --from-yaml <case.yaml>
#
# A CSV row says what the engine read; the ballot art says what the voter did —
# for a 101 case that picture is the lesson, and the CSV is the receipt.
_ART_RE = re.compile(r"_ballot_(\d+)\.png$")


def _esc_attr(text):
    # ">" MUST be escaped too: a ballot row comment naturally contains one
    # ("Almond > Berry > Cocoa"), and a Markdown inline-HTML parser ends the tag
    # at the first ">", spilling the rest of the tag onto the page as text.
    return (str(text).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


# A table cell will happily crush an image to 68px: `max-width: 100%` (both
# Material's CSS and GitHub's) makes the picture's min-content width ~0, so the
# auto table layout hands the column whatever the score columns don't want. The
# `min-width` is what keeps the ballot legible; the table scrolls inside its own
# container instead. Wider casts get a smaller picture so the table still fits.
def _art_width(n_cast, kind="score", max_score=5):
    """Rendered width for one ballot picture.

    A grade ballot ignores the cast size: it never shares a row (see
    `_ballot_art`), so its width is set purely by legibility. Its headings are
    drawn at 1.9% of the image width, so 640px puts them at ~12px and anything
    under ~575 starts to fail — which is precisely why it cannot sit beside a
    column per candidate in a 688px content column.
    """
    if kind == "grade":
        return 640
    # A wide Range ballot has the same problem for the same reason: 0–9 is 11
    # bubble columns on a canvas ~15% wider than the 0–5 grid, so at the usual
    # 330px the digits land around 8px and stop being legible. Give it the grade
    # ballot's width. A 0–5 Range ballot is geometrically the STAR grid with the
    # stars removed, so it keeps the ordinary widths.
    if kind == "range" and max_score > 5:
        return 640
    if n_cast <= 3:
        return 330
    return 260 if n_cast <= 6 else 220


# Past this many candidates, a column per candidate stops being a ballot you can
# read across and becomes a spreadsheet — one Scores column instead.
MAX_CANDIDATE_COLUMNS = 6


def _grade_art_args(yaml_path, data, page_dir):
    """`_ballot_art` arguments for a `grades:` case file, or None.

    A grade file is not an election YAML — no `ballots:` block, no mirror, no
    generated page — but it is still a ballot somebody marked, and the transposed
    table it stores (a row per candidate) is exactly what a beginner cannot read.
    So the art comes from the same place it does for every other case, and this
    turns the file into the (cast, rows) shape the table builder wants.
    """
    try:
        scale = ballot_art.grade_scale(data.get("grade_scale", "1-10"))
        cast, rows, voters = ballot_art.parse_grade_block(
            data["grades"], scale, data.get("voter_notes"))
    except (ballot_art.CaseBallotError, KeyError, AttributeError):
        return None
    titles = [ballot_art.grade_row_title(v, r.note) for v, r in zip(voters, rows)]
    return dict(parsed=(cast, rows), kind="grade", grades=tuple(scale), titles=titles)


def _ballot_art(yaml_path, ballots_text, page_dir, kind="score",
                parsed=None, grades=(), titles=None):
    """(caption, table lines, text lead-in) for this case's art, or None.

    The table is the point: one row per ballot, the marked-up picture beside the
    very numbers the file records, under a column per candidate. A beginner can
    read a filled bubble straight across into its column instead of being asked
    to hold the CSV and the picture in their head at once.

    `kind` picks which ballot was drawn ("score", "approval" or "grade") so the
    caption and the alt text describe the paper the voter actually held. A grade
    case arrives already `parsed` (its block is transposed, so the parser is a
    different one) and carries its `grades` scale and per-voter `titles`, which a
    `#` comment can't supply on that layout.
    """
    stem = os.path.splitext(os.path.basename(yaml_path))[0]
    img_dir = os.path.join(os.path.dirname(yaml_path), "img")
    found = []
    for path in glob.glob(os.path.join(glob.escape(img_dir), glob.escape(stem) + "_ballot_*.png")):
        m = _ART_RE.search(path)
        if m:
            found.append((int(m.group(1)), path))
    if not found:
        return None
    found.sort()

    if parsed is not None:
        cast, rows = parsed
    else:
        # A Range case is parsed against ITS OWN scale, not STAR's. Parsing a
        # 0–9 ballot with the default 0–5 cap raised CaseBallotError and the art
        # was silently dropped — the picture sat on disk and no page showed it,
        # which is exactly the failure `test_ballot_art` exists to catch.
        cap = ballot_art.RANGE_DRAW_MAX if kind == "range" else ballot_art.MAX_SCORE
        try:
            cast, rows = ballot_art.parse_ballot_block(ballots_text, cap)
        except ballot_art.CaseBallotError:
            return None              # art we can't line up with the numbers

    # Same rule the range engine and the drawer use: the scale is the highest
    # score anyone actually gave, so picture, page and report agree.
    max_score = 5
    if kind == "range":
        max_score = max(
            [s for r in rows for s in r.scores if s is not None] or [1]) or 1

    by_candidate = len(cast) <= MAX_CANDIDATE_COLUMNS
    width = _art_width(len(cast), kind, max_score)
    spill = {"approval": "Approvals", "grade": "Grades"}.get(kind, "Scores")

    drawn = []
    for n, path in found:
        if not 1 <= n <= len(rows):
            continue
        row = rows[n - 1]
        title = (titles[n - 1] if titles
                 else ballot_art.row_title(n, row.weight, row.note))
        alt = ballot_art.alt_text(ballot_art.Ballot(
            title, cast, row.scores, img_dir, quoted=False, kind=kind,
            grades=tuple(grades), max_score=max_score))
        src = os.path.relpath(path, page_dir).replace(os.sep, "/")
        drawn.append((row, alt, src))
    if not drawn:                    # art on disk, but none of it matched a row
        return None

    if kind == "grade":
        # A grade ballot STACKS instead of sharing a row. Beside a column per
        # candidate the table measured 974px against a 688px content column and
        # simply spilled: MkDocs Material leaves these wrappers at
        # `overflow-x: visible`, so the grades were unreachable rather than
        # merely off-screen. Shrinking the picture is not the way out — its
        # word-headings stop being readable under ~575px — so the grades the
        # file records go UNDER each ballot instead of beside it. Dropping
        # `min-width` here is deliberate too: with nothing to defend a table
        # column, the picture may scale down on a narrow screen, and the text
        # line below is what carries the grades when it does.
        lines = []
        for row, alt, src in drawn:
            lines.append(f'<img src="{src}" width="{width}" '
                         f'alt="{_esc_attr(alt)}">')
            cells = [c if c else "—" for c in row.cells]
            said = " · ".join(f"{who} **{g}**" for who, g in zip(cast, cells))
            if row.weight > 1:
                said = f"×{row.weight} — {said}"
            lines += ["", said, ""]
        lines.pop()                  # no trailing blank inside the block
    else:
        # No `Voters` column: the picture's own title states the count for a
        # weighted row (`row_title` guarantees it), so a column repeating it
        # bought nothing and cost 100px — enough to push a weighted table to
        # 694px against a 688px content column, where it silently spilled off
        # the page. The alternative was shrinking every picture to 260px, which
        # traded legibility everywhere for a fit it still didn't achieve.
        header = (["Ballot as marked"]
                  + (list(cast) if by_candidate
                     else [f"{spill} ({', '.join(cast)})"]))
        align = [":--"] + [":--:"] * (len(header) - 1)
        lines = ["| " + " | ".join(header) + " |", "|" + "|".join(align) + "|"]
        for row, alt, src in drawn:
            img = (f'<img src="{src}" width="{width}" style="min-width:{width}px" '
                   f'alt="{_esc_attr(alt)}">')
            cells = [c if c else "-" for c in row.cells]
            lines.append("| " + " | ".join(
                [img] + (cells if by_candidate
                         else ["`" + ", ".join(cells) + "`"])) + " |")

    shown = len(drawn)
    caption = "The ballot as marked" if shown == 1 else "The ballots as marked"
    lead = ("The same ballot as the file records it:" if shown == 1
            else "The same ballots as the file records them:")
    if shown < len(rows):
        # Never let a partial set read as the whole electorate.
        caption += f" (the first {shown} of {len(rows)} ballot rows)"
        lead = "Every ballot in the file, as text:"
    caption += (" — a filled **Yes** is a `1` in that candidate's column, a filled "
                "**No** a `0`:" if kind == "approval" else
                " — the filled bubble is the grade given, and the grade is the "
                "word in its column. The grades the file records are repeated "
                "under each ballot:" if kind == "grade" else
                " — the filled bubble is the score given, and the score is the "
                "number in its column:")
    return caption, lines, lead


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


# The engine-report fence is wrapped in pymdownx.snippets section markers so a
# hand-authored companion page can include exactly this block:
#
#     --8<-- "<set>/cases/cases_pages/<stem>.md:report"
#
# written bare (not inside a fence — the include brings its own). That is how a
# companion shows the count without pasting it: same idiom readme.md uses to
# feed index.md. Including the `_tabulated` mirror instead would drag in the
# ~50-line YAML echo and, on a big field like the CA governor case, 785 lines of
# audit. HTML comments render as nothing, so the generated page is unchanged.
SNIPPET_START = "<!-- --8<-- [start:report] -->"
SNIPPET_END = "<!-- --8<-- [end:report] -->"

# Ballot art on a HAND-AUTHORED page can't use that include: the <img> paths in
# the generated table are relative to the generated page, and a snippet is
# pasted verbatim, so every picture would 404 from a page at a different depth.
# Instead a lesson page marks the spot and this script fills it in, with paths
# relative to THAT page:
#
#     <!-- ballots:small_abstention_c2_b5 -->
#     <!-- /ballots -->
#
# Same contract as `case-meta`: everything between the markers is generated,
# everything outside is the author's, and the staleness test fails on drift.
#
# A case with no picture still fills the block — with the file's own `ballots:`
# text in a fence, the same rendering its generated page carries. That is the
# only surface a RANKED case ever had: nothing draws a ranked ballot (the drawer
# refuses them outright), so before this every ranked lesson hand-typed its
# profile as a Markdown table — 38 pages of an election transcribed by hand
# beside a generated report of the same file, with no check that the two agreed
# and two readings of the leading column (`| 9 | A > B > C |` is nine voters,
# `| 3 | Clara > Amy > Bruno |` is voter #3) live on one page in
# `topics/ties/batch_elimination.md`. The schema form has neither problem: it is
# the file, so it cannot drift, and `N:` means one thing.
BALLOT_BLOCK_RE = re.compile(
    r"<!-- ballots:([A-Za-z0-9_.\-]+) -->\n?(.*?)<!-- /ballots -->", re.S)

# The engine report on a hand-authored page turned out to have the same problem,
# reached from the other side. Writing the include bare —
#
#     --8<-- "<set>/cases/cases_pages/<stem>.md:report"
#
# renders the count on the MkDocs site and NOTHING on GitHub, which has never
# heard of pymdownx.snippets and prints the directive itself as a line of
# literal text. Since this repo is read on both surfaces, 82 pages were showing
# a "What the engine says" heading followed by `--8<-- "…"` and no report.
#
# So the report gets the ballot-art treatment: the lesson marks the spot,
#
#     <!-- report:bv2105r2_w3vvff_ice_cream_recheck -->
#     <!-- /report -->
#
# and this script pastes in exactly what the include used to pull — the fence
# between SNIPPET_START/SNIPPET_END on that case's generated page. One source of
# truth still (the generated page, itself built from the `_tabulated` mirror),
# drift still fails a test, and now it renders on both surfaces. The marker
# names a bare stem because generated-page stems are unique repo-wide; a
# collision drops the stem from the index rather than guessing between them.
REPORT_BLOCK_RE = re.compile(
    r"<!-- report:([A-Za-z0-9_.\-]+) -->\n?(.*?)<!-- /report -->", re.S)

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
    disp, docs = METHOD_DOCS.get(method, (str(method), "07_Concepts/README.md"))
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
    art = _ballot_art(yaml_path, ballots_text, page_dir, kind)
    if art:
        caption, table, lead = art
        L.append(caption)
        L.append("")
        L += table
        L.append("")
        L.append(lead)
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
            L.append(SNIPPET_START)
            L.append("```text")
            L.append(lead)
            L.append("```")
            L.append(SNIPPET_END)
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
            L.append(SNIPPET_START)
            L.append("```text")
            L.append(report)
            L.append("```")
            L.append(SNIPPET_END)
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
def _has_ballots(path):
    """True when this yaml is an election file render() will produce a page for.

    Mirrors render()'s own precondition (a `ballots:` key somewhere in the file);
    kept next to the caller that needs it so the sibling list and the page set
    cannot drift apart."""
    try:
        data = yaml.safe_load(open(path, encoding="utf-8").read())
    except Exception:
        return False
    return isinstance(data, (dict, list)) and _find_first(data, ["ballots"]) is not None


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
            # `ymls` becomes the "More cases in this set" footer on every page in
            # the folder, so it must list only files that GET a page. render()
            # returns None for a yaml with no `ballots:` block — the grade-ballot
            # cases in felsenthal_paradoxes/cases are the live example, carrying a
            # `grades:` block instead because Felsenthal's 1-10 and A-J scales fit
            # neither the engine's 0-5 validation nor BetterVoting. Listing them
            # anyway pointed 71 case pages at 5 pages that are never written.
            ymls = [f for f in ymls if _has_ballots(os.path.join(dirpath, f))]
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


# --------------------------------------------------------------------------- #
# Placeable managed blocks — where they may live, and what a bare stem means
# --------------------------------------------------------------------------- #
# Hand-authored pages that place a `ballots:` or `report:` marker live all over
# the repo, not just under ROOTS — 07_Concepts/, YAML_library/ and the method
# folders all use them — so this walk starts at the repo root. Both markers have
# to be found by the SAME walk: the ballot half once walked ROOTS only, which
# meant a block on a cross-method concept page was never even looked at. It got
# no fill and, worse, no note, because `ballot_blocks_for()` (which writes the
# note) was never called on that page — and `check_ballot_blocks()` inherited the
# blind spot, so no test could catch the page shipping without its picture.
#
# `_notes/` and CLAUDE.md are skipped because they DOCUMENT the markers; filling
# in a doc's example would turn the documentation into a report.
_SKIP_DIRS = ("site", "node_modules", "_notes", "img")
_SKIP_FILES = ("CLAUDE.md", "AGENTS.md")


def _hand_authored_md_pages():
    """Every hand-authored Markdown page in the repo that a marker may sit on."""
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames
                       if not d.startswith(".") and d not in _SKIP_DIRS
                       and not d.endswith(GENERATED_SUFFIXES)]
        for fn in sorted(filenames):
            if fn.endswith(".md") and fn not in _SKIP_FILES:
                yield os.path.join(dirpath, fn)


_PAGES_BY_STEM = None


def _generated_pages_by_stem():
    """{stem: absolute generated page path}, built once.

    A stem that appears twice is dropped rather than resolved by guesswork —
    the callers then leave a visible note, which is the honest answer to an
    ambiguous marker.
    """
    global _PAGES_BY_STEM
    if _PAGES_BY_STEM is None:
        idx, dupes = {}, set()
        for dirpath, dirnames, filenames in os.walk(REPO):
            dirnames[:] = [d for d in dirnames
                           if not d.startswith(".") and d not in _SKIP_DIRS]
            if not os.path.basename(dirpath).endswith("_pages"):
                continue
            for fn in filenames:
                if not fn.endswith(".md"):
                    continue
                stem = fn[:-3]
                if stem in idx:
                    dupes.add(stem)
                idx[stem] = os.path.join(dirpath, fn)
        for stem in dupes:
            idx.pop(stem, None)
        _PAGES_BY_STEM = idx
    return _PAGES_BY_STEM


def _case_by_stem(stem):
    """The case YAML behind a bare `<stem>`, found repo-wide, or None.

    Resolution runs through the generated-page index rather than the filesystem,
    which makes it unambiguous by construction: a generated page sits at
    `<folder>/<folder>_pages/<stem>.md` beside `<folder>/<stem>.yaml`, and a
    stem claimed by two pages is dropped from the index instead of guessed at.
    That is what lets `report:` accept a bare stem with no path, and it is the
    same guarantee a `ballots:` stem needs when the page asking for the art
    lives in a different tree from the case.
    """
    page = _generated_pages_by_stem().get(stem)
    if not page:
        return None
    folder = os.path.dirname(os.path.dirname(page))
    for ext in (".yaml", ".yml"):
        cand = os.path.join(folder, stem + ext)
        if os.path.isfile(cand):
            return cand
    return None


_GRADE_CASES_BY_STEM = None


def _grade_cases_by_stem():
    """{stem: absolute case path} for the `grades:` files, built once.

    Grade cases — Majority Judgment's words, Felsenthal's A–J letters — are not
    LH election files, so they get no `_tabulated` mirror and no generated page.
    That makes them the one family `_case_by_stem()` structurally cannot see,
    because it is keyed on generated pages. Their ballots *are* drawn, and the
    lesson carrying the art is often in another tree entirely (the §A9 paradox
    page in `07_Concepts/` showing a case from `method_comparisons/`), so
    without this the marker resolves to nothing and the page prints a
    "no case named" note next to art that exists on disk.

    Same contract as the page index: a stem claimed twice is dropped rather than
    guessed at, so this widens the search to one well-defined family without
    giving up the uniqueness guarantee the docstring above relies on.
    """
    global _GRADE_CASES_BY_STEM
    if _GRADE_CASES_BY_STEM is None:
        idx, dupes = {}, set()
        for dirpath, dirnames, filenames in os.walk(REPO):
            dirnames[:] = [d for d in dirnames
                           if not d.startswith(".") and d not in _SKIP_DIRS
                           and not d.endswith("_tabulated")]
            for fn in filenames:
                if not fn.endswith((".yaml", ".yml")):
                    continue
                path = os.path.join(dirpath, fn)
                try:
                    text = open(path, encoding="utf-8").read()
                except OSError:
                    continue
                if not re.search(r"^grades:", text, re.M):
                    continue
                stem = fn.rsplit(".", 1)[0]
                if stem in idx:
                    dupes.add(stem)
                idx[stem] = path
        for stem in dupes:
            idx.pop(stem, None)
        _GRADE_CASES_BY_STEM = idx
    return _GRADE_CASES_BY_STEM


# --------------------------------------------------------------------------- #
# Ballot art on hand-authored pages — the placeable managed block
# --------------------------------------------------------------------------- #
def _case_for_stem(page_path, stem):
    """The case YAML a `<!-- ballots:<stem> -->` marker refers to.

    Looked up beside the page (`cases/<stem>.yaml`, the repo-standard layout)
    and in the page's own folder (flat case folders), then one level up — a
    lesson often sits above the folder that holds its cases.

    Failing that, searched *downward* through the page's own subtree, so a
    method's front door (`04_Approval/README.md`) can show a ballot from a case
    two levels below it (`02_Examples/cases/…`). That front door is where a
    beginner actually lands, which makes it the page that most needs a picture.
    The search stays inside the method folder and only accepts a unique hit —
    two same-named cases mean the marker is ambiguous, so it gets nothing rather
    than a coin flip.

    Proximity runs out at the method folder, though, and a cross-method page
    (`07_Concepts/topics/…`) is nowhere near the case it wants to show. Rather
    than widen the *filesystem* search — where a bare stem really could match
    anything — the last resort is `_case_by_stem()`, the same generated-page
    index the `report:` marker resolves through, which is unambiguous by
    construction. Proximity still goes first: it is the one thing that can tell
    two same-named cases apart, and the index just drops those.

    Grade cases need one more step after that: having no generated page, they
    are absent from that index entirely, so `_grade_cases_by_stem()` indexes
    them directly under the same drop-the-duplicates rule.
    """
    here = os.path.dirname(page_path)
    up = os.path.dirname(here)
    for base in (here, up):
        for cand in (os.path.join(base, "cases", stem + ".yaml"),
                     os.path.join(base, stem + ".yaml")):
            if os.path.isfile(cand):
                return cand
    for base in (here, up):
        # Never widen to the repo root: a bare stem there could match anything.
        if not base or os.path.abspath(base) == REPO:
            continue
        hits = sorted(glob.glob(os.path.join(glob.escape(base), "**", stem + ".yaml"),
                                recursive=True))
        if len(hits) == 1:
            return hits[0]
    return _case_by_stem(stem) or _grade_cases_by_stem().get(stem)


def _schema_fence(kind, ballots_text):
    """The case's own `ballots:` text, rendered as its generated page renders it.

    Byte-identical to the generated page's Ballots section (minus the art), so a
    lesson and the case page show one election written one way — and, being the
    file itself, it cannot drift from the report below it.
    """
    lines = [HOW_TO_READ[kind]]
    if re.search(r"[~&?%]|(^|,)\s*-\s*(,|$)", ballots_text, re.M):
        lines += ["", f"Markers on these ballots: {MARKER_LEGEND}."]
    return "\n".join(lines + ["", "```text", ballots_text, "```"]) + "\n"


def ballot_blocks_for(page_path, text=None):
    """The filled-in ballot blocks this page asks for: {marker text: new text}.

    Returns None when the page has no marker. A case with art gets the picture
    table; one without gets `_schema_fence()` — the ballots as the YAML records
    them — because a lesson that asked for its election should get the election,
    and for a ranked case that fence is the only form there is.

    A marker naming a case that *could* be drawn but hasn't been keeps a visible
    note above the fence, and one naming no case at all says so instead: the two
    need opposite fixes (draw the art, or fix the stem), and `check_ballot_blocks
    ()` fails the page on either drifting.
    """
    text = open(page_path, encoding="utf-8").read() if text is None else text
    if not BALLOT_BLOCK_RE.search(text):
        return None
    out = {}
    page_dir = os.path.dirname(page_path)
    for m in BALLOT_BLOCK_RE.finditer(text):
        stem = m.group(1)
        src = _case_for_stem(page_path, stem)
        if not src:
            body = (f"*(No case named `{stem}` in this repo — check the stem "
                    f"against the case file's name.)*\n")
        else:
            rel_src = os.path.relpath(src, REPO).replace(os.sep, "/")
            body = (f"*(No ballot art for `{stem}` — draw it with "
                    f"`build_style_ballot_images.py --from-yaml {rel_src}`.)*\n")
            data = yaml.safe_load(open(src, encoding="utf-8").read())
            ballots = _find_first(data, ["ballots"]) if isinstance(data, (dict, list)) else None
            art = None
            if ballots is not None:
                ballots_text = str(ballots).rstrip("\n")
                kind = _ballot_kind(ballots_text,
                                    _norm_method(_find_first(data, ["voting_method"])))
                art = _ballot_art(src, ballots_text, page_dir, kind)
                if not art:
                    fence = _schema_fence(kind, ballots_text)
                    # Nothing draws a ranked ballot, so the fence isn't a
                    # fallback there — it's the answer, and a "draw it" nudge
                    # would be advice no tool can take.
                    body = fence if kind == "ranked" else body + "\n" + fence
            elif isinstance(data, dict) and data.get("grades") is not None:
                # A grade-ballot file. It gets no generated page of its own, so
                # this block is the ONLY place its ballots are ever drawn for a
                # reader — which makes it the mechanism that matters here.
                kwargs = _grade_art_args(src, data, page_dir)
                if kwargs:
                    art = _ballot_art(src, "", page_dir, **kwargs)
            if art:
                caption, table, _lead = art
                body = "\n".join([caption, "", *table]) + "\n"
        out[m.group(0)] = f"<!-- ballots:{stem} -->\n{body}<!-- /ballots -->"
    return out


def apply_ballot_blocks(text, blocks):
    for old, new in blocks.items():
        text = text.replace(old, new)
    return text


def pages_with_ballot_blocks():
    """{page path: {marker: filled block}} for every page that asks for art."""
    found = {}
    for path in _hand_authored_md_pages():
        blocks = ballot_blocks_for(path)
        if blocks:
            found[path] = blocks
    return found


def check_ballot_blocks():
    """Pages whose ballot block drifted from the art/YAML behind it."""
    stale = []
    for path, blocks in pages_with_ballot_blocks().items():
        cur = open(path, encoding="utf-8").read()
        if apply_ballot_blocks(cur, blocks) != cur:
            stale.append(path)
    return stale


# --------------------------------------------------------------------------- #
# Engine reports on hand-authored pages — the placeable managed block
# --------------------------------------------------------------------------- #
def _generated_report(stem):
    """The report fence from `<stem>`'s generated page, or None."""
    page = _generated_pages_by_stem().get(stem)
    if not page or not os.path.isfile(page):
        return None
    text = open(page, encoding="utf-8").read()
    if SNIPPET_START not in text or SNIPPET_END not in text:
        return None
    return text.split(SNIPPET_START, 1)[1].split(SNIPPET_END, 1)[0].strip("\n")


def report_blocks_for(page_path, text=None):
    """The filled-in report blocks this page asks for: {marker text: new text}.

    Returns None when the page has no marker. The body is the generated page's
    report fence verbatim — the same bytes the `--8<--` include used to pull, so
    converting a page changes what GitHub shows and not what the site shows.
    """
    text = open(page_path, encoding="utf-8").read() if text is None else text
    if not REPORT_BLOCK_RE.search(text):
        return None
    out = {}
    for m in REPORT_BLOCK_RE.finditer(text):
        stem = m.group(1)
        report = _generated_report(stem)
        body = (f"{report}\n" if report else
                f"*(No generated report for `{stem}` — run the case once, then "
                f"`build_yaml_pages.py`.)*\n")
        out[m.group(0)] = f"<!-- report:{stem} -->\n{body}<!-- /report -->"
    return out


def apply_report_blocks(text, blocks):
    for old, new in blocks.items():
        text = text.replace(old, new)
    return text


def pages_with_report_blocks():
    """{page path: {marker: filled block}} for every page that asks for a report."""
    found = {}
    for path in _hand_authored_md_pages():
        blocks = report_blocks_for(path)
        if blocks:
            found[path] = blocks
    return found


def check_report_blocks():
    """Pages whose report block drifted from the generated page behind it."""
    stale = []
    for path, blocks in pages_with_report_blocks().items():
        cur = open(path, encoding="utf-8").read()
        if apply_report_blocks(cur, blocks) != cur:
            stale.append(path)
    return stale


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

    art_pages = pages_with_ballot_blocks()
    drawn = 0
    for p, blocks in sorted(art_pages.items()):
        cur = open(p, encoding="utf-8").read()
        new = apply_ballot_blocks(cur, blocks)
        if new != cur:
            open(p, "w", encoding="utf-8").write(new)
            drawn += 1
    print(f"ballot blocks: {len(art_pages)} hand-authored page(s) ({drawn} updated)")

    # Last: the generated pages above are what these blocks copy from.
    report_pages = pages_with_report_blocks()
    embedded = 0
    for p, blocks in sorted(report_pages.items()):
        cur = open(p, encoding="utf-8").read()
        new = apply_report_blocks(cur, blocks)
        if new != cur:
            open(p, "w", encoding="utf-8").write(new)
            embedded += 1
    print(f"report blocks: {len(report_pages)} hand-authored page(s) ({embedded} updated)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
