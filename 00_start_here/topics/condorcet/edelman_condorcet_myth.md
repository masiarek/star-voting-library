# The strongest case against the Condorcet winner — Edelman's "Myth of the Condorcet Winner," tabulated

*Paul H. Edelman — Professor of Mathematics **and** Law at Vanderbilt — published ["The Myth of the Condorcet Winner"](https://scholarship.law.vanderbilt.edu/faculty-publications/595/) (22 Supreme Court Economic Review 207, 2015; [journal page](https://www.journals.uchicago.edu/doi/full/10.1086/682019)) to refute "the consensus among legal scholars that, when choosing among multiple alternatives, the Condorcet winner, should it exist, is the preferred option." Where the [FairVote article we claim-checked](fairvote_condorcet_claim_check.md) fails on contact with a countable election, this paper is the **serious version of the anti-Condorcet argument** — the math is right, the theorems are real, and engaging it honestly makes the whole debate sharper. So we tabulated it, live.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/gmfv4c) · **[results ↗](https://bettervoting.com/gmfv4c/results)** (election `gmfv4c`, BV2173) — Edelman's 81-voter profile, four races on the same voters: STAR, Ranked Robin, RCV-IRV, Choose-One.

## The cancellation argument

Edelman's centerpiece (his Section III) is this 81-voter profile — which, per his own footnote, was invented by **Condorcet himself as an attack on Borda**, and was later turned *against* the Condorcet criterion by Saari and by Balinski & Laraki:

| Voters | Preference |
|---:|---|
| 30 | Ada > Ben > Cara |
| 1 | Ada > Cara > Ben |
| 29 | Ben > Ada > Cara |
| 10 | Ben > Cara > Ada |
| 10 | Cara > Ada > Ben |
| 1 | Cara > Ben > Ada |

**Ada is the Condorcet winner**: 41–40 over Ben, 60–21 over Cara. But Edelman points at two buried voter blocs — (10 Ben>Cara>Ada, 10 Cara>Ada>Ben, 10 Ada>Ben>Cara) and (1 Ada>Cara>Ben, 1 Cara>Ben>Ada, 1 Ben>Ada>Cara). Each is a perfectly symmetric cycle he calls a **Condorcet component**: within the bloc, every pairwise vote ties exactly, so — he argues — "the only reasonable conclusion is that all three alternatives are tied," and a bloc that collectively ties should **cancel out**. Remove those 33 voters and the remaining 48 say something unambiguous: 20 Ada>Ben>Cara vs 28 Ben>Ada>Cara — *"it is rather clear that B should be the winner."* Yet Ada, not Ben, is the Condorcet winner. Balinski & Laraki proved this isn't a fluke: **no social choice function is Condorcet consistent and "cancels properly"** — you must pick a side.

## What the methods say — live

Every majoritarian count elects **Ada**; every positional/summation count elects **Ben**. That's not a coincidence — it's the two worldviews the theorem says can't coexist:

| Elects **Ada** (majoritarian / pairwise) | Elects **Ben** (positional / cancellation-respecting) |
|---|---|
| Condorcet winner (41–40, 60–21) | Borda count (Ben 109, Ada 101, Cara 33) |
| Ranked Robin — record 2–0–0 | Score sum (5/2/0 map): Ben 257, Ada 233, Cara 77 |
| RCV-IRV — Cara out (31/39/11), then 41–40 | Choose-One Plurality: Ben 39, Ada 31, Cara 11 |
| **STAR's automatic runoff** — Ada 41–40 | **STAR's scoring round** — Ben first, 257–233 |

STAR is the one method that shows **both counts in one election** — its scoring round *is* a proper-cancelling summation (a Condorcet component adds the same total to every candidate, so it cancels exactly, like Borda), and its runoff *is* the majoritarian step. The engine's `[Runoff Reversal]` block narrates the handoff:

```
--- Runoff (Preference) Matrix ---
                 |    * Ada     |   * Ben     |     Cara    |
-------------------------------------------------------------
         * Ada > |     ---      |41 -  0 - 40 |60 -  0 - 21 |
         * Ben > | 40 -  0 - 41 |    ---      |69 -  0 - 12 |
          Cara > | 21 -  0 - 60 |12 -  0 - 69 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Ada — matches the STAR winner

[Divergence from STAR]
  STAR                   = Ada
  Choose-One (Plurality) = Ben   (differs from STAR)
  Approval               = Ben   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Ben)
 - Runoff Round Winner   = (Ada)
  Candidate Ben earned the highest total score, but
  Candidate Ada won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).
```

So "who should win Edelman's election?" is precisely the repo's [majoritarian-vs-utilitarian split](../what_makes_a_good_winner.md), with a 240-year pedigree: Condorcet built the example to embarrass Borda's count; Saari — Borda's great modern champion — reversed the polarity and used the same example to embarrass Condorcet's criterion. Neither side ever "won," because the two ideals genuinely disagree here, 41 voters to 40.

## The component on its own — everything ties, and the engine says so

The 30-voter Condorcet component is worth tabulating alone: [edelman_perfect_component_c3_b30](../../../method_comparisons/edelman_condorcet_myth/edelman_condorcet_myth_pages/edelman_perfect_component_c3_b30.md). Every pairwise vote is 20–10 *in a cycle*, every score sum is 70, every candidate holds exactly ten 5s. The LH engine's tiebreak ladder exhausts — scores tie 70/70/70, pairwise ties 30/30/30, five-star counts tie 10/10/10 — and it prints its rare honest flag: **"[Lot-decided tie — rare] … the result here was set by lot, not by the votes."** Then the cycle itself decides the runoff (whichever pair the lot admits, one beats the other 20–10). Any method must do something arbitrary with this electorate; the teaching value is an engine that *tells you* it's being arbitrary. This one is **LH-only** deliberately — a BetterVoting version would resolve the ties at random, so its result couldn't be frozen.

## The no-show argument (Section IV) — real, and it cuts every direction

Edelman's second line is theoretical: by a theorem of H. Peyton Young, **"No social choice function that is Condorcet consistent is also join consistent"** — if two electorates separately pick C, a Condorcet-consistent method can pick something else when they vote together. His worked example (sequential pairwise voting, the agenda A-vs-B then winner-vs-C): group X (3 A>B>C, 3 C>A>B, 5 B>C>A) chooses **C**; group Y (5 B>A>C, 1 A>C>B, 5 C>B>A) also chooses **C**; the combined 22 voters choose **B** — Ben beats A 15–7 and C 13–9, a genuine Condorcet winner that neither group wanted. A delegation could advance its interests by *staying home* — the **no-show paradox**, which Riker called a "very serious defect." Edelman's real-world illustration is Burlington 2009 — where, as he notes, the method in use was IRV, "which is not Condorcet consistent," and the Condorcet winner came in *third*.

Two honest notes, both already in this repo's canon:

- **This critique reaches STAR too.** STAR's runoff step makes it fail the Participation criterion in rare constructed cases — the same family of pathology, documented openly in [RCV-IRV vs STAR](../rcv_irv_vs_star.md) and [STAR's honest limits](../../STAR_Voting/properties_and_limits/STAR_honest_limits.md). No method escapes Gibbard–Satterthwaite; the choice is which failures, how often, and how visibly.
- **It reaches IRV harder.** IRV fails join consistency *and* Participation *and* the Condorcet criterion — Edelman's Burlington example is an IRV election. This paper lends no comfort to "RCV fixes everything" claims; Edelman himself advocates none of these methods (he ends by gesturing at behavioral economics, not a ballot reform).

