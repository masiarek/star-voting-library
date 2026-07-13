# Run a paper-ballot STAR demo (from a BetterVoting election)

*The complete hands-on loop for a teacher, workshop leader, or anyone running a demo election: create a real election on **BetterVoting**, print matching **paper ballots**, have the room vote, **hand-count** the result, and check your tally against BetterVoting's official one. Three independent counts — paper, platform, and the engine — that agree. This page is how to use the ballot-printing tool and run the whole loop.*

**Level: reference (a teaching tool).** Companions: [Teaching STAR Voting](teaching_star_voting.md) · [Count a STAR election by hand](count_star_by_hand.md).

## The loop at a glance

```text
  1. Make the election on BetterVoting  ─→  get the BV id  (bettervoting.com/<id>)
  2. Print matching paper ballots        ─→  bv_ballot_sheet.py  →  PDF
  3. Vote on paper                        ─→  fill 0–5 bubbles
  4. Hand-count                           ─→  add the columns · runoff (count_star_by_hand)
  5. Compare to BetterVoting              ─→  bettervoting.com/<id>/results
  6. (advanced) scan paper back to YAML   ─→  OCR → the LH engine
```

## Step 1 — make the election, get the BV id

Create your election at [bettervoting.com](https://bettervoting.com) (or, for a batch of test elections, via [`create_bv_test_election.py`](../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.py)). The **BV id** is the code in the URL — `bettervoting.com/`**`<id>`** — and the official tally will live at `bettervoting.com/<id>/results`. That id is what ties your paper ballots back to the online election.

## Step 2 — print matching paper ballots

The tool is [`STARVote_LH_tabulation_engine/tools_adam/bv_ballot_sheet.py`](../../STARVote_LH_tabulation_engine/tools_adam/bv_ballot_sheet.py) (stdlib only — runs with plain `python3`). Feed it the candidates and title **three ways**:

```bash
# A) from a repo election YAML — auto-picks up the title, candidates, and bv_election_id
python3 STARVote_LH_tabulation_engine/tools_adam/bv_ballot_sheet.py \
    --yaml 01_STAR/_main/bv2184_fyy886_lunch_vote.yaml --copies 30 --out lunch.html

# B) from a frozen BetterVoting export
python3 .../bv_ballot_sheet.py --bv-export path/to/<case>_bv_export.json --copies 30

# C) manually (your own demo election)
python3 .../bv_ballot_sheet.py --candidates "Ada,Ben,Cara" --title "Class President" \
    --bv-id demo1 --copies 30
```

**Ready-made real elections to demo with** — live on BetterVoting with memorable URLs, so you get paper ballots *and* an online tally to check against:
- the [team lunch](../../01_STAR/_main/_main_pages/bv2184_fyy886_lunch_vote.md) — `--yaml 01_STAR/_main/bv2184_fyy886_lunch_vote.yaml` (3 options, politics-free, the simplest);
- **[What Makes the Best Pet?](https://bettervoting.com/pet)** (`bettervoting.com/pet`) — 7 pets (Bird, Cat, Python, Dog, Fish, Rabbit, Rat), single-winner STAR, a classroom crowd-pleaser:
  ```bash
  python3 STARVote_LH_tabulation_engine/tools_adam/bv_ballot_sheet.py \
      --candidates "Bird,Cat,Python,Dog,Fish,Rabbit,Rat" \
      --title "What Makes the Best Pet?" --bv-id pet --serials --copies 25
  ```
- the **meta** version, [`bettervoting.com/meta_pets`](https://bettervoting.com/meta_pets) — the *same* pets voted **four ways** (Plurality / IRV / Approval / STAR), for a class to see how the method changes the winner. Pair it with [Criteria at a glance](../criteria_at_a_glance.md).

**Output — the `--out` extension picks the format:**
- **`.txt`** → **plain ASCII**, zero dependencies, prints from anywhere (`lpr lunch.txt` or any editor); one ballot per page via the form-feed character, `( )` circles to mark, and the results URL printed (no QR). The simplest, most portable option.
- **`.pdf`** → a print-ready **PDF** directly (e.g. `--out lunch.pdf` → a 30-page PDF, **one ballot per page**, straight to the printer — needs the `playwright` library, `playwright install chromium` once).
- **`.html`** (or omit `--out`) → a self-contained styled **HTML file** with the scannable QR; open it and **Print → Save as PDF** yourself. This is also the automatic fallback if playwright isn't installed.

Each ballot carries:

- the **election & race descriptions** (if your BV election has them) — the election description prints as a blurb under the title, the race description as the ballot question,
- the **0–5 bubble grid** (one row per candidate — voters fill one bubble),
- the **STAR instructions** ("give your favorite 5… the two highest-scoring have an automatic runoff"),
- the **BV election id and results URL** printed on every ballot, so paper and platform stay linked, and
- a **QR code** (top-right) that opens the online election when scanned — handy for "vote on paper *and* online, then compare." (The QR needs the tiny pure-Python `segno` library — `uv pip install segno`; without it the tool just prints the URL text and skips the QR, so it still runs with plain `python3`.)

The ballot is styled after the **official Equal Vote STAR ballot** — STAR VOTING header, bulleted instructions, Worst/Best labels, star column headers, digit-in-bubble cells, zebra stripes (in the official ballot grays: bubbles `#666`, stars `#ccc`, highlight `#ececec`), and the "two highest scoring are finalists" footer — so it's instantly familiar to anyone who's seen STAR before.

**Add the real STAR logo (optional, recommended).** The built-in header is a drawn facsimile so the tool works with no assets. For a polished print run, add the **official STAR Voting logo** with `--logo`. Two are bundled in [`tools_adam/assets/`](../../STARVote_LH_tabulation_engine/tools_adam/assets/):
- `--logo STARVote_LH_tabulation_engine/tools_adam/assets/BW_long_form.jpg` — the horizontal lockup (recommended; fits the header cleanly),
- `--logo STARVote_LH_tabulation_engine/tools_adam/assets/bw_logo_star.jpg` — the round seal (lighter-ink alternative).

These are the Equal Vote Coalition's trademark, included for STAR education/promotion (see [assets/README.md](../../STARVote_LH_tabulation_engine/tools_adam/assets/README.md) for attribution); official brand assets live at [starvoting.org](https://www.starvoting.org).

**Recommended setup for a classroom print run** — the black-and-white long-form logo on the ballot, and your local chapter in the footer (a color chapter logo like STAR Voting NC's is built for dark backgrounds, so it's an ink-heavy black box on a white ballot — keep the chapter as footer text instead):

```bash
python3 STARVote_LH_tabulation_engine/tools_adam/bv_ballot_sheet.py \
    --bv-export path/to/<election>_bv_export.json \
    --copies 30 --serials --promo \
    --chapter "STAR Voting NC (facebook.com/groups/starvotingnc)" \
    --logo STARVote_LH_tabulation_engine/tools_adam/assets/BW_long_form.jpg \
    --out ballots.pdf
```

Useful flags: `--copies N` (how many ballots), `--per-page N` (ballots per printed page — **default 1**, one per page; bump to 2+ to save paper), `--out FILE` (`.txt` / `.pdf` / `.html`), `--no-qr`, `--serials` (numbered "receipt" ballots — see *Verifiability* below), `--write-ins N` (blank write-in rows), `--promo` (footer line linking starvoting.org · equal.vote · bettervoting.com), `--chapter "TEXT"` (append your local chapter), `--logo FILE` (embed your own SVG/PNG logo in the header, replacing the drawn wordmark), and `--selftest`. Run `--help` for all of them.

## Step 3 — vote on paper

Hand out the ballots. Each voter fills **one bubble per candidate**, 0 (worst) to 5 (best); a blank row counts as 0. Equal scores are fine.

## Step 4 — hand-count

This is the whole point — STAR is genuinely countable by hand:

1. **Scoring round:** add each candidate's column of scores; the two highest totals are the **finalists**.
2. **Runoff:** sort the ballots into three piles — *prefers finalist A*, *prefers finalist B*, *no preference* — and count the two preference piles.

Full walkthrough: [Count a STAR election by hand](count_star_by_hand.md). Roles for a bigger count (caller / talliers / observer) and the official procedure: [Teaching STAR Voting](teaching_star_voting.md) · [BetterVoting — Hand Counting STAR](https://docs.bettervoting.com/help/hand_count.html).

## Step 5 — compare to BetterVoting

Have the same voters also vote online (or enter the paper ballots), and confirm your **hand tally matches** `bettervoting.com/<id>/results`. The teachable moment: the result is *transparent and reproducible* — the paper count, the platform, and the [LH engine](../../STARVote_LH_tabulation_engine/) all agree, and anyone in the room can verify it.

### Paper *and* online at once — and less work for you

The QR makes this a **hybrid** demo, and that's a feature, not a compromise: some voters fill a paper ballot, others just **scan the QR and vote online** on the same election. The nice part for the presenter is that it *cuts* your workload. **Online votes need no transcription** — BetterVoting tabulates them the instant they're cast — so you can send most of the room to the QR (zero paper handling) and keep just a handful of paper ballots to *demonstrate* the hand-count. The more people scan, the less scanning and typing you do, and the paper and online votes still land in one tally to compare. (It also reframes Step 6: OCR only ever matters for the paper ballots you *choose* to keep — every QR voter has already closed the loop.)

## Step 6 (advanced) — scan the paper back into YAML

The **return path** is to photograph the filled ballots and OCR the scores into a YAML the [LH engine](../why_yaml_test_cases.md) tabulates — closing the loop from paper to a fully-auditable digital count. That tool needs a vision engine and careful design, so it's the **roadmap**, not built yet; the design is below. **Until then, transcribe the paper ballots into a YAML by hand** using the same rules — the format is trivial (a candidate header, then one row of 0–5 scores per ballot).

## Design notes — the flow, and how a mistake becomes YAML

**Ballots with and without a BV election.** A ballot is meant to be *self-sufficient*; the BV link is an enhancement, not a requirement.
- **With** a `--bv-id`: the ballot prints the id, the results URL, and a scannable **QR** — paper and platform stay linked.
- **Without** one (an **LH-only** demo — no BetterVoting): still a perfectly valid ballot; it just carries the generic STAR heading and **no QR** (the QR only earns its place when there's an election to open). For traceability, put a date or set name in `--title`. If you *want* a QR anyway — say, to a "learn how STAR works" page — pass `--qr-url <URL>` (it works with or without a BV election).

**Flagging mistakes — reuse the repo's markers, don't invent a scheme.** The repo already has a marker vocabulary for exactly this (see [CLAUDE.md](../../CLAUDE.md) / the [markers glossary](STAR_ballot_voting_styles.md)): every marker tabulates as **0** *and* is reported. So an ambiguous mark maps cleanly:

| On the paper ballot | Meaning | In the YAML |
|---|---|---|
| exactly **one** bubble filled in a row | a valid 0–5 score | that digit (e.g. `4`) |
| **two or more** bubbles in one row (e.g. 2, 4 *and* 5) | ambiguous / overvote | **`?`** (spoiled — counts as 0, flagged) |
| **no** bubble in a row | no score given | `0` (or `-` for "left blank") |
| a stray mark, or illegible | can't read it confidently | `?` + a line in the run log for human review |

So *"the voter marked 2, 4 and 5 for one candidate"* becomes a **`?`** in that candidate's column — the engine already knows what to do with it (score it 0, surface it as spoiled), and a human can review every flagged row. No new mechanism needed — and the ballot itself warns the voter up front (*"two or more bubbles is a spoiled score for that candidate"*).

**The OCR tool, respecified in the repo's terms** (the goal, not the letter of the original spec):

1. Read each ballot image; locate the candidate rows and the 0–5 bubble grid.
2. Per row, count filled bubbles → **1** = that score · **0** = `0` · **≥2** = `?` (spoiled).
3. Anything below a confidence threshold, or unreadable → `?` and log for review.
4. Emit a standard `voting_method: STAR` YAML (candidate header + one scored/marked row per ballot) **plus a run log** naming every flagged ballot.
5. Tabulate in the [LH engine](../why_yaml_test_cases.md), which already reports spoiled ballots — loop closed.

When that tool gets built, the right way is against a **local OCR engine** with a **synthetic-ballot round-trip self-test** (render ballots with known scores → OCR → assert they match), so it's *verified before it's trusted* on real scans.

## Fun extensions (and what they secretly teach)

**Write-in candidates** (`--write-ins N`). Adds N blank *"Write-in: ______"* rows with their own 0–5 grid — realistic (BetterVoting supports write-ins too) and easy on paper. The *hard* part isn't printing them; it's **tallying** them: the return-path tool has to read a hand-written *name* and match write-ins across ballots ("Bob" = "bob" = "Bobby"?). So treat write-in matching as a design question for the OCR step, not the ballot.

**Ballot receipts & verifiability** (`--serials`). Each ballot gets a number — *"Ballot #7 — keep this to verify it was counted."* After the count, publish the list of serials that were counted and have each voter confirm theirs is on it. That demonstrates a genuinely important property: **counted as cast** — you can check your ballot made it into the tally.

But here's the honest catch, and it *is* the lesson: **a serial that anyone can link back to you breaks the [secret ballot](../GLOSSARY.md).** If a sign-in sheet maps *name → serial*, a coercer or vote-buyer could demand your number and check how you voted. Real elections resolve this tension with **end-to-end verifiability (E2E-V)** — cryptographic receipts that let you confirm your vote was counted *without* revealing (or being able to prove to anyone) how you voted. So the serial demo is the perfect way to introduce *why verifiability is hard*: you want **both** "confirm it counted" **and** "nobody can tell how I voted," and getting both at once takes real cryptography. (BetterVoting's per-voter unique numbers are the platform's version of this receipt.)

For a classroom: use serials to show "counted as cast," then ask *"what would go wrong if we posted a name-to-number list?"* — that discussion is the actual education. Keep serials **unlinked** to identity in any real use.

**Every ballot says so, in print.** Because a numbered ballot invites an immediate (and correct) objection — *"wait, that breaks the secret ballot!"* — the tool prints a standing notice on **every** ballot by default: *"EDUCATION ONLY — a STAR Voting teaching demo, not a secret ballot."* That's what lets the serial be a *teaching device* instead of a red flag: the ballot itself declares it's a demo. Change the wording with `--notice "..."`, or drop it with `--no-notice` (not recommended — it's the thing that heads off the objection).

### Should you number the ballots? (`--serials` is off by default)

Numbering cuts both ways, so it's a deliberate choice — here's how to make it:

| Number them (`--serials`) when… | Leave them unnumbered (default) when… |
|---|---|
| **verifiability is the lesson** — you *want* to demonstrate "counted as cast" and then discuss the secret-ballot tension | the point is **how STAR works** (score → runoff) and a numbering tangent would distract |
| you want to **reconcile the count** ("all 30 ballots back, none duplicated") | the room is mixed/adult and a numbered ballot would trigger objections before you're ready to teach them |
| — | you might **reuse the ballots casually** later (no privacy footgun) |

**Why off by default:** a default is used by whoever *isn't* thinking about it, and a serial only pays off when it's **paired with the discussion** ("what would break if we posted a name→number list?"). So the tool keeps the clean, on-topic ballot as the default and makes numbering a conscious opt-in — when you type `--serials`, that's your cue to actually teach the verifiability lesson (and to keep the numbers **unlinked** to any name). **Teaching verifiability? Reach for `--serials`.** Otherwise the plain ballot is the right call.

*Scope note (so nobody rabbit-holes this):* the whole serial demo runs on **paper + hand-count** — print serialized ballots, count them, publish the list of counted serials. You don't need BetterVoting or any digital plumbing for it, and you shouldn't try to thread serials through BV's vote API (it doesn't carry them, and it isn't needed). A genuinely *digital* verifiable count is **end-to-end verifiability (E2E-V)** — a cryptography topic beyond this teaching repo. The lesson is already complete on paper; stop there.

## Why do this (the teaching value)

- **Demystifies the method** — students *see* that STAR is simple to count, not a black box.
- **Three independent counts that agree** — paper, BetterVoting, and the LH engine — which is exactly the trust story ("don't believe it, check it").
- **Perfect for classrooms, clubs, and workshops** — everyone participates, and the result is theirs to verify.

## See also

- [Teaching STAR Voting](teaching_star_voting.md) — the presenter's guide (arc, terms, misconceptions)
- [Count a STAR election by hand](count_star_by_hand.md) · [Summability](STAR_summability.md) — why it scales
- [BetterVoting and the LH engine — one election, two reports](../tabulation_engines/bettervoting_and_the_engine.md) — the digital cross-check
