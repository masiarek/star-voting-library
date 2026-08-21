# Why Build "Silly" Tie Elections? — and a Map of Every Tie Case

*In praise of the contrived example. The tiny, symmetric elections in this repo — `5,5,5 / 4,4,4`, or `4,0,0 / 0,4,0 / 0,0,4` — will never show up at a polling place. That's the point: they're **probes**, built on purpose to drive a tabulation algorithm into its corners so we can see exactly what it does there.*

Part of the [Ties & Tie-Breaking](README.md) hub · companion to [STAR Tie-Breaking — The Full Chain](../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md).

---

## The apologia (why a "silly" case earns its keep)

A deliberately-degenerate election isn't pedantry — it's the same move as a unit test that feeds a function `0`, `-1`, and `MAX_INT`. Five concrete payoffs:

1. **It isolates one behavior.** A real election changes a dozen things at once. A two-ballot tie changes *nothing but the tie*, so whatever the engine does next is unambiguously the tie-break — nothing else can be causing it.
2. **It makes a real bug reproducible.** The contrived [`jfk7pd`](https://bettervoting.com/jfk7pd/results) ballots — two of them, still live on BetterVoting — are what turned "STAR sometimes shows something weird on ties" into a one-click repro that surfaced actual defects: the `NaN` display, the "no ballots have been cast" message, the silent random tie-break. The ballots are fake; the bugs they flushed out are real.
3. **It pins down the spec.** "What *should* happen when every rung ties?" is a real design question. A minimal case forces a definite, documented answer (here: the pre-published lot decides) instead of leaving it to whatever the code happens to do.
4. **It teaches the concept.** The clearest way to explain the "dead rung," or why each round breaks its tie with the *other* round's yardstick, is the smallest election that shows it. Big elections bury the lesson in noise.
5. **It becomes a regression test.** Once captured with an expected winner, the case guards the engine forever: if someone later reorders the tie-break cascade, these tiny files fail immediately.

**What each of the two examples above isolates:**

- **`5,5,5` then `4,4,4`** — every voter rates *all* candidates equally, so no ballot expresses any preference at all. Totals tie, every pairwise is "Equal Support," five-star ties: a **fully flat** dead heat. It probes *"what happens when the ballots say literally nothing to separate anyone?"* (See [Flat scores, ties & tie-breaking](../../../01_STAR/09_Parked/Flat_scores_ties/README.md).)
- **`4,0,0 / 0,4,0 / 0,0,4`** — a perfect rotation: three equal, mutually symmetric camps, and (capped at 4) **no 5s**, so the five-star rung is a *dead rung*. It probes *"a genuine k-way symmetric tie with no cardinal signal to break it"* — the 3-candidate analog of `jfk7pd`. (See [the three-way dead-rung tie](../../../01_STAR/03_Criteria/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_tie.md).)

**A sixth payoff, which outranks the other five: they aren't actually contrived.** The rotation above is the exact profile the standard impossibility proof constructs. Moulin (1983) shows that anonymity + neutrality + Pareto are incompatible with always naming one winner whenever the voter count `n` has a divisor `r` with `1 < r ≤ m` candidates — and the witness he builds is `k` voters per rotation of the top three, which at `k = 1` is `4,0,0 / 0,4,0 / 0,0,4` and at `k = 2` is [the symmetric six-voter cycle](../../../method_comparisons/reinforcement_paradox/README.md) this repo also runs. So these files weren't a hunt for a pathological corner; they were a reconstruction of the textbook example, arrived at independently. That also converts the arithmetic into a **search rule** for building more: want a forced tie at `m` candidates? Pick `n` with a prime factor `≤ m`. See [Ties Are Forced](ties_are_forced.md).

**And the honest caveat, so it stays balanced:** these exact symmetries are astronomically rare in a public election, and the tabulation is *correct* the whole way down — the interesting question is only *who wins a genuine tie*. But "rare" isn't "never": small electorates — clubs, boards, committees, local primaries, which are much of BetterVoting's actual use — tie far more often than statewide races do. The probe is how you make sure the rare case is handled *before* it decides a real seat.

---

## A map of every tie case (single-winner STAR)

Where a STAR result can land, from a clean win down to the lot. Each round has its own ladder; the lot is the floor of both.

```mermaid
flowchart TD
    A["Ballots (each candidate scored 0–5)"] --> B["Scoring Round: sum every candidate's scores"]
    B --> C{"Clear top two?"}
    C -->|yes| E["Two finalists advance"]
    C -->|"tie for a finalist slot"| D1{"Matchups won separates?<br/>(losers of the most are eliminated,<br/>repeat with the survivors)"}
    D1 -->|yes| E
    D1 -->|no| D2{"Five-star (most 5s) separates?"}
    D2 -->|yes| E
    D2 -->|"no — dead rung / tied"| D3["LOT decides the finalist"]
    D3 --> E
    E --> F["Automatic Runoff: which finalist do more voters prefer?"]
    F --> G{"One finalist preferred?"}
    G -->|yes| W(["Winner — decided by the ballots"])
    G -->|"tie (equal preference)"| H1{"Higher total score separates?"}
    H1 -->|yes| W
    H1 -->|no| H2{"Five-star (most 5s) separates?"}
    H2 -->|yes| W
    H2 -->|"no — dead rung / tied"| H3["LOT decides the winner"]
    H3 --> WL(["Winner — decided by lot (rare, audit-worthy)"])
```

The left spine (all "yes") is the ordinary election: a clean top two and a decisive runoff, no tiebreak ever consulted. Every rightward branch is a tie rung — and each one has a probe.

## Every branch has a test

| Branch reached | What it isolates | Probe |
|----------------|------------------|-------|
| Clean top two + decisive runoff | the baseline (no tiebreak) | [`Flat_scores_ties_01`](../../../01_STAR/09_Parked/Flat_scores_ties/README.md#case-01) |
| Scoring tie → **pairwise** breaks it | a finalist chosen by head-to-head | [dead-rung case 01](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md) |
| Scoring tie → **five-star** breaks it | a finalist chosen by most 5s | [dead-rung case 05](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md) |
| Scoring tie → **dead rung → lot** | no 5s; the lot picks the finalist | [dead-rung cap ladder](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md) |
| Runoff tie → **score** breaks it | winner by higher total score | [dead-rung case 04](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md) |
| Runoff tie → **five-star** breaks it | winner by most 5s | [dead-rung case 04/07](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md) |
| Runoff tie → **dead rung → lot** | no 5s; the lot picks the winner | [BV `jfk7pd`](../../../01_STAR/03_Criteria/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md) |
| Runoff tie → five-star **tied non-zero → lot** | rung runs, decides nothing | [dead-rung case 09](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md) |
| **Fully flat** (no preference anywhere) | ties at both loci at once | [`Flat_scores_ties_07`](../../../01_STAR/09_Parked/Flat_scores_ties/README.md#case-07) |
| **k-way symmetric** (rotation) | any of k wins by lot; divergence (k−1)/k | [three-way dead-rung](../../../01_STAR/03_Criteria/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_tie.md) |
| Scoring tie → **rung 1 eliminates**, survivors go on | 3+ tied, partial separation — the branch symmetry cannot test | [matchups-won probe](../../../01_STAR/03_Criteria/tie_break_ladder/cases/cases_pages/tie_break_ladder_matchups_eliminate_loser.md) |

Generate your own along any branch with [`generate_dead_rung_scenarios.py`](../../../STARVote_LH_tabulation_engine/tools_adam/generate_dead_rung_scenarios.md).

> **This map is v1 — single-winner STAR only.** Natural extensions later: abstentions / quorum interactions, multi-winner (Bloc / proportional) tie handling, and the RCV-IRV elimination-tie branch (see [Tie-Breaking: STAR vs. RCV-IRV](tiebreaking_star_vs_irv.md)).
>
> **Two of those are now done, by machine.** [Coarse ballots and the tie ladder](coarse_ballots_and_the_tie_ladder.md) sweeps 445,154 small elections across Bloc STAR, the proportional STAR family, Ranked Robin and Approval as well as single-winner STAR, classifying every tie against this map. Nothing it found needed a new branch — including the **partial-separation** case this table calls *"the branch symmetry cannot test"*, which turns out to be a shape rather than a rung and to recur under every method. It also reaches the abstention corner from below: the all-zeros election, where nobody scores anybody. RCV-IRV is still out; that branch has [its own pages](parallel_universe_tiebreaking.md).

## See also

- [STAR Tie-Breaking — The Full Chain](../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md) — the ladders in words.
- [The "dead rung" case set](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md) and [Flat scores, ties & tie-breaking](../../../01_STAR/09_Parked/Flat_scores_ties/README.md) — the probes themselves.
- [Tie-Breaking: STAR vs. RCV-IRV](tiebreaking_star_vs_irv.md) — why strict ranks make ties harder, not easier.
