# Reversal symmetry — when a method's "best" candidate is also its "worst"

*A voting method has **reversal symmetry** if flipping every voter's ballot — so everyone now expresses the exact opposite preference, as if choosing the **worst** candidate — can never re-elect the original winner. **RCV-IRV fails it:** here's a 24-voter election where IRV elects A whether the voters are picking the best candidate or the worst. It's a real, IRV-specific defect — conceded — though the example is a deliberately hard one (a Condorcet cycle), and the argument comes from a Range-advocacy source whose lean we disclose.*

→ Related: [IRV non-monotonicity](../../00_start_here/RCV_IRV/RCV_IRV_non_monotonicity.md) · [the participation / no-show paradox](../participation_no_show/) · [Condorcet cycles](../../00_start_here/RCV_Ranked_Robin/cycle_resolution.md) · glossary [`reversal symmetry`](../../00_start_here/GLOSSARY.md).

---

## The example

24 voters, three candidates, forming a **Condorcet cycle** (A beats B, B beats C, C beats A — nobody beats everyone):

| Voters | Ballot |
|---|---|
| 9 | B > C > A |
| 8 | A > B > C |
| 7 | C > A > B |

**Original — RCV-IRV elects A** ([`reversal_irv_original`](cases/cases_pages/reversal_irv_original.md)): C has the fewest first-choices, is eliminated, and C's ballots flow to A → **A wins 15–9.**

**Now reverse every ballot** (each voter expresses the exact opposite — as if electing the *worst* candidate) ([`reversal_irv_reversed`](cases/cases_pages/reversal_irv_reversed.md)): you'd expect A to finish *last*. Instead B is eliminated first, B's ballots flow to A, and **A wins again, 16–8.** IRV's "best" candidate and its "worst" candidate are the same one. That's a **reversal symmetry failure.**

## Which methods fail it

| Method | Reversal symmetry | On this example |
|---|:--:|---|
| **RCV-IRV**, Plurality | ❌ fail | IRV elects **A both ways** (winner = loser) |
| **Range / Score, Borda, Approval** | ✅ pass | additive — reversing the ballots reverses the totals |
| **Ranked Pairs, Schulze** (Condorcet) | ✅ pass | — |
| **STAR** | *avoids it here* | original → **B**, reversed → **A** ([star original](cases/cases_pages/reversal_star_original.md) · [reversed](cases/cases_pages/reversal_star_reversed.md)) — a *different* winner each way, so no winner=loser |
| **Ranked Robin** | *avoids it here* | flags the [cycle](../../00_start_here/RCV_Ranked_Robin/cycle_resolution.md) and resolves by margin |

**A careful, honest note on STAR:** the cases above show STAR *avoiding* the winner=loser on this electorate — **not** a proof that STAR satisfies reversal symmetry as a criterion. STAR is a hybrid (an additive scoring round plus a pairwise runoff), and the rank→score mapping used here (5/3/0) is a modeling choice. We claim only what we ran: STAR gives B then A, so its best and worst here differ.

## Keep it in proportion — the fair reading

- **The failure is real and IRV-specific** — worth knowing, and a clean symptom of the same root cause as [center squeeze](../../00_start_here/topics/center_squeeze/) and [non-monotonicity](../../00_start_here/RCV_IRV/RCV_IRV_non_monotonicity.md): IRV eliminates on *first-choice counts*, so reversing preferences doesn't cleanly reverse the outcome.
- **But the electorate is a deliberate Condorcet cycle** — there is *no* "correct" winner (Gibbard territory), so this is an engineered worst case, not a "STAR right, IRV wrong" story. Every method is on hard ground in a cycle.
- **Two of the source's other "disasters" are things we already cover.** The page's "strategic reversal" twist (raising A from bottom to top makes A *lose*) is plain [non-monotonicity](../../00_start_here/RCV_IRV/RCV_IRV_non_monotonicity.md); its "no-show" twist is the [participation paradox](../participation_no_show/). Nothing new there.
- **Disclose the lean.** The source is [rangevoting.org](https://www.rangevoting.org/IrvRevFail.html) — Warren Smith / the Center for Range Voting, an aggressively pro-**Range** advocacy site (advocacy-adjacent: strong for mechanics, weak for verdicts). Its framing ("psychotic," "insane," "silly myth") is polemic, and the criterion it prizes — like [self-consistency](../../00_start_here/RCV_IRV/RCV_IRV_non_monotonicity.md#a-sharper-critique-and-where-it-overreaches-reading-advocacy-critically) — is one *additive* methods have and elimination methods lack, so the argument is really a case for pure Score (it would fault STAR's runoff too, in principle). We include it because the library checks pro-Range anti-IRV arguments by the same standard it checks the [pro-RCV ones](../fairvote_star_whitepaper/). *(The page also cites "Peru 2006" as a real instance; we haven't verified that and don't repeat it as fact.)*

## Reproduce it

```
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/reversal_symmetry/cases/reversal_irv_original.yaml
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/reversal_symmetry/cases/reversal_irv_reversed.yaml
```
