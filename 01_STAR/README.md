# 01_STAR — single-winner STAR Voting

The library's headline method: **STAR** (Score Then Automatic Runoff) for one seat. You score every candidate **0–5**; the two highest-scoring candidates become finalists, and an **automatic runoff** gives each ballot's full vote to whichever finalist it scored higher. Two rounds, one ballot.

This folder is the **runnable examples** — tiny elections you can tabulate yourself, each isolating one idea. The *concept* explanations live next door in the [STAR Voting concepts folder](../00_start_here/STAR_Voting/README.md). New to STAR? Read those first:

- **[STAR — start here](../00_start_here/STAR_Voting/STAR_start_here.md)** — the "why" before the "how."
- **[The benefits of STAR](../00_start_here/STAR_Voting/getting_started/STAR_benefits.md)** — the case for it, in brief.
- **[The second round — FAQ](../00_start_here/STAR_Voting/the_count/STAR_second_round_FAQ.md)** — what the automatic runoff does, and the objections answered honestly.

---

## The learning path

Follow the examples roughly in this order. The levels (101 → 201 → 301) match the authoritative **[curriculum](../00_start_here/CURRICULUM.md)** — start there for the full sequence with pacing notes.

### Voting 101 — the basics (the ballot, the two rounds, the spoiler)

1. **The ballot and the two rounds.** Five coworkers, three lunches — the compromise everyone likes wins, shown on real BetterVoting results → [the team-lunch example](_main/_main_pages/bv2184_fyy886_lunch_vote.md). *(The running example paired with [STAR — start here](../00_start_here/STAR_Voting/STAR_start_here.md).)*
2. **The broad compromise, again.** A second three-candidate case to make the pattern stick → [three candidates](_main/_main_pages/02a_c3_b1_three-candidates.md).
3. **How you're allowed to vote.** Bullet votes, equal scores, low-score "protest" ballots, the eight-style gallery → [ballot styles](_main/_main_pages/03a_c3_b3_style-bullet-vote.md).
4. **The headline lesson — top scorer ≠ winner.** STAR's single most important behavior, as a 3→9-candidate progression with a control case → **[Runoff Reversal](runoff_overturns_leader/)**.
5. **The spoiler, in numbers.** Vote-splitting and the compromise winner → [the vote-splitting scenarios](_main/) · cross-method: [the split-voting set](../method_comparisons/split_voting/).

### Voting 201 — reading results & trusting the count

6. **Read the full audit report.** The minimal on-screen report vs the complete `_tabulated.txt` (preference matrix + score distribution + the runoff/Condorcet blocks) → the `_tabulated/` siblings in [Runoff Reversal](runoff_overturns_leader/).
7. **A real election, end to end.** A real 461-ballot BetterVoting STAR race, raw ballots → winner, read section by section → **["What Makes the Best Pet?"](pet_real_bv_election/)**.
8. **Edge cases & trust.** How ties resolve, and where BetterVoting's display diverges from the engine → [Flat scores, ties & tie-breaking](Flat_scores_ties/) · [abstain / blank / zero handling](abstain_bugs/).

### Voting 301 — criteria & edge behavior

