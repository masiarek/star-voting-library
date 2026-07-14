#!/usr/bin/env python3
"""
bv_ballot_sheet.py — generate printable STAR paper ballots for a demo / classroom
hand-count exercise, tied to a BetterVoting (BV) election.

The teacher's front-of-workflow tool: you make a real election on BetterVoting,
then print matching paper ballots so a room can vote by hand, hand-count the result
(see 00_start_here/STAR_Voting/count_star_by_hand.md), and compare to BV's official
tally. The `--out` extension picks the format: .txt = plain ASCII (zero deps, prints
anywhere, form-feed page breaks), .pdf = print-ready PDF (via playwright), .html
(default) = styled with a scannable QR (Print -> PDF). Each ballot carries the STAR
instructions, a 0-5 bubble grid per candidate, and the BV election id + results URL
so paper and platform stay linked. Default is one ballot per page.

ONE input route (by design — see bv_ballot_sheet_FSD.md §5.1):
  --bv-export FILE     a BetterVoting export JSON. Everything the ballot needs —
                       title, candidates, election id, and the election + race
                       descriptions — comes from the export. So the workflow is
                       always: create the election on BV -> export its JSON ->
                       print from that. (`create_bv_test_election.py` saves the
                       JSON automatically when it creates the election.)
  --title / --question  optional overrides (e.g. a cleaner ballot title than the
                        verbose BV one). Output styling flags: see --help.

Optional deps: `segno` (QR), `playwright` (direct .pdf) — both degrade gracefully.
`--selftest` runs known-answer checks. Design spec: bv_ballot_sheet_FSD.md.

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
import mimetypes
import os
import re
import sys
import textwrap


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


def from_bv_export(path):
    """Return (title, bv_id, [candidates], election_desc, race_desc) from a frozen
    BV export JSON."""
    data = json.load(open(path, encoding="utf-8"))
    # A frozen BV UI export nests everything under a capitalized "Election" key
    # (siblings "Ballots"/"Results"); older/plain GETs use lowercase or are flat.
    election = data if not isinstance(data, dict) else (
        data.get("Election") or data.get("election") or data)
    title = election.get("title") or election.get("name")
    bv_id = (election.get("election_id") or election.get("id")
             or data.get("election_id") or data.get("Election", {}).get("election_id"))
    cands = _find_candidate_names(data)
    if not cands:
        raise SystemExit(f"Could not find candidate names in {path} "
                         f"(pass --candidates manually).")
    edesc = election.get("description") or None
    races = election.get("races") or []
    rdesc = races[0].get("description") if races and isinstance(races[0], dict) else None
    return title, bv_id, cands, edesc, (rdesc or None)


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
# Kept 7-bit ASCII (plain '-') so it survives into the .txt output unchanged.
DEFAULT_NOTICE = "EDUCATION ONLY - a STAR Voting teaching demo, not a secret ballot."


def qr_data_uri(url):
    """An inline QR (data: URI) for `url` if the pure-python `segno` library is
    installed; None otherwise (the tool stays stdlib-only, QR just degrades)."""
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
    """Render the ballot HTML straight to a print-ready PDF via headless Chromium
    (the already-declared `playwright` dep). Returns True on success; False if
    playwright isn't installed/usable, so the caller can fall back to writing HTML.
    page.pdf() emulates print media, so the @media-print page-breaks apply."""
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
        print(f"[pdf] playwright present but PDF render failed ({e}); "
              "falling back to HTML.")
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
body { font-family: -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
       margin: 0; color: #111; }
.ballot { position: relative; border: 3px solid #111; border-radius: 10px;
          padding: 16px 22px 14px; margin: 12px; page-break-inside: avoid; }
.notice { border: 1.5px solid #c0392b; border-radius: 5px; padding: 3px 8px;
          margin: 0 0 10px; font-size: 10.5px; font-weight: 700; color: #c0392b;
          text-align: center; text-transform: uppercase; letter-spacing: .4px; }
.brand { display: flex; align-items: center; justify-content: space-between; gap: 10px; margin: 2px 0 8px; }
.brand .logo-slot { flex: 1; display: flex; align-items: center; justify-content: center; gap: 12px; }
.brand .logo { width: 50px; height: 50px; flex: none; }
.brand .blogo { display: block; margin: 0 auto; max-height: 74px; max-width: 100%; }
.brand .word { font-weight: 800; font-size: 30px; letter-spacing: .5px; line-height: 1; }
.brand .tag { font-weight: 800; font-size: 10.5px; letter-spacing: 1.5px; color: #5a7683; margin-top: 3px; }
.title { text-align: center; font-size: 16px; font-weight: 700; margin: 2px 0 1px; }
.edesc { text-align: center; font-style: italic; color: #555; font-size: 12px; margin: 0 0 2px; }
.q { text-align: center; color: #333; font-size: 12.5px; margin: 0 0 6px; }
.inst { margin: 6px 0 2px 22px; padding: 0; font-size: 13.5px; }
.inst li { margin: 1px 0; }
.fine { margin: 2px 0 6px 22px; font-size: 10.5px; color: #666; }
.qr { flex: none; text-align: center; font-size: 9px; color: #555; }
.qr img { display: block; margin: 0 auto; }
.qr span { display: block; margin-top: 1px; }
table.grid { border-collapse: collapse; width: 100%; margin: 4px 0 6px; }
.grid td, .grid th { text-align: center; padding: 0; vertical-align: middle; }
.grid td.cand, .grid th.chl { text-align: left; width: 30%; font-weight: 800; font-size: 15px; padding-left: 6px; }
.wb td { font-weight: 800; font-size: 13px; padding: 1px 0; }
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
.explain { text-align: center; font-size: 12.5px; line-height: 1.35; margin: 6px 4px 2px;
           padding-top: 8px; border-top: 1.5px solid #111; }
.foot { margin-top: 8px; font-size: 10.5px; color: #555; display: flex; justify-content: space-between; }
.foot .eid { font-weight: 800; font-size: 12.5px; color: #111; }
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
                  qr_size=88):
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

    results = (f'results: bettervoting.com/{html.escape(bv_id)}/results'
               if bv_id else 'STAR Voting — Score Then Automatic Runoff')
    idpieces = []
    if serial is not None:
        idpieces.append(f'Ballot <span class="serial">#{html.escape(str(serial))}</span> '
                        f'— keep this to verify it was counted')
    idpieces.append(f'Election <span class="eid">{html.escape(bv_id)}</span>'
                    if bv_id else 'demo ballot')
    idline = " · ".join(idpieces)

    cls = "ballot pagebreak" if break_after else "ballot"
    notice_block = f'<div class="notice">{html.escape(notice)}</div>' if notice else ""
    title_block = f'<p class="title">{html.escape(title)}</p>' if title else ""
    blurb_block = f'<p class="edesc">{html.escape(blurb)}</p>' if blurb else ""
    q_block = f'<p class="q">{html.escape(question)}</p>' if question else ""
    promo_block = f'<p class="promo">{promo}</p>' if promo else ""

    # Header row: vote QR (left), logo (center), results QR (right). Balance with a
    # spacer if only one QR exists, so the logo stays centered.
    def _qr_cell(uri, caption):
        return (f'<div class="qr"><img src="{uri}" alt="QR code" '
                f'style="width:{qr_size}px;height:{qr_size}px">'
                f'<span>{html.escape(caption)}</span></div>' if uri else "")
    left_qr = _qr_cell(vote_qr_uri, "scan to vote")
    right_qr = _qr_cell(results_qr_uri, "scan for results")
    spacer = f'<div style="width:{qr_size}px;flex:none"></div>'
    if left_qr and not right_qr:
        right_qr = spacer
    elif right_qr and not left_qr:
        left_qr = spacer
    logo_content = (f'<img class="blogo" src="{logo_uri}" alt="STAR Voting">' if logo_uri
                    else (f'{STAR_LOGO}<div><div class="word">STAR VOTING</div>'
                          f'<div class="tag">SCORE · THEN · AUTOMATIC · RUNOFF</div></div>'))
    brand = (f'<div class="brand">{left_qr}'
             f'<div class="logo-slot">{logo_content}</div>{right_qr}</div>')
    return f"""
