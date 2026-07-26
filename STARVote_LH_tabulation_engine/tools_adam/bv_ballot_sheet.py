#!/usr/bin/env python3
"""
bv_ballot_sheet.py — generate printable STAR paper ballots for a demo / classroom
hand-count exercise, tied to a BetterVoting (BV) election.

The teacher's front-of-workflow tool: you make a real election on BetterVoting,
then print matching paper ballots so a room can vote by hand, hand-count the result
(see 00_start_here/STAR_Voting/hands_on/count_star_by_hand.md), and compare to BV's official
tally. Output is a **print-ready PDF** (the only format), rendered from the ballot
HTML via headless Chromium. Each ballot carries the STAR instructions, a 0-5 bubble
grid per candidate, two QRs (vote + results), and the BV election id — so paper and
platform stay linked. Default is one ballot per page.

ONE input route (by design — see bv_ballot_sheet_FSD.md §5.1):
  --bv-export FILE     a BetterVoting export JSON. Everything the ballot needs —
                       title, candidates, election id, and the election + race
                       descriptions — comes from the export. So the workflow is
                       always: create the election on BV -> export its JSON ->
                       print from that. (`create_bv_test_election.py` saves the
                       JSON automatically when it creates the election.)
  --title / --question / --blurb  optional overrides (e.g. a cleaner ballot title
                        than the verbose BV one; --blurb "" prints no description
                        blurb). Output styling flags: see --help.

Requires `playwright` (PDF render) and `segno` (QR — every ballot links to a live BV
election, so it must be scannable; missing segno is an error unless --no-qr).
`--selftest` runs known-answer checks. Spec: bv_ballot_sheet_FSD.md.

Examples
--------
  python3 bv_ballot_sheet.py --bv-export path/to/<election>_bv_export.json \\
      --title "Best Ice Cream Flavor" --serials --logo assets/BW_long_form.jpg \\
      --verify-bv --out ballots.pdf
  python3 bv_ballot_sheet.py --selftest
"""

import argparse
import base64
import html
import json
import re
import mimetypes
import os
import sys


# --------------------------------------------------------------------------- #
# Read title / candidates / id / descriptions from a BetterVoting export JSON.  #
# --------------------------------------------------------------------------- #
def _find_candidate_names(obj):
    """Best-effort recursive search of a BV export for candidate display names."""
    names = []
    if isinstance(obj, dict):
        if isinstance(obj.get("candidates"), list):
            for c in obj["candidates"]:
                if isinstance(c, dict):
                    nm = c.get("candidate_name") or c.get("name") or c.get("longName")
                    if nm:
                        names.append(str(nm))
            if names:
                return names
        for v in obj.values():
            names = _find_candidate_names(v)
            if names:
                return names
    elif isinstance(obj, list):
        for v in obj:
            names = _find_candidate_names(v)
            if names:
                return names
    return names


def from_bv_export(path, race_index=0):
    """Return (title, bv_id, [candidates], election_desc, race_desc) from a frozen
    BV export JSON. This tool prints ONE contest; `race_index` selects which race
    when the export has several (a multi-race export warns to stderr — see main)."""
    data = json.load(open(path, encoding="utf-8"))
    # A frozen BV UI export nests everything under a capitalized "Election" key
    # (siblings "Ballots"/"Results"); older/plain GETs use lowercase or are flat.
    election = data if not isinstance(data, dict) else (
        data.get("Election") or data.get("election") or data)
    title = election.get("title") or election.get("name")
    bv_id = (election.get("election_id") or election.get("id")
             or data.get("election_id") or data.get("Election", {}).get("election_id"))
    edesc = election.get("description") or None

    races = [r for r in (election.get("races") or []) if isinstance(r, dict)]
    if races:
        # A genuine multi-race export: warn (we print only ONE contest) and let
        # --race pick which. Out-of-range is a clear error, not a silent wrap.
        if len(races) > 1:
            listing = "; ".join(
                f'[{i}] {_race_label(r)}' for i, r in enumerate(races))
            print(f"note: this export has {len(races)} races — printing race "
                  f"[{race_index}] only. Use --race N to pick another.\n"
                  f"      races: {listing}", file=sys.stderr)
        if not (0 <= race_index < len(races)):
            raise SystemExit(f"--race {race_index} is out of range: the export has "
                             f"{len(races)} race(s) (valid 0..{len(races) - 1}).")
        race = races[race_index]
        cands = _find_candidate_names(race) or _find_candidate_names(data)
        rdesc = race.get("description") or None
    else:
        # Single-race or flat export: keep the original recursive candidate search.
        cands = _find_candidate_names(data)
        rdesc = None

    if not cands:
        raise SystemExit(f"Could not find candidate names in {path}.")
    return title, bv_id, cands, edesc, (rdesc or None)


TEST_ID_RE = re.compile(r"^\s*BV\w*\d\w*\s*(?:—|–|-{1,2}|:)\s*")


def strip_test_id(text):
    """Drop a leading repo Test ID ("BV2252 — ") from a title.

    The BV<n> id is an INTERNAL cross-reference (registry, sheet, git) and rides
    the BV election + race titles on purpose — but it means nothing to a voter
    holding a paper ballot, so it never prints. The ballot's traceable id is the
    election id in the footer (e.g. 6tthfv), which is what actually resolves.
    Keep it with --keep-test-id."""
    if not text:
        return text
    return TEST_ID_RE.sub("", text, count=1).strip() or text.strip()


