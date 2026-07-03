# The spoiler effect

*A **spoiler** is a candidate who can't win but still changes who does — by splitting
another candidate's support. It's the single most-felt flaw of choose-one voting, the
reason "don't waste your vote on a third party" is common advice, and the problem every
reform on this site is partly trying to fix.*

→ Glossary: [`spoiler effect`](GLOSSARY.md) · the root cause:
[vote splitting & the equally-weighted vote](STAR_Voting/equally_weighted_vote.md) ·
runnable demos: [the split-voting set](../method_comparisons/split_voting/README.md)

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
| **[Choose-One / Plurality](plurality.md)** | Full spoiler effect — the classic case above. |
| **[RCV-IRV](RCV_IRV/RCV-IRV-Hare.md)** | Reduces the *classic* spoiler: a trailing similar candidate is eliminated and their ballots transfer, instead of splitting the vote outright. But elimination on first-choices creates its **own** failure — [center squeeze](RCV_IRV/RCV_IRV_center_squeeze.md) — and can still spoil in some configurations. |
| **[Ranked Robin / RCV-RR](RCV_Ranked_Robin/ranked_robin.md)** | Reads the whole ballot and elects the head-to-head (Condorcet) winner — no elimination rounds, so no vote splitting or center squeeze. Only a rare **Condorcet cycle** can produce a spoiler. |
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

## How social choice theory frames it

A method is **spoilerproof** when it satisfies **Independence of Irrelevant
Alternatives (IIA)**: whether the winner is A or B should not depend on some losing
third candidate C. Sidney Morgenbesser's joke captures the principle — a diner picks
apple pie over blueberry and cherry; told the cherry is sold out, he says "in that
case I'll have the blueberry." Condorcet was the first to study the spoiler effect, in
the 1780s.

Susceptibility depends heavily on the method (Wikipedia's summary):

| Electoral system | Spoiler effect |
|---|:--:|
| [Plurality](plurality.md) | **High** |
| Runoffs / [RCV-IRV](RCV_IRV/RCV-IRV-Hare.md) | **Medium** |
| Condorcet methods ([Ranked Robin / RCV-RR](RCV_Ranked_Robin/ranked_robin.md), Schulze, Ranked Pairs) | **Low** (only in a cyclic tie) |
| Score / median ([Approval](Approval_Voting/approval_voting.md), [Score](Range_Voting/range_voting.md), [STAR](STAR_Voting/STAR_start_here.md)) | **None** (on an absolute scale) |

Two theorems sit under this. **Arrow's impossibility theorem** shows no *ranked*
method can fully escape spoilers; **rated** methods aren't subject to Arrow, so they
*can* be spoilerproof — with one caveat: only if voters score on an **absolute** scale.
If voters rescale their scores around who's running (a *relative* scale), a spoiler can
reappear — which is exactly STAR's [narrow residual](STAR_Voting/residual_vote_splitting.md).

Methods that fail IIA can be gamed by **strategic nomination**. The Borda count has a
severe *entry* incentive — a faction can "clone their way to victory" by running many
candidates, which made Borda himself concede "my system is meant only for honest men."
Plurality has the opposite, an *exit* incentive: similar candidates get pressured to
drop out or merge so they don't split the vote. (Theory suggests **90–99% of real
elections have a Condorcet winner**, so cyclic-tie spoilers are rare; the first
Condorcet cycle found in a ranked US election was in 2021.)

## The rhetoric: "a vote for X is a vote for Y"

The spoiler effect has its own political vocabulary, all of it aimed at pressuring
voters not to "split the vote": **"a vote for X is a vote for Y."** The line recurs
across decades — "a vote for Perot is a vote for Clinton" (1992); Al Gore's campaign on
"a vote for Nader is a vote for Bush" (2000, and again in 2004); "a vote for Cruz is a
vote for Trump" in the 2016 GOP primary; and a 2024 Democratic ad branding Jill Stein a
spoiler for Trump. This is **lesser-evil / strategic-voting** pressure — the human cost
of a spoiler-prone ballot — and defusing it is much of the point of reform: on an
Approval, Score, or STAR ballot you can honestly support your favorite *and* a viable
compromise, so "a vote for X is a vote for Y" stops being true.

## A real IRV spoiler — Burlington 2009

The 2009 Burlington, Vermont mayoral election (run by RCV-IRV) is the textbook proof
that instant runoff does **not** remove spoilers. **Andy Montroll was the Condorcet
winner** — he beat every other candidate head-to-head — but he was eliminated in an
early round for too few first choices. Republican **Kurt Wright** acted as the spoiler,
and the seat went to **Bob Kiss**, even though most voters preferred Montroll to Kiss.
That's a [center-squeeze](RCV_IRV/RCV_IRV_center_squeeze.md) spoiler, and it's why IRV
rates "Medium," not "None," in the table above.

The most prominent recent example is **[Alaska's 2022 U.S. House special election](RCV_IRV/RCV_IRV_alaska_2022.md)**,
where RCV-IRV eliminated the Condorcet winner (Begich), a losing candidate (Palin)
spoiled the result, and the outcome was even non-monotonic — three IRV pathologies in
one real federal race.

## See it happen

- [The split-voting set](../method_comparisons/split_voting/README.md) — the
  spoiler progression from plurality through each reform, on the same ballots.
- [Star Wars vote split](../method_comparisons/split_voting/_main/_main_pages/04_star_wars_vote_split.md)
  — a compact worked example (Skywalker & Leia split the Rebel vote).
- [Plurality vs. majority](../method_comparisons/split_voting/_main/_main_pages/00_plurality_vs_majority.md)
  — where the minority winner comes from.
- Debate framing: [what's so good about STAR — Segment 1](STAR_Voting/whats_so_good_about_STAR_Voting.md)

Sources: [Spoiler effect — Wikipedia](https://en.wikipedia.org/wiki/Spoiler_effect),
[Spoiler effect rhetoric — Wikipedia](https://en.wikipedia.org/wiki/Spoiler_effect_rhetoric),
[Independence of irrelevant alternatives — Wikipedia](https://en.wikipedia.org/wiki/Independence_of_irrelevant_alternatives),
[2009 Burlington mayoral election — Wikipedia](https://en.wikipedia.org/wiki/2009_Burlington_mayoral_election)

# file: spoiler_effect.md
