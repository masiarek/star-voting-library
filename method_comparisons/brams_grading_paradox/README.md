# Brams' grading paradox — grades vs head-to-head, counted

*The most famous Approval advocate's case against grading systems, run through the engine. Steven Brams' three-voter example shows the top-grades candidate (Adams) is not the head-to-head champion (Baker). True — but counted under **STAR**, the example vindicates the automatic runoff: STAR elects Baker, the [Condorcet winner](../../00_start_here/topics/condorcet/). What the construction actually indicts is pure score summation — and its proposed Approval fix turns out to depend entirely on where each voter draws the 0/1 line.*

**Provenance.** The example and its theorem are published in Brams & Potthoff, ["The paradox of grading systems"](https://link.springer.com/article/10.1007/s11127-015-0303-6) (*Public Choice* 165, 2015, pp. 193–210; [free preprint](https://mpra.ub.uni-muenchen.de/63268/)) and appear in Brams' talks; he raised the argument to this repo's author in correspondence (September 2024) as the case for Approval over STAR. Brams co-wrote the modern case for Approval voting itself, so this is the steelman, from the source. (His other appearance in this library: [many IRV pathologies in one election](../paradoxes_and_whoops/bv2159_f4cjpy_brams_irv_pathologies.md).)

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
| Approve anything above 0 — the LH engine's reading | (1,0,0) (1,1,1) (1,1,1) | 3–2–2 | **Adams** |
| Approve grades ≥ 2 (the top half of the scale) | (1,0,0) (1,1,1) (0,1,0) | 2–2–1 | **Adams–Baker tie** |
| Approve only a top grade (3) | (1,0,0) (0,1,1) (0,0,0) | 1–1–1 | **three-way tie** |

Same grades, four reasonable cuts, three different outcomes. The "indisputable" winner is Adams, Baker, or a tie depending on a choice the method silently delegates to each voter — Approval's [threshold dilemma](../../00_start_here/Approval_Voting/approval_honest_limits.md), and the reason [there is no single STAR-vs-Approval divergence rate](../star_vs_approval_divergence.md). (On Arrow: cardinal ballots do sidestep Arrow's ranking framework, as Brams says — but [Gibbard's theorem](../../00_start_here/topics/gibbard_satterthwaite_theorem.md) applies to every method, Approval included; the strategic burden just relocates to the threshold.)

## The honest concession

STAR is **not** Condorcet-compliant: when the Condorcet winner isn't among the top two by score, the runoff never sees them — worked case: [STAR misses the Condorcet winner](../paradoxes_and_whoops/bv2156_3grpbb_star_misses_condorcet.md); the [divergence ledger](../divergence_review/INDEX.md) tracks how often methods disagree across the whole library, base rate included. So the fair scoreboard reads: pure Score fails this example; STAR's runoff repairs it here (a Condorcet check on the two finalists) but carries no guarantee; Approval "never misses" only relative to its own ballots' one-bit shadow. Every method trades something — say which trade you're making ([reading these fairly](../paradoxes_and_whoops/reading_these_fairly.md)). For the companion steelman *against* privileging the Condorcet winner at all, see [Edelman's "Myth of the Condorcet Winner," counted](../edelman_condorcet_myth/).

## Files

| Page (read this) | What it shows | src |
|---|---|:--:|
| [the case page](brams_grading_paradox_pages/brams_grading_paradox_c3_b3.md) | ballots, full engine report, cross-references | [`.yaml`](brams_grading_paradox_c3_b3.yaml) |

LH-only for now — a BetterVoting election (BV2189) can back it whenever wanted; the ballots are three tiny score rows. Up: [method_comparisons — same ballots, different methods](../).

# file: README.md
