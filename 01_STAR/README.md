# 01_STAR — single-winner STAR Voting

The library's headline method: **STAR** (Score Then Automatic Runoff) for one seat. You score every candidate **0–5**; the two highest-scoring candidates become finalists, and an **automatic runoff** gives each ballot's full vote to whichever finalist it scored higher. Two rounds, one ballot.

This folder is the **runnable examples** — tiny elections you can tabulate yourself, each isolating one idea. The *concept* explanations live next door in [`00_start_here/STAR_Voting/`](../00_start_here/STAR_Voting/). New to STAR? Read those first:

- **[STAR — start here](../00_start_here/STAR_Voting/STAR_start_here.md)** — the "why" before the "how."
- **[The benefits of STAR](../00_start_here/STAR_Voting/STAR_benefits.md)** — the case for it, in brief.
- **[The second round — FAQ](../00_start_here/STAR_Voting/STAR_second_round_FAQ.md)** — what the automatic runoff does, and the objections answered honestly.

---

## The learning path

Follow the examples roughly in this order. The levels (101 → 201 → 301) match the authoritative **[curriculum](../00_start_here/CURRICULUM.md)** — start there for the full sequence with pacing notes.

### Voting 101 — the basics (the ballot, the two rounds, the spoiler)

1. **Mechanics, two candidates.** Watch the two rounds turn with nothing surprising competing for attention → [`_main` · simplest example](_main/_main_pages/01a_c2_b1_two-candidates.md). *(With only two candidates STAR agrees with ordinary voting — that's the point of starting here.)*
2. **Add a third candidate — why it matters.** The winner becomes the broad compromise → [`_main` · three candidates](_main/_main_pages/02a_c3_b1_three-candidates.md).
3. **How you're allowed to vote.** Bullet votes, equal scores, low-score "protest" ballots, the eight-style gallery → [`_main` · ballot styles](_main/_main_pages/03a_c3_b3_style-bullet-vote.md).
4. **The headline lesson — top scorer ≠ winner.** STAR's single most important behavior, as a 3→9-candidate progression with a control case → **[Runoff Reversal](runoff_overturns_leader/)**.
5. **The spoiler, in numbers.** Vote-splitting and the compromise winner → [`_main` vote-splitting scenarios](_main/) · cross-method: [the split-voting set](../method_comparisons/split_voting/).

### Voting 201 — reading results & trusting the count

6. **Read the full audit report.** The minimal on-screen report vs the complete `_tabulated.txt` (preference matrix + score distribution + the runoff/Condorcet blocks) → the `_tabulated/` siblings in [Runoff Reversal](runoff_overturns_leader/).
7. **A real election, end to end.** A real 461-ballot BetterVoting STAR race, raw ballots → winner, read section by section → **["What Makes the Best Pet?"](pet_real_bv_election/)**.
8. **Edge cases & trust.** How ties resolve, and where BetterVoting's display diverges from the engine → [Flat scores, ties & tie-breaking](Flat_scores_ties/) · [abstain / blank / zero handling](abstain_bugs/).

### Voting 301 — criteria & edge behavior

9. **The Majority Criterion** (and the "relaxed" version) → [majority_criterion](majority_criterion/).
10. **The "dead rung"** — when STAR's five-star tiebreaker can't fire and the tie falls to the lot → [tie_break_dead_rung](tie_break_dead_rung/).
11. **None of the Above** — a protest electorate where NOTA actually wins → [none_of_the_above](none_of_the_above/).
12. **The honest limits & the reversal debate** → [STAR's honest limits](../00_start_here/STAR_Voting/STAR_honest_limits.md) · [the second-round FAQ](../00_start_here/STAR_Voting/STAR_second_round_FAQ.md).

---

## Every example set in this folder

| Set | Level | What it teaches |
|---|:---:|---|
| [`_main` — the teaching progression](_main/) | 101 | The core sequence: two-candidate intros → third candidate → ballot styles → abstentions → quorum → vote-splitting → display options (28 files, one idea at a time). |
| [Runoff Reversal — top scorer ≠ winner](runoff_overturns_leader/) | 101→301 | Real BetterVoting elections where the runoff **confirms** or **overturns** the score leader — STAR's headline lesson, plus the convincing-vs-jarring reversal pair. |
| ["What Makes the Best Pet?"](pet_real_bv_election/) | 201 | A real 461-ballot BV race imported and reconciled line by line — the whole pipeline, raw ballots to winner. |
| [Flat scores, ties & tie-breaking](Flat_scores_ties/) | 201 | Flat/tied scores meet the tiebreak cascade meet reporting — two-view cases exposing one tie behavior each (and BV bugs). |
| [abstain_bugs](abstain_bugs/) | 201 | BetterVoting's abstain/blank/zero handling reproduced and cross-checked — the "0 tallied votes yet a winner" divergence. |
| [majority_criterion](majority_criterion/) | 301 | Two 5-voter elections isolating STAR's Majority-Criterion behavior (and the Relaxed Majority Criterion). |
| [tie_break_dead_rung](tie_break_dead_rung/) | 301 | The "dead rung": when no tied candidate holds a 5, the five-star tiebreak reads 0–0 and the lot decides. |
| [none_of_the_above](none_of_the_above/) | 301 | BV215 — a protest election where None of the Above tops the scores and wins the runoff. |

---

## Run a file yourself

From the engine directory:

```
python starvote_larry_hastings.py "01_STAR/_main/02a_c3_b1_three-candidates.yaml"
```

Every file writes a full audit report to its `_tabulated.txt` sibling — watch for the **[Runoff Reversal]** block, which prints whenever the score leader and the runoff winner differ.

## Related

- **Concept docs:** [`00_start_here/STAR_Voting/`](../00_start_here/STAR_Voting/) · the curriculum: [CURRICULUM.md](../00_start_here/CURRICULUM.md)
- **STAR vs other methods** (RCV-IRV, Approval, Score): [`method_comparisons/`](../method_comparisons/)
- **Multi-winner STAR:** [Bloc STAR](../02_STAR_Bloc/) · [Proportional STAR](../03_STAR_PR/)
- **Conversation scripts** (Larry ↔ Adam): [What's so good about STAR](../00_start_here/STAR_Voting/whats_so_good_about_STAR_Voting.md) · [Why do you love STAR](../00_start_here/STAR_Voting/why_do_you_love_STAR_Voting.md) · [full index](../00_start_here/conversation_scripts.md)

# file: README.md
