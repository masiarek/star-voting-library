# assets — logos for the paper-ballot tool

Images used by [`bv_ballot_sheet.py`](../bv_ballot_sheet.py)'s `--logo` flag.

## STAR Voting logos

- **`BW_long_form.jpg`** — the horizontal STAR VOTING lockup ("SCORE · THEN · AUTOMATIC · RUNOFF"). **The recommended ballot-header logo** (black-and-white, prints cleanly on a white ballot).
- **`bw_logo_star.jpg`** — the round STAR VOTING seal. A lighter-ink alternative (mostly outline).
- **`NC_STAR_Logo1.jpg`** — the STAR Voting **North Carolina** chapter lockup. **Color, on a solid black background** — so it's for **color prints / slides / digital**, not a B&W paper ballot: the white "STAR VOTING" text needs the dark box (it would vanish on white paper), and the black box is heavy ink. For a printed ballot, prefer `BW_long_form.jpg` and put the chapter in the footer with `--chapter` (the tool's recommended setup). If STAR Voting NC has a *dark-text / light-background* variant, that one could go on the ballot directly.

**Attribution & rights.** These are the **STAR Voting** logo, a trademark of the **Equal Vote Coalition** (starvoting.org / equal.vote). They are included here for **STAR Voting education and promotion** — the purpose the Coalition distributes them for. Use them only in that spirit and where you have the right to (e.g. as a local chapter such as STAR Voting NC). They are **not** covered by this repository's own license; all rights remain with the Equal Vote Coalition. Get official brand assets from <https://www.starvoting.org>.

The tool's built-in header (when no `--logo` is given) is a *drawn facsimile*, not this asset — so the tool works with no bundled logo at all.
