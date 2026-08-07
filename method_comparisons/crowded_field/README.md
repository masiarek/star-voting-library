# The crowded field — one electorate, three ballot sizes

**Level: 201 → 301 · deep dive**

→ The measurement behind it: [Why more candidates make every method miss](../../07_Concepts/topics/condorcet/why_more_candidates_miss.md) · the rate it explains: [Condorcet efficiency, measured](../../07_Concepts/topics/condorcet/condorcet_efficiency_measured.md) · [all method comparisons](../README.md)

Sixty-five voters. They never change their minds — not once, anywhere on this page. **Diego beats every rival head-to-head at every rung**, so on the one question "who does this electorate actually prefer?" the answer is the same in all three elections below.

What changes is how many other names are on the paper. Three candidates, then five, then seven. Watch the winners come apart.

| Field | [Ranked&nbsp;Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) | [STAR](../../01_STAR/01_Learn/README.md) | Score | [Approval](../../04_Approval/01_Learn/README.md) | [RCV-IRV](../../06_Other/RCV_IRV/concepts/README.md) | [Choose-One](../../07_Concepts/topics/plurality.md) |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| **3 candidates** | Diego | Diego | Diego | Diego | Diego | Diego |
| **5 candidates** | Diego | Diego | Diego | Diego | **Elsa** | **Bruno** |
| **7 candidates** | Diego | **Clara** | **Clara** | **Felix** | **Clara** | **Greta** |

At three candidates every method in the library agrees. At seven, four different people win, and only the Condorcet method still returns the candidate the voters prefer over each of the others. **Nothing was added to this election but candidates.**

---

## The setup

Everyone lives on one axis — call it left to right, or cheap to expensive, or slow to fast. Voters sit in seven blocs; candidates stand at fixed points and never move.

```text
position     0       4       8       12      16      20      24
voter blocs  |       |       |       |       |       |       |
  (65 total) 6      10      13       9      12       8       7

rung 1 (3)     A                   D                     G
rung 2 (5)     A         B         D     E               G
rung 3 (7)     A         B     C   D     E   F           G

             A=Ana(1)   B=Bruno(6)   C=Clara(9)   D=Diego(11)
             E=Elsa(14)   F=Felix(16)   G=Greta(22)
```

Each rung adds one candidate on each side of Diego, and the pair added at rung 3 stands closer in than the pair added at rung 2. Diego never moves, and neither does anybody's opinion.

A voter's opinion of a candidate is just how close that candidate stands: **utility = minus the distance.** From that one rule every ballot is *derived*, never hand-written —

- the **0–5 score ballot** is each bloc's own min-max scaling of its utilities (the repo's `scores_from_util()`, shared with the simulations so there is one rule and not two);
- the **ranked ballot** is those same utilities in order;
- the **approval ballot** is the score ballot thresholded at 4.

[`build_ladder.py`](build_ladder.py) does exactly that and writes the twelve case files. `--check` re-derives them and fails if a committed file has drifted, so the claim "nothing was tuned" is enforced rather than promised.

**No result on this page is decided by a tie-break.** At every rung the plurality count, both score placings, the runoff, every IRV elimination and the approval count resolve outright. That was hard to arrange and it is the point: an earlier draft had RCV-IRV eliminating on a tied round, and the whole "IRV misses the Condorcet winner" result flipped when the engine broke that tie the other way. A demonstration that turns on a coin demonstrates nothing.

---

## Rung 1 — three candidates, and nobody disagrees

Diego takes **34 of 65 first choices** — an outright majority, so even Choose-One and RCV-IRV land on him. He leads the scoring round 266 to 123, and wins the runoff 50–15 with not one voter undecided between the finalists.

