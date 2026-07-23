# Ranked Robin vs. Consensus Choice — same method, different package

*Two organizations promote what is essentially the same Condorcet method under two friendly brand names. People often summarize this as "the difference is purely branding." That's **nearly** right, and the two places it's wrong are the two places worth understanding: **the cycle rule**, and **what else comes bundled with the method**.*

**Level: reference** (a 201/301 aid). The method itself: [Ranked Robin](ranked_robin.md). The wider terminology map: [the naming decoder](condorcet_naming_decoder.md).

## The short version

| | **Ranked Robin** | **Consensus Choice** |
|---|---|---|
| Promoted by | [Equal Vote Coalition](https://www.equal.vote/ranked_robin) | [Better Choices for Democracy](https://www.betterchoices.vote/consensus-choice) |
| Ballot | ranked; equal ranks allowed; ranking all is optional | ranked; ranking all is optional |
| Core count | every pair head-to-head; most wins (Copeland) | every pair head-to-head; most wins (Copeland) |
| **Cycle / tie rule** | **sum of win margins** | **"Most Wins, Smallest Loss"** |
| **Scope of the proposal** | **a tabulation method** | **a multi-step reform package** (open qualifying election → 4+ advance → Consensus Choice general) |
| Other names | Consensus Voting, RCV-RR, Copeland | — |

**Whenever a Condorcet winner exists, they elect the same person — always, identically.** They can only diverge in a cycle. So "same method" is a fair everyday summary and a wrong technical one, which is why the repo's house phrasing is *one method with several brands, not byte-identical algorithms*.

## Difference 1 — the cycle rule

This is the only place the *counts* can disagree.

- **Ranked Robin:** most head-to-head wins; ties broken by **sum of win margins** (total margin), then lot.
- **Consensus Choice:** *"Most Wins, Smallest Loss: The candidate with the most head-to-head wins is elected. If multiple candidates tie for most head-to-head wins, the one with the smallest head-to-head loss is elected."* — [Better Choices FAQ](https://www.betterchoices.vote/faqs)

"Smallest loss" is Minimax-flavored (judge by your **worst** defeat); "sum of margins" is a Borda-flavored aggregate (judge by your **whole record**). On the same cyclic ballots these can name different winners. Why anyone bothers inventing cycle rules at all: [cycle resolution](cycle_resolution.md).

> **A sourcing note.** Better Choices' main [Consensus Choice page](https://www.betterchoices.vote/consensus-choice) states **no cycle rule at all** — it describes only "the candidate who defeats every other candidate head-to-head." The Most-Wins-Smallest-Loss rule appears on their **FAQ** page. So "Consensus Choice doesn't say what happens in a cycle" is a claim you'll hear from people who read only the main page; it's outdated — cite the FAQ.

## Difference 2 — a method vs. a package (the one usually missed)

This is the larger difference, and it isn't about counting at all.

**Ranked Robin is a tabulation.** Equal Vote proposes it as a way to count a ranked ballot; whether it sits behind a primary is a separate question.

**Consensus Choice is sold as a multi-step reform.** Step 1 is *"an open qualifying election—without party restrictions—[that] determines at least four of the strongest candidates who advance to the general election."* Only step 2 onward is the pairwise count.

And here is the load-bearing gap: **neither the Consensus Choice page nor the FAQ specifies which voting method the qualifying election uses.** That matters enormously, because a Choose-One qualifying round reintroduces exactly the [vote-splitting](../../method_comparisons/split_voting/README.md) the reform exists to end — *before* the good method ever runs. A consensus candidate who would win the pairwise general can be split out of the top four and never reach it.

Two defensible positions on how much this matters, both held by serious people in the field:

- **It matters a lot.** If the primary doesn't eliminate vote-splitting, the general election's accuracy is capped by whatever the primary already distorted. Pair a top-4/5 open primary with a good method (STAR, Approval, Ranked Robin) or don't bother.
- **It matters little in practice.** With **four** candidates advancing, it's unlikely the consensus candidate fails to advance even under Plurality — four slots is a lot of slack. The sharper risk is *pre-primary* pressure on co-partisans to drop out, which a broad-support method (Approval) in the primary would blunt.

**We measured it** rather than leaving it as opinion — [`primary_method_simulation.py`](../../06_Other/simulations/primary_method_simulation.py), written up at [Qualifying-round simulation](../../06_Other/simulations/README.md#qualifying-round-primary-method-simulation). Field of 9 candidates, 501 voters, realistic spatial model, general = Ranked Robin:

| Qualifying method, **top 4 advance** | Consensus (Condorcet) winner dropped |
|---|:--:|
| **Plurality** | **17.3%** |
| Approval (≥4) | 0.4% |
| Score (STAR's scoring round) | 0.0% |
| Ranked Robin | 0.0% (by construction) |

Three things follow, and they matter for how to talk about this reform:

1. **Four slots is real slack — and not enough.** Plurality's drop rate falls from 45.5% at top-2 to 17.3% at top-4, so the optimistic view is directionally right. But a reform whose selling point is electing the consensus candidate would discard that candidate in **about one election in six**, in its own first round, before the pairwise count ever runs.
2. **The fix is nearly free.** Approval in the qualifying round cuts 17.3% → 0.4% — roughly 40×, for a ballot no harder to explain or administer. There is no accuracy argument for Choose-One in the primary and a large one against it.
3. **The method matters more than the number of slots.** Top-4 → top-5 under Plurality buys 17.3% → 11.8%. Plurality → Approval at the *same* top-4 buys 17.3% → 0.4%.

There's also a structural reason this is the whole ballgame: with a **Condorcet general**, a consensus winner who *advances* always wins (they beat every survivor by definition). So the qualifying round is the **only** place accuracy can be lost — which is exactly why an unspecified primary method isn't a footnote. Caveats and the full sweep (factional and noise models, VSE, N=2–5) are in the writeup; sincere ballots only, and pre-primary candidate drop-outs are not modelled.

## The example everyone uses (verified)

The minimal abstract [center squeeze](../RCV_IRV/RCV_IRV_center_squeeze.md) — five ballots, three candidates. B is nobody's rallying point and everybody's acceptable second:

```
A>B>C
A>B>C
C>B>A
C>B>A
B>A>C
```

**Ranked Robin / Consensus Choice** — B beats A 3–2 and beats C 3–2, so B is the Condorcet winner and both methods elect B:

```
Round-Robin — every pair, head-to-head (For – Against):
   B  beats A   3 – 2
   A  beats C   3 – 2
   B  beats C   3 – 2

Win–loss record — Copeland score = wins + ½·ties:
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  B          2–0–0         2      +2  A, C
    2  A          1–1–0         1      +0  C
    3  C          0–2–0         0      -2  —

Winner — Ranked Robin (RCV-RR): B
   beats every opponent head-to-head — the Condorcet winner.
```

**RCV-IRV** eliminates B first — one first-choice ranking — and elects A:

```
ROUND 1
Candidate      Votes  Status
-----------  -------  --------
A                  2  Hopeful
C                  2  Hopeful
B                  1  Rejected

FINAL RESULT
A                  3  Elected
```

Note this example has **no cycle**, so it demonstrates the *shared* behavior of the Condorcet family against IRV — it cannot distinguish Ranked Robin from Consensus Choice. To tell those two apart you need a cyclic profile; that's what [cycle resolution](cycle_resolution.md) is for. A named, larger worked example: [the consensus center wins the round-robin](ranked_robin.md#a-worked-example-the-consensus-center-wins-the-round-robin).

## How to talk about it

- **"Same method" is fine in conversation.** Both are Condorcet; both elect the Condorcet winner; both avoid center squeeze. Don't derail a friendly discussion over the tiebreak.
- **"Purely branding" is the overstatement to avoid.** It's branding **plus** a different cycle rule **plus** a different proposal scope. In a technical room, that distinction is the whole conversation.
- **Ask about the primary.** When someone proposes Consensus Choice, the productive question isn't about the pairwise count — that part is solid. It's *"what method does the qualifying election use?"* That's where the reform's accuracy is actually at risk, and as of this writing the answer is publicly unspecified.
- **Fragmentation has been the real cost.** This branch of the movement has been siloed for years, with disagreement over wonky details acting as a barrier to Condorcet methods getting adopted at all. Convergence between the two camps is more valuable than winning the tiebreak argument.

## Cross-references

- [The naming decoder](condorcet_naming_decoder.md) — round-robin / Copeland / Condorcet / Ranked Robin / Consensus, and [the three senses of "consensus"](condorcet_naming_decoder.md#the-word-consensus-carries-three-different-jobs)
- [Ranked Robin](ranked_robin.md) — the method, with the sibling-branding note
- [Cycle resolution](cycle_resolution.md) — where the two tiebreaks actually differ
- [Ranked Robin's honest limits](RCV_RR_honest_limits.md) — what a ranked ballot can't see, for either brand
- [Center squeeze](../RCV_IRV/RCV_IRV_center_squeeze.md) — what both methods avoid and IRV doesn't

*Sources: [betterchoices.vote/consensus-choice](https://www.betterchoices.vote/consensus-choice) and [/faqs](https://www.betterchoices.vote/faqs) (advocacy — the source for their brand and rule, not a neutral referee); [equal.vote/ranked_robin](https://www.equal.vote/ranked_robin) (likewise, the other camp). Both retrieved 2026-07-23. Neutral ground for the family: [Wikipedia — Condorcet method](https://en.wikipedia.org/wiki/Condorcet_method).*
