# BV2144 — Felsenthal Example 1: four plurality paradoxes in one 7-voter election

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/mxfmhm) · **[results ↗](https://bettervoting.com/mxfmhm/results)** (election `mxfmhm`).

One tiny election — 7 voters, 3 candidates — demonstrates four paradoxes of Choose-One (Plurality) voting **simultaneously**, then shows STAR resolving all four. Two races on the same electorate: a Choose-One race (Ana wins) and a STAR race with the rankings mapped to 0–5 scores (Bo wins).

## Source

Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / Centre for Philosophy of Natural and Social Science, London School of Economics; revised 26 May 2010. Presented at the Leverhulme Trust *Voting Power in Practice* workshop, Château du Baffy, Normandy, 30 July – 2 August 2010. Appendix "Exemplifying the Various Paradoxes that Afflict the Various Procedures", §A1 ("Demonstrating Paradoxes Afflicting the Plurality Procedure"), **Example 1**.

## The election

7 voters rank three candidates (Felsenthal's *a, b, c* → cast as **Ana, Bo, Cal**):

```
No. of voters    Preference ordering
      3          Ana > Bo > Cal
      2          Bo  > Cal > Ana
      2          Cal > Bo  > Ana
```

The head-to-head facts: **Bo is the Condorcet winner** (beats Ana 4–3 and Cal 5–2). **Ana is the Condorcet loser** (loses to both) **and the absolute loser** — a majority, 4 of 7 voters, rank Ana dead **last**.

## The four paradoxes (Choose-One race)

All four are *simple* paradoxes in Felsenthal's classification — the surprising outcome follows from the ballots as cast — except the spoiler, which is *conditional* (it appears when one datum, Cal's presence, changes). Each links to its teaching page:

| Paradox | What happens here | Teaching page |
|---|---|---|
| Condorcet winner paradox | Bo beats everyone head-to-head, yet loses | [condorcet_winner_paradox.md](../../00_start_here/voting_paradoxes/condorcet_winner_paradox.md) |
| Condorcet loser paradox | Ana loses to everyone head-to-head, yet wins | [condorcet_loser_paradox.md](../../00_start_here/voting_paradoxes/condorcet_loser_paradox.md) |
| Absolute loser paradox | A majority ranks Ana *last*, yet Ana wins | [absolute_loser_paradox.md](../../00_start_here/voting_paradoxes/absolute_loser_paradox.md) |
| SCC / spoiler | If Cal drops out, Bo beats Ana 4–3 | [spoiler_scc.md](../../00_start_here/voting_paradoxes/spoiler_scc.md) |

Choose-One counts only first choices: **Ana 3, Bo 2, Cal 2 → Ana wins** — the candidate a majority ranked last.

## The STAR race — same voters, different tabulation

Ranks map to scores with the house map (N=3: top=5, mid=3, bottom=1). Scores: **Bo 25, Ana 19, Cal 19** — a scoring-round tie for the second finalist slot, broken by head-to-head preference (Cal beats Ana 4–3, so Cal advances). Bo wins the automatic runoff **5–2**. STAR elects the Condorcet winner; all four paradoxes above vanish under the same voters' preferences.

## View 1 — BetterVoting

Live results: **[bettervoting.com/mxfmhm/results ↗](https://bettervoting.com/mxfmhm/results)**. BV elects **Ana** in the Choose-One race and **Bo** in the STAR race — matching the LH engine on both (BV's tiebreak `perm` is pinned as `lot_numbers` in the Plurality YAML; it only touches the moot Bo/Cal second-place tie).

## View 2 — LH engine

Choose-One race ([bv2144_mxfmhm_plurality.yaml](cases/bv2144_mxfmhm_plurality.yaml)):

```
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 7 ballots.
Count × Ana,Bo,Cal
    3 ×   1, 0,  0
    2 ×   0, 1,  0
    2 ×   0, 0,  1

Scoring Round
 The two highest-scoring candidates advance to the next round.
   Ana           -- 3 -- First place
   Bo            -- 2 -- Tied for second place
   Cal           -- 2 -- Tied for second place

Automatic Runoff Round
   Ana           -- 3 -- First place
   Cal           -- 2
   Equal Support -- 2
 Ana wins.
   Voters with a preference: 5 of 7 (2 Equal Support).
   Ana 3 (60%) vs Cal 2 (40%); majority = 3.

Winner — Choose-One / Plurality Voting Method (single winner)
 Ana
```

(The Bo/Cal tie for the *second finalist slot* runs down LH's tie ladder to the pre-published lot — irrelevant to the winner: Ana beats either finalist. Full ladder in the [tabulated mirror](cases/cases_tabulated/bv2144_mxfmhm_plurality_tabulated.txt).)

STAR race ([bv2144_mxfmhm_star.yaml](cases/bv2144_mxfmhm_star.yaml)):

```
--- STAR Voting Method (single winner) ---
 Tabulating 7 ballots.
Count × Ana,Bo,Cal
    3 ×   5, 3,  1
    2 ×   1, 5,  3
    2 ×   1, 3,  5

Scoring Round
   Bo            -- 25 -- First place
   Ana           -- 19 -- Tied for second place
   Cal           -- 19 -- Tied for second place
 Bo advances, but there's a two-way tie for second.

Scoring Round: First tiebreaker
 The candidate preferred in the most head-to-head matchups advances.
   Cal           -- 4 -- Second place
   Ana           -- 3
 Bo and Cal advance.

Automatic Runoff Round
   Bo            -- 5 -- First place
   Cal           -- 2
 Bo wins.
   Voters with a preference: 7 of 7 (no Equal Support).
   Bo 5 (71%) vs Cal 2 (29%); majority = 4.

Winner — STAR Voting Method (single winner)
 Bo
```

## Agreement

| Race | BetterVoting | LH engine | Agree? |
|---|---|---|---|
| Choose-One (Plurality) | Ana | Ana | ✓ |
| STAR (ranks→scores) | Bo | Bo | ✓ |

Frozen export: [bv2144_mxfmhm_bv_export.json](cases/bv2144_mxfmhm_bv_export.json). Full engine detail: [plurality mirror](cases/cases_tabulated/bv2144_mxfmhm_plurality_tabulated.txt) · [STAR mirror](cases/cases_tabulated/bv2144_mxfmhm_star_tabulated.txt).
