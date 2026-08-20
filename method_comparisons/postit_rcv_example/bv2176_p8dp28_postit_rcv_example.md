# The Post-it RCV example (20 voters) — the runoff RCV-IRV never held

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/p8dp28) · **[results ↗](https://bettervoting.com/p8dp28/results)** (election `p8dp28`, Test ID **BV2176**).

The 20-voter election from Equal Vote's video **["Updated: How does RCV work? — With Post-its!"](https://youtu.be/Vte4nly_Neg)** — the whiteboard demo that walks through an RCV-IRV count sticky note by sticky note, then asks the question the count itself never asks: *was the eliminated candidate actually stronger head-to-head?* Four candidates (Purple, Green, Blue, Pink), one electorate, three tabulations live on BetterVoting: RCV-IRV elects **Purple**, STAR (on the video's own 0–5 scores) elects **Blue**, and Ranked Robin exposes a Condorcet cycle whose 2–1 tie goes to Green. Same ballots, three defensible winners: the tabulation decides. For two years this page said the Ranked Robin race split the engines — Green on BetterVoting, Blue in the LH engine — and that was a bug on our side, corrected below. <!-- terminology-ok: bare RCV is inside the quoted video title -->

## The ballots

The same 20 voters, ranked (the video's Post-its) and scored 0–5 (the video's STAR comparison):

| # voters | ranked ballot | scores (Purple, Green, Blue, Pink) |
|---:|:--|:--|
| 7 | Purple | 5, 0, 0, 0 |
| 6 | Green > Blue > Pink | 0, 5, 4, 3 |
| 2 | Blue > Pink | 0, 0, 5, 4 |
| 1 | Blue > Green > Pink | 0, 4, 5, 3 |
| 1 | Blue > Purple | 4, 0, 5, 0 |
| 1 | Pink > Green > Purple | 3, 4, 0, 5 |
| 1 | Pink > Purple | 4, 0, 0, 5 |
| 1 | Pink | 0, 0, 0, 5 |

First choices: Purple 7, Green 6, Blue 4, Pink 3. Score totals: Purple 46, Blue 44, Pink 44, Green 38.

## The video's count — and the video's question

**RCV-IRV** (the whiteboard walk-through): round 1 eliminates Pink (3 first choices; 1 ballot transfers to Green, 1 to Purple, 1 bullet-vote exhausts). Round 2 stands at Purple 8, Green 7, Blue 4 — Blue is eliminated (1 to Green, 1 to Purple, and both Blue>Pink ballots exhaust, Pink being already gone). Final: **Purple 9, Green 8**, with 3 of the 20 ballots exhausted — Purple wins with 9 of the 17 still-active ballots.

The video then flips the round-2 elimination: *what if Green (7 votes) had gone out instead of Blue (4)?* All six Green>Blue>Pink ballots land on Blue, and **Blue wins 10–9**. That hypothetical is not a fluke of transfer order — it is the actual head-to-head: on these 20 ballots **Blue beats Purple 10–9**. RCV-IRV eliminated Blue without ever holding that matchup.

**STAR** holds it automatically. Scoring round: Purple 46 advances; the **44–44 tie** between Blue and Pink for the second finalist slot breaks by the official protocol's next rung — head-to-head, where Blue is preferred over Pink 10–3. The automatic runoff is then exactly the matchup the video asked about: **Blue 10, Purple 9** (1 Equal Support) — Blue wins. It is also a **Runoff Reversal**: the score leader (Purple, 46) loses the majority check, STAR working as designed. BetterVoting concurs on every rung (`tieBreakType: head_to_head` on the scoring tie).

## One electorate, three counts

| Race (BV) | Method | BV winner | LH winner | How |
|---|---|:--:|:--:|:--|
| Post-its 20 voters — STAR | STAR | **Blue** | **Blue** | 46/38/44/44; second-finalist tie → head-to-head Blue 10–3 Pink; runoff Blue 10–9 (Runoff Reversal) |
| Post-its 20 voters — RCV-IRV | IRV | **Purple** | **Purple** | 7/6/4/3 → 8/7/4 → 9–8; 3 exhausted |
| Post-its 20 voters — Ranked Robin | RankedRobin (Copeland) | **Green** | **Green** | 2-way Copeland tie at 2–1, settled by the finalists' own head-to-head (below) |

## The Ranked Robin race — a two-way tie, settled at the first rung

There is **no Condorcet winner** here: the pairwise picture is a genuine cycle (Purple beats Green 9–8, Green beats Blue 7–4, Blue beats Purple 10–9 — and Pink beats Purple 12–8). Green and Blue each go **2–1** (Copeland 2), so the tally stops and Ranked Robin's published [degrees of ties](../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md) take over. With exactly two finalists the **1st Degree — greatest sum of win margins over the other finalists — is simply their own match**: Green beats Blue **7–4**, so Green wins the tie +3 to −3. BetterVoting reports the same, live, by the same reasoning.

**This race is one of four live BetterVoting elections where the LH engine got that wrong**, and the one where it was written up at greatest length. Until 2026-08-19 the engine had no 1st Degree rung: it broke a Copeland tie by *total margin over the whole field* — the protocol's **2nd Degree** — where Blue's +5 edges Green's +4, and it elected **Blue**, the candidate who had just lost the finalists' match 4–7. The page you are reading described that as the two engines' "ladders parting ways," a difference of convention between two defensible rules. It was not a convention; it was a missing rung, and BetterVoting was the engine following the spec. The independent `pref_voting` Copeland check never took a side — it reports the leader *set* {Blue, Green} and declines — which is exactly why it could not catch this: a cross-check that only asks *"is the winner inside the tied set?"* passes both a correct and an incorrect tiebreak.

