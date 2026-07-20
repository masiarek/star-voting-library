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

A beats B (22–11), B beats C (23–10), C beats A (21–12) — a rock-paper-scissors cycle, so **no Condorcet winner**. Each of A, B, C also beats D, E, F, so all three tie at **4 wins**. Ranked Robin breaks the tie by total win margin — but **A and B tie there too** (+101 each), with C just behind (+95):

```
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  A          4–1–0         4    +101  B, D, E, F
    2  B          4–1–0         4    +101  C, D, E, F
    3  C          4–1–0         4     +95  A, D, E, F
```

So margin drops C, and the winner is a **coin flip between A and B** (resolved by lot). The A-faction has a 50% shot.

### After teaming — A runs clones and locks in the win

Now the A-faction fields two clones, A1 and A2, ranked together in A's old slot:

```
12:A1>A2>B>C>D>E>F
11:B>C>A1>A2>D>E>F
10:C>A1>A2>B>D>E>F
```

The extra body reshapes the margins. A1's margin jumps to **+134**, and by absorbing votes the A-team pushes **B out of the top tier** (B falls to 4 wins; A1 and C reach 5). A1 now beats C on margin outright — **no lot needed**:

```
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  A1         5–1–0         5    +134  B, A2, D, E, F
    2  C          5–1–0         5    +104  A1, A2, D, E, F
    3  B          4–2–0         4     +90  C, D, E, F
    4  A2         4–2–0         4     +68  B, D, E, F
```

By "sacrificing" A2 to crowd out B, the A-faction converted a 50/50 coin flip into a **guaranteed A1 win**. That is a clone-independence (teaming) failure: running clones changed the outcome in the cloning faction's favor.

## The catch: the failure depends on the tiebreak

Here is the part that matters for this repo. The teaming attack only works because Ranked Robin broke the tie by **margin**. Engines don't agree on that rung (see [rr_tiebreak_lh_vs_bv.md](rr_tiebreak_lh_vs_bv.md)):

| Engine | 2-way tie rung | After-teaming winner |
|--------|----------------|----------------------|
| **Equal Vote protocol / LH** | total **margin** | **A1** — teaming succeeds |
| **BetterVoting** `RankedRobin.ts` | **head-to-head** (else random) | **C** — teaming fails |

After teaming, A1 and C tie at 5 wins, but **C beats A1 head-to-head, 21–12**. An engine that breaks a 2-way tie by head-to-head (BetterVoting) therefore elects **C**, not A1 — the attack backfires. An engine that breaks it by margin (LH, and the Equal Vote Coalition's published protocol) elects **A1** — the attack works. So "Ranked Robin fails clone independence by teaming" is true **of the margin tiebreak**, not of every Ranked Robin implementation. BetterVoting's simpler head-to-head/random tiebreak happens to resist this particular teaming (and, on the pre-clone 3-way tie, just picks at random).

## Bottom line

Ranked Robin passes vote-splitting clone independence outright: **cloning a candidate can't make that candidate lose.** It can fail *teaming* only when there's no Condorcet winner and the winner turns on a margin tiebreak. It's a narrow, tiebreak-specific edge case — worth knowing, easy to overstate.

## In this repo

- LH-only case pair (deterministic teaming via margin): [`clone_teaming_01_pre`](../../05_Ranked_Robin/clone_independence/cases/clone_teaming_01_pre.yaml) → A (lot), [`clone_teaming_02_post`](../../05_Ranked_Robin/clone_independence/cases/clone_teaming_02_post.yaml) → A1 (margin).
- BetterVoting companions (the divergence, where teaming fails): [BV2142 — pre](../../05_Ranked_Robin/clone_independence/bv2142_4gfwdq_clone_cycle_pre.md) (BV random → C) and [BV2143 — teaming](../../05_Ranked_Robin/clone_independence/bv2143_9pr3wr_teaming_fails.md) (BV head-to-head → C, teaming fails). Confirmed live: BV `4gfwdq` / `9pr3wr`.
