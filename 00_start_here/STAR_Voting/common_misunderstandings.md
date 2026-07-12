# Common misunderstandings about STAR Voting

*STAR is simple, but a handful of things trip almost everyone up on first hearing. Here are the honest, plain-language answers to the gut reactions — the ones that start with "wait, but isn't it…". (For the step-by-step mechanics, see the [FAQ](STAR_FAQ.md); this page is for the doubts.)*

**Level: 101.**

## About filling out the ballot

**"Do I have to rate every candidate?"**
No. Score the ones you have an opinion about; leave the rest blank (a blank counts as **0**). Rating only your favorite (a "bullet vote") is perfectly valid — you're just choosing not to weigh in on the others. → [ways to fill out the ballot](STAR_ballot_voting_styles.md)

**"Can I give two candidates the same score?"**
Yes — and this is a real advantage over ranking. If you honestly like two candidates equally, score them both a 5 (or both a 2). You're **never forced to invent a preference** you don't feel. → [Equal Support](are_equal_score_votes_discounted.md)

**"Isn't giving someone a 0 throwing my vote away?"**
No. A 0 is a real, expressed score — "I do not support this candidate" — not a non-vote. And because you score everyone *independently*, supporting your favorite never helps your worst choice. You literally **cannot split your own vote**. → [no "wasted" votes](../wasted_votes.md)

## About how it's counted

**"Isn't STAR just averaging the scores?"**
No — and this is the single most important thing to get. If STAR just added up (or averaged) scores, a bland candidate everyone rates a mild 3 could beat a candidate a *majority* rates 5. STAR adds the **automatic runoff**: after the scores pick the top two, it asks "**which of these two do more voters actually prefer?**" That majority check is exactly what an average can't do — it's why STAR elects the majority's choice, not the highest arithmetic mean. → [why two rounds](STAR_Automatic_Runoff.md)

**"Is the runoff a second trip to the polls / a runoff election?"**
No. The "runoff" is **automatic** — it's computed from the same ballots you already cast, in the same count, in seconds. You vote once. (That's the "**A**" in ST**A**R: *Automatic* Runoff.) → [the Automatic Runoff](STAR_Automatic_Runoff.md)

**"So a candidate everyone rates a middling 3 wins?"**
Only if no one is genuinely preferred over them. If a majority rates candidate A a 5 and the "safe" candidate B a 3, A and B may both reach the runoff — and then A wins, because more voters prefer A head-to-head. The runoff is precisely what stops a forgettable compromise from beating a majority favorite. → [runoff reversal](../../01_STAR/runoff_overturns_leader/)

## About strategy ("won't people game it?")

**"Won't everyone just vote all 5s and 0s?"**
The runoff removes the *reward* for that. In a pure score/average system, min-maxing (all 5s and 0s) is the winning move, so everyone does it. Under STAR, the final winner is decided by simple preference between the top two, so your honest in-between scores (a 3, a 4) still do real work — and **exaggerating doesn't pay**. Simulations find STAR the most **strategy-resistant** of the common methods (honest voting is about as likely to help as to hurt). And the worst case is mild: if voters *did* all bullet-vote, STAR just behaves like [Approval voting](../Approval_Voting/approval_voting.md) — still a good method, not a broken one. → [strategic voting](../strategic_voting.md)

**"My favorite can't win — should I score my realistic choice a 5 instead?"**
No need. You can safely give your **true favorite a 5** *and* your realistic backup a **4**. Supporting your favorite can't hurt your backup, and supporting your backup can't hurt your favorite reaching the runoff. You almost never have to [betray your favorite](favorite_betrayal_voting_301.md) — a trap that "pick one" and even RCV can force on you.

**"If I give my 2nd choice a 4, could that make them beat my 1st choice?"**
Almost never. In the runoff, your ballot backs whichever of the two finalists you scored *higher* — so if your favorite (5) and backup (4) are the two finalists, your vote goes to your favorite. Scoring the backup a 4 only helps them beat *other* candidates. (The honest caveat: in rare, constructed cases STAR can fail this "later-no-harm" guarantee — see [honest limits](STAR_honest_limits.md) — but for how you'd actually vote, score your real preferences.)

## About the bigger picture

**"Isn't this the same as ranked-choice voting (RCV)?"**
No. RCV uses a **ranked** ballot (1st, 2nd, 3rd) counted by elimination; STAR uses a **scored** ballot (0–5) with a runoff. Different ballot, different count, different behavior — STAR isn't [instant-runoff voting](../RCV_IRV/RCV-IRV-Hare.md). → [scores vs. ranks](../scores_and_ranks/scores_vs_ranks.md)

**"Scoring is for restaurants and movies — is it serious enough for elections?"**
Rating 0–5 is a *more* expressive, not less serious, way to say what you think — it captures both *who* you prefer and *how strongly*, which "pick one" throws away. It's the same intuition you already use everywhere; STAR just adds the runoff to make it a fair election method.

**"Isn't it too complicated?"**
To vote: score some candidates 0–5 — done. To count: add the columns, take the top two, count which is preferred. It's two steps of grade-school arithmetic, and it's **[hand-countable](count_star_by_hand.md)** — genuinely *simpler* to tally than RCV, which needs round-by-round central counting.

## Still have a doubt?

- The mechanics in detail, with worked examples: [STAR FAQ](STAR_FAQ.md) · [the second round, FAQ](STAR_second_round_FAQ.md)
- The honest weaknesses, stated plainly (no method is perfect): [STAR's honest limits](STAR_honest_limits.md)
- Start from the top: [STAR — start here](STAR_start_here.md) · try it: [count one by hand](count_star_by_hand.md) or run a poll at [bettervoting.com](https://bettervoting.com)
