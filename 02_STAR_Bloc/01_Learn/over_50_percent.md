# Over 50% — what a landslide actually buys

**One line:** a candidate can take **100% of the score and 100% of the runoff** and it still buys **exactly one seat** — Bloc STAR spends that majority electing them, then starts the next seat over on the same ballots, where a candidate two of the three voters scored **0** can win on 13% of the points with no majority anywhere in sight.

→ the count itself: [Bloc STAR](bloc_star.md) · the opposite configuration, where a majority *does* take everything: [the majority sweep](majority_sweep.md) · what a runoff percentage is a percentage *of*: [Runoff percentages — two denominators](../../01_STAR/01_Learn/the_count/runoff_percentages.md)

**Level: 201 · for voters**

---

## The ceiling case — over 50% of everything

Start where there is nothing to argue about. Three voters, three candidates; every ballot gives A five stars, one voter gives B a single point, nobody scores C at all ([full count →](../../01_STAR/02_Examples/cases/cases_pages/bv2263_xw23m9_over_50_percent.md) · [yaml](../../01_STAR/02_Examples/cases/bv2263_xw23m9_over_50_percent.yaml) · **[live on BetterVoting ↗](https://bettervoting.com/xw23m9/results)** — BV2263 `xw23m9`, where BV's tally agrees line for line):

<!-- report:bv2263_xw23m9_over_50_percent -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 3 ballots.
Count × A,B,C
    2 × 5,0,0
    1 × 5,1,0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 15 -- First place
   B             --  1 -- Second place
   C             --  0
 A and B advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 3 -- First place
   B             -- 0
   Equal Support -- 0
 A wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           A 3 (100%)  ·  B 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```
<!-- /report -->
A wins on every denominator a STAR result has:

| "Over 50%" of what? | A | how it's counted |
|---|:--:|---|
| the **maximum possible score** | 15 / 15 = **100%** | 3 ballots × 5 stars |
| the **ballots** in the runoff | 3 / 3 = **100%** | Equal Support left in the denominator |
| the **voters with a preference** | 3 / 3 = **100%** | Equal Support removed — the number that decides the race |

That is the whole reason this tiny election is worth keeping: it is the one case where those three numbers are the same, so it's the control you read every other result against. They come apart the moment a ballot rates the two finalists equally — see [two denominators](../../01_STAR/01_Learn/the_count/runoff_percentages.md).

**And note what did *not* happen: the count did not stop early.** A held every point on every ballot and was still put through the automatic runoff, because the scoring round only ever picks *finalists* — it never elects anyone. There is no "wins outright in round 1" shortcut in STAR, the way a majority of first choices ends an [RCV-IRV](../../06_Other/RCV_IRV/concepts/RCV-IRV-Hare.md) count in its first round. Two rounds, always. (Why the runoff is worth running even when it changes nothing: [the automatic runoff](../../01_STAR/01_Learn/the_count/STAR_Automatic_Runoff.md).)

## Now give the same electorate a second seat

[BV1815](../02_Examples/bv1815_bloc_3c2s_basic.md) is the multi-seat twin — three ballots again, A dominant again, but two seats to fill ([full count →](../02_Examples/cases/cases_pages/bv1815_bloc_3c2s_basic.md) · [yaml](../02_Examples/cases/bv1815_bloc_3c2s_basic.yaml)):

<!-- report:bv1815_bloc_3c2s_basic -->
```text
--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 3 ballots to fill 2 seats.
A,B,C
4,1,0
3,0,2
5,0,0

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 12 -- First place
   C             --  2 -- Second place
   B             --  1
 A and C advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 3 -- First place
   C             -- 0
   Equal Support -- 0
 A wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           A 3 (100%)  ·  C 0 (0%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   C             -- 2 -- First place
   B             -- 1 -- Second place
 C and B advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 1 -- Tied for first place
   C             -- 1 -- Tied for first place
   Equal Support -- 1
 There's a two-way tie for first.

[Bloc STAR: Round 2: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   C             -- 2 -- First place
   B             -- 1
 C wins.

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 A
 C
```
<!-- /report -->
Seat 1 is the ceiling case again in all but the last decimal: A holds **12 of 15** points (80% of the maximum), is the top-scored candidate on every ballot, and wins the runoff **3–0**. Seat 2 is a different election entirely — and this is what the same three denominators say about its winner:

| "Over 50%" of what? | C, at seat 2 | |
|---|:--:|---|
| the **maximum possible score** | 2 / 15 = **13%** | one voter scored C at all; the other two left C on 0 |
| the **ballots** in the runoff | 1 / 3 = **33%** | one prefers C, one prefers B, one rates them equally |
| the **voters with a preference** | 1 / 2 = **50%** | not *more* than half — a tie, not a majority |

**Nobody won that runoff.** STAR's runoff guarantees the winner is preferred to the other finalist by more voters — and when that guarantee can't be met, the seat falls to [the tie-break ladder](../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md), whose first rung is the score total: C's 2 beats B's 1. So the second seat on this board is held by a candidate a majority of the electorate gave zero points, seated by a rung rather than by a majority. Both engines agree on that — this is a real BetterVoting election ([results ↗](https://bettervoting.com/fk38pk/results), id `fk38pk`), and BV reports the same winners with `tieBreakType: "score"`.

It is also the clearest place to watch the denominators disagree in the wild. BetterVoting's results page paginates one card per seat, and on the seat-2 card all three runoff bars are labelled **33%** while the dashed *majority threshold* line is drawn at **1 vote** — level with the top of both candidate bars. On the seat-1 card, where nobody rated the finalists equally, the same line sits at 50% of the same axis and reads correctly. Both screenshots, side by side: [BV1815](../02_Examples/bv1815_bloc_3c2s_basic.md#view-1-bettervoting). The mismatch is [bettervoting#1471](https://github.com/Equal-Vote/bettervoting/issues/1471) and is presentation only — the count is right on both cards.

## Why the majority doesn't carry over

Bloc STAR fills seats by [running the whole count once per seat](bloc_star.md): elect, remove, re-run on the same unchanged ballots. **The removal step is where the landslide is spent.** A's twelve points and three head-to-head preferences elected A and then left the election with A; nothing about that first result is still on the table when seat 2 is counted. Round 2 is a fresh STAR election among whoever is left, and it is decided by the only thing the voters still disagree about.

Which is the honest version of the lesson: **these three voters were unanimous about a candidate, not about a slate.** Above A, their ballots have nothing in common — one prefers B, one prefers C, one rates both at zero. A group can be as cohesive as an electorate ever gets on the question "who should win?" and still be a three-way split on "who else?"

## This is not a bug, and it is not the sweep either

Two failure modes get confused here, and they are opposites:

- **[The majority sweep](majority_sweep.md)** — a cohesive majority that runs *several* candidates can take **every** seat, leaving a large minority with nothing. That is Bloc STAR's defining property and the reason to think hard before choosing it.
- **This page** — a majority that runs *one* candidate wins exactly that one seat, and hands the rest to whoever the leftovers favor. Same method, same majoritarian logic; the difference is entirely in how many candidates the majority put on the ballot.

Together they are one fact stated twice: Bloc STAR rewards **slate discipline** ([honest limits](bloc_honest_limits.md)). Winning big does not fill a board; running enough candidates does. If you want the second seat to reflect the second-largest group rather than the second-largest leftover, you want a proportional method — [STAR-PR](../../03_STAR_PR/01_Learn/) reweights the ballots that already won a seat so they count for less on the next one. That decision belongs before the ballots are printed: [Electing more than one, simply](../../07_Concepts/topics/electing_more_than_one.md).

## See also

- [Bloc STAR](bloc_star.md) — the elect–remove–re-run loop these two elections run
- [The majority sweep](majority_sweep.md) — the same majoritarian logic with a full slate behind it
- [The score leader can win no seat](score_leader_no_seat.md) — the third configuration: leading every scoring round and losing every runoff
- [Ties in Bloc STAR](bloc_tiebreaks.md) — the ladder that settled seat 2, and how a tie at one seat can change who wins a later one
- [Runoff percentages — two denominators](../../01_STAR/01_Learn/the_count/runoff_percentages.md) — the single-winner treatment of the table above
- [`GLOSSARY`](../../07_Concepts/GLOSSARY.md) — Equal Support, Bloc STAR, the tie-break ladder

# file: over_50_percent.md
