# Proportional on both sides — what the ballot alone changes

*Nine co-op members, five candidates, three seats. The same opinions recorded twice: once on a 0–5 score ballot, once as Yes/No approvals. Both halves counted **proportionally**, so the seat-filling philosophy is held constant and the committees differ for exactly one reason — the paper.*

→ Why the comparison is built this way: [Comparing multi-winner methods](../../07_Concepts/topics/comparing_multiwinner_methods.md) · the fork: [Electing more than one, simply](../../07_Concepts/topics/electing_more_than_one.md)

**Level: 301 · deep dive**

---

## The result

| Ballot | Tabulation | Committee |
|---|---|---|
| **0–5 scores** | [Allocated Score](../../03_STAR_PR/01_Learn/STAR_PR/allocated_score.md) | **Ben**, Chris, Amy |
| **0–5 scores** | [SSS](../../03_STAR_PR/01_Learn/STAR_PR/sequentially_spent_score.md) | **Ben**, Chris, Dana |
| Yes/No | seq-Phragmén | Chris, Dana, **Ella** |
| Yes/No | PAV | Chris, Dana, **Ella** |
| Yes/No | seqPAV | Chris, Dana, **Ella** |
| Yes/No | AV *(bloc — majoritarian, for reference)* | Chris, Dana, **Ella** |

Chris is seated by everything. **Ben is seated by both score rules and by no approval rule; Ella by all four approval rules and neither score rule.** That Ben-for-Ella trade is the finding, and it is carried by the ballot, not by any one method's eccentricity.

The score side does split its own third chair — Amy on Allocated Score, Dana on SSS. That is a genuine [allocated-vs-SSS divergence](../../03_STAR_PR/02_Examples/method_divergences/README.md) (the two rules retire Ben's supporters' weight differently), and it arrived here honestly: until the fork's 2026-08-09 [count-vs-weight fix](../../03_STAR_PR/03_Criteria/allocated_count_vs_weight/README.md) the engine's Allocated Score also said Dana, and the two score rules appeared to agree. Weight-true accounting — confirmed live against BetterVoting production — elects Amy. The Ben/Ella contrast is untouched by any of this.

## Why Ben and Ella swap

| | score total | scores | above the 3-star line | zeros |
|---|--:|---|--:|--:|
| **Ben** | **24** | 1,2,4,3,2,2,2,5,3 | 4 | **0** |
| **Ella** | 22 | 4,0,3,4,5,0,2,4,0 | **5** | **3** |

Ben scores *higher* and is approved *less*.

He is nobody's favourite and everybody's acceptable — a wall of 2s and 3s with **not one zero in the room**. Ella is the opposite shape: four voters rate her 4 or 5, and three give her nothing at all.

The threshold is what does it. Approving at ≥3 throws away everything underneath, so **Ben's steady 2s vanish entirely** while a bare 3 counts exactly as much as a 5. On the scored ballot Ben's floor is worth 24 points; on the approval ballot it is worth nothing, and Ella's five marks beat his four.

**An approval ballot cannot see a floor.** That is the whole finding, and it is the multi-winner form of the familiar single-winner point about [scores versus approval](../star_vs_approval_divergence.md).

## Read this carefully — the threshold is an assumption

The two files are not two elections. They are one set of opinions projected onto two papers, and the projection rule — **approve iff score ≥ 3** — is a *choice that changes the answer*. Ben clears a threshold of 2 five more times than Ella; Ella wins outright at 4.

So this is evidence about *this projection*, not proof that approval ballots elect worse committees. Real approval voters pick their own thresholds strategically, and would not all use 3. What the case does establish is narrower and still worth having: **holding the philosophy constant, the ballot alone can change who sits on a board** — so the ballot is not merely a convenience over the same underlying result.

It also shows the reverse of the usual worry. On this electorate the majoritarian approval rule (AV) and the three proportional ones agree completely, while the *ballot* split the outcome. The dominant variable is not always the one you expect, which is exactly why [the comparison discipline](../../07_Concepts/topics/comparing_multiwinner_methods.md) asks you to change one thing at a time.

## Run it

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/proportional_ballots/cases/coop_board_scores_allocated.yaml
```

The proportional approval rules are not in the LH engine — they come from Martin Lackner's [`abcvoting`](../../06_Other/abcvoting_tabulation_engine/README.md):

```bash
.venv/bin/python 06_Other/abcvoting_tabulation_engine/abc_tabulation.py method_comparisons/proportional_ballots/cases/coop_board_approval.yaml
```

## The cases

| Case | Ballot | Method | Winners | Read · run |
|---|---|---|---|---|
| Co-op board — scores | 0–5 | `allocated` | Amy, Ben, Chris | [count](cases/cases_pages/coop_board_scores_allocated.md) · [yaml](cases/coop_board_scores_allocated.yaml) |
| Co-op board — scores | 0–5 | `sss` | Ben, Chris, Dana | [count](cases/cases_pages/coop_board_scores_sss.md) · [yaml](cases/coop_board_scores_sss.yaml) |
| Co-op board — approvals | Yes/No | `Approval_Multi_Winner` (+ abcvoting) | Chris, Dana, Ella | [count](cases/cases_pages/coop_board_approval.md) · [yaml](cases/coop_board_approval.yaml) |

**Where this comes from.** Original to this repo. Located by exhaustive random search over 0–5 profiles at 5 candidates / 9 voters / 3 seats, keeping only profiles where both score tabulations agreed with each other, *all three* proportional approval rules agreed with each other, and the two sides differed. Every result is deterministic; no lot is involved. One honesty note: the search's "both score rules agree" filter ran on the pre-2026-08-09 engine, whose Allocated Score carried the [count-vs-weight bug](../../03_STAR_PR/03_Criteria/allocated_count_vs_weight/README.md) — under the fixed accounting the score rules split their third chair (Amy vs Dana), so this profile no longer satisfies the filter it was found with. The load-bearing property — Ben seated by every score rule, Ella by every approval rule, on the same opinions — holds under the fixed engine and is BetterVoting-confirmed.

## Related

- **The discipline this case obeys:** [Comparing multi-winner methods](../../07_Concepts/topics/comparing_multiwinner_methods.md)
- **The same question inside one ballot:** [when the STAR-PR methods disagree](../../03_STAR_PR/02_Examples/method_divergences/README.md) — three tabulations, one 0–5 ballot
- **The approval side's own theory:** [Thiele methods](../../04_Approval/01_Learn/Multiwinner_Approval/thiele_methods.md) · [Multiwinner Approval](../../04_Approval/01_Learn/Multiwinner_Approval/README.md)
- **Six methods, one electorate, axis labelled:** [Pets governance](../pets_governance/README.md)
