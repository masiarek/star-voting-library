# Brams' grading paradox — grades vs head-to-head, counted

*The most famous Approval advocate's case against grading systems, run through the engine. Steven Brams' three-voter example shows the top-grades candidate (Adams) is not the head-to-head champion (Baker). True — but counted under **STAR**, the example vindicates the automatic runoff: STAR elects Baker, the [Condorcet winner](../../00_start_here/topics/condorcet/). What the construction actually indicts is pure score summation — and its proposed Approval fix turns out to depend entirely on where each voter draws the 0/1 line.*

**Provenance.** The theorem and a family of examples are published in Brams & Potthoff, ["The paradox of grading systems"](https://link.springer.com/article/10.1007/s11127-015-0303-6) (*Public Choice* 165, 2015, pp. 193–210; [free preprint](https://mpra.ub.uni-muenchen.de/63268/)); Brams raised the argument to this repo's author in correspondence (September 2024) as the case for Approval over STAR. The case on this page is the **talk-slide variant** of the paper's Example 2: the published version gives voter 3 the grades (0,1,1) instead of (1,2,1), which leaves Baker and Chen tied in *every* head-to-head view — a [dead rung](../../01_STAR/tie_break_dead_rung/) a deterministic count must lot-break — while the slide variant sharpens it to a strict Condorcet winner. Brams co-wrote the modern case for Approval voting itself, so this is the steelman, from the source. (His other appearance in this library: [many IRV pathologies in one election](../paradoxes_and_whoops/bv2159_f4cjpy_brams_irv_pathologies.md).)

## The example — grades {0..3}, three voters

| | Adams | Baker | Chen |
|---|:--:|:--:|:--:|
| voter 1 | 3 | 0 | 0 |
| voter 2 | 2 | 3 | 3 |
| voter 3 | 1 | 2 | 1 |
| **grade total** | **6** | 5 | 4 |

Adams has the best grades. But head-to-head, **Baker beats Adams 2–1** (voters 2 and 3) and **Baker beats Chen 1–0** (the other two ballots grade them equal) — Baker is the Condorcet winner. Brams' point: a grading count and the head-to-head count can disagree, and when they do, "the grading system elected the wrong candidate" is a live attack.

## Three counts, one election

- **Score (sum the grades):** **Adams**. This is the method the example genuinely indicts.
- **Head-to-head (Condorcet):** **Baker**.
- **STAR:** finalists Adams & Baker (the two best grade totals) → runoff **Baker, 2–1**. **STAR elects the Condorcet winner here.** The critique names STAR, but the construction can't reach it: STAR is not "highest average grade" — the automatic runoff is a head-to-head majority check on the two finalists, and it catches exactly the discrepancy the critique warns about. The engine's report, in full:

```text
=== Brams' grading paradox — the grade leader loses the runoff ===

--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Adams   | * Baker   |    Chen   |
-----------------------------------------------------
     * Adams > |    ---     |1 - 0 - 2  |1 - 1 - 1  |
     * Baker > | 2 - 0 - 1  |   ---     |1 - 2 - 0  |
        Chen > | 1 - 1 - 1  |0 - 2 - 1  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Baker — matches the STAR winner

[Divergence from STAR]
  STAR     = Baker
  Approval = Adams   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Adams)
 - Runoff Round Winner   = (Baker)
  Candidate Adams earned the highest total score, but
  Candidate Baker won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).


--- STAR Voting Method (single winner) ---
 Tabulating 3 ballots.
Adams,Baker,Chen
    3,    0,   0
    2,    3,   3
    1,    2,   1

Scoring Round
 The two highest-scoring candidates advance to the next round.
   Adams         -- 6 -- First place
   Baker         -- 5 -- Second place
   Chen          -- 4
 Adams and Baker advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Baker         -- 2 -- First place
   Adams         -- 1
   Equal Support -- 0
 Baker wins.
   Voters with a preference: 3 of 3 (no Equal Support).
   Baker 2 (67%) vs Adams 1 (33%); majority = 2.

Winner — STAR Voting Method (single winner)
 Baker
```

Note the engine's own `[Divergence from STAR]` block: `Approval = Adams (differs from STAR)`. Hold that thought.

## "Approval prevents this" — where the theorem is true, and what it costs

Brams' accompanying theorem: dichotomize the grades to 0/1 and the discrepancy is *impossible* — the approval winner is also the pairwise champion, and there are no Condorcet cycles. **The theorem is true — and it is the [approval-runoff echo](../../00_start_here/Approval_Voting/approval_top_two.md) wearing a bow tie.** On 0/1 ballots every pairwise margin computed from the ballots *is* the approval margin (shared approvals cancel), so of course the approval winner "beats" everyone head-to-head and nothing can cycle: a one-bit ballot cannot disagree with itself. The guarantee is bought by discarding the very information in which a disagreement could be expressed.

And the dispute doesn't vanish — it moves into the voting booth. "Dichotomize the grades" means every voter picks a threshold, and the winner depends on which one they pick:

| The 0/1 cut applied to the same grades | Ballots become | Totals A–B–C | The "indisputable" winner |
|---|---|:--:|---|
| Brams' slide cut — each voter approves their top grades | (1,0,0) (0,1,1) (0,1,0) | 1–2–1 | **Baker** |
| Approve anything above 0 (the minimal uniform cut) | (1,0,0) (1,1,1) (1,1,1) | 3–2–2 | **Adams** |
| Approve grades ≥ 2 (the top half of the scale) | (1,0,0) (1,1,1) (0,1,0) | 2–2–1 | **Adams–Baker tie** |
| Approve only a top grade (3) | (1,0,0) (0,1,1) (0,0,0) | 1–1–1 | **three-way tie** |

Same grades, four reasonable cuts, three different outcomes. Even the engine's `Approval = Adams` line above is a fifth cut at work: its comparison block approves **3+ stars** (calibrated for real 0–5 STAR ballots), which only the 3s on these ballots clear — approval totals 1–1–1, and the tie falls to the left-most column. The threshold decides, always; that *is* the point. The "indisputable" winner is Adams, Baker, or a tie depending on a choice the method silently delegates to each voter — Approval's [threshold dilemma](../../00_start_here/Approval_Voting/approval_honest_limits.md), and the reason [there is no single STAR-vs-Approval divergence rate](../star_vs_approval_divergence.md). (On Arrow: cardinal ballots do sidestep Arrow's ranking framework, as Brams says — but [Gibbard's theorem](../../00_start_here/topics/gibbard_satterthwaite_theorem.md) applies to every method, Approval included; the strategic burden just relocates to the threshold.)