<div class="{cls}">
  {notice_block}
  {brand}
  {title_block}{blurb_block}{q_block}
  <ul class="inst">{bullets}</ul>
  <p class="fine">Fill one bubble per row. Two or more bubbles in a row spoils that candidate's score.</p>
  <table class="grid">
    <tr class="wb"><td></td><td>Worst</td><td></td><td></td><td></td><td></td><td>Best</td></tr>
    <tr class="colhead"><th class="chl">Candidate</th>{colheads}</tr>
    {''.join(rows)}
  </table>
  <div class="explain">{explain}</div>
  <p class="foot"><span>{idline}</span><span>{results}</span></p>
  {promo_block}
</div>"""


def render_sheet(title, question, candidates, bv_id, copies, per_page,
                 qr=True, serials=False, write_ins=0, notice="", blurb="",
                 promo="", logo_uri="", qr_size=88):
    # Two QRs when there's a BV election: vote (left) and results (right).
    # (bv_id is None only when --verify-bv found the id doesn't resolve → no QR.)
    vote_url = f"https://bettervoting.com/{bv_id}" if bv_id else None
    results_url = f"https://bettervoting.com/{bv_id}/results" if bv_id else None
    vote_qr_uri = qr_data_uri(vote_url) if (vote_url and qr) else None
    results_qr_uri = qr_data_uri(results_url) if (results_url and qr) else None
    pp = max(1, per_page)
    ballots = "\n".join(
        render_ballot(title, question, candidates, bv_id,
                      vote_qr_uri=vote_qr_uri, results_qr_uri=results_qr_uri,
                      serial=(i + 1 if serials else None), write_ins=write_ins,
                      notice=notice, blurb=blurb, promo=promo,
                      logo_uri=logo_uri, qr_size=qr_size,
                      # force a page break after every `per_page` ballots (but not
                      # after the last — a trailing break makes a blank page).
                      break_after=((i + 1) % pp == 0 and i + 1 < copies))
        for i in range(copies))
    perpage_txt = ('one ballot per page' if pp == 1 else f'{pp} ballots per page')
    hint = ('<p class="noprint" style="margin:12px 18px;color:#666;font-size:13px">'
            f'{copies} ballots · {perpage_txt} — use your browser\'s '
            'Print → "Save as PDF" (or run with --out ballots.pdf for a PDF directly). '
            'This is the print-and-hand-count front end; '
            'count with count_star_by_hand.md, then compare to BetterVoting.</p>')
    return (f'<!doctype html><html><head><meta charset="utf-8">'
            f'<title>STAR ballots — {html.escape(title or bv_id or "demo")}</title>'
            f'<style>{CSS}</style></head><body>{hint}{ballots}</body></html>')


# --------------------------------------------------------------------------- #
# Plain-ASCII output: zero dependencies, prints from anywhere (`lpr file.txt`   #
# or any editor). One ballot per page via the form-feed char (\f). No QR (the   #
# URL is printed instead) — the purest, most portable ballot.                   #
# --------------------------------------------------------------------------- #
TEXT_WIDTH = 72


def _ascii_row(label, name_w):
    cells = "  ".join(f"({n})" for n in range(6))
    return f"  {label[:name_w].ljust(name_w)}  {cells}"


def render_ballot_text(title, question, candidates, bv_id, serial=None,
                       write_ins=0, notice="", blurb="", promo=""):
    rule = "=" * TEXT_WIDTH
    name_w = min(max([len(c) for c in candidates] + [9]) + 1, 26)
    lines = [rule]
    lines.append("* STAR VOTING *".center(TEXT_WIDTH).rstrip())
    lines.append("Score - Then - Automatic - Runoff".center(TEXT_WIDTH).rstrip())
    if title:
        lines.append("")
        lines.append(title.center(TEXT_WIDTH).rstrip())
    if serial is not None:
        lines.append(f"  Ballot #{serial} - keep this to verify it was counted")
    if notice:
        bar = "  " + "-" * (TEXT_WIDTH - 4)
        lines.append("")
        lines.append(bar)
        for ln in textwrap.wrap(notice, TEXT_WIDTH - 4):
            lines.append("  " + ln)
        lines.append(bar)
    if blurb:
        lines.append("")
        lines += textwrap.wrap(blurb, TEXT_WIDTH - 2, initial_indent="  ",
                               subsequent_indent="  ")
    if question:
        lines.append("")
        lines += textwrap.wrap(question, TEXT_WIDTH - 2, initial_indent="  ",
                               subsequent_indent="  ")
    lines.append("")
    for b in INSTRUCTION_BULLETS:
        wrapped = textwrap.wrap(b, TEXT_WIDTH - 6)
        for j, ln in enumerate(wrapped):
            lines.append(("  - " if j == 0 else "    ") + ln)
    lines.append("  Fill one bubble per row; two or more spoils that score.")
    lines.append("")
    cellblock = "  ".join(f"({n})" for n in range(6))
    pre = "  " + " " * name_w + "  "
    lines.append(pre + "Worst" + " " * (len(cellblock) - 9) + "Best")
    for c in candidates:
        lines.append(_ascii_row(c, name_w))
    for _ in range(write_ins):
        lines.append(_ascii_row("Write-in: " + "_" * max(0, name_w - 10), name_w))
    lines.append("")
    lines.append("  " + "-" * (TEXT_WIDTH - 4))
    for l in EXPLAIN_LINES:
        lines.append("  " + l)
    lines.append("")
    if bv_id:
        lines.append(f"  Election {bv_id}  |  results: bettervoting.com/{bv_id}/results")
    else:
        lines.append("  STAR Voting - Score Then Automatic Runoff")
    if promo:
        lines.append("  " + promo)
    lines.append(rule)
    return "\n".join(lines)


def render_sheet_text(title, question, candidates, bv_id, copies, per_page,
                      serials=False, write_ins=0, notice="", blurb="", promo=""):
    pp = max(1, per_page)
    out = []
    for i in range(copies):
        out.append(render_ballot_text(title, question, candidates, bv_id,
                                      serial=(i + 1 if serials else None),
                                      write_ins=write_ins, notice=notice, blurb=blurb,
                                      promo=promo))
        last = (i + 1 == copies)
        if not last:
            # form-feed = a hard page break for printers; a blank gap otherwise.
            out.append("\f" if (i + 1) % pp == 0 else "\n")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------- #
# Self-tests.                                                                  #
# --------------------------------------------------------------------------- #
def selftest():
    ok = True
    html_out = render_sheet("Test", "Score each", ["Ann", "Bob", "Cal"], "abc123",
                            copies=3, per_page=2)
    checks = [
        ("all three candidates present", all(n in html_out for n in ("Ann", "Bob", "Cal"))),
        ("bv id + results url", "bettervoting.com/abc123/results" in html_out),
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
    # plain-ASCII output: zero deps, form-feed page breaks, results URL not QR.
    txt = render_sheet_text("Pets", "q", ["ala", "bob"], "mptvrm",
                            copies=3, per_page=1, serials=True)
    is_ascii = all(ord(ch) < 128 for ch in txt)
    txtchecks = [
        ("ascii: candidates + results url present",
         "ala" in txt and "bob" in txt and "bettervoting.com/mptvrm/results" in txt),
        ("ascii: one-per-page form-feeds (3 copies -> 2)", txt.count("\f") == 2),
        ("ascii: 6 markable bubbles per candidate row", "(0)  (1)  (2)  (3)  (4)  (5)" in txt),
        ("ascii: STAR VOTING wordmark + Worst/Best", "STAR VOTING" in txt and "Worst" in txt and "Best" in txt),
        ("ascii: finalist explanation", "two highest scoring candidates are finalists" in txt),
        ("ascii: serial receipt line", "Ballot #1 - keep" in txt),
        ("ascii: strictly 7-bit ASCII (no QR, no unicode)", is_ascii),
    ]
    for label, cond in txtchecks:
        print(f"[selftest] {label}: {'OK' if cond else 'FAIL'}")
        ok &= cond
    # QR is optional (needs segno); test whichever path applies. With a bv_id there
    # are TWO QRs — vote (left) + results (right).
    if qr_data_uri("https://bettervoting.com/abc123"):
        has_qr = (html_out.count('class="qr"') == 2 * 3   # 2 QRs x 3 ballots
                  and "scan to vote" in html_out and "scan for results" in html_out
                  and "data:image/svg" in html_out)
        print(f"[selftest] two QRs (vote + results) embedded: {'OK' if has_qr else 'FAIL'}")
        ok &= has_qr
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
    txt_d = render_sheet_text("Pets", "Which pet is best?", ["A"], "x", copies=1,
                              per_page=1, blurb="Our class demo election.")
    desc_checks = [
        ("HTML ballot shows election description (blurb)",
         'class="edesc"' in html_d and "Our class demo election." in html_d),
        ("HTML ballot shows race description (question)", "Which pet is best?" in html_d),
        ("ASCII ballot shows both descriptions",
         "Our class demo election." in txt_d and "Which pet is best?" in txt_d),
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
    # demonstration / secret-ballot notice: on by default, both formats, off-able.
    html_n = render_sheet("T", "q", ["A"], "x", copies=1, per_page=1, qr=False,
                          notice=DEFAULT_NOTICE)
    html_off = render_sheet("T", "q", ["A"], "x", copies=1, per_page=1, qr=False,
                            notice="")
    txt_n = render_sheet_text("T", "q", ["A"], "x", copies=1, per_page=1,
                              notice=DEFAULT_NOTICE)
    notice_checks = [
        ("notice: default text mentions 'not a secret ballot'",
         "not a secret ballot" in DEFAULT_NOTICE),
        ("notice: HTML ballot shows it (class=notice)",
         'class="notice"' in html_n and "secret ballot" in html_n),
        ("notice: --no-notice omits it from HTML", 'class="notice"' not in html_off),
        ("notice: ASCII ballot shows it and stays 7-bit",
         "secret ballot" in txt_n and all(ord(c) < 128 for c in txt_n)),
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
    ap.add_argument("--title", help="optional: override the ballot title (e.g. a cleaner "
                                    "name than the verbose BV title)")
    ap.add_argument("--question", help="optional: override the ballot question line")
    ap.add_argument("--copies", type=int, default=30)
    ap.add_argument("--per-page", type=int, default=1,
                    help="ballots per printed page (default 1 — one ballot per page, "
                         "the right choice for ballots you hand out individually)")
    ap.add_argument("--out", default="ballots.html",
                    help="output file — extension picks the format: .txt = plain "
                         "ASCII (zero deps, prints anywhere), .pdf = print-ready PDF "
                         "(needs `playwright`), .html (default) = styled, Print → PDF")
    ap.add_argument("--no-qr", action="store_true",
                    help="omit the QR code (QR needs the `segno` library)")
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
    ap.add_argument("--qr-size", type=int, default=88, metavar="PX",
                    help="QR code size in pixels (default 88; bump up for easier scanning)")
    ap.add_argument("--verify-bv", action="store_true",
                    help="before printing, check the BV id resolves to a real election; "
                         "if it doesn't, drop the QR + results link (print LH-only) so "
                         "voters never scan a dead link. Needs network; skips gracefully "
                         "offline. Recommended before a real print run.")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        raise SystemExit(0 if selftest() else 1)

    # ONE input route: a BetterVoting export supplies title, candidates, id, and
    # descriptions. Create the election first, then print from its export.
    if not args.bv_export:
        raise SystemExit("Provide --bv-export FILE (a BetterVoting export JSON). "
                         "Create the election on BV first, then print from its export. "
                         "Run --selftest to verify the tool.")
    t2, bv_id, candidates, edesc, rdesc = from_bv_export(args.bv_export)
    title = args.title or t2

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

    # From the export: election description → blurb under the title; race
    # description → the question line (--question overrides).
    blurb = (edesc or "").strip()
    question = (args.question or rdesc
                or "Score each candidate from 0 (worst) to 5 (best).").strip()
    notice = "" if args.no_notice else (args.notice or DEFAULT_NOTICE)

    # Optional promo footer (links are parameters, not the description — off by
    # default so the base ballot matches the clean official design). --chapter
    # implies --promo. Built per format: HTML uses "·", ASCII uses "|".
    promo_parts = ["starvoting.org", "equal.vote", "bettervoting.com"] \
        if (args.promo or args.chapter) else []
    if args.chapter:
        promo_parts.append(args.chapter.strip())
    is_txt = args.out.lower().endswith(".txt")
    if promo_parts:
        sep = " | " if is_txt else " · "
        joined = sep.join(promo_parts if is_txt
                          else [html.escape(p) for p in promo_parts])
        promo = "Learn more: " + joined
    else:
        promo = ""
    logo_uri = logo_data_uri(args.logo) if (args.logo and not is_txt) else ""

    # Plain-ASCII output: zero deps, prints anywhere, one ballot per page via \f.
    if args.out.lower().endswith(".txt"):
        sheet = render_sheet_text(title, question, candidates, bv_id, args.copies,
                                  args.per_page, serials=args.serials,
                                  write_ins=args.write_ins, notice=notice, blurb=blurb,
                                  promo=promo)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(sheet)
        pp = max(1, args.per_page)
        layout = "one per page" if pp == 1 else f"{pp} per page"
        print(f"Wrote {args.copies} STAR ballots ({len(candidates)} candidates, "
              f"{layout}) to {os.path.abspath(args.out)}")
        print("Plain text — print with `lpr` or any editor (form-feed = page break). "
              "No dependencies, no QR (the results URL is printed).")
        if bv_id:
            print(f"Linked to BetterVoting election {bv_id} "
                  f"(results: https://bettervoting.com/{bv_id}/results).")
        return

    sheet = render_sheet(title, question, candidates, bv_id, args.copies,
                         args.per_page, qr=not args.no_qr, serials=args.serials,
                         write_ins=args.write_ins, notice=notice,
                         blurb=blurb, promo=promo, logo_uri=logo_uri, qr_size=args.qr_size)

    want_pdf = args.out.lower().endswith(".pdf")
    wrote_pdf = False
    if want_pdf:
        wrote_pdf = html_to_pdf(sheet, args.out)
        if not wrote_pdf:
            # Graceful fallback: no playwright → write the HTML beside it so the
            # user can still Print → PDF. (Keeps the tool runnable on plain python3.)
            args.out = args.out[:-4] + ".html"
            print("[pdf] `playwright` not available — install it (uv pip install "
                  "playwright && playwright install chromium) for direct PDF. "
                  f"Writing HTML instead: {args.out}")

    if not wrote_pdf:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(sheet)

    pp = max(1, args.per_page)
    layout = "one per page" if pp == 1 else f"{pp} per page"
    print(f"Wrote {args.copies} STAR ballots ({len(candidates)} candidates, {layout}) "
          f"to {os.path.abspath(args.out)}")
    if wrote_pdf:
        print("Print-ready PDF — send it straight to the printer.")
    else:
        print("Open it in a browser and Print → Save as PDF.")
    if bv_id:
        print(f"Linked to BetterVoting election {bv_id} "
              f"(results: https://bettervoting.com/{bv_id}/results).")


if __name__ == "__main__":
    main()
