# STAR-PR — a voter's FAQ

*You are at the kitchen table with a sample ballot: a grid of names and stars, three seats to fill. You are not wondering about algorithms. You are wondering whether your vote counts and what happens to it. These are those questions.*

**Level: 101 · for voters**

→ the shorter conceptual answer: [Proportional to *what*?](proportional_to_what.md) · the method itself: [STAR-PR](STAR_PR/README.md) · the same ballots counted majoritarian instead: [Bloc STAR vs Proportional STAR](../../method_comparisons/bloc_vs_pr/README.md)

---

## "If I just give people 0 to 5 stars, how do we get 3 winners?"

The count runs in **rounds**, one per seat.

1. Add up all the stars. The highest total wins the **first seat**.
2. That winner's strongest supporters are marked **represented** — enough of them to fill one seat's worth, and no more.
3. Count again *without* those voters. The new highest total wins the **second seat**.
4. Repeat until the seats are full.

That's it. The ballot never changes; you fill it in once. The count just keeps asking "who do the people who *don't have anyone yet* want?"

## "Do I have to score everyone?"

No. Score as many or as few as you like.

- **A blank counts as zero.** It does not spoil your ballot and it cannot invalidate anything.
- You can give the **same score to several candidates** — that says "I don't have a preference between these", which is a real and useful thing to say.
- There is no "pick up to three" rule even though three seats are up. Nothing is rationed. See [the ballot](../../02_STAR_Bloc/01_Learn/bloc_star_ballot.md) for why that line matters.

One thing worth knowing: a blank means *zero*, not *no opinion*. If you have genuinely never heard of a candidate, scoring them in the middle says that more accurately than leaving them blank does — [the long version](../../01_STAR/01_Learn/properties_and_limits/abstention_vs_zero_vs_nota.md).

## "How can it be proportional if I'm scoring individuals, not a party?"

Because the system builds the "party" out of your ballot, on the fly.

You never join anything. But if two hundred people all gave five stars to the same candidate, that is a group — it just never registered, never named itself, and may not know it exists. The count finds those groups in the scores and gives each one that is big enough a seat.

Which means the groups can be anything the electorate actually cares about: an ideological camp, a neighbourhood, everyone worried about one specific issue. [The full answer](proportional_to_what.md).

## "What is Bloc STAR, and why is it different?"

Bloc STAR fills every seat the way single-winner STAR fills one: highest scorers become finalists, and the finalist **more voters prefer** wins the seat. Then it removes that winner and does the whole thing again — **with everybody's ballot still at full strength**.

That last part is the difference. If 51% of town likes the same three people, that 51% decides all three seats and the other 49% elects nobody. STAR-PR prevents that by setting aside each winner's supporters before the next seat is decided.

> **Careful with a common shortcut:** Bloc STAR is *not* "the top 3 by points". Every seat ends in a runoff, so the candidate with the most stars can lose — and in a real 100-voter election in this library, the top scorer wins [no seat at all](../../02_STAR_Bloc/01_Learn/score_leader_no_seat.md), losing all four runoffs 51–49.

## "Then why would anyone use Bloc STAR?"

Because sometimes a sweep is the right answer.

If you are electing officers who must govern as a unit, or at-large positions where you want the people **most voters** actually prefer, a majoritarian result is what you want — you are not trying to seat the opposition, you are trying to find broad agreement. Bloc STAR is for that.

Proportional STAR is for bodies meant to *represent* rather than to agree: councils, boards, anything where a minority viewpoint having a voice is the point. [The fork, in plain language](../../07_Concepts/topics/electing_more_than_one.md).

## "My favourite won — and now my ballot is 'spent'. Am I being punished?"

No. You got what you came for. It is less like a penalty and more like **spending a budget**, or **taking turns**.

The framing that helps: **a seat costs a certain number of voters.** Three seats and thirty voters means one seat costs ten. When your candidate wins, ten voters "paid" for that seat — and if you were one of them, you have already been served. Your neighbour hasn't. The next seat is theirs to decide.

Three ways of seeing why it *has* to work like this:

- **It stops a monopoly.** If 51% of town gives five stars to the same three people and their ballots stayed at full strength, that 51% would simply out-vote everyone again for the second seat, and again for the third. They would take everything. That is not a hypothetical — it is exactly what [Bloc STAR](../../method_comparisons/bloc_vs_pr/README.md) does, on purpose, for the elections where a sweep is the right answer.
- **It is turn-taking.** Once a group has its representative, the count says: *fine — now let the people who still have nobody use their full weight.*
- **It is the engine of proportionality itself.** Without it, "proportional" would be a label with no mechanism behind it.