## More from the paper — two examples worth counting

The full paper ([MPRA preprint](https://mpra.ub.uni-muenchen.de/63268/)) grades the paradox from weak (the average-grade and head-to-head winner *sets* overlap but differ) to strong (no overlap at all), and two of its constructions earned their own case files here:

- **[Example 6 — three counts, three winners](brams_grading_paradox_pages/brams_ex6_three_winners_c3_b9.md)** (Amos, Bree, Cole; 9 voters, grades {0..2}). The paper's showpiece, proven by exhaustive search to be the *unique* minimal bloc-structured election of its kind: the **grade totals** crown Amos (11–10–10), the **median grade** crowns Bree (2 vs 1 vs 1 — the Majority Judgment answer), and **head-to-head** crowns Cole, who beats both rivals. STAR sides with head-to-head — the score round ties Bree/Cole at 10, the tiebreak advances Cole (he beats Bree 4–2), and Cole wins the runoff 3–2. Every bloc's preferences are dichotomous, so their natural Approval ballots elect Cole too (6–5–7); a uniform any-non-zero cut elects Amos (9–5–7). One election, and "who should win?" gets a different answer from every aggregation philosophy — the whole methods debate in nine ballots.
- **[Example 3 — two candidates](brams_grading_paradox_pages/brams_ex3_two_candidates_c2_b5.md)** (Alan, Beth; 5 voters). The strong paradox needs no third candidate: two all-in fans put Alan ahead on grade totals 4–3, but three of five voters grade Beth higher, and STAR's runoff elects her 3–2. The purest "strength of support vs number of supporters" collision — nothing else in the election to blame.

Two more findings worth carrying, no case files needed:

- **At two grades, RCV-IRV is the odd one out.** The paper's Proposition 2 shows that on 0/1 ballots the median-grade and Borda counts collapse into Approval — same winner, always — but the **Hare (IRV) elimination machinery does not**: their 27-voter approval-ballot counterexample has Approval, head-to-head, median, and Borda all electing the same candidate while Hare eliminates that candidate first. Even on the simplest possible ballot, elimination order can defect from every aggregate count. (No LH case: reproducing it faithfully needs fractional splitting of tied ranks, which the vendored RCV-IRV engine doesn't do.)
- **How often does the grade-leader-vs-head-to-head split happen?** Their impartial-culture simulation puts the weak paradox at **22%–56%**, rising with the number of candidates and with the number of grades (up to about 7), peaking around 5–8 voters — and the authors themselves stress these are near-certain *overestimates* of real electorates, the same caveat this repo attaches to every simulated rate ([there is no single divergence number](../star_vs_approval_divergence.md)).

## The honest concession

STAR is **not** Condorcet-compliant: when the Condorcet winner isn't among the top two by score, the runoff never sees them — worked case: [STAR misses the Condorcet winner](../paradoxes_and_whoops/bv2156_3grpbb_star_misses_condorcet.md); the [divergence ledger](../divergence_review/INDEX.md) tracks how often methods disagree across the whole library, base rate included. So the fair scoreboard reads: pure Score fails this example; STAR's runoff repairs it here (a Condorcet check on the two finalists) but carries no guarantee; Approval "never misses" only relative to its own ballots' one-bit shadow. Every method trades something — say which trade you're making ([reading these fairly](../paradoxes_and_whoops/reading_these_fairly.md)). For the companion steelman *against* privileging the Condorcet winner at all, see [Edelman's "Myth of the Condorcet Winner," counted](../edelman_condorcet_myth/).

## Files

| Page (read this) | What it shows | src |
|---|---|:--:|
| [the slide example](brams_grading_paradox_pages/brams_grading_paradox_c3_b3.md) | grade leader Adams vs Condorcet winner Baker; STAR's runoff catches it | [`.yaml`](brams_grading_paradox_c3_b3.yaml) |
| [Example 6 — three counts, three winners](brams_grading_paradox_pages/brams_ex6_three_winners_c3_b9.md) | Score→Amos, median→Bree, head-to-head→Cole; STAR (and the blocs' natural Approval ballots) side with Cole; the tiebreak rung on display | [`.yaml`](brams_ex6_three_winners_c3_b9.yaml) |
| [Example 3 — two candidates](brams_grading_paradox_pages/brams_ex3_two_candidates_c2_b5.md) | the strong paradox at c=2: grade totals say Alan, three of five voters say Beth; the runoff is the whole story | [`.yaml`](brams_ex3_two_candidates_c2_b5.yaml) |

All three are LH-only for now — BetterVoting elections (BV2189+) can back them whenever wanted; every ballot set is a handful of tiny score rows. Up: [method_comparisons — same ballots, different methods](../).

# file: README.md