## Where this leaves us

Edelman's conclusion — *"There are, alas, no self-evident correct alternatives even in the situations where a Condorcet winner exists"* — is, verbatim, the thesis of this repo's [What makes a "good" winner?](../what_makes_a_good_winner.md) The paper demolishes Condorcet-as-axiom; it does not crown a rival. Read it alongside the [FairVote claim check](fairvote_condorcet_claim_check.md) as the pair of anti-Condorcet arguments: one that dissolves under tabulation, and one that survives it — and notice that the survivor's lesson is symmetrical. If the Condorcet winner isn't sacrosanct, then a method missing it occasionally (STAR, by design, in rare profiles) isn't automatically broken — and by the same token, electing it usually is a *chosen* ideal, not a proof of correctness. Name your ideal, show the ballots, count.

## The demo elections

| Page (start here) | What it shows | Live results | Source | Full report |
|---|---|---|---|---|
| [BV2173 — Edelman's 81 voters](../../../method_comparisons/edelman_condorcet_myth/edelman_condorcet_myth_pages/bv2173_gmfv4c_edelman_saari_cancellation.md) | Condorcet winner Ada vs cancellation/Borda winner Ben; STAR shows both counts (Ben 257–233 in scores, Ada 41–40 in the runoff); RR and IRV → Ada, Plurality → Ben | **[results ↗](https://bettervoting.com/gmfv4c/results)** | [yaml](../../../method_comparisons/edelman_condorcet_myth/bv2173_gmfv4c_edelman_saari_cancellation.yaml) | [tabulated](../../../method_comparisons/edelman_condorcet_myth/edelman_condorcet_myth_tabulated/bv2173_gmfv4c_edelman_saari_cancellation_tabulated.txt) |
| [The perfect component, alone](../../../method_comparisons/edelman_condorcet_myth/edelman_condorcet_myth_pages/edelman_perfect_component_c3_b30.md) | 30 voters, everything ties (70/70/70 scores, 20–10 cyclic pairwise); the engine's tiebreak ladder exhausts and flags the lot-decided result — LH-only by design | — (not freezable on BV) | [yaml](../../../method_comparisons/edelman_condorcet_myth/edelman_perfect_component_c3_b30.yaml) | [tabulated](../../../method_comparisons/edelman_condorcet_myth/edelman_condorcet_myth_tabulated/edelman_perfect_component_c3_b30_tabulated.txt) |

Related: [Condorcet topic hub](README.md) · [FairVote claim check](fairvote_condorcet_claim_check.md) · [What makes a "good" winner?](../what_makes_a_good_winner.md) · [STAR's honest limits](../../STAR_Voting/properties_and_limits/STAR_honest_limits.md) · [cycle resolution](../../RCV_Ranked_Robin/cycle_resolution.md) · [the math behind Condorcet](../../RCV_Ranked_Robin/the_math_behind_condorcet.md)

# file: edelman_condorcet_myth.md
