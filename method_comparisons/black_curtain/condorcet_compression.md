# When compression moves the Condorcet winner — Black Curtain #1, read three ways

*Five voters, one set of opinions, three ways of writing them down. On the full score ballot **Cal** is the [Condorcet winner](../../07_Concepts/topics/condorcet/) — he beats everyone head-to-head. Compress those same opinions into approve / don't-approve and the Condorcet winner becomes **Bob** — legitimately, on the ballots as recorded. Neither count is wrong. The difference is the compression, and you can watch exactly where it happens: in the **Equal Support** column of the pairwise matrix.*

→ The set: [The Black Curtain](README.md) · the theory this is the limit of: [Approval in the theory literature](../../04_Approval/concepts/approval_in_the_literature.md) · [Approval's honest limits](../../04_Approval/concepts/approval_honest_limits.md) · [scores vs ranks](../../07_Concepts/scores_and_ranks/scores_vs_ranks.md). Cases: [01 full scores](cases/cases_pages/Black_Curtain_01_c3_b5_hidden-consensus.md) · [01a the approval count](cases/cases_pages/Black_Curtain_01a_c3_b5_approval.md) · [01b the compressed ballot](cases/cases_pages/Black_Curtain_01b_c3_b5_dichotomous.md).

---

## The five voters

Three voters love Cal and can't stand Ann; two are the mirror image. **Every one of the five rates Bob a 4** — nobody's favorite, everybody's strong second.

| voter | Ann | Bob | Cal |
|---|---|---|---|
| 1 | 0 | 4 | **5** |
| 2 | 0 | 4 | **5** |
| 3 | 0 | 4 | **5** |
| 4 | **5** | 4 | 0 |
| 5 | **5** | 4 | 0 |

That is the whole election. Everything below is the same five rows, written down with less resolution each time.

## Reading 1 — the full score ballot

Every voter has a strict opinion about every pair, so the pairwise matrix has **no Equal Support anywhere**, and Cal wins all three of his matchups:

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |     Ann    |  * Bob    |  * Cal    |
-----------------------------------------------------
         Ann > |    ---     |2 - 0 - 3  |2 - 0 - 3  |
       * Bob > | 3 - 0 - 2  |   ---     |2 - 0 - 3  |
       * Cal > | 3 - 0 - 2  |3 - 0 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Cal — matches the STAR winner
```

Cal is the Condorcet winner and the STAR winner — the 3-voter majority's favorite, and their preference for Cal over Bob (5 vs 4) is what the runoff reads. Full report: [Black Curtain #1](cases/cases_pages/Black_Curtain_01_c3_b5_hidden-consensus.md).

## Reading 2 — the approval count

Now the same voters mark an approval ballot. Following the source video's threshold, a 3 or better is an approval — so voters 1–3 approve {Bob, Cal} and voters 4–5 approve {Ann, Bob}:

```text
--- Approval Voting (single winner) ---
 Tabulating 5 ballots (any non-zero score = approval).

   Bob -- 5 (100%) -- Elected
   Cal -- 3 (60%)
   Ann -- 2 (40%)
```

**Bob wins, unanimously approved.** This is the headline result of the Black Curtain set: same voters, different method, different winner. Full report: [01a](cases/cases_pages/Black_Curtain_01a_c3_b5_approval.md).

## Reading 3 — the approval marks, read pairwise

Here is the step that makes the lesson precise. Take those approval marks and read them as a *ballot* — approved above not-approved, nothing said within either group — then ask the head-to-head questions again ([case 01b](cases/cases_pages/Black_Curtain_01b_c3_b5_dichotomous.md)):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |     Ann    |  * Bob    |  * Cal    |
-----------------------------------------------------
         Ann > |    ---     |0 - 2 - 3  |2 - 0 - 3  |
       * Bob > | 3 - 2 - 0  |   ---     |2 - 3 - 0  |
       * Cal > | 3 - 0 - 2  |0 - 3 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Bob — matches the STAR winner
```

**Bob is now the Condorcet winner**, and honestly so: he beats Cal 2–0 and Ann 3–0 on these ballots. Nobody prefers Cal to Bob any more — not because anyone changed their mind, but because the three voters who prefer Cal approved *both* of them, and an approval ballot has no way to say which one they like better.

## Where the information went

Compare the two matrices in one place. The Equal Support column was **zero everywhere** on the score ballot; on the compressed ballot it holds every preference the count needs:

| Pair | Full scores | Compressed to approve / don't-approve |
|---|---|---|
| **Cal vs Bob** | Cal **3–2** (voters 1–3 rate Cal 5, Bob 4) | Bob **2–0**, with **3 Equal Support** — the Cal-over-Bob preference is gone |
| **Ann vs Bob** | Bob **3–2** (voters 4–5 rate Ann 5, Bob 4) | Bob **3–0**, with **2 Equal Support** — the Ann-over-Bob preference is gone |
| **Cal vs Ann** | Cal **3–2** | Cal **3–2** — unchanged; nobody approved both |
| **Condorcet winner** | **Cal** | **Bob** |

Read the pattern: the compression didn't blur things at random. It erased, for every single voter, the distinction between **their favorite and their acceptable compromise** — and preserved perfectly the distinction between the candidates they love and the one they loathe. That is what a one-bit ballot is *for*, and it is also exactly the distinction [STAR's automatic runoff](../../01_STAR/concepts/the_count/STAR_Automatic_Runoff.md) uses to decide the election. Take it away and the runoff has nothing left to read.