<!-- report:crowded_field_c3_star -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 65 ballots.
Count × Ana,Diego,Greta
   13 ×   3,    5,    0
   12 ×   0,    5,    4
   10 ×   5,    4,    0
    9 ×   0,    5,    0
    8 ×   0,    3,    5
    7 ×   0,    2,    5
    6 ×   5,    3,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Diego         -- 266 -- First place
   Greta         -- 123 -- Second place
   Ana           -- 119
 Diego and Greta advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Diego         -- 50 -- First place
   Greta         -- 15
   Equal Support --  0
 Diego wins.
   Runoff math:
     65  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     65  voters with a preference  (majority = 33)
           Diego 50 (77%)  ·  Greta 15 (23%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Diego
```
<!-- /report -->

Full counts: [STAR](cases/cases_pages/crowded_field_c3_star.md) · [Ranked Robin](cases/cases_pages/crowded_field_c3_ranked_robin.md) · [RCV-IRV](cases/cases_pages/crowded_field_c3_irv.md) · [Approval](cases/cases_pages/crowded_field_c3_approval.md)

This rung exists to close off the obvious objection. If the methods disagree later, it is not because the electorate is strange — with a small field this electorate is so unambiguous that six methods reading four different ballots all return the same person.

## Rung 2 — five candidates, and the choose-one family leaves

Bruno joins at 6 and Elsa at 14, one on each side of Diego. **Not one voter has changed their mind**, and Diego still beats all four rivals head-to-head.

But Diego's first choices collapse from 34 to **9**. That is arithmetic, not persuasion: Bruno and Elsa now stand between him and voters who previously had nobody closer. Choose-One elects **Bruno** (23 first choices), and RCV-IRV eliminates Diego early and elects **Elsa**.

```
first choices, rung 2 (from crowded_field_c5_irv.yaml, round 1)
   Bruno  23   ← Choose-One winner
   Greta  15
   Elsa   12
   Diego   9   ← beats all four of them head-to-head
   Ana     6
```

STAR, Score, Approval and Ranked Robin all still elect Diego. The score ballot has not run out of room yet, and the runoff is decisive: Diego 38, Elsa 27.

Full counts: [STAR](cases/cases_pages/crowded_field_c5_star.md) · [Ranked Robin](cases/cases_pages/crowded_field_c5_ranked_robin.md) · [RCV-IRV](cases/cases_pages/crowded_field_c5_irv.md) · [Approval](cases/cases_pages/crowded_field_c5_approval.md)

## Rung 3 — seven candidates, and the score ballot runs out of room

Clara joins at 9 and Felix at 16, one on each side again. Diego **still beats all six rivals head-to-head** — including Clara, 36–29.

STAR elects Clara anyway. And the interesting part is *how*:

- Clara edges Diego in the scoring round, **225 to 219**.
- **Both reach the runoff.** So this is *not* the top-two rule discarding the compromise candidate — the mechanism everybody reaches for first, and not the one operating here.
- In the runoff, **25 of the 65 voters express no preference at all** between Clara and Diego. Clara wins what is left, 23–17.

Diego's 36–29 win over Clara is real on the spectrum and simply is not on the paper. Seven candidates on a six-rung ballot (0–5) does not leave enough room to separate two candidates standing two steps apart, so a third of the electorate is recorded as indifferent between them.

<!-- report:crowded_field_c7_star -->
```text
[Divergence from STAR]
  STAR                   = Clara
  Choose-One (Plurality) = Ana   (differs from STAR)
  RCV-IRV                = Felix   (differs from STAR)
  Approval               = Diego   (differs from STAR)
  Note: 65 of 65 ballots (100%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/crowded_field_c7_star_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 65 ballots.
Count × Ana,Bruno,Clara,Diego,Elsa,Felix,Greta
   13 ×   3,    5,    5,    4,   3,    2,    0
   12 ×   0,    2,    3,    3,   4,    5,    3
   10 ×   5,    5,    4,    3,   2,    2,    0
    9 ×   0,    2,    4,    5,   4,    4,    0
    8 ×   0,    1,    2,    3,   4,    4,    5
    7 ×   0,    1,    2,    2,   3,    4,    5
    6 ×   5,    4,    3,    3,   2,    1,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Clara         -- 225 -- First place
   Diego         -- 219 -- Second place
   Elsa          -- 208
   Felix         -- 208
   Bruno         -- 196
   Ana           -- 119
   Greta         -- 111
 Clara and Diego advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Clara         -- 23 -- First place
   Diego         -- 17
   Equal Support -- 25
 Clara wins.
   Runoff math:
     65  ballots cast
   − 25  Equal Support (no preference between the two finalists)
     ──
     40  voters with a preference  (majority = 21)
           Clara 23 (57%)  ·  Diego 17 (42%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Clara
```
<!-- /report -->

Read the pairwise matrix against the score totals: **Diego wins every column and loses the election.** The engine's own `[Condorcet Winner]` line reads off the score ballots, and on those there is no strict Condorcet winner at all — which is the same fact from the other end.

**Ignore the `[Divergence from STAR]` lines in that report**, and note why, because it is the same lesson once more. To guess at RCV-IRV and Choose-One the engine has to convert scores to ranks, and its own note says *65 of 65 ballots had equal non-zero scores* — so those two lines are reporting a tie-break, not a method. Counted on real ranked ballots ([`crowded_field_c7_irv.yaml`](cases/cases_pages/crowded_field_c7_irv.md)) RCV-IRV elects **Clara** and Choose-One elects **Greta** on 15 of 65. Approval, which has a ballot of its own and needs no conversion, elects **Felix**.

Four winners, six methods, one unchanged electorate.

Full counts: [STAR](cases/cases_pages/crowded_field_c7_star.md) · [Ranked Robin](cases/cases_pages/crowded_field_c7_ranked_robin.md) · [RCV-IRV](cases/cases_pages/crowded_field_c7_irv.md) · [Approval](cases/cases_pages/crowded_field_c7_approval.md)

---

## Read this fairly — four things it does not show

**1. It is a construction, not a survey.** These candidate positions were searched for, not stumbled on. What makes the ladder worth anything is that the *same* effects are measurable at scale over randomly drawn electorates — every method's Condorcet efficiency falls with field size across all four electorate models, and the mechanisms behind it are measured rather than asserted: [Why more candidates make every method miss](../../07_Concepts/topics/condorcet/why_more_candidates_miss.md). Treat this folder as the worked example and that page as the evidence.

**2. Ranked Robin is reading a better ballot.** The RR and IRV files get a full-resolution ranking; the STAR and Approval files get six rungs and two. At seven candidates a 0–5 ballot **cannot** express a strict ranking at all — six rungs, seven candidates — so part of what separates the Condorcet column from the score columns at rung 3 is *ballot expressiveness*, not tabulation rule. That cut is not a get-out for STAR, because a real 0–5 STAR election really does have only six rungs and really would elect Clara. But it does mean the automatic runoff is not what failed here, and anyone quoting rung 3 as "STAR's top-two rule loses the compromise candidate" has the mechanism backwards.

**3. Approval's column depends on where the line is drawn.** These files approve at 4+. Approve at 3+ and it is a different election. There is no such thing as "Approval's answer" without the cutoff attached, which is why it is stated on every Approval file here.

**4. Choose-One and RCV-IRV are counted on the ranked files, deliberately.** The STAR files' `[Divergence from STAR]` block has to convert scores to ranks to guess at them, and at rung 3 nearly every ballot carries tied scores — so that block is measuring the score-to-rank tie-break rather than the method, and says so in its own note. The numbers quoted above come from `crowded_field_c*_irv.yaml`, where the ballots are real rankings.

---

## The files

Twelve cases, all generated by [`build_ladder.py`](build_ladder.py). LH-only — no BetterVoting election backs them, because the ballots are derived from a construction rather than cast by anyone.

| Rung | STAR | Ranked Robin | RCV-IRV | Approval |
|---|---|---|---|---|
| 3 candidates | [page](cases/cases_pages/crowded_field_c3_star.md) · [`yaml`](cases/crowded_field_c3_star.yaml) | [page](cases/cases_pages/crowded_field_c3_ranked_robin.md) · [`yaml`](cases/crowded_field_c3_ranked_robin.yaml) | [page](cases/cases_pages/crowded_field_c3_irv.md) · [`yaml`](cases/crowded_field_c3_irv.yaml) | [page](cases/cases_pages/crowded_field_c3_approval.md) · [`yaml`](cases/crowded_field_c3_approval.yaml) |
| 5 candidates | [page](cases/cases_pages/crowded_field_c5_star.md) · [`yaml`](cases/crowded_field_c5_star.yaml) | [page](cases/cases_pages/crowded_field_c5_ranked_robin.md) · [`yaml`](cases/crowded_field_c5_ranked_robin.yaml) | [page](cases/cases_pages/crowded_field_c5_irv.md) · [`yaml`](cases/crowded_field_c5_irv.yaml) | [page](cases/cases_pages/crowded_field_c5_approval.md) · [`yaml`](cases/crowded_field_c5_approval.yaml) |
| 7 candidates | [page](cases/cases_pages/crowded_field_c7_star.md) · [`yaml`](cases/crowded_field_c7_star.yaml) | [page](cases/cases_pages/crowded_field_c7_ranked_robin.md) · [`yaml`](cases/crowded_field_c7_ranked_robin.yaml) | [page](cases/cases_pages/crowded_field_c7_irv.md) · [`yaml`](cases/crowded_field_c7_irv.yaml) | [page](cases/cases_pages/crowded_field_c7_approval.md) · [`yaml`](cases/crowded_field_c7_approval.yaml) |

Run one:

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/crowded_field/cases/crowded_field_c7_star.yaml
```

Rebuild them all from the positions, or check the committed files still match:

```bash
uv run method_comparisons/crowded_field/build_ladder.py --check
```

Every Ranked Robin rung is additionally cross-checked against `pref_voting`'s independent Copeland — a library nobody here wrote — which agrees at all three:

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/ranked_robin_report.py method_comparisons/crowded_field/cases/crowded_field_c7_ranked_robin.yaml
```

---

**See also:** [Why more candidates make every method miss](../../07_Concepts/topics/condorcet/why_more_candidates_miss.md) (the measurement) · [Condorcet efficiency, measured](../../07_Concepts/topics/condorcet/condorcet_efficiency_measured.md) (the rates) · [center squeeze](../../07_Concepts/topics/center_squeeze/README.md) (rung 2's mechanism, named) · [the divergence ledger](../divergence_review/INDEX.md) (real library elections where methods disagree) · [Condorcet efficiency topic hub](../../07_Concepts/topics/condorcet/README.md)
