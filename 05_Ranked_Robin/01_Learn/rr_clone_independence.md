# Ranked Robin and clone independence — crowding, teaming, and a tiebreak that matters

*Clone independence asks: can adding a near-identical candidate (a "clone") change who wins in a way that helps whoever ran the clone? Ranked Robin is **mostly** cloneproof, but it has one narrow failure — and whether that failure even fires depends on **which tiebreak** an engine uses. This page works the electowiki example and shows the LH-vs-BetterVoting split.*

→ Method: [Ranked Robin](ranked_robin.md) · tiebreaks: [rr_tiebreak_lh_vs_bv.md](rr_tiebreak_lh_vs_bv.md) · cycles: [cycle_resolution.md](cycle_resolution.md) · limits: [RCV_RR_honest_limits.md](RCV_RR_honest_limits.md)

## Two kinds of clone attack

- **Crowding (vote-splitting):** run clones of a *rival* to split their support and knock them down. Ranked Robin **passes** here — because it counts head-to-head wins, not first-choices, cloning a candidate can never make that candidate lose. Running clones of your opponent doesn't split them apart the way it does under Choose-One or IRV.
- **Teaming:** run clones of *yourself* so that your bloc fields several bodies, hoping the method rewards the crowd. This is the one Ranked Robin can fail — and **only** in an election with **no Condorcet winner** (a top cycle). With a Condorcet winner there's no tie to exploit, so teaming has nothing to grab.

## The worked example (electowiki)

### Before cloning — a 3-way tie settled by a coin flip

33 voters, six candidates. A, B, C form a cycle; D, E, F trail.

```
12:A>B>C>D>E>F
11:B>C>A>D>E>F
10:C>A>B>D>E>F
```

A beats B (22–11), B beats C (23–10), C beats A (21–12) — a rock-paper-scissors cycle, so **no Condorcet winner**. Each of A, B, C also beats D, E, F, so all three tie at **4 wins**, and all three are *finalists*. Ranked Robin's [1st Degree tiebreaker](../03_Criteria/rr_tiebreaks/degrees_of_ties.md) compares their margins against each other only: A +2, B +2, C −4, so C is dropped and A and B are still level. Its 2nd Degree compares margins over the whole field — and **A and B tie there too** (+101 each, with C just behind at +95):

```
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  A          4–1–0         4    +101            +2  B, D, E, F
    2  B          4–1–0         4    +101            +2  C, D, E, F
    3  C          4–1–0         4     +95            -4  A, D, E, F
```

Both degrees are exhausted with two candidates still level, so the winner is a **coin flip between A and B** (resolved here by a published lot). The A-faction has a 50% shot.

### After teaming — A runs clones and locks in the win

Now the A-faction fields two clones, A1 and A2, ranked together in A's old slot:

```
12:A1>A2>B>C>D>E>F
11:B>C>A1>A2>D>E>F
10:C>A1>A2>B>D>E>F
```

The extra body reshapes the field. By absorbing votes the A-team pushes **B out of the top tier** (B falls to 4 wins; A1 and C reach 5), so the finalists are now A1 and C rather than A, B and C — and with only two finalists there is no lot to reach: the 1st Degree is decisive. It just does not decide the way the A-faction wanted. A1's margin over the whole field jumps to **+134** against C's +104, but that is the *2nd Degree*, and it is never asked:

```
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  C          5–1–0         5    +104            +9  A1, A2, D, E, F
    2  A1         5–1–0         5    +134            -9  A2, B, D, E, F
    3  A2         4–2–0         4     +68             —  B, D, E, F
    4  B          4–2–0         4     +90             —  C, D, E, F
```

**C beats A1 head-to-head, 21–12**, so the 1st Degree elects **C** and the attack backfires. Running the clones still changed the outcome — before cloning the count ends in a coin flip, after it a single candidate wins outright — so clone independence still fails here, by *crowding*: B was squeezed out of the finalist set by candidates who could not win. What fails with it is the claim that **teaming pays**. It pays only if the tie is settled on margins over the whole field, which is the 2nd Degree, and the 2nd Degree is out of reach while the 1st separates the finalists.

> **electowiki's own worked example gets this wrong**, and this page repeated it until 2026-08-19. The article's clone-independence section concludes that after cloning "A1 wins after the tiebreaker" — which its own 1st Degree rule does not support, on its own ballots. So did this repo's engine, for the same reason: it had no 1st Degree rung and went straight to total margin. The correction is written up in [degrees of ties](../03_Criteria/rr_tiebreaks/degrees_of_ties.md).

> **This is not our construction alone.** The same failure was raised on [electowiki's Ranked Robin talk page](https://electowiki.org/wiki/Talk:Ranked_Robin) in November 2021 by the contributor Kristomun, questioning the article's claim that clone failures have a limited range. Their version separates the two channels cleanly: **crowding** fails the *Copeland* component, while ordinary **teaming inside the Smith set** fails the *Borda* (margins) component. That distinction is exactly the one the degrees ladder encodes — crowding reshapes who the finalists are, and margins only get consulted once they cannot be separated by their own matches. Worth knowing that the wart was documented by the method's own community, not just by its critics.

## The catch: the attack depends on which rung you use

Here is the part that matters for this repo. Whether teaming *pays* turns entirely on which rung settles the two-way tie (see [rr_tiebreak_lh_vs_bv.md](rr_tiebreak_lh_vs_bv.md) and [degrees of ties](../03_Criteria/rr_tiebreaks/degrees_of_ties.md)):

| Rung used on the two finalists | After-teaming winner |
|--------|----------------------|
| **1st Degree** — margins over the other finalists, i.e. their head-to-head. The protocol's rule, BetterVoting's rule, and this engine's rule since 2026-08-19 | **C** — the attack backfires |
| **2nd Degree** — margins over the whole field. Correct only once the finalists are level against each other | **A1** — the attack pays |

After teaming, A1 and C tie at 5 wins, and **C beats A1 head-to-head, 21–12**. So "Ranked Robin fails clone independence by teaming" needs restating: what the clones reliably do is **change the outcome by crowding out B**, which is a clone failure whichever rung you use. What they do not do, under the method as published, is deliver the win to the faction that ran them.

## Bottom line

Ranked Robin passes vote-splitting clone independence outright: **cloning a candidate can't make that candidate lose.** It can fail *teaming* only when there's no Condorcet winner and the winner turns on a margin tiebreak. It's a narrow, tiebreak-specific edge case — worth knowing, easy to overstate.

## In this repo

- LH-only case pair: [`clone_teaming_01_pre`](../03_Criteria/clone_independence/cases/clone_teaming_01_pre.yaml) → A (both degrees exhausted, so lot), [`clone_teaming_02_post`](../03_Criteria/clone_independence/cases/clone_teaming_02_post.yaml) → C (1st Degree).
- BetterVoting companions: [BV2142 — pre](../03_Criteria/clone_independence/bv2142_4gfwdq_clone_cycle_pre.md) (BV has no degrees for a 3-way tie, so random → C) and [BV2143 — teaming](../03_Criteria/clone_independence/bv2143_9pr3wr_teaming_fails.md) (BV head-to-head → C). Confirmed live: BV `4gfwdq` / `9pr3wr`. Both engines now elect C after teaming; before 2026-08-19 this engine said A1.
