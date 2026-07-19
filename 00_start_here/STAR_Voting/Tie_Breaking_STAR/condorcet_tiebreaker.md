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

## Why it looks like Ranked Robin — because mechanically it *is* one

If this ladder feels like it belongs to a different method, that instinct is correct. "Most head-to-head matchups won, break ties by margin" **is** the [Ranked Robin](../../RCV_Ranked_Robin/README.md) (Copeland) algorithm. Equal Vote's Condorcet Tiebreaker is Ranked Robin's own logic **borrowed to settle a STAR tie** — a miniature round-robin run *only among the tied candidates*, and *only* when STAR's normal rounds (score, then head-to-head) finish exactly even.

Keep the two roles distinct:

- **STAR the method** is unchanged — voters score 0–5, the top two by score meet in an automatic runoff. This protocol never touches a decided election.
- **The Condorcet Tiebreaker** is a *tie-break* deployed inside STAR (per Equal Vote's own doc, for both scoring-round and runoff ties). It happens to run RR-style pairwise arithmetic because that is a natural, matrix-based way to rank candidates STAR's own rungs couldn't separate.

So Ranked Robin is where this arithmetic *lives as a whole method*; here the same arithmetic is a *subroutine* that only fires on an exact STAR tie. (Ranked Robin's own tie-break story — Copeland ties broken by margin, and where LH and BetterVoting diverge — is [rr_tiebreak_lh_vs_bv.md](../../RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md).)

## It is a *tiebreaker*, not Condorcet compliance

This is the one thing to keep straight, because the name invites the opposite conclusion. Adding this protocol does **not** make STAR [Condorcet-compliant](../properties_and_limits/STAR_honest_limits.md):

- It only fires on an **actual tie**. Almost every election is decided long before any tiebreaker runs.
- It reads the matrix **among the tied candidates** — a Condorcet winner who never reached the runoff (was a close third on score) is **already gone** and cannot be rescued by it.
- So STAR-with-the-Condorcet-Tiebreaker still fails the Condorcet criterion in exactly the cases STAR always did. The [cycle-spoiler case (BV2212)](../../../01_STAR/iia_cycle_spoiler/bv2212_g3f7r2_cycle_spoiler.md) shows a Condorcet *cycle* driving a STAR result with **no tie at all** — the Condorcet Tiebreaker never even runs there. *Condorcet in the tiebreaker ≠ Condorcet in the outcome.*

---

## Worked example 1 — the ladder doing real work

Nine voters, three candidates, real score ballots — the LH engine confirms every number below:

```
Count × Rosa,Sam,Tess
    4 ×    5,  3,   1
    3 ×    1,  5,   3
    2 ×    3,  1,   5
```

Their head-to-head (preference) matrix is a **cycle** — each beats one and loses to one, so there is no Condorcet winner *among them*:

```
               |   * Rosa   |  * Sam    |    Tess   |
      * Rosa > |    ---     |6 - 0 - 3  |4 - 0 - 5  |
       * Sam > | 3 - 0 - 6  |   ---     |7 - 0 - 2  |
        Tess > | 5 - 0 - 4  |2 - 0 - 7  |   ---     |
  No Condorcet winner (majority cycle: Rosa > Sam > Tess > Rosa)
```

Now suppose these three are **tied** and a tiebreaker must choose among them. Walk the Condorcet Tiebreaker on this real matrix:

- **Step 1 — Matches won:** Rosa 1 (beat Sam), Sam 1 (beat Tess), Tess 1 (beat Rosa). A three-way cycle ties this rung. *Continue.*
- **Step 2 — Total preference votes:** Rosa 6 + 4 = **10**, Sam 3 + 7 = **10**, Tess 2 + 5 = **7**. Tess (7) is eliminated; Rosa and Sam tie at 10. *Continue between Rosa and Sam.*
- **Step 3 — Win margin:** Rosa's winning margin is **+3** (6–3 over Sam); Sam's is **+5** (7–2 over Tess). Sam's is larger → **Sam wins the tiebreak.** *Decided — random is never reached.*

Here is the payoff, and it is the whole reason this is a **third** protocol: on the *same nine ballots*, **LH's ladder would break the identical three-way tie differently.** After matches-won ties on the cycle, LH consults **five-star counts** — Rosa has four 5s, Sam three, Tess two — so LH's rung 2 picks **Rosa**, while the Condorcet Tiebreaker's rung 2/3 (preference votes, then margin) picks **Sam**. Same tie, same ballots, two protocols, two winners. Steps 1–3 are not decoration: a genuine cycle sinks past "matches won," and the deeper rungs still name a deterministic — and *distinct* — winner. (Aside: the full STAR count here also elects Rosa, by a different route — Rosa and Sam tie the scoring round at 29 each, both advance, and Rosa takes the runoff 6–3.)

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
