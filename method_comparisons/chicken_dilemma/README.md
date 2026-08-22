# The Chicken (Burr) Dilemma — when allies must play chicken, and STAR ends the standoff

*A strategic seam of **Approval** (and pure Score): two similar candidates who must cooperate to beat a third can end up in a **game of chicken** — approve both ally and you risk a tie; bullet-vote your favorite and you might win, or, if both sides defect, hand victory to the candidate the majority opposes. Named the **Burr dilemma** after the 1800 Jefferson–Burr tie. **STAR turns the slippery slope into a non-slippery one** — the runoff lets you support both allies honestly without ever needing to bullet.*

→ Part of the strategic-pathology set: [The strategic pathologies — five Molochs, and where STAR stands](../../07_Concepts/topics/strategic_pathologies.md). Framing from Jameson Quinn. Related: [Approval voting](../../04_Approval/01_Learn/approval_voting.md) · [strategic voting](../../07_Concepts/topics/strategic_voting.md) · [STAR's honest limits](../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md).

---

## The scenario

Two similar candidates, **A** and **B**, must team up to beat **C**, whom the majority opposes:

| Voters | Utilities | Preference |
|---|---|---|
| 35 | A 9, B 8, C 0 | A > B > C |
| 25 | A 8, B 9, C 0 | B > A > C |
| 40 | C 9 | C |

A 60-voter majority prefers *either* ally to C. The question is whether they can coordinate.

## When both sides defect → C wins on 40% ([`chicken_approval_both_defect`](cases/cases_pages/chicken_approval_both_defect.md))

The bottom of the slope, now run rather than described. The 35 A-first voters approve only A; the 25 B-first voters approve only B. Neither is lying about who they prefer — each is just withholding approval from an ally to win the intra-faction contest:

```
C -- 40  <- Elected
A -- 35
B -- 25
```

**Sixty voters preferred either ally to C, and C won.** Approval never forced that split; the faction's two halves each declined to support the other.

**Where the avalanche starts.** With `a` of the 35 A-first voters and `b` of the 25 B-first voters bullet-voting, A holds `60 − b` approvals and B holds `60 − a`. C takes the lead only once **both `a > 20` and `b > 20`** — so it is not one defector who does the damage, it is defection becoming general. That threshold is precisely what makes the Approval slope slippery, and precisely what STAR's runoff removes.

This is Approval's exact counterpart to [STAR's residual split](../split_voting/_main/_main_pages/05a_residual_split_bullet-voting.md), where a 60% side loses to a 40% opponent the same way. Both are **self-inflicted**: the ballot offered a remedy and the voters declined it — a real difference from Choose-One, where no remedy is on offer at all, but not immunity. Neither method should be sold as immune. → [vote splitting & the spoiler effect](../split_voting/README.md)

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

This is the same fix as Quinn's [**3-2-1 voting**](../../07_Concepts/topics/three_two_one_voting.md): a final head-to-head step means a small number of defectors can't start an avalanche. In this scenario a *determined* bloc of 21+ B-voters could still rate A a 0 to try to force B through — STAR is **not** strategy-proof ([Gibbard](../../07_Concepts/topics/gibbard_satterthwaite_theorem.md) forbids that) — but:

- **it takes a large, coordinated, risky defection**, not a one-voter nudge that snowballs; and
- **the risk is real**: over-bulleting your ally down to 0 can put *C* in the runoff against your favorite and cost you the election.

So STAR keeps the chicken dilemma's *non-slippery* form (which Quinn argues "isn't really Moloch at all") while shedding the slippery Approval version. Honest cooperation is a stable, safe default.

Game-theoretically, chicken/snowdrift has **two strong equilibria** (A concedes, or B concedes) — and coordination games like this only stay cooperative when defection is *punished*. STAR builds the punishment in: over-bulleting your ally toward 0 risks putting the majority-opposed C in the runoff against your favorite, so the method itself penalizes the defection that would unravel cooperation. No outside enforcement or "social glue" required.

## Keep it fair

- **This is a genuine Approval/Score seam** — the honest concession the [scorecard](../../07_Concepts/topics/strategic_pathologies.md) makes for the score family. Approval's simplicity has a cost: with only a yes/no cut, allies can't say "I back you, but my favorite more" without risking a tie.
- **STAR mitigates but does not abolish it.** The claim is "non-slippery, honesty-stable," not "immune." Naming that limit is the point.
- **IRV abolishes the chicken dilemma outright** — but only by creating a [center squeeze](../center_squeeze/README.md) instead (a defector in the chicken dilemma looks exactly like a fringe first-choice under IRV). Quinn argues that trade is worse; the [monotonicity](../monotonicity/README.md) and [favorite-betrayal](../favorite_betrayal_irv/README.md) pages show why.

## Reproduce it

```
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/chicken_dilemma/cases/chicken_star.yaml
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/chicken_dilemma/cases/chicken_approval.yaml
```

*Source of the framing: Jameson Quinn, "The Six Voting Molochs" (advocacy-adjacent; Quinn's own fix is 3-2-1, of which STAR's runoff is a close cousin). The A/B tie is inherent to the scenario, so this case is LH-verified rather than frozen from a random BetterVoting tie-break.*
