# The spoiler effect

*A **spoiler** is a candidate who can't win but still changes who does — by splitting
another candidate's support. It's the single most-felt flaw of choose-one voting, the
reason "don't waste your vote on a third party" is common advice, and the problem every
reform on this site is partly trying to fix.*

→ Glossary: [`spoiler effect`](GLOSSARY.md) · the root cause:
[vote splitting & the equally-weighted vote](STAR_Voting/equally_weighted_vote.md) ·
runnable demos: [the split-voting set](../method_comparisons/split_voting/README_split_voting.md)

---

## What it is

You have three candidates: two similar ones (say two progressives) and one different
(a conservative). Most voters prefer *either* progressive to the conservative — but
choose-one forces each voter to pick **exactly one**. The two progressives **divide**
their shared supporters, so neither reaches the top, and the conservative wins with a
minority. The weaker progressive was the **spoiler**: they couldn't win, but their
presence flipped the result.

Nothing about the electorate's actual preferences changed — only the ballot's refusal
to let a voter support more than one candidate. That's why the spoiler effect is a
property of the **counting rule**, not of voters being fickle.

## The root cause: one mark

The spoiler comes from **vote splitting** — similar candidates sharing one pool of
supporters who are each allowed only one mark. Fix the ballot so a voter can back
several candidates at once, or express *degree* of support, and the forced split goes
away. This is the same root the [equally-weighted-vote](STAR_Voting/equally_weighted_vote.md)
argument starts from.

## How each method handles it

| Method | Spoiler behavior |
|---|---|
| **Choose-One / Plurality** | Full spoiler effect — the classic case above. |
| **[RCV-IRV](RCV_IRV/RCV-IRV-Hare.md)** | Reduces the *classic* spoiler: a trailing similar candidate is eliminated and their ballots transfer, instead of splitting the vote outright. But elimination on first-choices creates its **own** failure — [center squeeze](RCV_IRV/RCV_IRV_center_squeeze.md) — and can still spoil in some configurations. |
| **[Approval](Approval_Voting/approval_voting.md)** | Approve *both* similar candidates — they no longer split, since a supporter can back all of them. |
| **[Score / Range](Range_Voting/range_voting.md), [STAR](STAR_Voting/STAR_start_here.md)** | Score each candidate independently, so running an ally doesn't bleed your support. STAR adds a majoritarian runoff on top. |

## Spoiler ≠ center squeeze

These get conflated, but they're different failures:

- **Vote splitting / spoiler** — *similar* candidates share one pool of supporters (the
  progressives above). The fix is letting voters support more than one.
- **[Center squeeze](RCV_IRV/RCV_IRV_center_squeeze.md)** — a *distinct* moderate,
  liked by both sides, is eliminated by RCV-IRV for too few **first** choices even
  though they'd beat each rival head-to-head. The voters here are *different*, not
  shared. This one is IRV-specific.

## Does STAR fully escape it?

Almost. STAR removes the *forced* split, but a **narrow, self-inflicted residual**
survives in the top-two runoff — a faction can still split itself if it refuses to use
the score ballot honestly. That edge case (and why it's minor) is
[STAR's residual vote-splitting](STAR_Voting/residual_vote_splitting.md).

## See it happen

- [The split-voting set](../method_comparisons/split_voting/README_split_voting.md) — the
  spoiler progression from plurality through each reform, on the same ballots.
- [Star Wars vote split](../method_comparisons/split_voting/_main/_main_pages/04_star_wars_vote_split.md)
  — a compact worked example (Skywalker & Leia split the Rebel vote).
- [Plurality vs. majority](../method_comparisons/split_voting/_main/_main_pages/00_plurality_vs_majority.md)
  — where the minority winner comes from.
- Debate framing: [what's so good about STAR — Segment 1](../interviews_conversations/whats_so_good_about_STAR_Voting.md)

# file: spoiler_effect.md
