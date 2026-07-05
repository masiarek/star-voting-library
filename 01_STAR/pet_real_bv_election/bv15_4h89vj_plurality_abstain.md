# BV15 — Plurality + abstentions: the turnout undercount

*BetterVoting test **BV15** (`4h89vj`, "Basic – 2 candidates – Plurality – Abstain"). The Plurality instance of **bettervoting#740** — a **reporting** gap, not a tabulation bug. BetterVoting elects the right winner (Andre) but its results widget reports only the **meaningful** ballots as "voters," dropping the fully-abstained ones from the headline turnout. The count is short by exactly the number of abstentions.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/4h89vj) · **[results ↗](https://bettervoting.com/4h89vj/results)** (election `4h89vj`).

Reference file: [`bv15_4h89vj_plurality_abstain.yaml`](bv15_4h89vj_plurality_abstain.yaml) (`expected_winners: [Andre]`). Frozen export: [`bv15_4h89vj_plurality_abstain_bv_export.json`](bv15_4h89vj_plurality_abstain_bv_export.json). Backs sheet row **BV15**. Issue: [bettervoting#740](https://github.com/Equal-Vote/bettervoting/issues/740) (*"Add 'stats for nerds' widget including abstentions"*).

## The finding (label it right)

The sheet/tracker calls this "star-server#740", but the repo moved from `star-server` to `bettervoting` — the **number stayed**, so it is **bettervoting#740**. And #740 is **not a tabulation error**: its title is *"Add 'stats for nerds' widget including abstentions,"* and the body (Adam's own report) says *"We are missing abstentions in the vote count… As-is: 2 voters. Should be: 5 voters (3 abstentions and 2 meaningful)."* The winner is computed correctly; the **displayed turnout** is what's wrong.

Crucially, BetterVoting's backend already has the numbers. The frozen export's `summaryData` reads **`nTallyVotes: 7`, `nAbstentions: 5`** (7 + 5 = 12 cast) — correct. So #740 is purely that the **results UI never surfaces** the 5 abstentions or the 12-ballot total; it shows the 7 as if that were the whole turnout.

## The election

Plurality, 2 candidates, **12 ballots** — five for Andre, two for Blake, five blank:

```
Andre,Blake
5,0   × 5   Andre  (a choose-one vote for Andre)
0,5   × 2   Blake  (a choose-one vote for Blake)
-,-   × 5   blank  — true abstentions (no score for anyone)
```

Andre 5, Blake 2 → **Andre wins** (BV `tieBreakType: none`; no tie).

## Why the LH file is STAR, not Plurality

The LH engine has **no standalone Plurality method** — its methods are STAR / Bloc / SSS / RRV / Allocated, plus auto RCV-IRV / Approval / Ranked Robin. With two candidates and choose-one ballots, *every* reasonable method elects the plurality leader, so each "vote for X" is modelled as a STAR **5/0** ballot. STAR, Approval, and Choose-One Plurality all name Andre here (no divergence to show). The point is the **count** — and STAR's self-reconciling runoff line prints exactly the accounting #740 is missing.

## The LH report (the accounting #740 wants)

```text
--- STAR Voting Method (single winner) ---
 Tabulating 12 ballots. Note: 5 of 12 ballots are marked as abstentions.
Count × Andre,Blake
    5 ×     5,    0
    5 ×     -,    -
    2 ×     0,    5

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  Abs  | Total   Avg
Andre      5  0  0  0  0  2    5  |    25   3.6
Blake      2  0  0  0  0  5    5  |    10   1.4

Scoring Round
   Andre         -- 25 -- First place
   Blake         -- 10 -- Second place
 Andre and Blake advance.

Automatic Runoff Round
   Andre         -- 5 -- First place
   Blake         -- 2
   Equal Support -- 5
 Andre wins.
   Voters with a preference: 7 of 12 (5 Equal Support).
   Andre 5 (71%) vs Blake 2 (29%); majority = 4.

Winner — STAR Voting Method (single winner)
 Andre
```

The `Abs` column (5 for each candidate = the 5 blank ballots) and the runoff line **`7 of 12 (5 Equal Support)`** are precisely the "stats for nerds" turnout breakdown #740 asks BetterVoting to add — LH reconciles `12 = 7 + 5` on the page. Full audit copy: [`_tabulated` mirror](pet_real_bv_election_tabulated/bv15_4h89vj_plurality_abstain_tabulated.txt).

## LH ↔ BetterVoting

| Quantity | BetterVoting `summaryData` | LH engine | Agree? |
|---|:--:|:--:|:--:|
| Winner | Andre | Andre | ✓ |
| Meaningful ballots | `nTallyVotes` 7 | 7 (voters with a preference) | ✓ |
| Abstentions | `nAbstentions` 5 | 5 (blank ballots) | ✓ |
| Ballots cast | (7 + 5 =) 12 | 12 | ✓ |

Both engines agree on every number. The **only** gap is display: LH puts `12 = 7 + 5` on the results page; BetterVoting's widget currently shows the 7 alone. This case pins the correct turnout accounting as the reference for #740 — and shows LH's runoff-reconciliation line as a ready model for the fix.

## See also

- [This set's lesson (README)](README.md) · [small_case abstention lesson](small_case_abstention_lesson.md) — the LH↔BV "no-preference" reconciliation these cases share.
- [Abstention vs Equal Support — minimal STAR test](pet_real_bv_election_pages/small_abstention_c2_b5.md) — the STAR sibling of this counting question.
- [Ballot & terminology basics](../../00_start_here/ballot_and_terminology_basics.md) · [Glossary](../../00_start_here/GLOSSARY.md) · [BV registry](../../00_start_here/YAML_test_case_index/BV_registry.md).
