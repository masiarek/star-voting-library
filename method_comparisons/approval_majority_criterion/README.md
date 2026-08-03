# Approval and the majority criterion — Hamlin & Hua's own example, counted five ways

The tabulatable evidence behind [Claim check — Hamlin & Hua (2023), *The case for approval voting*](../../04_Approval/01_Learn/hamlin_hua_2023.md). One electorate — the worked example printed in that paper's §4.1 — read five ways, so you can watch a [majority criterion](../../07_Concepts/topics/majority_criterion/README.md) failure happen, see exactly where the deciding information goes, and test the paper's own defence of it.

Until now this repo asserted that Approval fails the majority criterion (it's a row in the [criterion table](../../07_Concepts/topics/majority_criterion/README.md#which-methods-and-where)) but only ever *worked* STAR's version of the failure. This set fills that gap — using the example the approval side chose for itself.

**The electorate.** 100 voters, three candidates, kept at the paper's own labels because the point is line-by-line correspondence with the printed example:

| voters | preference | the approval ballot §4.1 assumes they cast |
|--:|---|---|
| 60 | A > B > C | A + B |
| 30 | B > C > A | B + C |
| 10 | C > B > A | C + B |

A is the first choice of 60%. B is approved on all 100 ballots. **Approval elects B.**

| Page (read this) | What it shows | src |
|---|---|:--:|
| [01 — the approval count as printed](cases/cases_pages/hh41_01_approval_as_printed.md) | **B wins, 100 approvals (100%)**, A 60, C 40 — the failure exactly as the paper prints it. Note the 30 and the 10 cast *identical* ballots and collapse to one 40-voter row | [`.yaml`](cases/hh41_01_approval_as_printed.yaml) |
| [02 — the same preferences, counted pairwise](cases/cases_pages/hh41_02_preferences_ranked_robin.md) | **A is the [Condorcet winner](../../07_Concepts/topics/condorcet/)** — beats B 60–40 and C 60–40. The paper opens §4.1 noting a Condorcet winner needn't exist; in its own example one does, and Approval doesn't elect it | [`.yaml`](cases/hh41_02_preferences_ranked_robin.yaml) |
| [03 — the same marks read pairwise](cases/cases_pages/hh41_03_marks_read_pairwise.md) | Would a runoff on approval ballots fix it? No: **"Voters with a preference: 40 of 100 (60 Equal Support)."** The 60 who prefer A approved both, so they say nothing in the head-to-head | [`.yaml`](cases/hh41_03_marks_read_pairwise.yaml) |
| [04 — the paper's own utility stipulation, on a 0–5 ballot](cases/cases_pages/hh41_04_stipulated_utilities_star.md) | §4.1 says a real utility gap "would require certain assumptions." Written down, those assumptions are three ballot rows: **score round A 380, B 370** — the gap really is tiny, and **STAR elects A anyway**, 60–40 in the runoff | [`.yaml`](cases/hh41_04_stipulated_utilities_star.yaml) |
| [05 — the majority bullet-votes instead](cases/cases_pages/hh41_05_majority_bullet_votes.md) | Same voters, same opinions, one threshold moved: **A wins 60–40**. The violation lives in where the line is drawn, not in the electorate | [`.yaml`](cases/hh41_05_majority_bullet_votes.yaml) |

## The one table that carries the lesson

Same 100 voters, same opinions, every row an engine result:

| what the ballot recorded | who wins | by how much |
|---|:--:|---|
| full preferences, pairwise ([02](cases/cases_pages/hh41_02_preferences_ranked_robin.md)) | **A** | beats B 60–40, C 60–40 |
| first choices only (Choose-One / RCV-IRV) | **A** | 60% in round one |
| the paper's stipulated utilities, 0–5 ([04](cases/cases_pages/hh41_04_stipulated_utilities_star.md)) | **A** | score 380–370, runoff 60–40 |
| approve / don't approve ([01](cases/cases_pages/hh41_01_approval_as_printed.md)) | **B** | 100 – 60 |
| the same marks, pairwise ([03](cases/cases_pages/hh41_03_marks_read_pairwise.md)) | **B** | 40 – 0, with 60 Equal Support |

Read the last two rows against the third. On the full-resolution ballot A and B are ten points apart in five hundred — a coin flip, exactly as the paper argues. Compressed to checkmarks, the same electorate reports B over A by **100 to 60**. The compression doesn't merely lose the gap; it manufactures a landslide in the opposite direction. That is a sharper statement of [Approval's honest limits §1](../../04_Approval/01_Learn/approval_honest_limits.md#1-no-preference-strength-or-order) than the limits page itself makes.

## Fairness notes

- **The paper's framework is the right one, and this repo already uses it.** Hamlin & Hua argue a criterion violation should be judged on *frequency × severity*, not as a pass/fail checkbox. Agreed — [the same standard](../../07_Concepts/topics/criteria_at_a_glance.md) is what stops this library treating "STAR fails the majority criterion" as a knockout. Case 04 concedes their severity point outright.
- **It cuts against STAR too.** STAR fails the majority criterion as well — worked at [BV95a / BV95b](../../01_STAR/03_Criteria/majority_criterion/README.md). The difference is the trigger: STAR's failure needs the majority to support **two** rivals, Approval's needs **one**. That is the [Relaxed Majority Criterion](../../07_Concepts/topics/majority_criterion/README.md#the-relaxed-majority-criterion-equal-votes-answer), and it is a difference of degree, not of kind.
- **Case 05 is a counterfactual and is labelled one.** The paper's assumed ballots are case 01; case 05 changes them to isolate what the example depends on.

Concept hubs: [majority criterion](../../07_Concepts/topics/majority_criterion/README.md) · [Approval Voting](../../04_Approval/01_Learn/) · [Approval in the theory literature](../../04_Approval/01_Learn/approval_in_the_literature.md) · [Black Curtain — the same compression, five ballots](../black_curtain/README.md) · up: [method_comparisons — same ballots, different methods](../)

# file: README.md
