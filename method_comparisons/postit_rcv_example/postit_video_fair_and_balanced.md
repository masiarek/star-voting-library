# Is the Post-it video fair and balanced? — a claim-check with live elections

The lesson page for the whole Post-it set: a claim-by-claim check of Equal Vote's video ["Updated: How does RCV work? — With Post-its!"](https://youtu.be/Vte4nly_Neg), with every claim reproduced (or stress-tested) as a **live BetterVoting election** and an LH tabulation you can re-run.

**The three live elections:**

- **BV2176** [`p8dp28`](https://bettervoting.com/p8dp28/results) — the video's election, three races (STAR / RCV-IRV / Ranked Robin) → [case page](bv2176_p8dp28_postit_rcv_example.md)
- **BV2177** [`v8r66y`](https://bettervoting.com/v8r66y/results) — the same 20 voters, **all seven BV methods**, four different winners → [case page](bv2177_v8r66y_seven_methods.md)
- **BV2178** [`8kg698`](https://bettervoting.com/8kg698/results) — the video's round-2 hypothetical **made real** by a two-ballot flip → [case page](bv2178_8kg698_switch_made_real.md)

## What the video gets right

**The RCV-IRV count is exactly correct.** Every round reproduces digit-for-digit in two independent tabulators (the LH engine and BetterVoting's live count): 7/6/4/3 → Pink out → 8/7/4 → Blue out → **Purple 9, Green 8**, with 3 of 20 ballots exhausted. No quibble anywhere.

**The core criticism is real, and it needs no scores to state.** RCV-IRV eliminated Blue in round 2 without ever asking the head-to-head question, and on these very ballots **Blue beats Purple 10–9**. That fact is pure rank arithmetic — count, for each ballot, which of the two is ranked higher. The winner was decided by *which* candidate got eliminated, not by *who voters preferred* between the finalists-that-might-have-been.

**The exhausted-ballot and shrinking-majority points are fair.** Purple's final "majority" is 9 of 17 still-active ballots (53%) — but 9 of 20 cast (45%). Three voters' ballots ran out of rankings and simply left the room before the final question was asked.

## Where a sharp critic pushes back

**1. The "what if Green were eliminated instead?" scenario is a hypothetical IRV would never execute.** At that point Green held 7 votes to Blue's 4; last place is eliminated, full stop. Stated as an elimination counterfactual, it can sound like IRV mis-executed its own rules — it didn't. The honest version of the point is the pairwise fact above (Blue beats Purple 10–9), which needs no counterfactual. And it *can* be made real: in **[BV2178](bv2178_8kg698_switch_made_real.md)**, two of the six Green>Blue>Pink voters genuinely prefer Blue first — and RCV-IRV then lands the video's exact hypothetical tally, Blue 10, Purple 9. Two ballots is all the elimination order's cliff-edge needs.

**2. There is no "rightful winner" here to be robbed of.** The video's framing suggests RCV-IRV denied the stronger candidate. But this electorate is a **Condorcet cycle**: Blue beats Purple 10–9, yes — but Green beats Blue 7–4, and Purple beats Green 9–8 (and Pink beats Purple 12–8). *Every* candidate loses to somebody. Blue is not a Condorcet winner the way, say, Nashville is in the Tennessee example; Blue merely wins the *particular* matchup STAR's runoff happens to hold. BetterVoting's own Ranked Robin race elects **Green** on these ballots ([the LH engine's ladder says Blue](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md) — a documented tiebreak divergence, not a bug). A fully balanced telling is harsher on IRV and humbler for STAR: what's damning for IRV is not that it missed "the right winner" — none exists — it's that it **never looked at the evidence**. What's humbling for STAR is that its winner here is *a* defensible choice, not *the* provable one.

**3. The 0–5 scores are the video's invention — and the gap sizes do the work.** The 20 voters never actually scored anyone; the video assigned scores to its own ranked ballots. To the video's credit, the assignment is clean: **all 20 score ballots are strictly order-consistent with their rankings** (we verified this programmatically, ballot by ballot — every ranked candidate outscores every unranked one, and every rank step is a strict score drop). So the scores are *correct* as an expression of the ranks. But they are not *implied* by the ranks — and that difference decides the election:

| Scoring of the same rankings | Scoring round (P/G/B/K) | Finalists | STAR winner |
|---|---|---|:--:|
| The video's generous gaps (5,4,3 down-ballot) | 46 / 38 / **44** / 44 | Purple & Blue | **Blue** 10–9 |
| Stingy gaps (5,2,1 down-ballot) | 40 / **34** / 32 / 26 | Purple & Green | **Purple** 9–8 |

Same 20 rankings, both scorings strictly consistent with them — and STAR flips between *disagreeing* with IRV (Blue) and *agreeing* with it (Purple). Blue's spot in the runoff hangs on the six Green fans scoring their second choice a generous 4 (and even then Blue only ties Pink 44–44 for the slot, advancing on the head-to-head). **This is not a gotcha — it is STAR's entire premise:** preference *strength* is real information that ranked ballots cannot carry, and STAR's answer legitimately depends on it. A video demonstrating STAR must invent that information; a real STAR election collects it from the voters. The fair conclusion is narrower than the video implies: *if* voters feel the way the video's scores say, STAR elects Blue — and IRV elects Purple either way, because it never asks.

**4. Conversions are never neutral — the Approval race proves it in one line.** The video's scores use only 0/3/4/5, so converting them to Approval ballots at any threshold from 1 to 3 gives identical votes — and elects **Pink** (12 approvals, riding the Green fans' 3-for-their-last-choice). Approve only 4s and 5s: **Blue** wins. Only 5s: **Purple** wins. Three defensible thresholds, three winners ([live as BV2177's Approval race](bv2177_v8r66y_seven_methods.md), threshold ≤ 3). Anyone who says "just simplify to Approval" has chosen a winner and may not know it.

## The verdict

**Fair on the count, advocacy in the frame.** The video's arithmetic is flawless and its central complaint — IRV decides by elimination order and never consults the head-to-head — is true and important. Its two rhetorical shortcuts are presenting an elimination IRV cannot perform as a near-miss (fixed live by [BV2178](bv2178_8kg698_switch_made_real.md)), and presenting invented preference strengths as if they were data (stress-tested above — under stingier but equally consistent scores, STAR agrees with IRV). And it stops one twist short of full honesty about its own example: there is **no consensus winner in this electorate at all** — run all seven of BetterVoting's methods on it and **all four candidates win somewhere** ([BV2177](bv2177_v8r66y_seven_methods.md)):

| Purple | Green | Blue | Pink |
|:--:|:--:|:--:|:--:|
| RCV-IRV, Choose-One, STV, STAR-PR(1) | Ranked Robin (BV's ladder) | STAR (and LH's RR ladder) | Approval (approve = any support) |

## Lessons to take away

1. **"RCV" names a ballot, not a result.** The identical ranked ballots elect Purple (IRV/STV), Green (BV's Ranked Robin), or Blue (LH's Ranked Robin ladder). Say which *tabulation* you mean.
2. **IRV's real flaw here is ignorance, not error.** It executed its rules perfectly — and its rules never look at 10–9. The strongest criticism is the evidence it *doesn't consult*, not a winner it "got wrong."
3. **Preference strength is information.** STAR's divergence from IRV on this profile exists *because* the scores say the Green fans strongly back Blue. Change the strength, keep the ranks, and the divergence vanishes. That is a feature when voters supply the scores — and an assumption when a video does.
4. **Every conversion picks a winner.** Ranks→scores (5,4,3 vs 5,2,1: Blue vs Purple) and scores→approvals (threshold 3/4/5: Pink/Blue/Purple) are editorial acts. Show your conversion rule or your comparison isn't reproducible.
5. **Cycles are knife-edges.** Two ballots ([BV2178](bv2178_8kg698_switch_made_real.md)) dissolve the cycle into a clean Condorcet winner and snap every ballot-reading method into unanimity — while Choose-One never notices. When methods disagree, suspect a cycle; when a cycle, expect *defensible* disagreement (even between two correct engines).

## Reproduce everything

| Claim | Where to check |
|---|---|
| The video's IRV rounds | [BV2176 IRV race](https://bettervoting.com/p8dp28/results) · [LH mirror](postit_rcv_example_tabulated/bv2176_p8dp28_irv_tabulated.txt) |
| Blue beats Purple 10–9 | any race's pairwise matrix, e.g. [the RR mirror](postit_rcv_example_tabulated/bv2176_p8dp28_ranked_robin_tabulated.txt) |
| STAR → Blue under the video's scores | [BV2176/77 STAR races](https://bettervoting.com/v8r66y/results) · [LH mirror](postit_rcv_example_tabulated/bv2176_p8dp28_star_tabulated.txt) |
| STAR → Purple under stingy scores | re-score [bv2176_p8dp28_star.yaml](bv2176_p8dp28_star.yaml) with 5→5, 4→2, 3→1 and re-run (40/34/32/26; runoff Purple 9–8) |
| Approval threshold picks the winner | [BV2177 Approval race](https://bettervoting.com/v8r66y/results) (threshold ≤ 3 → Pink) · [LH mirror](postit_rcv_example_tabulated/bv2177_v8r66y_approval_tabulated.txt) |
| The switch, real | [BV2178](https://bettervoting.com/8kg698/results) · [LH mirror](postit_rcv_example_tabulated/bv2178_8kg698_irv_tabulated.txt) |

Related: [terminology tips](../../00_start_here/TIPS_terminology.md) · [RR tiebreaks, LH vs BV](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md) · [center squeeze](../center_squeeze/) · up: [method_comparisons](../)

# file: postit_video_fair_and_balanced.md
