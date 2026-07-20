# BV132 — verify number of votes cast (Bloc STAR) · issue [#1073](https://github.com/Equal-Vote/bettervoting/issues/1073)

*BetterVoting reports the wrong number of voters on a Bloc STAR election: it drops the two "flat" ballots (every candidate scored the same) as abstentions. The winners are still correct — the bug is the vote count / turnout, not the result.*

Reference files: [`bv132_verify_votes_bloc.yaml`](cases/bv132_verify_votes_bloc.yaml) (LH, `expected_winners: [C, B]`) · frozen export [`bv132_verify_votes_bloc_bv_export.json`](cases/bv132_verify_votes_bloc_bv_export.json) (BV election `3494cb`). Backs sheet row **BV132**.

## The election

Bloc STAR, 3 candidates, **2 seats**, 4 ballots — two of them flat:

```
A,B,C
1,1,1     ← flat (no preference)
5,5,5     ← flat (no preference)
1,2,3
1,2,3
```

## View 1 — BetterVoting (the bug)

BetterVoting's result page shows **"2 voters"** and scoring totals **A=2, B=4, C=6** — which is *only* the two `1,2,3` ballots. The two flat ballots have been dropped. (Winners shown: **C and B**.) The frozen export confirms why: its `summaryData` carries `nAbstentions: 2`, `nTallyVotes: 2` — BV classified the flat ballots as **abstentions**.

*(Drop the BV screenshot into an `img/` subfolder as `img/3494cb_result.png` to add it here.)*

## View 2 — the LH report (all four ballots counted)

The same ballots through the reference engine. Note **"Tabulating 4 ballots,"** the score distribution (each candidate's real total), and — the key line — the runoff denominator **"2 of 4 (2 Equal Support)"**: LH keeps the two flat ballots in the count as *Equal Support* (no preference) rather than discarding them.

```
--- Bloc STAR Voting Method (2 winners) ---
 Tabulating 4 ballots.
A,B,C
1,1,1
5,5,5
1,2,3
1,2,3

[Score Distribution] (number of ballots giving each score)
   5  4  3  2  1  0  | Total   Avg
A  1  0  0  0  3  0  |     8   2.0
B  1  0  0  2  1  0  |    10   2.5
C  1  0  2  0  1  0  |    12   3.0
 Want to fill 2 seats.

Round 1: Scoring Round
   C  -- 12 -- First place
   B  -- 10 -- Second place
   A  --  8
 C and B advance.
Round 1: Automatic Runoff Round
   C  -- 2 -- First place
   B  -- 0
   Equal Support -- 2
 C wins.
   Voters with a preference: 2 of 4 (2 Equal Support).   ← all 4 ballots counted

Round 2: Scoring Round
   B  -- 10 -- First place
   A  --  8 -- Second place
 B and A advance.
Round 2: Automatic Runoff Round
   B  -- 2 -- First place
   A  -- 0
   Equal Support -- 2
 B wins.

Winners — Bloc STAR Voting Method (2 winners)
 C
 B
```

Full audit copy: [`_main_tabulated/bv132_verify_votes_bloc_tabulated.txt`](cases/cases_tabulated/bv132_verify_votes_bloc_tabulated.txt).

## The diagnostic (where the ballots go)

The frozen export localizes the defect precisely:

- **Ingestion is fine.** The export's `Ballots` array holds **all 4** ballots.
- **Tabulation drops them.** `summaryData` reports `nAbstentions: 2`, `nTallyVotes: 2`; the score totals (A=2/B=4/C=6) are only the two non-flat ballots. So BV treats a fully-flat ballot as an abstention and removes it from the count.
- **Winners are unaffected.** A flat ballot adds equally to every candidate and is Equal in every head-to-head, so it can never change a STAR/Bloc result — LH and BV both elect **C, B**. The visible harm is the wrong voter count / turnout (and any percentage or quorum computed from it).

## Related

- [#1407](https://github.com/Equal-Vote/bettervoting/issues/1407) — flat ballot mis-filed as abstention (the same root cause).
- [#1035](https://github.com/Equal-Vote/bettervoting/issues/1035) — `NaN` on equal ties/preferences (same ballot family).
- [#904](https://github.com/Equal-Vote/bettervoting/issues/904) — the export also labels `votingMethod: "STAR"` rather than "Bloc STAR".
- Concept: [Flat scores, ties & tie-breaking](../../01_STAR/Flat_scores_ties/README.md) · [why flat ballots don't change the winner](../../00_start_here/topics/ties/why_contrived_tie_cases.md).
