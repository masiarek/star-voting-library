# 01_STAR — single-winner STAR Voting

*One ballot, two rounds: score everyone 0–5, then an automatic runoff between the top two scorers.*

<img src="01_Learn/img/star_ballot_official_evc.png" width="460" alt="A STAR Voting ballot: five candidates — Andre, Blake, Carmen, David, Erin — each scored 0 to 5. Instructions at top: give your favorite five stars, give your last choice zero or leave blank, equal scores are allowed, score other candidates as desired. This voter marks Andre 5, Blake 0, Carmen 4, David 4, Erin 1. Footer: the two highest scoring candidates are finalists, your full vote goes to the finalist you prefer, and the finalist with the most votes wins.">

*The ballot ([Equal Vote](https://www.equal.vote/star)) — note Carmen and David both score 4: equal scores are allowed, so you are never forced to invent a preference you don't feel. And Erin's 1 still outranks Blake's 0 — the ballot records **how much** you like each candidate, not just the order.*

The library's headline method: **STAR** (Score Then Automatic Runoff) for one seat. You score every candidate **0–5**; the two highest-scoring candidates become finalists, and an **automatic runoff** gives each ballot's full vote to whichever finalist it scored higher. Two rounds, one ballot.

Everything about STAR lives in this one folder: the *concept* explanations in [`01_Learn/`](01_Learn/README.md), and the **runnable examples** — tiny elections you can tabulate yourself, each isolating one idea — in the subfolders below. New to STAR? Read the concepts first:

- **New here? — the gentle on-ramp** (what STAR is and why it matters, before any mechanics) → **[STAR — start here](01_Learn/STAR_start_here.md)**
- **Why STAR? — the quick, exciting wins** → [the benefits of STAR](01_Learn/getting_started/STAR_benefits.md); then the *complete* case in plain points → [Why STAR Voting](../07_Concepts/topics/Why_STAR_Voting.md). *Prefer ranked ballots?* → [Why Ranked Robin](../05_Ranked_Robin/01_Learn/why_ranked_robin.md).
- **How the count works** → [the Scoring Round](01_Learn/the_count/STAR_Scoring_Round.md) + [the Automatic Runoff](01_Learn/the_count/STAR_Automatic_Runoff.md) (two rounds, one ballot), and the objections answered honestly in [the second-round FAQ](01_Learn/the_count/STAR_second_round_FAQ.md)
- **Have a specific question?** → [STAR FAQ — mechanics, with worked examples](01_Learn/getting_started/STAR_FAQ.md). **Skeptical?** → [STAR for skeptics](01_Learn/getting_started/star_for_skeptics.md)
- **Do it, don't just read it** → [Hands-on](01_Learn/hands_on/README.md): [run a paper-ballot demo](01_Learn/hands_on/running_a_paper_ballot_demo.md) · [count a STAR election by hand](01_Learn/hands_on/count_star_by_hand.md) · [teach it](01_Learn/hands_on/teaching_star_voting.md)
- **The full course** → [Curriculum — Voting 101 / 201 / 301](../07_Concepts/CURRICULUM.md)

---

## The learning path

Follow the examples roughly in this order. The levels (101 → 201 → 301) match the authoritative **[curriculum](../07_Concepts/CURRICULUM.md)** — start there for the full sequence with pacing notes.

### Voting 101 — the basics (the ballot, the two rounds, the spoiler)

1. **The ballot and the two rounds.** Five coworkers, three lunches — the compromise everyone likes wins, shown on real BetterVoting results → [the team-lunch example](02_Examples/cases/cases_pages/bv2184_fyy886_lunch_vote.md). *(The running example paired with [STAR — start here](01_Learn/STAR_start_here.md).)*
2. **The broad compromise, again.** A second three-candidate case to make the pattern stick → [three candidates](02_Examples/cases/cases_pages/02a_c3_b1_three-candidates.md).
3. **How you're allowed to vote.** Bullet votes, equal scores, low-score "protest" ballots, the eight-style gallery → [ballot styles](02_Examples/cases/cases_pages/03a_c3_b3_style-bullet-vote.md).
4. **The headline lesson — top scorer ≠ winner.** STAR's single most important behavior, as a 3→9-candidate progression with a control case → **[Runoff Reversal](02_Examples/runoff_overturns_leader/README.md)**.
5. **The spoiler, in numbers.** Vote-splitting and the compromise winner → [the vote-splitting scenarios](02_Examples/README.md) · cross-method: [the split-voting set](../method_comparisons/split_voting/README.md).

### Voting 201 — reading results & trusting the count

6. **Read the full audit report.** The minimal on-screen report vs the complete `_tabulated.txt` (preference matrix + score distribution + the runoff/Condorcet blocks) → the `_tabulated/` siblings in [Runoff Reversal](02_Examples/runoff_overturns_leader/README.md).
7. **A real election, end to end.** A real 461-ballot BetterVoting STAR race, raw ballots → winner, read section by section → **["What Makes the Best Pet?"](04_Real_Elections/pet_real_bv_election/README.md)**.
8. **Edge cases & trust.** How ties resolve → [the tie-break ladder](03_Criteria/tie_break_ladder/README.md) · [abstain / blank / zero handling](04_Real_Elections/abstain_bugs/README.md).

### Voting 301 — criteria & edge behavior

9. **The Majority Criterion** (and the "relaxed" version) → [the two 5-voter elections](03_Criteria/majority_criterion/README.md).
10. **The "dead rung"** — when STAR's five-star tiebreaker can't fire and the tie falls to the lot → [the dead-rung case](03_Criteria/tie_break_dead_rung/README.md).
11. **None of the Above** — a protest electorate where NOTA actually wins → [the NOTA election](03_Criteria/none_of_the_above/README.md).
12. **The honest limits & the reversal debate** → [STAR's honest limits](01_Learn/properties_and_limits/STAR_honest_limits.md) · [the second-round FAQ](01_Learn/the_count/STAR_second_round_FAQ.md).
13. **Practice — predict, then peek.** Fourteen worked problems with hidden, tested solutions — reading drills, criteria probes (consistency, participation, later-no-harm), strategy gambles, the real 1994 Olympics ballots, a Ranked Robin cycle, build-your-own constructions, a multi-winner wing (Bloc vs proportional, STV transfers), and Approval's threshold dilemma → **[the exercises set](05_Practice/README.md)**.

---

## How this folder is arranged

Five numbered buckets, in reading order. **Every method folder in the library uses the same five**, so once you know the shape here you know it for [Bloc STAR](../02_STAR_Bloc/README.md), [Proportional STAR](../03_STAR_PR/README.md), [Approval](../04_Approval/README.md) and [Ranked Robin](../05_Ranked_Robin/README.md) too. Difficulty is *not* in the folder names — a case can be 101 for its basic idea and 301 for the deep dive — so levels are marked per set, and the authoritative sequence stays in the [curriculum](../07_Concepts/CURRICULUM.md).

| | Bucket | What lives there |
|---|---|---|
| **01** | [Learn](01_Learn/README.md) | The concept pages: what STAR is, how the two rounds count, the properties and the honest limits. Start here if you're reading, not running. |
| **02** | [Examples](02_Examples/README.md) | The teaching progression — the smallest elections, one new idea each — plus the headline lesson, Runoff Reversal. |
| **03** | [Criteria](03_Criteria/README.md) | What STAR guarantees and where it doesn't: Majority, favorite betrayal, IIA, the Test of Balance, NOTA, and the whole tie-breaking cascade. |
| **04** | [Real elections](04_Real_Elections/README.md) | Live BetterVoting races imported and reconciled against the engine — including the divergences that turn out to be BV bugs. |
| **05** | [Practice](05_Practice/README.md) | Predict-then-peek problems with tested answer keys. |
| **09** | [Parked](09_Parked/README.md) | Kept, but off the learning path. |

### The sets, by level

| Set | Bucket | Level | What it teaches |
|---|---|:---:|---|
| [The teaching progression](02_Examples/README.md) | 02 | 101 | The core sequence: the team-lunch example → three candidates → ballot styles → abstentions → quorum → vote-splitting → display options (one idea at a time). |
| [Runoff Reversal — top scorer ≠ winner](02_Examples/runoff_overturns_leader/README.md) | 02 | 101→301 | Real BetterVoting elections where the runoff **confirms** or **overturns** the score leader — STAR's headline lesson, plus the convincing-vs-jarring reversal pair. |
| [Equal and opposite](03_Criteria/equal_and_opposite/README.md) | 03 | 201 | The Test of Balance: two exact-opposite ballots cancel completely, and the winner never moves. |
| [The tie-break ladder](03_Criteria/tie_break_ladder/README.md) | 03 | 201 | The happy path: ties the deterministic rungs settle before the lot is ever reached. |
| [The Majority Criterion](03_Criteria/majority_criterion/README.md) | 03 | 301 | Two 5-voter elections isolating STAR's Majority-Criterion behavior (and the Relaxed Majority Criterion). |
| [Favorite betrayal](03_Criteria/favorite_betrayal/README.md) | 03 | 301 | The rare construction where STAR's FBC leak shows with numbers — and scoring your favorite lower pays. |
| [IIA & the cycle spoiler](03_Criteria/iia_cycle_spoiler/README.md) | 03 | 301 | In a genuine Condorcet cycle, a candidate who cannot win still changes who does — on sincere ballots. |
| [The dead rung — when the tiebreak can't fire](03_Criteria/tie_break_dead_rung/README.md) | 03 | 301 | The "dead rung": when no tied candidate holds a 5, the five-star tiebreak reads 0–0 and the lot decides. |
| [None of the Above](03_Criteria/none_of_the_above/README.md) | 03 | 301 | BV215 — a protest election where None of the Above tops the scores and wins the runoff. |
| ["What Makes the Best Pet?"](04_Real_Elections/pet_real_bv_election/README.md) | 04 | 201 | A real 461-ballot BV race imported and reconciled line by line — the whole pipeline, raw ballots to winner. |
| [Runoff reversals on BV](04_Real_Elections/runoff_reversal_bv_cases/README.md) | 04 | 201 | The headline behavior on real ballots: BV's own screenshots beside the engine's report. |
| [Abstain, blank & zero handling](04_Real_Elections/abstain_bugs/README.md) | 04 | 201 | BetterVoting's abstain/blank/zero handling reproduced and cross-checked — the "0 tallied votes yet a winner" divergence. |
| [Exercises — predict, then peek](05_Practice/README.md) | 05 | 201→301 | Fourteen worked problems with collapsible solutions: district consistency, the tenth-ballot participation paradox, five-verdicts-one-electorate, the 1994 Olympics ballots, center squeeze, bullet-vote backfire, the Equal Support reading drill, build-your-own reversal, a Ranked Robin cycle ladder, later-no-harm both ways, recruit-a-spoiler, Bloc-vs-proportional seats, the Approval threshold dilemma, and the STV transfer machine. |

*Parked, not on the learning path: [two-candidate STAR](09_Parked/silly_two_cand_STAR/README.md) — deliberately-trivial two-candidate cases. With only two candidates the runoff just echoes the scores, so there's nothing distinctive to learn; kept for completeness and as engine test fixtures. And [flat scores & ties](09_Parked/Flat_scores_ties/README.md) — eight ballots engineered to tie at every locus, swept on one page; the tie-breaking that teaches is [the ladder](03_Criteria/tie_break_ladder/README.md) and [the dead rung](03_Criteria/tie_break_dead_rung/README.md).*

---

## Run a file yourself

From the engine directory:

```
python starvote_larry_hastings.py "01_STAR/02_Examples/cases/02a_c3_b1_three-candidates.yaml"
```

Every file writes a full audit report to its `_tabulated.txt` sibling — watch for the **[Runoff Reversal]** block, which prints whenever the score leader and the runoff winner differ.

## Related

- **Concept docs:** [the STAR Voting concepts folder](01_Learn/README.md) · the curriculum: [CURRICULUM.md](../07_Concepts/CURRICULUM.md)
- **STAR vs other methods** (RCV-IRV, Approval, Score): [the method-comparisons folder](../method_comparisons/README.md)
- **Multi-winner STAR:** [Bloc STAR](../02_STAR_Bloc/README.md) · [Proportional STAR](../03_STAR_PR/README.md)
- **Conversation scripts** (Larry ↔ Adam): [What's so good about STAR](01_Learn/reference/whats_so_good_about_STAR_Voting.md) · [full index](../07_Concepts/about_this_repo/conversation_scripts.md)

# file: README.md
