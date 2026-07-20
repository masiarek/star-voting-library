# The Dark Horse — how the Borda count can elect a nobody with *zero* honest support

*A strategic pathology of the [Borda count](../../00_start_here/GLOSSARY.md) (and any strictly-ranked point method): a candidate every voter honestly ranks **last** can **win**, because each faction is tempted to bury its rivals behind the harmless nobody — and if they all do, the nobody backs into victory. It's a **prisoner's dilemma** in ballot form. **STAR and Ranked Robin can't be dark-horsed**, because a score (or a pairwise comparison) lets you oppose a rival without being forced to prop anyone up.*

→ Part of the strategic-pathology set: [The strategic pathologies — five Molochs, and where STAR stands](../../00_start_here/topics/strategic_pathologies.md). Framing from Jameson Quinn (Center for Election Science). Related: [strategic voting](../../00_start_here/topics/strategic_voting.md) · [what makes a good winner?](../../00_start_here/topics/what_makes_a_good_winner.md).

---

## The scenario (Quinn's "Dark Horse 3")

Four candidates. **D is a nobody** — the honest *last* choice of every single voter. Three factions:

| Voters | Honest preference |
|---|---|
| 34 | A > B > C > D |
| 33 | B > A > C > D |
| 33 | C > A > B > D |

A is the honest winner every sensible way you count: the utilitarian favorite *and* the [Condorcet winner](../../00_start_here/topics/condorcet/) (A beats B, C, and D head-to-head).

## Honest Borda → A. All-strategic Borda → **D**. (verified with `pref_voting`)

Under Borda, each voter must hand out 3, 2, 1, 0 points. Honestly, that elects A:

```
HONEST Borda:   A 234,  B 200,  C 166,  D 0     → A wins
```

But the only way to hurt your rival under Borda is to rank *someone* above them — and the safe someone is the harmless **D**. So each faction is tempted to rank D **second**, burying its rivals at the bottom. If **all three** factions do it:

```
ALL-STRATEGIC Borda:  D 200,  A 168,  B 133,  C 99   → D wins
```

**D — the honest last choice of 100% of voters — wins.** Nobody wanted D; everyone only used D as a weapon against their rivals, and the weapon won the election.

### Why it's a prisoner's dilemma

- If **one** faction buries its rivals behind D, that faction profits.
- If **all** factions do it, they **all** lose to D — the worst outcome for everyone.
- Honesty is the socially best play, but each faction's *individual* incentive is to defect. Classic prisoner's dilemma — which is exactly why Quinn calls Dark Horse a "Moloch."

The root cause: Borda **forces** you to award points in rank order, so opposing a rival *requires* elevating someone else. There's no way to say "I oppose both my rival and the nobody equally."

## STAR and Ranked Robin can't be dark-horsed

A **score** ballot breaks the trap: you give your rival a **0** *and* the nobody D a **0**. Opposing a rival never props up anyone. Scored honestly (favorite 5, the compromise ~1, D a 0):

```
STAR Scoring Round
   A -- 236 -- First place
   B -- 232 -- Second place
   C -- 198
   D --   0            ← the nobody stays a nobody
Automatic Runoff
   A -- 34   vs   B -- 33     → A wins

[Divergence from STAR]  STAR = A ;  Ranked Robin (RCV-RR) = A
```

- **STAR → A** ([`dark_horse_star`](cases/cases_pages/dark_horse_star.md)) — D can never rise, because no voter has any reason to give D a point.
- **Ranked Robin → A** — burying a rival *below* D doesn't help you win a single pairwise matchup, so the incentive to do it never exists; A beats everyone head-to-head.

That's Quinn's own prescription, satisfied: *"don't force people to dishonestly support D merely in order to oppose some other candidate."* A score ballot doesn't force it.

## Keep it fair

- **This is a Borda problem, not a "ranked ballot" problem** in general — [Ranked Robin](../../00_start_here/RCV_Ranked_Robin/README.md) uses the same ranked ballots and is immune, because it reads pairwise wins, not positional points. It's *positional point* methods (Borda and its kin) that are dark-horse-prone.
- **It's the mildest Moloch.** Dark Horse is "outstandingly evil but not particularly powerful" (Quinn): it needs a strictly-ranked point method almost nobody proposes for public office, and iterated "social glue" tends to hold honesty in place. The reason to name it is *mechanism design* — pick a method that doesn't create the trap at all.
- **STAR isn't strategy-proof** in general ([Gibbard](../../00_start_here/topics/gibbard_satterthwaite_theorem.md) forbids that) — see its own [chicken/Burr seam](../chicken_dilemma/) and [honest limits](../../00_start_here/STAR_Voting/properties_and_limits/STAR_honest_limits.md). The claim here is narrow and true: STAR has **no Dark Horse**.

## Reproduce it

```
# STAR / Ranked Robin side (LH engine):
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/dark_horse_borda/cases/dark_horse_star.yaml

# Borda side (pref_voting — the LH engine doesn't tabulate Borda):
uv run python -c "
from pref_voting.profiles import Profile
from pref_voting.scoring_methods import borda
n={'A':0,'B':1,'C':2,'D':3}
def P(r): return Profile([tuple(n[c] for c in o) for _,o in r], rcounts=[c for c,_ in r])
honest=[(34,'ABCD'),(33,'BACD'),(33,'CABD')]
strat =[(34,'ADBC'),(33,'BDAC'),(33,'CDAB')]
print('honest ->',[list(n)[w] for w in borda(P(honest))])
print('strategic ->',[list(n)[w] for w in borda(P(strat))])"
```

*Source of the framing: Jameson Quinn, "The Six Voting Molochs" (advocacy-adjacent — Quinn favors Approval/3-2-1, not STAR specifically, which makes the "STAR has no Dark Horse" point an outside verdict rather than our own cheerleading). The Borda math is standard and reproduced here with `pref_voting`.*
