# Comparing multi-winner methods — change one thing at a time

**One line:** a multi-winner method is two independent choices — *what the ballot lets you say* and *how the seats get filled* — and a comparison that changes both at once cannot tell you which one caused the difference. Match the half you are not testing, or the result is uninterpretable.

→ The fork itself, in plain language: [Electing more than one, simply](electing_more_than_one.md) · the sibling guardrail for individual cases: [Reading these fairly](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md)

**Level: 201 · for debaters**

---

## The trap, concretely

> *"Bloc Approval and Proportional STAR elected different committees — so the 0–5 ballot must be doing something the Yes/No ballot can't."*

That conclusion does not follow, and the sentence is a good example of how easy the mistake is to make in good faith. **Two** things differ between those methods, not one:

1. the **ballot** — Yes/No versus 0–5, and
2. the **seat-filling philosophy** — majoritarian (fill every seat with whoever the most voters want) versus proportional (share the seats among factions).

When the committees differ, the difference is unattributable. It could be the extra expressiveness of scores. It could be that one method was trying to seat a minority and the other wasn't. Almost certainly it is mostly the second, because the majoritarian/proportional gap is by far the larger effect — it is the whole reason proportional methods exist, and on a cohesive electorate it can change *every* seat.

## The two variables

|  | Majoritarian — "the N best" | Proportional — "mirror the electorate" |
|---|---|---|
| **Yes/No ballot** | Bloc Approval (`av`) | PAV · seqPAV · seq-Phragmén |
| **0–5 score ballot** | [Bloc STAR](../../02_STAR_Bloc/README.md) | [Allocated Score · SSS · RRV](../../03_STAR_PR/01_Learn/STAR_PR/README.md) |
| **Ranked ballot** | Bloc Ranked Robin | [STV](../../06_Other/STV/README.md) |
| **Choose-one ballot** | [Block Plurality · SNTV · Limited Voting](../../method_comparisons/multi_member_plurality/README.md) | — |

Read the table as a grid, not a list. **Move along a row** and you are testing the ballot, with philosophy held constant. **Move down a column** and you are testing the philosophy, with the ballot held constant. **Move diagonally and you have learned nothing** — which is the whole content of this page.

## The pairings that answer a question

**Testing the ballot** (philosophy held constant):

- Bloc Approval ↔ **Bloc STAR** — both majoritarian, so a divergence is attributable to what the paper let voters say. This is the honest version of "what does 0–5 buy over Yes/No?"
- PAV or seq-Phragmén ↔ **Allocated Score** — the same question on the proportional side.
- STV ↔ **STAR-PR** — ranked versus scored, both proportional. Worked in this repo at [STV vs STAR-PR](../../03_STAR_PR/01_Learn/stv/proportional_stv_vs_star.md).

**Testing the philosophy** (ballot held constant):

- Bloc STAR ↔ STAR-PR — one 0–5 ballot, two seat-filling rules. The cleanest demonstration of the fork, because nothing about the voting changes.
- Bloc Approval ↔ PAV — the same, on approval ballots.

**Testing neither** — Bloc Approval ↔ STAR-PR, Bloc STAR ↔ STV, SNTV ↔ PAV. Two variables, one result.

## "Same ballot" needs a stated rule

There is a subtlety in the row comparisons worth naming, because it is where a careful comparison can still go wrong. Voters do not hold "an approval ballot" and "a score ballot" — they hold **opinions**, and each ballot records a different amount of them. To put the same electorate on both papers you must **project** the richer ballot onto the poorer one: *approve every candidate scored 3 or more*, say.

That threshold is a **choice, and it changes the answer.** A voter who scores 5/3/0 approves two candidates at a threshold of 3 and one at a threshold of 4. So any ballot-comparison silently depends on an assumption about how voters would behave with a cruder instrument — which is exactly the [approval threshold problem](../../04_Approval/01_Learn/Multiwinner_Approval/README.md), and it is real rather than pedantic. **State the threshold**, and treat the comparison as evidence about *that* projection rather than about approval voting in general.

## When a mixed spread is fine

None of this forbids putting six methods on one electorate. It forbids putting six methods on one electorate and then **attributing** the differences to a single cause.

[Pets governance](../../method_comparisons/pets_governance/README.md) does it correctly: one 22-voter electorate, six methods, framed from the first sentence as showing "the majoritarian-vs-proportional divide," with the majoritarian group sweeping and the proportional group seating the minority. The spread is the lesson, and the page names the axis rather than pretending there is one method-quality ranking underneath.

The failure mode is not variety. It is an unlabelled axis.

## The short version

Before writing "method A and method B disagree, therefore X":

1. Name the **ballot** each one uses.
2. Name the **philosophy** each one fills seats by.
3. If both differ, either fix one and re-run, or drop the causal claim and report the divergence as a divergence.
4. If the comparison crosses ballot types, **state the projection rule** you used.

The same discipline applied to individual edge cases is [Reading these fairly](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md); the same discipline applied to *which* fork you want in the first place is [Electing more than one, simply](electing_more_than_one.md).

## Related

- **The fork:** [Electing more than one, simply](electing_more_than_one.md) — majoritarian vs proportional in plain language
- **The majoritarian family:** [Bloc STAR among the at-large methods](../../02_STAR_Bloc/01_Learn/bloc_star_vs_other_bloc_methods.md)
- **The proportional families:** [the three STAR-PR methods](../../03_STAR_PR/01_Learn/STAR_PR/README.md) · [Thiele methods on approval ballots](../../04_Approval/01_Learn/Multiwinner_Approval/thiele_methods.md)
- **A worked row comparison:** [Proportional on both sides](../../method_comparisons/proportional_ballots/README.md) — one electorate, two ballots, both proportional; the third seat moves
- **Within-family divergence, done right:** [when the STAR-PR methods disagree](../../03_STAR_PR/02_Examples/method_divergences/README.md) — three tabulations, one ballot, one philosophy, so the difference is attributable
- **The engine for the approval half:** [abcvoting](../../06_Other/abcvoting_tabulation_engine/README.md)
