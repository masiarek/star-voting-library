# Bloc STAR vs Proportional STAR — the same ballots, two councils

*Two voters. Three candidates. Two seats. One ballot design. Two different answers — and you can check the whole thing in your head.*

**Level: 101 · for voters**

Both methods here use the **identical 0–5 STAR ballot**. Nothing changes for the voter. What changes is the count, and this folder is the smallest possible demonstration of what that difference actually does.

→ the majoritarian method: [Bloc STAR](../../02_STAR_Bloc/README.md) · the proportional one: [STAR-PR](../../03_STAR_PR/README.md) · what "proportional" promises: [what proportional actually means](../../03_STAR_PR/01_Learn/what_proportional_means.md)

---

## The election

Two voters are filling two seats from three candidates.

| | Ana | Ben | Cleo |
|---|--:|--:|--:|
| **Voter 1** | 0 | 0 | 1 |
| **Voter 2** | 2 | 3 | 0 |
| **Total** | 2 | 3 | 1 |

Voter 1 is lukewarm about exactly one candidate, Cleo. Voter 2 prefers Ben, would accept Ana, and has no time for Cleo.

## Seat 1: both methods agree

Ben has the most points (3) and wins the first seat under either count. Nothing interesting has happened yet — which is the point. **The two methods only part company once somebody has already been elected.**

## Seat 2: this is where they split

**Bloc STAR** re-runs the same count on the remaining candidates, with **every ballot still at full weight**. Ana (2) beats Cleo (1), so Ana takes the second seat.

> **Bloc STAR elects: Ben and Ana.**

**Proportional STAR** asks a different question first: *who is already represented?* With two seats and two voters, one seat is worth one voter — the [Hare quota](../../03_STAR_PR/01_Learn/STAR_PR/README.md) here is exactly **1 ballot**. Ben was elected on Voter 2's support, so Voter 2 is now **represented** and their ballot is set aside. Only Voter 1 is left to decide seat 2, and Voter 1 wants Cleo.

> **Proportional STAR elects: Ben and Cleo.**

## What just happened

Voter 2 got **both** of their preferred candidates under Bloc STAR. Under Proportional STAR they got one, and Voter 1 — who got nothing at all under Bloc — got the other.

That is the entire difference between the two families, and it needs only two ballots to show:

- **Bloc STAR** asks *"who do the voters most want?"* — once per seat, with everyone voting every time. A cohesive majority can therefore take **every** seat. That is a feature when you want the body to speak with one voice, and a bug when you want it to represent everybody.
- **Proportional STAR** asks *"who is not yet represented?"* — so each seat is decided by the voters who have not yet won one.

Neither is cheating. They answer different questions, and choosing between them is a decision about what the body you are electing is *for*.

## How quickly can they diverge?

**Immediately.** Two ballots is the smallest election in which a two-seat race can be meaningfully counted at all, and it is already enough. This pair was found by exhaustively searching every tie-free profile of 3 candidates × 0–5 scores in ballot-count order, so no smaller example exists.

Worth being precise about *why* this one diverges, because there are two different reasons Bloc and PR can disagree and only one of them is about proportionality:

1. **The runoff** — Bloc STAR finishes each seat with an automatic runoff; Allocated Score elects the highest *scorer* outright. So they can differ even on **seat 1**, whenever a runoff reverses the score order. That is really a [STAR-vs-Score](../../01_STAR/01_Learn/the_count/STAR_Automatic_Runoff.md) difference wearing a multi-winner coat.
2. **The reweighting** — the one above. Seat 1 agrees; the methods part company only because one of them remembers who has already been served.

This example is deliberately the second kind.

## Run it yourself

Same ballots in both files; only `voting_method:` differs.

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/bloc_vs_pr/cases/min_bloc_c3_b2.yaml
```

| Case | Method | Elects | Files |
|---|---|---|---|
| Smallest divergence — majoritarian | `bloc` | **Ben, Ana** | [yaml](cases/min_bloc_c3_b2.yaml) |
| Smallest divergence — proportional | `allocated` | **Ben, Cleo** | [yaml](cases/min_pr_c3_b2.yaml) |

## Where to go next

- **The same lesson at human scale** — ten ballots, two seats, a 60% majority: [exercise 12 — bloc vs proportional](../../01_STAR/05_Practice/ex12_bloc_vs_proportional.md)
- **Why a majority can take everything** — [the majority sweep](../../02_STAR_Bloc/01_Learn/majority_sweep.md)
- **What proportionality does and does not promise** — [what "proportional" actually means](../../03_STAR_PR/01_Learn/what_proportional_means.md)
- **The other proportional methods** — Allocated Score is one of three the engine runs; [STAR-PR](../../03_STAR_PR/01_Learn/STAR_PR/README.md) has the comparison

*(Still to come in this folder: the same boundary drawn against RCV-IRV and Ranked Robin, and the cases where the **proportional** methods disagree with each other — Allocated Score vs Sequentially Spent Score vs Reweighted Range.)*