9. **The Majority Criterion** (and the "relaxed" version) → [the two 5-voter elections](majority_criterion/).
10. **The "dead rung"** — when STAR's five-star tiebreaker can't fire and the tie falls to the lot → [the dead-rung case](tie_break_dead_rung/).
11. **None of the Above** — a protest electorate where NOTA actually wins → [the NOTA election](none_of_the_above/).
12. **The honest limits & the reversal debate** → [STAR's honest limits](../00_start_here/STAR_Voting/properties_and_limits/STAR_honest_limits.md) · [the second-round FAQ](../00_start_here/STAR_Voting/the_count/STAR_second_round_FAQ.md).
13. **Practice — predict, then peek.** Fourteen worked problems with hidden, tested solutions — reading drills, criteria probes (consistency, participation, later-no-harm), strategy gambles, the real 1994 Olympics ballots, a Ranked Robin cycle, build-your-own constructions, a multi-winner wing (Bloc vs proportional, STV transfers), and Approval's threshold dilemma → **[the exercises set](exercises/README.md)**.

---

## Every example set in this folder

| Set | Level | What it teaches |
|---|:---:|---|
| [The teaching progression](_main/) | 101 | The core sequence: the team-lunch example → three candidates → ballot styles → abstentions → quorum → vote-splitting → display options (one idea at a time). |
| [Runoff Reversal — top scorer ≠ winner](runoff_overturns_leader/) | 101→301 | Real BetterVoting elections where the runoff **confirms** or **overturns** the score leader — STAR's headline lesson, plus the convincing-vs-jarring reversal pair. |
| ["What Makes the Best Pet?"](pet_real_bv_election/) | 201 | A real 461-ballot BV race imported and reconciled line by line — the whole pipeline, raw ballots to winner. |
| [Flat scores, ties & tie-breaking](Flat_scores_ties/) | 201 | Flat/tied scores meet the tiebreak cascade meet reporting — two-view cases exposing one tie behavior each (and BV bugs). |
| [Abstain, blank & zero handling](abstain_bugs/) | 201 | BetterVoting's abstain/blank/zero handling reproduced and cross-checked — the "0 tallied votes yet a winner" divergence. |
| [The Majority Criterion](majority_criterion/) | 301 | Two 5-voter elections isolating STAR's Majority-Criterion behavior (and the Relaxed Majority Criterion). |
| [The dead rung — when the tiebreak can't fire](tie_break_dead_rung/) | 301 | The "dead rung": when no tied candidate holds a 5, the five-star tiebreak reads 0–0 and the lot decides. |
| [None of the Above](none_of_the_above/) | 301 | BV215 — a protest election where None of the Above tops the scores and wins the runoff. |
| [Exercises — predict, then peek](exercises/README.md) | 201→301 | Fourteen worked problems with collapsible solutions: district consistency, the tenth-ballot participation paradox, five-verdicts-one-electorate, the 1994 Olympics ballots, center squeeze, bullet-vote backfire, the Equal Support reading drill, build-your-own reversal, a Ranked Robin cycle ladder, later-no-harm both ways, recruit-a-spoiler, Bloc-vs-proportional seats, the Approval threshold dilemma, and the STV transfer machine. |

*Parked, not on the learning path: [two-candidate STAR](silly_two_cand_STAR/) — deliberately-trivial two-candidate cases. With only two candidates the runoff just echoes the scores, so there's nothing distinctive to learn; kept for completeness and as engine test fixtures.*

---

## Run a file yourself

From the engine directory:

```
python starvote_larry_hastings.py "01_STAR/_main/02a_c3_b1_three-candidates.yaml"
```

Every file writes a full audit report to its `_tabulated.txt` sibling — watch for the **[Runoff Reversal]** block, which prints whenever the score leader and the runoff winner differ.

## Related

- **Concept docs:** [the STAR Voting concepts folder](../00_start_here/STAR_Voting/README.md) · the curriculum: [CURRICULUM.md](../00_start_here/CURRICULUM.md)
- **STAR vs other methods** (RCV-IRV, Approval, Score): [the method-comparisons folder](../method_comparisons/)
- **Multi-winner STAR:** [Bloc STAR](../02_STAR_Bloc/) · [Proportional STAR](../03_STAR_PR/)
- **Conversation scripts** (Larry ↔ Adam): [What's so good about STAR](../00_start_here/STAR_Voting/reference/whats_so_good_about_STAR_Voting.md) · [Why do you love STAR](../00_start_here/STAR_Voting/reference/why_do_you_love_STAR_Voting.md) · [full index](../00_start_here/about_this_repo/conversation_scripts.md)

# file: README.md