---

## LH engine reports (View 2)

### STAR — Blue (the runoff the video asked for)

<!-- report:bv2176_p8dp28_star -->
```text
[Divergence from STAR]
  STAR                   = Blue
  Choose-One (Plurality) = Purple   (differs from STAR)
  RCV-IRV                = Purple   (differs from STAR)
  Approval               = Pink   (differs from STAR)
  RCV-RR                 = Green   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bv2176_p8dp28_star_RCV-IRV_tabulated.txt
  RCV-RR round-robin: cases_tabulated/bv2176_p8dp28_star_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (Purple)
 - Runoff Round Winner   = (Blue)
  Candidate Purple earned the highest total score, but
  Candidate Blue won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 20 ballots.
Count × Purple,Green,Blue,Pink
    7 ×      5,    0,   0,   0
    6 ×      0,    5,   4,   3
    2 ×      0,    0,   5,   4
    1 ×      0,    4,   5,   3
    1 ×      4,    0,   5,   0
    1 ×      3,    4,   0,   5
    1 ×      4,    0,   0,   5
    1 ×      0,    0,   0,   5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Purple        -- 46 -- First place
   Blue          -- 44 -- Tied for second place
   Pink          -- 44 -- Tied for second place
   Green         -- 38
 Purple advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Blue          -- 10 -- Second place
   Pink          --  3
   Equal Support --  7
 Purple and Blue advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Blue          -- 10 -- First place
   Purple        --  9
   Equal Support --  1
 Blue wins.
   Runoff math:
     20  ballots cast
   −  1  Equal Support (no preference between the two finalists)
     ──
     19  voters with a preference  (majority = 10)
           Blue 10 (53%)  ·  Purple 9 (47%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Blue
```
<!-- /report -->
### RCV-IRV — Purple (the video's whiteboard rounds)

```
ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Purple             7  Hopeful
Green              6  Hopeful
Blue               4  Hopeful
Pink               3  Rejected

ROUND 2
Candidate      Votes  Status
-----------  -------  --------
Purple             8  Hopeful
Green              7  Hopeful
Blue               4  Rejected
Pink               0  Rejected
Blank Votes        1  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Purple             9  Elected
Green              8  Rejected
Blue               0  Rejected
Pink               0  Rejected
Blank Votes        3  Rejected
```

### Ranked Robin — the cycle, the 2–1 tie, and the 1st Degree

```text title="Abridged for the lesson — the round-robin and win–loss blocks of the full report"
Round-Robin — every pair, head-to-head (For – Against):
   Purple  beats Green     9 –  8
   Blue    beats Purple   10 –  9
   Pink    beats Purple   12 –  8
   Green   beats Blue      7 –  4
   Green   beats Pink      7 –  5
   Blue    beats Pink     10 –  3

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  Green      2–1–0         2      +4            +3  Blue, Pink
    2  Blue       2–1–0         2      +5            -3  Pink, Purple
    3  Pink       1–2–0         1      -5             —  Purple
    4  Purple     1–2–0         1      -4             —  Green

Winner — Ranked Robin (RCV-RR): Green
   *** 2 candidates tie for the most wins (Green, Blue) — tied on the tally, not a cycle (some of them beat others head-to-head, but no loop closes). Resolved by the 1st Degree tiebreaker: Green has the greatest sum of win margins over the other finalists (+3).
```

Read the two margin columns against each other and the whole bug is one line wide: **Margin** is the 2nd Degree (whole field) and puts Blue ahead by one point; **vs finalists** is the 1st Degree and puts Green ahead by six. The protocol asks the narrow question first. BetterVoting's live result for the same race is **Green**, and has been since the election was minted.

---

## Files

| Race | YAML | `_tabulated` mirror |
|---|---|---|
| STAR (lead) | [page](cases/cases_pages/bv2176_p8dp28_star.md) · [bv2176_p8dp28_star.yaml](cases/bv2176_p8dp28_star.yaml) | [txt](cases/cases_tabulated/bv2176_p8dp28_star_tabulated.txt) |
| RCV-IRV | [page](cases/cases_pages/bv2176_p8dp28_irv.md) · [bv2176_p8dp28_irv.yaml](cases/bv2176_p8dp28_irv.yaml) | [txt](cases/cases_tabulated/bv2176_p8dp28_irv_tabulated.txt) |
| Ranked Robin | [page](cases/cases_pages/bv2176_p8dp28_ranked_robin.md) · [bv2176_p8dp28_ranked_robin.yaml](cases/bv2176_p8dp28_ranked_robin.yaml) | [txt](cases/cases_tabulated/bv2176_p8dp28_ranked_robin_tabulated.txt) |

Frozen BetterVoting export (Election + Ballots + Results): [bv2176_p8dp28_bv_export.json](cases/bv2176_p8dp28_bv_export.json) — BV's stored winners are STAR **Blue**, RCV-IRV **Purple**, Ranked Robin **Green**, and the corrected LH engine now matches all three. The export was frozen while the third one still read as a disagreement, so it is also the receipt for the bug.

Related: [the video](https://youtu.be/Vte4nly_Neg) · [degrees of ties](../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md) · [cycle resolution](../../05_Ranked_Robin/01_Learn/cycle_resolution.md) · up: [method_comparisons](../README.md)

*BetterVoting result screenshots (View 1) can be dropped into `img/` as `img/p8dp28_<what>.png` and linked here.*

# file: bv2176_p8dp28_postit_rcv_example.md
