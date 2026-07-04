# 01_STAR — single-winner STAR Voting

The library's headline method: **STAR** (Score Then Automatic Runoff) for one seat. Score every candidate 0–5; the two highest-scoring candidates go to an automatic runoff decided by which of the two each ballot prefers.

| Where | What |
|---|---|
| [01_STAR / _main — the STAR teaching progression](_main/) | the teaching progression — two-candidate intros, ballot styles, abstentions, quorum, vote-splitting scenarios, display options |
| [When the top-scoring candidate isn't the winner](runoff_overturns_leader/) | the Runoff Reversal set — real BetterVoting elections where the runoff confirms or overturns the score leader |
| [Flat scores, ties & tie-breaking — and the BetterVoting bugs](Flat_scores_ties/) | ties and flat-score edge cases, and how the tiebreakers resolve them |
| [A real BetterVoting election, end to end — "What Makes the Best Pet?"](pet_real_bv_election/) | a real 461-ballot BetterVoting race, imported and reconciled line by line |

Cross-method contrasts featuring STAR (vs RCV-IRV, Approval, Score) live in [`../method_comparisons/`](../method_comparisons). Multi-winner STAR: [`../02_STAR_Bloc/`](../02_STAR_Bloc) and [`../03_STAR_PR/`](../03_STAR_PR). Concept docs: [`../00_start_here/STAR_Voting/`](../00_start_here/STAR_Voting).

**Conversation scripts** (Larry ↔ Adam): [What's so good about STAR](../00_start_here/STAR_Voting/whats_so_good_about_STAR_Voting.md) · [Why do you love STAR](../00_start_here/STAR_Voting/why_do_you_love_STAR_Voting.md) · [Aren't equal-score votes discounted?](../00_start_here/STAR_Voting/are_equal_score_votes_discounted.md) · [Favorite betrayal](../00_start_here/STAR_Voting/favorite_betrayal_voting_301.md) — full index: [Conversation scripts — index](../00_start_here/conversation_scripts.md).

# file: README.md