def from_spec(name=None, race_index=0):
    """PRE-MINT PREVIEW route: read an election straight from the sibling data
    module `bv_election_specs.py` — BEFORE it exists on BetterVoting.

    Returns the same 5-tuple as from_bv_export(), with bv_id = None (there is no
    election yet, so no QR and no results link). BV elections are PERMANENT and
    undeletable, so this is the cheap look-before-you-leap: print the ballot, read
    the title and candidate list on paper, THEN mint. (An offline route existed
    early on, was removed in the 2026-07 one-route simplification, and is back —
    deliberately — as a preview of a real spec rather than a free-form ballot.)

    `name` is a module attribute (e.g. "GOODBERRYS_SPEC"); omitted, it takes the
    single entry of that module's ELECTIONS list."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    try:
        import bv_election_specs as specs
    except ImportError as ex:                                  # pragma: no cover
        raise SystemExit(f"Could not import bv_election_specs.py ({ex}).")
    catalog = specs.spec_names()
    if name:
        spec = catalog.get(name)
        if spec is None:
            raise SystemExit(f"bv_election_specs.py has no election spec named "
                             f"{name!r}.\nAvailable: " + ", ".join(sorted(catalog)))
    else:
        # ELECTIONS is normally EMPTY (you point it at a spec only for the run that
        # mints it), so bare --spec usually can't guess — name one.
        pool = list(getattr(specs, "ELECTIONS", []) or [])
        if len(pool) != 1:
            raise SystemExit(
                f"ELECTIONS holds {len(pool)} election(s), so there's nothing to "
                f"preview by default — name a spec: --spec NAME\nAvailable: "
                + ", ".join(sorted(catalog)))
        spec = pool[0]

    races = spec.get("races") or [{"title": spec.get("title"),
                                   "candidates": spec.get("candidates") or []}]
    if not (0 <= race_index < len(races)):
        raise SystemExit(f"--race {race_index} is out of range: this spec has "
                         f"{len(races)} race(s) (valid 0..{len(races) - 1}).")
    race = races[race_index]
    if len(races) > 1:
        print(f"note: this spec has {len(races)} races — previewing race "
              f"[{race_index}] only. Use --race N to pick another.", file=sys.stderr)
    cands = list(race.get("candidates") or [])
    if not cands:
        raise SystemExit("That spec/race has no candidates.")
    title = spec.get("title") or race.get("title")
    # The race title stands in for the question line — but a flat (single-race)
    # spec has no race title of its own, so it would just echo the election title.
    rtitle = race.get("title")
    question = rtitle if (rtitle and rtitle != title) else None
    return title, None, cands, spec.get("description"), question


def _race_label(race):
    """A short 'method / title' tag for a race, for the multi-race warning."""
    method = race.get("voting_method") or race.get("votingMethod")
    title = race.get("title") or race.get("race_title")
    if method and title:
        return f"{method}: {title}"
    return str(method or title or "(untitled race)")


# --------------------------------------------------------------------------- #
# HTML ballot rendering.                                                       #
# --------------------------------------------------------------------------- #
INSTRUCTIONS = ("Score each candidate 0 to 5 (fill ONE bubble per row). "
                "Give your favorite 5, your last choice 0 (or leave blank). "
                "Equal scores are allowed. Two or more bubbles in a row is a "
                "spoiled score for that candidate. The two highest-scoring "
                "candidates have an automatic runoff.")

# Printed on every ballot by default: this tool only ever makes DEMO ballots, so
# a standing notice keeps that honest and — crucially — makes the optional serial
# number read as a teaching device, not surveillance (a numbered *real* ballot
# would break the secret ballot). Suppress with --no-notice; override with --notice.
# Kept simple 7-bit ASCII (plain '-') for maximum print/font compatibility.
DEFAULT_NOTICE = "EDUCATION ONLY - a STAR Voting teaching demo, not a secret ballot."

# Where a PREVIEW ballot's stand-in QR points. Deliberately a real but **CLOSED**
# BetterVoting election (BV151 — "Compare RCV-IRV and STAR", state: closed), so a
# scan lands somewhere honest where **no vote can be cast**. The alternatives are
# both worse: an invented election id prints a scannable dead link (the failure
# FR-12 exists to prevent), and an OPEN election would invite a stray vote into
# someone else's tally. Override with --preview-qr URL.
PREVIEW_QR_URL = "https://bettervoting.com/qp8w68/results"
PREVIEW_QR_CAPTION = "TEST ONLY - sample QR"
PREVIEW_WATERMARK = "TEST ONLY"


def qr_data_uri(url):
    """An inline QR (data: URI) for `url` via the pure-python `segno` library, or
    None if segno isn't installed/usable. `main` treats None as an error when a QR is
    needed (a ballot with a live BV id must be scannable) — so segno is effectively
    required unless --no-qr is passed."""
    try:
        import segno
    except ImportError:
        return None
    try:
        return segno.make(url, error="m").svg_data_uri(scale=3, border=1)
    except Exception:
        return None

def verify_bv_id(bv_id, timeout=6):
    """Does a real BetterVoting election with this id exist? Returns True (yes),
    False (definitively no — a 4xx), or None (couldn't check: offline/timeout).
    Stdlib only (urllib). Guards against printing a QR/results link that 404s."""
    import urllib.request
    import urllib.error
    url = f"https://bettervoting.com/API/Election/{bv_id}"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return 200 <= r.status < 300
    except urllib.error.HTTPError as e:
        return False if 400 <= e.code < 500 else None
    except Exception:
        return None


def logo_data_uri(path):
    """Read a local image (SVG/PNG/JPG/…) into a self-contained data: URI so a
    custom logo can replace the drawn STAR wordmark in the ballot header. Returns
    '' on failure (the tool falls back to the built-in facsimile). HTML/PDF only —
    the ASCII output keeps the text wordmark."""
    try:
        data = open(path, "rb").read()
    except OSError:
        print(f"[logo] could not read {path}; using the built-in STAR wordmark.")
        return ""
    if os.path.splitext(path)[1].lower() == ".svg":
        mime = "image/svg+xml"
    else:
        mime = mimetypes.guess_type(path)[0] or "image/png"
    return f"data:{mime};base64,{base64.b64encode(data).decode('ascii')}"


def html_to_pdf(html_str, pdf_path):
    """Render the ballot HTML to a print-ready PDF via headless Chromium (the
    required `playwright` dep). Returns True on success, False if playwright isn't
    installed/usable (the caller then errors). page.pdf() emulates print media, so
    the @media-print page-breaks apply."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.set_content(html_str, wait_until="load")
            page.pdf(path=pdf_path, format="Letter", print_background=True,
                     margin={"top": "0.4in", "bottom": "0.4in",
                             "left": "0.4in", "right": "0.4in"})
            browser.close()
        return True
    except Exception as e:
        print(f"[pdf] PDF render failed ({e}).")
        return False


# A star-with-check lookalike of the STAR Voting mark (inline SVG — we can't embed
# Equal Vote's actual logo asset in a self-contained file, and every ballot says
# EDUCATION ONLY, so this is a teaching facsimile, not their trademark).
STAR_LOGO = ('<svg class="logo" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">'
             '<polygon points="50,6 61,38 95,38 67,58 78,90 50,71 22,90 33,58 5,38 39,38" '
             'fill="none" stroke="#7fa0ad" stroke-width="6" stroke-linejoin="round"/>'
             '<path d="M31,52 L44,65 L71,33" fill="none" stroke="#111" stroke-width="9" '
             'stroke-linecap="round" stroke-linejoin="round"/></svg>')
# Column-header stars use the official STAR-ballot gray for stars (#cccccc).
STAR_OUTLINE = ('<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">'
                '<polygon points="50,6 61,38 95,38 67,58 78,90 50,71 22,90 33,58 5,38 39,38" '
                'fill="none" stroke="#cccccc" stroke-width="6" stroke-linejoin="round"/></svg>')
INSTRUCTION_BULLETS = [
    "Give your favorite candidate(s) five stars.",
    "Give your last choice(s) zero or leave blank.",
    "Equal scores are allowed.",
    "Score other candidates as desired.",
]
EXPLAIN_LINES = [
    "The two highest scoring candidates are finalists.",
    "Your full vote goes to the finalist you prefer.",
    "The finalist with the most votes wins.",
]

CSS = """
:root { color-scheme: light; }
* { box-sizing: border-box; }
@page { size: Letter; margin: 0.4in; }
body { font-family: -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
       margin: 0; color: #111; }
.ballot { position: relative; border: 3px solid #111; border-radius: 10px;
          padding: 16px 22px 14px; margin: 12px; page-break-inside: avoid;
          display: flex; flex-direction: column; overflow: hidden; }
/* overflow:hidden is load-bearing, not cosmetic: the rotated nowrap watermark is
   wider than the page, and Chromium's page.pdf() SCALES the whole document down to
   fit its widest content — which silently shrank every ballot and undid the
   page-fill. Clipping to the ballot box keeps the sheet at 100%. */
.notice { border: 1.5px solid #c0392b; border-radius: 5px; padding: 3px 8px;
          margin: 0 0 10px; font-size: 10.5px; font-weight: 700; color: #c0392b;
          text-align: center; text-transform: uppercase; letter-spacing: .4px; }
.head { display: flex; align-items: flex-start; gap: 18px; margin: 2px 0 4px; }
.head-main { flex: 1 1 auto; min-width: 0; }
.head > .qr { align-self: center; }
.logo-slot { display: flex; align-items: center; justify-content: center; gap: 12px; margin: 0 0 4px; }
.logo-slot .logo { width: 50px; height: 50px; flex: none; }
.logo-slot .blogo { display: block; margin: 0 auto; max-height: 74px; max-width: 100%; }
.logo-slot .word { font-weight: 800; font-size: 30px; letter-spacing: .5px; line-height: 1; }
.logo-slot .tag { font-weight: 800; font-size: 10.5px; letter-spacing: 1.5px; color: #5a7683; margin-top: 3px; }
.title { text-align: center; font-size: 21px; font-weight: 700; margin: 2px 0 1px; }
.edesc { text-align: center; font-style: italic; color: #555; font-size: 13px; margin: 0 0 2px; }
.q { text-align: center; color: #333; font-size: 15px; margin: 0 0 6px; }
.inst { margin: 8px 0 2px 24px; padding: 0; font-size: 17px; }
.inst li { margin: 3px 0; }
.fine { margin: 2px 0 6px 24px; font-size: 12px; color: #666; }
.qr { flex: none; text-align: center; font-size: 9px; color: #555; }
.qr img { display: block; margin: 0 auto; }
.qr .cta { display: block; margin-top: 3px; font-size: 14px; font-weight: 800; color: #111; line-height: 1.15; }
.gridwrap { flex: 1 1 auto; display: flex; }
/* PREVIEW watermark: unmissable on paper, and it can't be cropped off the way a
   header notice can. print-color-adjust keeps Chromium from dropping the color. */
.wm { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center;
      font-size: 104px; font-weight: 900; color: #c0392b; opacity: .13; letter-spacing: 8px;
      transform: rotate(-28deg); pointer-events: none; z-index: 5; white-space: nowrap;
      -webkit-print-color-adjust: exact; print-color-adjust: exact; }
table.grid { border-collapse: collapse; width: 100%; margin: 4px 0 6px; }
.grid td, .grid th { text-align: center; padding: 0; vertical-align: middle; }
.grid td.cand, .grid th.chl { text-align: left; width: 30%; font-weight: 800; font-size: 17px; padding-left: 6px; }
.wb td { font-weight: 800; font-size: 14px; padding: 1px 0; }
.sh { position: relative; height: 36px; }
.sh .star svg { width: 34px; height: 34px; display: block; margin: 0 auto; }
.sh .n { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center;
         font-weight: 800; font-size: 14px; }
.sh .n0 { display: flex; align-items: center; justify-content: center; height: 36px;
          font-weight: 800; font-size: 16px; }
.grid tr.colhead th { border-bottom: 1.5px solid #bbb; }
.grid tr.cand td, .grid tr.cand th { padding: 7px 0; }
.grid tr.alt { background: #ececec; }
.bub { display: inline-flex; align-items: center; justify-content: center; width: 26px; height: 26px;
       border: 2px solid #666; border-radius: 50%; font-weight: 700; font-size: 13px; color: #444; }
.wline { display: inline-block; border-bottom: 1.5px solid #333; width: 62%; height: 1em; }
.explain { text-align: center; font-size: 14.5px; line-height: 1.35; margin: 6px 4px 2px;
           padding-top: 8px; border-top: 1.5px solid #111; }
.foot { margin-top: 8px; font-size: 16px; color: #555; display: flex; justify-content: space-between; align-items: center; gap: 12px; }
.foot .eid { font-weight: 800; color: #111; }
.promo { text-align: center; font-size: 10px; color: #5a7683; margin: 5px 0 0; }
.serial { font-weight: 700; }
@media print { .noprint { display: none; } .ballot { margin: 0 0 8px; }
  .ballot.pagebreak { page-break-after: always; } }
"""


def _colhead(n):
    """A column header cell: 0 plain, 1-5 a star outline with the number inside."""
    if n == 0:
        return '<th class="sh"><span class="n0">0</span></th>'
    return (f'<th class="sh"><span class="star">{STAR_OUTLINE}</span>'
            f'<span class="n">{n}</span></th>')


def render_ballot(title, question, candidates, bv_id, vote_qr_uri=None,
                  results_qr_uri=None, serial=None, write_ins=0,
                  break_after=False, notice="", blurb="", promo="", logo_uri="",
                  qr_size=176, qr_caption="Scan to vote online", watermark=""):
    bubbles = "".join(f'<td><span class="bub">{n}</span></td>' for n in range(6))
    rows = []
    for i, c in enumerate(candidates):
        alt = " alt" if i % 2 == 1 else ""
        rows.append(f'<tr class="cand{alt}"><td class="cand">{html.escape(c)}</td>{bubbles}</tr>')
    for k in range(write_ins):
        alt = " alt" if (len(candidates) + k) % 2 == 1 else ""
        rows.append(f'<tr class="cand{alt}"><td class="cand">Write-in: '
                    f'<span class="wline"></span></td>{bubbles}</tr>')
    colheads = "".join(_colhead(n) for n in range(6))
    bullets = "".join(f"<li>{html.escape(b)}</li>" for b in INSTRUCTION_BULLETS)
    explain = "<br>".join(html.escape(l) for l in EXPLAIN_LINES)

    results = (f'Election results: bettervoting.com/<span class="eid">{html.escape(bv_id)}</span>/results'
               if bv_id else 'STAR Voting — Score Then Automatic Runoff')
    idpieces = []
    if serial is not None:
        idpieces.append(f'Ballot <span class="serial">#{html.escape(str(serial))}</span> '
                        f'— keep this to verify it was counted')
    idpieces.append(f'Better Voting Election ID: <span class="eid">{html.escape(bv_id)}</span>'
                    if bv_id else 'demo ballot')
    idline = " · ".join(idpieces)

    cls = "ballot pagebreak" if break_after else "ballot"
    notice_block = f'<div class="notice">{html.escape(notice)}</div>' if notice else ""
    title_block = f'<p class="title">{html.escape(title)}</p>' if title else ""
    blurb_block = f'<p class="edesc">{html.escape(blurb)}</p>' if blurb else ""
    q_block = f'<p class="q">{html.escape(question)}</p>' if question else ""
    promo_block = f'<p class="promo">{promo}</p>' if promo else ""

    # Header band: the intro stack (logo, title, blurb, question, instructions)
    # fills the left column; the big vote QR rides in a fixed-width right rail.
    # The left stack is ~200px tall already, so a 176px QR costs (almost) no extra
    # height — the grid starts where it always did, and the QR sits in the corner
    # a thumb naturally holds. No QR -> the rail is empty and the stack goes full
    # width. (Layout by Fable, 2026-07-25; replaced the QR|logo|QR + spacer row.)
    logo_content = (f'<img class="blogo" src="{logo_uri}" alt="STAR Voting">' if logo_uri
                    else (f'{STAR_LOGO}<div><div class="word">STAR VOTING</div>'
                          f'<div class="tag">SCORE · THEN · AUTOMATIC · RUNOFF</div></div>'))
    vote_qr = (f'<div class="qr" style="width:{qr_size}px">'
               f'<img src="{vote_qr_uri}" alt="QR code — vote online" '
               f'style="width:{qr_size}px;height:{qr_size}px">'
               f'<span class="cta">{html.escape(qr_caption)}</span></div>'
               if vote_qr_uri else "")
    header = (f'<div class="head">'
              f'<div class="head-main">'
              f'<div class="logo-slot">{logo_content}</div>'
              f'{title_block}{blurb_block}{q_block}'
              f'<ul class="inst">{bullets}</ul>'
              f'</div>{vote_qr}</div>')
    # The results QR (opt-in, --results-qr) prints small, beside the results URL it
    # encodes — not in the header. One big call-to-action code per ballot.
    results_qr = (f'<span class="qr"><img src="{results_qr_uri}" alt="QR code — results" '
                  f'style="width:{qr_size // 2}px;height:{qr_size // 2}px">'
                  f'<span class="cta">results</span></span>'
                  if results_qr_uri else "")
    # `.ballot` is a flex column and `.gridwrap` is flex:1, so on a one-ballot page
    # the score grid stretches into the leftover height (taller rows) instead of
    # leaving the bottom third of the sheet blank. See render_sheet's min-height.
    wm_block = f'<div class="wm">{html.escape(watermark)}</div>' if watermark else ""
    return f"""
<div class="{cls}">
  {wm_block}
  {notice_block}
  {header}
  <div class="gridwrap"><table class="grid">
    <tr class="wb"><td></td><td>Worst</td><td></td><td></td><td></td><td></td><td>Best</td></tr>
    <tr class="colhead"><th class="chl">Candidate</th>{colheads}</tr>
    {''.join(rows)}
  </table></div>
  <div class="explain">{explain}</div>
  <p class="foot"><span>{idline}</span><span>{results}</span>{results_qr}</p>
  {promo_block}
</div>"""


def render_sheet(title, question, candidates, bv_id, copies, per_page,
                 qr=True, serials=False, write_ins=0, notice="", blurb="",
                 promo="", logo_uri="", qr_size=176, results_qr=False,
                 fill_page=True, placeholder_qr=None, watermark=""):
    # ONE QR by default — the big "scan to vote" code. The results URL prints as
    # text in the footer, and --results-qr adds a small code beside it.
    # (bv_id is None only when --verify-bv found the id doesn't resolve → no QR.)
    vote_url = f"https://bettervoting.com/{bv_id}" if bv_id else None
    results_url = f"https://bettervoting.com/{bv_id}/results" if bv_id else None
    vote_qr_uri = qr_data_uri(vote_url) if (vote_url and qr) else None
    results_qr_uri = (qr_data_uri(results_url)
                      if (results_url and qr and results_qr) else None)
    # A PREVIEW has no election id, so normally there's no QR at all — which makes
    # the layout hard to judge. `placeholder_qr` prints a stand-in code at the real
    # size, captioned so it can't be read as a vote link. It encodes a URL you pass
    # (default: BetterVoting's home page) and NEVER a made-up election id — a
    # fabricated id is the dead-link failure FR-12 exists to prevent.
    caption = "Scan to vote online"
    if placeholder_qr and not bv_id and qr:
        vote_qr_uri = qr_data_uri(placeholder_qr)
        caption = PREVIEW_QR_CAPTION
    pp = max(1, per_page)
    ballots = "\n".join(
        render_ballot(title, question, candidates, bv_id,
                      vote_qr_uri=vote_qr_uri, results_qr_uri=results_qr_uri,
                      qr_caption=caption, watermark=watermark,
                      serial=(i + 1 if serials else None), write_ins=write_ins,
                      notice=notice, blurb=blurb, promo=promo,
                      logo_uri=logo_uri, qr_size=qr_size,
                      # force a page break after every `per_page` ballots (but not
                      # after the last — a trailing break makes a blank page).
                      break_after=((i + 1) % pp == 0 and i + 1 < copies))
        for i in range(copies))
    # Fill the sheet. Letter (11in) minus the 0.4in print margins = 10.2in of
    # printable height; each ballot also carries a 12px margin (~0.17in). Giving
    # `.ballot` that min-height makes the flex column stretch the score grid into
    # what used to be blank paper at the bottom — taller rows, easier to mark —
    # instead of a ballot floating in the top two-thirds of the page.
    fill_css = ""
    if fill_page:
        avail = (10.2 / pp) - 0.18
        fill_css = f"\n.ballot {{ min-height: {avail:.2f}in; }}\n"
    return (f'<!doctype html><html><head><meta charset="utf-8">'
            f'<title>STAR ballots — {html.escape(title or bv_id or "demo")}</title>'
            f'<style>{CSS}{fill_css}</style></head><body>{ballots}</body></html>')


# --------------------------------------------------------------------------- #
# Self-tests.                                                                  #
# --------------------------------------------------------------------------- #
def selftest():
    ok = True
    html_out = render_sheet("Test", "Score each", ["Ann", "Bob", "Cal"], "abc123",
                            copies=3, per_page=2)
    checks = [
        ("all three candidates present", all(n in html_out for n in ("Ann", "Bob", "Cal"))),
        ("bv id + results url", 'bettervoting.com/<span class="eid">abc123</span>/results' in html_out),
        ("election id label", "Better Voting Election ID:" in html_out),
        ("3 ballots rendered", html_out.count('class="ballot') == 3),
        ("0-5 bubble grid (18 bubbles/ballot = 3 cands x 6)", html_out.count('class="bub"') == 3 * 6 * 3),
        ("html escaping of a tricky name",
         "&lt;b&gt;" in render_ballot("t", "q", ["<b>"], None)),
        # official-style chrome
        ("STAR VOTING wordmark present", "STAR VOTING" in html_out),
        ("bulleted instructions (favorite five stars)",
         "favorite candidate(s) five stars" in html_out),
        ("Worst / Best column labels", "Worst" in html_out and "Best" in html_out),
        ("zebra stripe on even candidate row", 'class="cand alt"' in html_out),
        ("star column headers (1-5)", html_out.count('class="star"') == 3 * 5),
        ("finalist explanation footer",
         "two highest scoring candidates are finalists" in html_out),
        ("bubbles carry their digit", '<span class="bub">5</span>' in html_out),
    ]
    for label, cond in checks:
        print(f"[selftest] {label}: {'OK' if cond else 'FAIL'}")
        ok &= cond
    # serials + write-in rows
    s2 = render_sheet("T", "q", ["A", "B"], "x", copies=2, per_page=1,
                      qr=False, serials=True, write_ins=1)
    extra = [
        ("serial numbers per ballot", '#1</span>' in s2 and '#2</span>' in s2),
        ("write-in row added (1 per ballot x 2)", s2.count("Write-in:") == 2),
        ("bubbles = (2 cands + 1 write-in) x 6 x 2 ballots",
         s2.count('class="bub"') == (2 + 1) * 6 * 2),
    ]
    for label, cond in extra:
        print(f"[selftest] {label}: {'OK' if cond else 'FAIL'}")
        ok &= cond
    # pagination: page-break after every `per_page` ballots, never after the last.
    one = render_sheet("T", "q", ["A"], None, copies=3, per_page=1, qr=False)
    two = render_sheet("T", "q", ["A"], None, copies=3, per_page=2, qr=False)
    page = [
        ("one-per-page: breaks after all but last (3 copies -> 2 breaks)",
         one.count('class="ballot pagebreak"') == 2),
        ("two-per-page: break after ballot 2 only (3 copies -> 1 break)",
         two.count('class="ballot pagebreak"') == 1),
    ]
    for label, cond in page:
        print(f"[selftest] {label}: {'OK' if cond else 'FAIL'}")
        ok &= cond
    # Test ID stripping: BV<n> is internal, never printed on a voter's ballot.
    tid = [
        ("strips 'BV2252 — ' from a title",
         strip_test_id("BV2252 — Goodberry's, Cary NC") == "Goodberry's, Cary NC"),
        ("strips the hyphen and colon forms",
         strip_test_id("BV95a - Foo") == "Foo" and strip_test_id("BV130: Bar") == "Bar"),
        ("leaves a normal title alone",
         strip_test_id("Best Flavor 2026") == "Best Flavor 2026"),
        ("doesn't eat a title that merely starts with BV-ish words",
         strip_test_id("BVI referendum — options") == "BVI referendum — options"),
    ]
    for label, cond in tid:
        print(f"[selftest] {label}: {'OK' if cond else 'FAIL'}")
        ok &= cond
    # Page fill: the one-per-page default stretches each ballot to the sheet.
    fill = render_sheet("T", "q", ["A"], None, copies=1, per_page=1, qr=False)
    nofill = render_sheet("T", "q", ["A"], None, copies=1, per_page=1, qr=False,
                          fill_page=False)
    fillchecks = [
        ("fill-page injects a min-height", ".ballot { min-height: 10.02in; }" in fill),
        ("--no-fill-page omits it", "min-height" not in nofill),
        ("grid is wrapped so it can stretch", 'class="gridwrap"' in fill),
    ]
    for label, cond in fillchecks:
        print(f"[selftest] {label}: {'OK' if cond else 'FAIL'}")
        ok &= cond
    # QR is optional (needs segno); test whichever path applies. Default is ONE big
    # vote QR; --results-qr adds a small one in the footer.
    if qr_data_uri("https://bettervoting.com/abc123"):
        has_qr = (html_out.count('class="qr"') == 1 * 3   # 1 QR x 3 ballots
                  and "Scan to vote online" in html_out
                  and "data:image/svg" in html_out)
        print(f"[selftest] one big vote QR embedded (no results QR by default): "
              f"{'OK' if has_qr else 'FAIL'}")
        ok &= has_qr
        both = render_sheet("T", "q", ["A"], "abc123", copies=2, per_page=1,
                            results_qr=True)
        two = (both.count('class="qr"') == 2 * 2 and ">results<" in both)
        print(f"[selftest] --results-qr adds the footer code: {'OK' if two else 'FAIL'}")
        ok &= two
        # Placeholder QR: preview-only, captioned as a stand-in, and it must never
        # override a real election's own code.
        ph = render_sheet("T", "q", ["A"], None, copies=1, per_page=1,
                          placeholder_qr=PREVIEW_QR_URL, watermark=PREVIEW_WATERMARK)
        real = render_sheet("T", "q", ["A"], "abc123", copies=1, per_page=1,
                            placeholder_qr="https://example.com/nope")
        phk = [
            ("placeholder QR prints on a preview (no bv_id)",
             ph.count('class="qr"') == 1 and PREVIEW_QR_CAPTION in ph),
            ("preview watermark rendered", 'class="wm">TEST ONLY<' in ph),
            ("real ballots carry no watermark", 'class="wm"' not in real),
            ("placeholder never displaces a real election's QR",
             PREVIEW_QR_CAPTION not in real and "Scan to vote online" in real),
            ("no placeholder + no id -> still no QR",
             'class="qr"' not in render_sheet("T", "q", ["A"], None, copies=1,
                                              per_page=1)),
        ]
        for label, cond in phk:
            print(f"[selftest] {label}: {'OK' if cond else 'FAIL'}")
            ok &= cond
    else:
        no_qr = 'class="qr"' not in html_out
        print(f"[selftest] graceful no-QR (segno absent): {'OK' if no_qr else 'FAIL'}")
        ok &= no_qr
    # BV-export parsing: a frozen UI export nests everything under capitalized
    # "Election" (siblings "Ballots"/"Results") — regression guard for that schema.
    import tempfile, os
    export = {"Election": {"title": "Pets", "election_id": "mptvrm",
                           "description": "Our class demo election.",
                           "races": [{"description": "Which pet is best?",
                                      "candidates": [{"candidate_name": "ala"},
                                                     {"candidate_name": "bob"}]}]},
              "Ballots": [], "Results": []}
    fd, tmp = tempfile.mkstemp(suffix=".json")
    with os.fdopen(fd, "w") as f:
        json.dump(export, f)
    try:
        t, bid, cs, ed, rd = from_bv_export(tmp)
        bv_ok = (t == "Pets" and bid == "mptvrm" and cs == ["ala", "bob"]
                 and ed == "Our class demo election." and rd == "Which pet is best?")
    finally:
        os.remove(tmp)
    print(f"[selftest] BV export (capital 'Election'): title+id+candidates+descriptions: "
          f"{'OK' if bv_ok else 'FAIL'}")
    ok &= bv_ok
    # descriptions print on the ballot: election desc as blurb, race desc as question.
    html_d = render_sheet("Pets", "Which pet is best?", ["A"], "x", copies=1,
                          per_page=1, qr=False, blurb="Our class demo election.")
    desc_checks = [
        ("ballot shows election description (blurb)",
         'class="edesc"' in html_d and "Our class demo election." in html_d),
        ("ballot shows race description (question)", "Which pet is best?" in html_d),
    ]
    for label, cond in desc_checks:
        print(f"[selftest] {label}: {'OK' if cond else 'FAIL'}")
        ok &= cond
    # custom logo: embeds as a data URI and replaces the drawn wordmark.
    fd2, logo_path = tempfile.mkstemp(suffix=".svg")
    with os.fdopen(fd2, "w") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg"><rect width="10" height="10"/></svg>')
    try:
        uri = logo_data_uri(logo_path)
        html_l = render_sheet("T", "q", ["A"], "x", copies=1, per_page=1, qr=False,
                              logo_uri=uri)
    finally:
        os.remove(logo_path)
    logo_checks = [
        ("logo: file embeds as an svg data URI", uri.startswith("data:image/svg+xml;base64,")),
        ("logo: header uses <img> and drops the drawn wordmark",
         'class="blogo"' in html_l and "SCORE · THEN" not in html_l),
        ("logo: missing file degrades to '' (keeps wordmark)", logo_data_uri("/no/such.png") == ""),
    ]
    for label, cond in logo_checks:
        print(f"[selftest] {label}: {'OK' if cond else 'FAIL'}")
        ok &= cond
    # demonstration / secret-ballot notice: on by default, off-able.
    html_n = render_sheet("T", "q", ["A"], "x", copies=1, per_page=1, qr=False,
                          notice=DEFAULT_NOTICE)
    html_off = render_sheet("T", "q", ["A"], "x", copies=1, per_page=1, qr=False,
                            notice="")
    notice_checks = [
        ("notice: default text mentions 'not a secret ballot'",
         "not a secret ballot" in DEFAULT_NOTICE),
        ("notice: ballot shows it (class=notice)",
         'class="notice"' in html_n and "secret ballot" in html_n),
        ("notice: --no-notice omits it", 'class="notice"' not in html_off),
    ]
    for label, cond in notice_checks:
        print(f"[selftest] {label}: {'OK' if cond else 'FAIL'}")
        ok &= cond
    print(f"[selftest] {'ALL PASS' if ok else 'FAILURES PRESENT'}")
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bv-export", metavar="FILE",
                    help="a BetterVoting export JSON — the ONLY input route. Title, "
                         "candidates, election id, and descriptions all come from it. "
                         "Create the election on BV first, then print from its export.")
    ap.add_argument("--race", type=int, default=0, metavar="N",
                    help="which contest to print when the export has several races "
                         "(0 = the first, the default). A multi-race export prints ONE "
                         "race and warns; use this to pick a different one.")
    ap.add_argument("--title", help="optional: override the ballot title (e.g. a cleaner "
                                    "name than the verbose BV title)")
    ap.add_argument("--question", help="optional: override the ballot question line")
    ap.add_argument("--spec", nargs="?", const="", metavar="NAME",
                    help="PRE-MINT PREVIEW: print from an election spec in "
                         "bv_election_specs.py instead of a BV export — BEFORE the "
                         "election exists on BetterVoting. No id, so no QR and no "
                         "results link; the ballot is stamped PREVIEW. BV elections "
                         "are permanent, so look at the paper first. Bare --spec "
                         "takes the single entry of ELECTIONS.")
    ap.add_argument("--blurb", metavar="TEXT",
                    help="optional: an italic description blurb under the title. OFF "
                         "by default — a BV election description is written for the "
                         "voting page (long, and often narrates the expected outcome), "
                         "which makes for a poor ballot. --blurb-auto prints it anyway.")
    ap.add_argument("--blurb-auto", action="store_true",
                    help="use the export's election description as the blurb (the old "
                         "default; verbose — check it doesn't spoil a live vote)")
    ap.add_argument("--keep-test-id", action="store_true",
                    help="keep a leading repo Test ID (\"BV2252 — \") in the printed "
                         "title. Off by default: BV<n> is an internal cross-reference, "
                         "meaningless to a voter; the footer election id is the real one.")
    ap.add_argument("--copies", type=int, default=30)
    ap.add_argument("--per-page", type=int, default=1,
                    help="ballots per printed page (default 1 — one ballot per page, "
                         "the right choice for ballots you hand out individually)")
    ap.add_argument("--out", default=None,
                    help="output PDF path (default ballots.pdf, or "
                         "<spec>_preview.pdf for a --spec preview). PDF is the only "
                         "format; rendered via headless Chromium (needs `playwright`).")
    ap.add_argument("--no-qr", action="store_true",
                    help="deliberately print without the vote QR. (Otherwise a QR is "
                         "required — a ballot with a live BV id must be scannable — so "
                         "a missing `segno` library is an error, not a QR-less ballot.)")
    ap.add_argument("--preview-qr", nargs="?", const=PREVIEW_QR_URL, metavar="URL",
                    help=f"PREVIEW ONLY: the stand-in QR's target. Defaults to "
                         f"{PREVIEW_QR_URL} — a real but CLOSED BV election, so a "
                         f"scan lands somewhere honest where no vote can be cast. "
                         f"A preview prints this automatically; pass a URL to point "
                         f"it elsewhere, or --no-qr for none. Never encodes a made-up "
                         f"election id (that would be a scannable dead link).")
    ap.add_argument("--no-watermark", action="store_true",
                    help="omit the diagonal TEST ONLY watermark on a --spec preview")
    ap.add_argument("--results-qr", action="store_true",
                    help="also print a small results QR beside the results URL in the "
                         "footer (off by default — the URL already prints as text, and "
                         "one big call-to-action code beats two competing ones)")
    ap.add_argument("--no-fill-page", action="store_true",
                    help="don't stretch the ballot to fill the printed page (default is "
                         "to stretch, so the score grid uses the whole sheet)")
    ap.add_argument("--serials", action="store_true",
                    help="number each ballot (a 'keep this to verify it was counted' "
                         "receipt — see the secret-ballot caveat in the demo page)")
    ap.add_argument("--write-ins", type=int, default=0, metavar="N",
                    help="add N blank write-in rows per ballot")
    ap.add_argument("--notice", metavar="TEXT",
                    help="the 'this is a demo, not a secret ballot' notice printed on "
                         f"every ballot (default: \"{DEFAULT_NOTICE}\")")
    ap.add_argument("--no-notice", action="store_true",
                    help="omit the demonstration/secret-ballot notice (not recommended "
                         "— it's what keeps the serial number a teaching device)")
    ap.add_argument("--promo", action="store_true",
                    help="add a small footer promo line linking the STAR education/"
                         "platform sites (starvoting.org, equal.vote, bettervoting.com)")
    ap.add_argument("--chapter", metavar="TEXT",
                    help="append your local chapter to the promo footer, e.g. "
                         "\"STAR Voting NC (facebook.com/groups/starvotingnc)\" "
                         "(implies --promo)")
    ap.add_argument("--logo", metavar="FILE",
                    help="a local image (SVG/PNG/JPG) to embed in the header, "
                         "replacing the drawn STAR wordmark (HTML/PDF only; embedded "
                         "as a self-contained data URI). ASCII keeps the text wordmark.")
    ap.add_argument("--qr-size", type=int, default=176, metavar="PX",
                    help="vote QR size in pixels (default 176 — big enough to scan "
                         "across a table; the optional footer results QR prints at half)")
    ap.add_argument("--verify-bv", action="store_true",
                    help="before printing, check the BV id resolves to a real election; "
                         "if it doesn't, drop the QR + results link (print LH-only) so "
                         "voters never scan a dead link. Needs network; skips gracefully "
                         "offline. Recommended before a real print run.")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        raise SystemExit(0 if selftest() else 1)

    # TWO routes, and the distinction is when in the workflow you are:
    #   --bv-export  the real ballot for an election that EXISTS (id, QR, results).
    #   --spec       a PREVIEW of an election that doesn't exist yet — the dry run
    #                you want before an irreversible, permanent BV create.
    if args.bv_export and args.spec is not None:
        raise SystemExit("Pick one route: --bv-export (a real, created election) or "
                         "--spec (a pre-mint preview of a spec).")
    preview = args.spec is not None
    # A real ballot's QR must point at its own election — never a stand-in.
    if args.preview_qr and not preview:
        raise SystemExit("--preview-qr is for --spec previews only. A ballot printed "
                         "from a real election must carry that election's own QR.")
    if preview:
        t2, bv_id, candidates, edesc, rdesc = from_spec(args.spec or None, args.race)
    elif args.bv_export:
        t2, bv_id, candidates, edesc, rdesc = from_bv_export(args.bv_export, args.race)
    else:
        raise SystemExit("Provide --bv-export FILE (a BetterVoting export JSON) for a "
                         "real ballot, or --spec [NAME] to preview an election spec "
                         "before it's created on BV. Run --selftest to verify the tool.")
    title = args.title or t2
    # A voter's ballot doesn't carry our internal BV<n> Test ID (see strip_test_id).
    if not args.keep_test_id:
        title = strip_test_id(title)
        rdesc = strip_test_id(rdesc)

    # Guard against a dead BV link: a QR/results URL should only appear for a REAL,
    # already-created election. --verify-bv confirms the id resolves; if it doesn't,
    # drop to LH-only (no bv_id -> no QR, no results line).
    if args.verify_bv and bv_id:
        exists = verify_bv_id(bv_id)
        if exists is False:
            print(f"[verify-bv] No BetterVoting election '{bv_id}' — printing LH-only "
                  f"(no QR, no results link). Create it on BV first, or omit the id.")
            bv_id = None
        elif exists is None:
            print(f"[verify-bv] Couldn't reach BetterVoting to check '{bv_id}'; "
                  f"keeping the link as given.")
        else:
            print(f"[verify-bv] BetterVoting election '{bv_id}' confirmed.")

    # A ballot with a real election id MUST carry a QR (voters scan it to vote).
    # So `segno` is required unless the QR is deliberately suppressed (--no-qr) or
    # there's no id to link to (a bad id dropped by --verify-bv). Missing segno with a
    # live id is an error, not a silent QR-less ballot.
    if bv_id and not args.no_qr and qr_data_uri(f"https://bettervoting.com/{bv_id}") is None:
        raise SystemExit(
            "This ballot needs a QR code (it links to BetterVoting election "
            f"'{bv_id}'), but the `segno` QR library isn't available. Install it:\n"
            "    uv pip install segno\n"
            "…or pass --no-qr to print without a QR on purpose.")

    # Blurb: OFF unless asked for. A BV election description is written for the
    # voting page — long, and it often narrates the expected outcome — so printing
    # it under the ballot title is both noise and a spoiler risk. --blurb TEXT sets
    # your own; --blurb-auto restores the export's description.
    blurb = (args.blurb if args.blurb is not None
             else (edesc if args.blurb_auto else "")) or ""
    blurb = blurb.strip()
    question = (args.question or rdesc
                or "Score each candidate from 0 (worst) to 5 (best).").strip()
    notice = "" if args.no_notice else (args.notice or DEFAULT_NOTICE)
    if preview and not args.no_notice:
        notice = args.notice or ("PREVIEW - this election has NOT been created on "
                                 "BetterVoting yet. Do not hand out.")

    # Optional promo footer (links are parameters, not the description — off by
    # default so the base ballot matches the clean official design). --chapter
    # implies --promo.
    promo_parts = ["starvoting.org", "equal.vote", "bettervoting.com"] \
        if (args.promo or args.chapter) else []
    if args.chapter:
        promo_parts.append(args.chapter.strip())
    promo = ("Learn more: " + " · ".join(html.escape(p) for p in promo_parts)
             if promo_parts else "")
    logo_uri = logo_data_uri(args.logo) if args.logo else ""

    sheet = render_sheet(title, question, candidates, bv_id, args.copies,
                         args.per_page, qr=not args.no_qr, serials=args.serials,
                         write_ins=args.write_ins, notice=notice,
                         blurb=blurb, promo=promo, logo_uri=logo_uri,
                         qr_size=args.qr_size, results_qr=args.results_qr,
                         fill_page=not args.no_fill_page,
                         placeholder_qr=(args.preview_qr or PREVIEW_QR_URL) if preview else None,
                         watermark=(PREVIEW_WATERMARK
                                    if (preview and not args.no_watermark) else ""))

    # PDF is the only output. It's rendered from the ballot HTML via headless
    # Chromium (playwright), which is therefore required.
    # A preview gets its own filename so it can't be mistaken for — or overwrite —
    # the real print run sitting next to it.
    default_out = (f"{(args.spec or 'spec').lower()}_preview.pdf" if preview
                   else "ballots.pdf")
    out = args.out or default_out
    out = out if out.lower().endswith(".pdf") else os.path.splitext(out)[0] + ".pdf"
    if not html_to_pdf(sheet, out):
        raise SystemExit(
            "PDF render needs `playwright`. Install it once:\n"
            "    uv pip install playwright && playwright install chromium")

    pp = max(1, args.per_page)
    layout = "one per page" if pp == 1 else f"{pp} per page"
    print(f"Wrote {args.copies} STAR ballots ({len(candidates)} candidates, {layout}) "
          f"to {os.path.abspath(out)}")
    if preview:
        qr_note = ("the ballot has no QR" if args.no_qr else
                   f"its QR is a stand-in pointing at {args.preview_qr or PREVIEW_QR_URL} "
                   f"(a CLOSED election — nothing can be voted from it)")
        print(f"PREVIEW ONLY — this election does not exist on BetterVoting yet, so "
              f"{qr_note}.\nHappy with it? Create the election "
              f"(create_bv_test_election.py), then reprint from its export.")
    else:
        print("Print-ready PDF — send it straight to the printer.")
    if bv_id:
        print(f"Linked to BetterVoting election {bv_id} "
              f"(results: https://bettervoting.com/{bv_id}/results).")


if __name__ == "__main__":
    main()
