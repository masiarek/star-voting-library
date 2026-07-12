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

It writes a self-contained **HTML file**; open it in a browser and **Print → Save as PDF**. Each ballot carries:

- the **0–5 bubble grid** (one row per candidate — voters fill one bubble),
- the **STAR instructions** ("give your favorite 5… the two highest-scoring have an automatic runoff"), and
- the **BV election id and results URL** printed on every ballot, so paper and platform stay linked.

Useful flags: `--copies N` (how many ballots), `--per-page N` (layout hint), `--out FILE`, and `--selftest` (verify the tool). Run `--help` for all of them.

## Step 3 — vote on paper

Hand out the ballots. Each voter fills **one bubble per candidate**, 0 (worst) to 5 (best); a blank row counts as 0. Equal scores are fine.

## Step 4 — hand-count

This is the whole point — STAR is genuinely countable by hand:

1. **Scoring round:** add each candidate's column of scores; the two highest totals are the **finalists**.
2. **Runoff:** sort the ballots into three piles — *prefers finalist A*, *prefers finalist B*, *no preference* — and count the two preference piles.

Full walkthrough: [Count a STAR election by hand](count_star_by_hand.md). Roles for a bigger count (caller / talliers / observer) and the official procedure: [Teaching STAR Voting](teaching_star_voting.md) · [BetterVoting — Hand Counting STAR](https://docs.bettervoting.com/help/hand_count.html).

## Step 5 — compare to BetterVoting

Have the same voters also vote online (or enter the paper ballots), and confirm your **hand tally matches** `bettervoting.com/<id>/results`. The teachable moment: the result is *transparent and reproducible* — the paper count, the platform, and the [LH engine](../../STARVote_LH_tabulation_engine/) all agree, and anyone in the room can verify it.

## Step 6 (advanced) — scan the paper back into YAML

The **return path** is to photograph the filled ballots and OCR the scores into a YAML the [LH engine](../why_yaml_test_cases.md) tabulates — closing the loop from paper to a fully-auditable digital count. That's a harder tool (it needs an OCR / vision engine, confidence thresholds, and human review of illegible marks), and it **isn't built yet** — the functional spec (batch of images → grayscale/deskew → read the 0–5 grid → validate → emit `voting_method: STAR` YAML with a run log) is the documented roadmap. **Until then, just transcribe the paper ballots into a YAML by hand** — the format is trivial (a candidate header, then one comma-separated row of 0–5 scores per ballot) — and run the engine.

## Why do this (the teaching value)

- **Demystifies the method** — students *see* that STAR is simple to count, not a black box.
- **Three independent counts that agree** — paper, BetterVoting, and the LH engine — which is exactly the trust story ("don't believe it, check it").
- **Perfect for classrooms, clubs, and workshops** — everyone participates, and the result is theirs to verify.

## See also

- [Teaching STAR Voting](teaching_star_voting.md) — the presenter's guide (arc, terms, misconceptions)
- [Count a STAR election by hand](count_star_by_hand.md) · [Summability](STAR_summability.md) — why it scales
- [BetterVoting and the LH engine — one election, two reports](../tabulation_engines/bettervoting_and_the_engine.md) — the digital cross-check