## This is not an indictment of Approval

The tempting conclusion — *"Approval got it wrong"* — doesn't survive the third reading. Run **STAR** on the compressed ballots and it also elects Bob (scoring round Bob 25, Cal 15; runoff Bob 2, Cal 0, Equal Support 3). So does any Condorcet method, since Bob beats everyone. **Every method here elects Bob once the ballot is dichotomous**, because the preference that favored Cal is no longer on the ballot for any of them to count. The counting rule isn't what changed the winner; the *ballot* is. That distinction is the whole point of [the Black Curtain](README.md): what your ballot can record bounds what any method can know.

It also isn't an argument that Cal is the "right" answer. Bob is unanimously approved and everyone's strong second; Cal is the passionate favorite of a 3–2 majority and rated zero by the other two. Which one *should* win is the values question the source video is asking — this page is only about which questions each ballot leaves it possible to ask.

## What it says about "Approval = Borda = Condorcet"

There's a clean theory result behind this: on the domain of **[dichotomous preferences](../../07_Concepts/GLOSSARY.md#the-wider-field-computational-social-choice)** — weak rankings with exactly two indifference classes, which is precisely what an approval ballot is — approval voting coincides with [Borda](../../06_Other/other_ranked_methods/borda.md) *and* with every Condorcet method, and a Condorcet winner is guaranteed to exist. No cycles are possible there.

Reading 3 satisfies that theorem exactly: the compressed profile has a Condorcet winner (Bob), and the approval count picks him. So the theorem is not in question — this case is an instance of it.

What the case shows is the **size of the domain restriction**. Approval ballots in a real election are not drawn from a dichotomous electorate; they are produced by voters compressing richer opinions on the spot, and the Condorcet winner of what they compressed can differ from the Condorcet winner of what they wrote. The equivalence describes the ballots, not the voters. That's the difference between "Approval elects the Condorcet winner" (overclaim) and "Approval elects the Condorcet winner *of the approval ballots*" (true, and much weaker than it sounds). Background and sources: [Approval in the theory literature](../../04_Approval/concepts/approval_in_the_literature.md).

## Run it yourself

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/black_curtain/cases/Black_Curtain_01b_c3_b5_dichotomous.yaml
```

**An engine note, in the spirit of this folder's "verify, don't trust" lesson.** Case 01b encodes an approval as a **5** and a non-approval as a **0**. The magnitudes don't matter — the pairwise counts depend only on the two-class order, so a 1/0 ballot produces an identical matrix. But if you rewrite it as 1/0, the engine's `[Divergence from STAR]` cross-check prints a **wrong** Approval winner: that comparator hard-codes "a score of 3, 4 or 5 is an approval," so on a 1/0 ballot it sees nobody approving anybody and reports whichever candidate wins the resulting all-zero tiebreak. (The real Approval tabulator uses a different rule — *any non-zero score is an approval* — which is why [01a](cases/cases_pages/Black_Curtain_01a_c3_b5_approval.md) counts correctly.) The two disagree on any ballot using scores of 1 or 2; the same misprint is visible today in [`star_ala_approval`](../../01_STAR/_main/cases/cases_pages/star_ala_approval.md).

## See also

- [The Black Curtain](README.md) — the four-election set this case belongs to
- [Approval in the theory literature](../../04_Approval/concepts/approval_in_the_literature.md) — where the dichotomous-domain result comes from, and the three readings of what "approve" means
- [Approval — Honest Limits](../../04_Approval/concepts/approval_honest_limits.md) §4 — "can miss a majority favorite," of which this is the worked case
- [Approval + Top-Two](../../04_Approval/concepts/approval_top_two.md) — what a second head-to-head round recovers, and why it can't be automatic from 0/1 ballots
- [The fidelity ladder](../../07_Concepts/scores_and_ranks/fidelity_ladder.md) · [scores vs ranks](../../07_Concepts/scores_and_ranks/scores_vs_ranks.md) — converting between ballot resolutions, and what each conversion costs
- [Read as Range / Score voting](black_curtain_range.md) — the same four elections through the range engine

# file: condorcet_compression.md
