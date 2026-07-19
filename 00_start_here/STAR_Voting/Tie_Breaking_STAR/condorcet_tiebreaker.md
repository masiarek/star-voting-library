# Equal Vote's optional *Condorcet Tiebreaker*

**One line:** Equal Vote publishes **two** hand-count tiebreaker protocols for STAR — the recommended **5-Star Tiebreaker** and an optional **Condorcet Tiebreaker**. The Condorcet one walks a Copeland-style ladder — **matches won → total preference votes → win margin → random** — and it is a *tiebreaker*, **not** a claim that STAR elects the Condorcet winner.

> Source: **[starvoting.org/condorcet_tiebreaker](https://www.starvoting.org/condorcet_tiebreaker)** (Equal Vote Coalition — advocacy-adjacent, but a factual protocol doc). This page documents and works it; the [full ladder](tie_breaking.md) is the LH engine's chain, and [BetterVoting's automated protocol](https://docs.bettervoting.com/help/ties.html) is a third.

→ Level **301**. Builds on [STAR Tie-Breaking — The Full Chain](tie_breaking.md) and the **Head-to-head / pairwise** glossary entry.

---

## What it is (and when it applies)

It is an **optional** protocol for **hand counts**, offered as an alternative to Equal Vote's default 5-Star Tiebreaker. Like every tiebreaker, it runs **only when a round comes out exactly tied** — resolve any simple ties first. When you host online (BetterVoting or another Equal Vote–approved tool), ties are broken for you automatically and you never touch this by hand.

It reads the election's **preference (head-to-head) matrix** and applies four steps **in order**, stopping at the first that separates the tied candidates:

1. **Matches won** — favor the candidate who wins the most head-to-head matchups (this is the **[Copeland](../../RCV_Ranked_Robin/README.md)** score, and it is the "Condorcet" in the name: a candidate who beats every other *tied* candidate head-to-head wins here immediately).
2. **Total preference votes** — still tied? favor the candidate preferred by more voters *summed across all* their head-to-head matchups.
3. **Win margin** — still tied? favor the candidate with the largest margin (preferring votes minus opposing votes).
4. **Random** — a coin toss / draw is the floor, exactly as the other protocols bottom out at a random shuffle or a pre-drawn lot.

---

## It is a *tiebreaker*, not Condorcet compliance

This is the one thing to keep straight, because the name invites the opposite conclusion. Adding this protocol does **not** make STAR [Condorcet-compliant](../properties_and_limits/STAR_honest_limits.md):

- It only fires on an **actual tie**. Almost every election is decided long before any tiebreaker runs.
- It reads the matrix **among the tied candidates** — a Condorcet winner who never reached the runoff (was a close third on score) is **already gone** and cannot be rescued by it.
- So STAR-with-the-Condorcet-Tiebreaker still fails the Condorcet criterion in exactly the cases STAR always did. The [cycle-spoiler case (BV2212)](../../../01_STAR/iia_cycle_spoiler/bv2212_g3f7r2_cycle_spoiler.md) shows a Condorcet *cycle* driving a STAR result with **no tie at all** — the Condorcet Tiebreaker never even runs there. *Condorcet in the tiebreaker ≠ Condorcet in the outcome.*

---

## Worked example 1 — the ladder doing real work

Suppose three candidates tie (say, for the final finalist slot), and their head-to-head matchups form a **cycle** — each beats one and loses to one, so nobody is a Condorcet winner *among the tied set*:

| Head-to-head | Preferred | Opposed | Margin |
|---|---:|---:|---:|
| **Rosa** ▸ Sam | 15 | 12 | **+3** |
| **Sam** ▸ Tess | 16 | 11 | **+5** |
| **Tess** ▸ Rosa | 14 | 13 | **+1** |

Walk the ladder:

- **Step 1 — Matches won:** Rosa 1, Sam 1, Tess 1. A three-way cycle ties this rung. *Continue.*
- **Step 2 — Total preference votes:** Rosa 15 + 13 = **28**, Sam 12 + 16 = **28**, Tess 11 + 14 = **25**. Tess (25) is eliminated; Rosa and Sam tie at 28. *Continue between Rosa and Sam.*
- **Step 3 — Win margin:** Rosa's winning margin is **+3** (over Sam); Sam's is **+5** (over Tess). Sam's is larger → **Sam wins the tiebreak.** *Decided — random is never reached.*

The point: steps 1–3 are not decoration — a genuine cycle sinks past "matches won," and the deeper rungs still produce a deterministic winner. Note also that **LH's ladder would ask a different question here.** After the pairwise/matches-won rung ties, the LH engine consults **five-star counts**, not preference-votes-then-margin. Because rung 2 measures a different thing, the two protocols *can* name different winners on the same tied ballots — which is why this is a genuinely **third** protocol, not a restatement of the LH chain.

---

## Worked example 2 — even this reaches the floor

No deterministic protocol can break a **perfectly symmetric** tie, and the Condorcet Tiebreaker is no exception. Take the repo's real three-way scoring tie, [Flat scores 05 (BV555, `xmyf7k`)](../../../01_STAR/Flat_scores_ties/Flat_scores_ties_05_scoring_tie_3way_xmyf7k.md) — two identical ballots, `A=B=C=5, D=E=4`:

```
Scoring Round
   A -- 10 -- Tied for first place
   B -- 10 -- Tied for first place
   C -- 10 -- Tied for first place
 There's a three-way tie for first.

Scoring Round: First tiebreaker (head-to-head)
   A -- 0 · B -- 0 · C -- 0 · Equal Support -- 2      # every voter is indifferent among A, B, C
Scoring Round: Second tiebreaker (five-star)
   A -- 2 · B -- 2 · C -- 2                            # still tied
→ LH: resolved by LOT order → A, B advance (A wins)
```

Every voter scored A, B and C **equally**, so in every matchup among them the tally is 0–0. Run the Condorcet Tiebreaker on that matrix: **matches won** 0/0/0, **preference votes** 0/0/0, **win margin** 0/0/0 — all three deterministic rungs tie, and it drops to **step 4, random**. The three protocols therefore agree on the *verdict that the ballots cannot decide this*: LH uses its pre-published **lot** (→ A), BetterVoting uses a **random shuffle** (that run → C), and Equal Vote's Condorcet Tiebreaker would draw at random too. When voters are perfectly indifferent, there is simply nothing for any rung to weigh.

---

## Three protocols, side by side

| | Rung 1 | Rung 2 | Rung 3 | Floor |
|---|---|---|---|---|
| **LH engine** ([the chain](tie_breaking.md)) | pairwise / score | five-star | — | pre-published **lot** (deterministic) |
| **BetterVoting** ([protocol](https://docs.bettervoting.com/help/ties.html)) | pairwise (2-way only) / score | five-star | — | **random** shuffle |
| **Equal Vote Condorcet Tiebreaker** ([protocol](https://www.starvoting.org/condorcet_tiebreaker)) | matches won | total preference votes | win margin | **random** |

They agree on almost every real election (ties are rare, and most ties are broken at rung 1). They can diverge only on a genuinely tied race — and, as example 1 shows, the differing rung 2/3 means the *same* tied ballots can yield different winners. So a case that **turns on the terminal tiebreak** is protocol-specific: state which one you are using. See [LH vs BetterVoting — where the two STAR ladders differ](tie_breaking.md#lh-vs-bettervoting-where-the-two-star-ladders-differ) for the LH/BV half of this, and its Ranked Robin analog [rr_tiebreak_lh_vs_bv.md](../../RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md).

---

## See also

- **[starvoting.org/condorcet_tiebreaker](https://www.starvoting.org/condorcet_tiebreaker)** — the source protocol (Equal Vote).
- [STAR Tie-Breaking — The Full Chain](tie_breaking.md) — the LH engine's ladder, rung by rung.
- [STAR — Honest Limits §1](../properties_and_limits/STAR_honest_limits.md) — why STAR is not Condorcet-compliant, tiebreaker or no.
- [The cycle-spoiler case (BV2212)](../../../01_STAR/iia_cycle_spoiler/bv2212_g3f7r2_cycle_spoiler.md) — a Condorcet cycle driving a STAR result with no tie at all.