**One precision worth having, because the loose version misleads.** People often say "your ballot loses some of its power." Under [Allocated Score](STAR_PR/README.md) — the method meant by Proportional STAR — that is not quite it. A quota's worth of supporters is spent from the top score group down, so most spent ballots are used **completely**, and ballots the quota never reaches keep **100%** even if they scored the winner five stars. A *fraction* is kept only by the score group sitting on the quota boundary. ("Weight reduced a little for everyone who supported the winner" describes [Reweighted Range Voting](STAR_PR/README.md), a different member of the family.)

And one honest caveat on the arithmetic: proportionality is approximate, not exact. A group that is 60% of voters does not get exactly 60% of the seats, because seats do not divide that finely — in [the worked example](../../method_comparisons/bloc_vs_pr/README.md#the-same-thing-at-readable-scale-left-centre-right), 60% of voters take two seats of three, which is 67%. The guarantee is that a group large enough to reach a quota can claim a seat, not that every group's share lands on the nose. [Why exact proportionality almost never happens](what_proportional_means.md).

Either way, you are not losing power you should have kept. You are declining to spend it twice.

## "If my candidate wins in a landslide, is my vote wasted?"

No, and this is the case where the fine print works in your favour.

Suppose a seat costs 1,000 voters and your candidate got 5,000 five-star supporters. The count doesn't spend all 5,000 — it needs 1,000. Since everyone in that group scored the winner identically, it takes **one fifth of each of their ballots** and hands the rest back.

So you keep 80% of your voting power for the next seat. That is the [fractional surplus handling](STAR_PR/README.md) step, and its whole purpose is that voters who supported a winner *equally* are treated *equally* — nobody gets fully spent while an identical ballot next to them walks away untouched.

## "If I give my second favourite 4 stars, could that spend my ballot? Should I just bullet vote?"

The honest answer: **the pull toward bullet voting is real but weak, and this deserves testing rather than reassurance.**

Here is what is actually true. To be spent, the count has to reach *your* score group while filling the quota — supporters are taken from the top down, 5-star group first, then 4-star, and so on. A big winner never gets that far. And a backup you scored 4 can only "cost" you anything by *winning a seat*, which is the outcome you wanted when you scored them 4.

What you give up by bullet voting is concrete and immediate: your ballot then says nothing about which of the remaining candidates you'd prefer, in every round after the first. That is a certain loss traded against a speculative one.

Where honesty ends and this becomes an open question: whether a sophisticated voter could gain on average is one of the items on the [STAR-PR committee's own research list](what_proportional_means.md), not a settled result. Anyone telling you it is definitely strategy-proof is overclaiming.

## "Who does this math? Can I check it?"

This is the weakest point of proportional methods generally, and it deserves a straight answer.

STAR-PR is **not batch-summable**. Precincts cannot each report a total that gets added up, because deciding who is "represented" depends on individual ballots. The counting has to happen centrally, on the full ballot set.

What you *can* do: the rules are fully specified and deterministic, so given the ballots anyone can re-run the count and get the same answer — with different software, or by hand for a small election. That is why this library publishes the ballots alongside every result, and cross-checks its engine against independent implementations. It is verifiability by *reproduction* rather than by precinct arithmetic.

It is also a genuine argument for smaller districts: fewer ballots per count is easier to audit. [The honest cost list](STAR_PR/README.md).

## "If my favourite loses, does my 3-star vote for someone else actually matter?"

Yes — and this is where scores earn their keep.

Your 3 counts toward that candidate's total in **every round your ballot is still live**. Candidates who are nobody's favourite but lots of people's acceptable choice get elected on exactly this kind of support. In [the worked example](../../method_comparisons/bloc_vs_pr/README.md#the-same-thing-at-readable-scale-left-centre-right), a centre candidate wins a seat with only two voters in their own camp — because voters on both sides scored them 1s and 2s, and those added up.

Under a choose-one ballot, that candidate gets nothing and those voters are invisible. The 3 you were unsure about is precisely the mark a scored ballot can hear.

## See also

- [Proportional to *what*?](proportional_to_what.md) — the conceptual version of question 3
- [Bloc STAR vs Proportional STAR](../../method_comparisons/bloc_vs_pr/README.md) — the same ballots, two councils, starting from two voters
- [STAR-PR — the three methods](STAR_PR/README.md) — how `allocated`, `sss` and `rrv` differ
- [What "proportional" actually means](what_proportional_means.md) — the 201/301 version, including what it does *not* promise
- [The STAR ballot](../../01_STAR/01_Learn/voting_styles/README.md) — every legal way to fill one in
