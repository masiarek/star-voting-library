# The Chicken (Burr) Dilemma — when allies must play chicken, and STAR ends the standoff

*A strategic seam of **Approval** (and pure Score): two similar candidates who must cooperate to beat a third can end up in a **game of chicken** — approve both ally and you risk a tie; bullet-vote your favorite and you might win, or, if both sides defect, hand victory to the candidate the majority opposes. Named the **Burr dilemma** after the 1800 Jefferson–Burr tie. **STAR turns the slippery slope into a non-slippery one** — the runoff lets you support both allies honestly without ever needing to bullet.*

→ Part of the strategic-pathology set: [The strategic pathologies — five Molochs, and where STAR stands](../../00_start_here/topics/strategic_pathologies.md). Framing from Jameson Quinn. Related: [Approval voting](../../00_start_here/Approval_Voting/approval_voting.md) · [strategic voting](../../00_start_here/topics/strategic_voting.md) · [STAR's honest limits](../../00_start_here/STAR_Voting/properties_and_limits/STAR_honest_limits.md).

---

## The scenario

Two similar candidates, **A** and **B**, must team up to beat **C**, whom the majority opposes:

| Voters | Utilities | Preference |
|---|---|---|
| 35 | A 9, B 8, C 0 | A > B > C |
| 25 | A 8, B 9, C 0 | B > A > C |
| 40 | C 9 | C |

A 60-voter majority prefers *either* ally to C. The question is whether they can coordinate.

## Under Approval → a 60–60 tie, and a slippery slope ([`chicken_approval`](cases/cases_pages/chicken_approval.md))

Honestly, the 60 A/B voters approve **both** allies (both are well above the midpoint); the 40 C voters approve C:

```
A -- 60   (tie)
B -- 60   (tie)
C -- 40
```

C is safely beaten — but A and B are in an **exact tie**, decided by nothing but the coin-flip of a tie-break (as Jefferson and Burr were in 1800). So each side is tempted to **bullet-vote** — approve *only* its favorite — to win outright:

- If 1 A-voter bullets → A wins. Then 2 B-voters bullet → B wins. Then 2 more A-voters defect… a **slippery slope**.
- If both sides defect far enough (over ~20 each), the A/B vote collapses and **C — the majority-opposed candidate — slips through.**

That's the chicken dilemma: cooperation is fragile, defection is tempting, and mutual defection elects the worst outcome. (Like Dark Horse, it's a coordination trap — but here the two equilibria are "A cooperates, B defects" or vice versa, each of which *feels* unfair.)

## Under STAR → A wins, honestly, no chicken ([`chicken_star`](cases/cases_pages/chicken_star.md))

Scored honestly on 0–5, the A/B voters give **both** allies high marks — because under STAR the **runoff**, not the raw sum, decides between them:

```
Scoring Round
   A -- 275 -- First place
   B -- 265 -- Second place
   C -- 200            ← the majority-opposed candidate is beaten
Automatic Runoff
   A -- 35   vs   B -- 25     → A wins (the honest pairwise winner)

[Divergence from STAR]  STAR = A ;  Ranked Robin (RCV-RR) = A
```

No bullet-voting incentive: giving your ally a 4 instead of a 0 **cannot** cost your favorite the win — if A and B are the two finalists, the runoff picks the one *you* prefer, and if C sneaks into the runoff instead, your honest 4 for your ally is exactly what beats C. So both sides safely score both allies high, C loses, and the honest pairwise winner A prevails. **The slope is gone.**

## Why STAR converts slippery → non-slippery

This is the same fix as Quinn's **3-2-1 voting**: a final head-to-head step means a small number of defectors can't start an avalanche. In this scenario a *determined* bloc of 21+ B-voters could still rate A a 0 to try to force B through — STAR is **not** strategy-proof ([Gibbard](../../00_start_here/topics/gibbard_satterthwaite_theorem.md) forbids that) — but:

- **it takes a large, coordinated, risky defection**, not a one-voter nudge that snowballs; and
- **the risk is real**: over-bulleting your ally down to 0 can put *C* in the runoff against your favorite and cost you the election.

So STAR keeps the chicken dilemma's *non-slippery* form (which Quinn argues "isn't really Moloch at all") while shedding the slippery Approval version. Honest cooperation is a stable, safe default.

Game-theoretically, chicken/snowdrift has **two strong equilibria** (A concedes, or B concedes) — and coordination games like this only stay cooperative when defection is *punished*. STAR builds the punishment in: over-bulleting your ally toward 0 risks putting the majority-opposed C in the runoff against your favorite, so the method itself penalizes the defection that would unravel cooperation. No outside enforcement or "social glue" required.

## Keep it fair

- **This is a genuine Approval/Score seam** — the honest concession the [scorecard](../../00_start_here/topics/strategic_pathologies.md) makes for the score family. Approval's simplicity has a cost: with only a yes/no cut, allies can't say "I back you, but my favorite more" without risking a tie.
- **STAR mitigates but does not abolish it.** The claim is "non-slippery, honesty-stable," not "immune." Naming that limit is the point.
- **IRV abolishes the chicken dilemma outright** — but only by creating a [center squeeze](../center_squeeze/) instead (a defector in the chicken dilemma looks exactly like a fringe first-choice under IRV). Quinn argues that trade is worse; the [monotonicity](../monotonicity/) and [favorite-betrayal](../favorite_betrayal_irv/) pages show why.

## Reproduce it

```
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/chicken_dilemma/cases/chicken_star.yaml
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/chicken_dilemma/cases/chicken_approval.yaml
```

*Source of the framing: Jameson Quinn, "The Six Voting Molochs" (advocacy-adjacent; Quinn's own fix is 3-2-1, of which STAR's runoff is a close cousin). The A/B tie is inherent to the scenario, so this case is LH-verified rather than frozen from a random BetterVoting tie-break.*
