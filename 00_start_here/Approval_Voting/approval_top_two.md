# Approval + Top-Two — the runoff you have to come back for

*An Approval primary plus a head-to-head general between the two most-approved: a real, field-tested reform package — St. Louis runs on it — and the sharpest little lesson in ballot design, because the runoff **must** be a second election: re-counting the same 0/1 ballots head-to-head just returns the approval count. STAR is this exact package folded into one ballot.*

→ Overview: [**Approval Voting**](approval_voting.md) (how the primary round works). · Companions: [honest limits](approval_honest_limits.md) · [multi-winner Approval](approval_multiwinner.md). · Curriculum: [301.4](../CURRICULUM.md).

---

## The package

**Approval + Top-Two** is a two-round system. **Round 1** is a single nonpartisan Approval primary: every candidate on one ballot regardless of party, every voter marks approve / not-approve on each, and the **two most-approved** advance. **Round 2** is an ordinary head-to-head general election, decided by majority. It keeps the familiar structure of the classic [two-round runoff](https://en.wikipedia.org/wiki/Two-round_system) (a Choose-One round feeding a top-two round — Georgia's runoffs, French presidential elections) while fixing round 1's defect: with an Approval ballot, supporting your favorite never splits your vote against the compromise you'd accept.

Two real-world flagships:

- **St. Louis, Missouri** adopted it as [Proposition D](https://ballotpedia.org/St._Louis,_Missouri,_Proposition_D,_Approval_Voting_Initiative_%28November_2020%29) in November 2020 (68% yes) and has elected its mayor, comptroller, and aldermen with it since 2021.
- **Oregon's "Unified Primary"** — Mark and Jon Frohnmayer's proposal (drafted 2011, statewide petition 2014) to nominate by Approval into a top-two general ([Wikipedia](https://en.wikipedia.org/wiki/Unified_primary)). The initiative fell short of the ballot, but the campaign founded the Equal Vote Coalition — and the follow-up question, *"could the runoff ride along on the ballot itself?"*, became STAR. That lineage is the last section below.

## Why bolt a Top-Two onto Approval?

The runoff answers, head-on, the two biggest questions an approval count leaves open (both are in [honest limits](approval_honest_limits.md)):

1. **The majority check.** An approval total measures *breadth* — it can crown everyone's lukewarm second choice over a candidate a majority actively prefers (limits §4). The runoff puts the two broadest candidates in front of the whole electorate one-on-one, and the majority settles it.
2. **A lower-stakes approval line.** "Where do I draw my line?" is the one hard strategic call an Approval ballot forces (limits §2). A nominating round softens it: your approvals now choose the *finalists*, not the winner — whatever you decided at the margin, your full preference between the survivors still gets its own dedicated say in round 2.

## Why the runoff has to be a *second election*

Here's the instructive part. Suppose you tried to spare everyone the second trip by making the runoff **automatic** — advance the two most-approved, then re-count *the same approval ballots* head-to-head. Try it on the flagship Approval example, [`approval_101`](../../04_Approval/_main/_main_pages/approval_101_c3_b5.md) (5 voters, live on BetterVoting — [results ↗](https://bettervoting.com/ff6mk3/results)). The LH engine's report:

```text
--- Approval Voting (single winner) ---
 Tabulating 5 ballots (any non-zero score = approval).

Ballots:
   columns = Ann, Bob, Cal      (1 = approve; 0 / blank / marker = not approved)
   1,1,0
   0,1,1
   1,1,0
   0,1,0
   1,0,1

   Bob -- 4 (80%) -- Elected
   Ann -- 3 (60%)
   Cal -- 2 (40%)
```

Finalists: Bob and Ann. Now ask each ballot which finalist it prefers:

| Ballot | Approved | In a Bob-vs-Ann runoff it says… |
|---|---|---|
| voter 1 | Ann ● Bob ● | approved both — **Equal Support** |
| voter 2 | Bob ● Cal ● | **Bob** |
| voter 3 | Ann ● Bob ● | approved both — **Equal Support** |
| voter 4 | Bob ● | **Bob** |
| voter 5 | Ann ● Cal ● | **Ann** |

The "instant runoff" says **Bob 2, Ann 1** — a margin of one vote. The approval count said **Bob 4, Ann 3** — a margin of one vote. That's not a coincidence, and no cleverer example escapes it: every ballot that approved **both** finalists (or neither) lands in [Equal Support](../STAR_Voting/are_equal_score_votes_discounted.md), and what remains is exactly *approved-Bob-only* versus *approved-Ann-only* — which **is** the approval margin. An automatic top-two runoff computed from 0/1 ballots reproduces the approval result — same winner, same margin, every election. It adds nothing.

What the runoff needs is information the checkmark never recorded: *which of two approved candidates the voter actually prefers.* Line up one opinion in three ballot styles and the gap is visible — say voter 1's true feeling is "Ann all the way; Bob would be fine":

| Candidate | Choose-One | **Approval (voter 1's actual ballot)** | Score 0–5 |
|---|:--:|:--:|:--:|
| Ann | ● | ● | 5 |
| Bob | ○ | ● | 3 |
| Cal | ○ | ○ | 0 |

The approval ballot records Ann = Bob, so in a runoff this voter has no voice. The second round therefore has to *collect new information* — either by bringing the voters back for another election (Approval + Top-Two), or by asking a richer question the first time (STAR). Ranked ballots carry the finalist preference too — that's what RCV-IRV's "instant" runoff consults; the 0/1 ballot is the one style with nothing to consult. (The full one-voter/three-ballots anatomy is [alternate ballot styles](../topics/ballot_styles.md).)

## St. Louis in practice

The first outing — the March 2021 mayoral primary, four candidates — shows the package working, and shows the second round genuinely measuring something new ([Ballotpedia](https://ballotpedia.org/Mayoral_election_in_St._Louis,_Missouri_%28March_2,_2021,_top-two_primary%29) · [Wikipedia](https://en.wikipedia.org/wiki/2021_St._Louis_mayoral_election)):

- **Round 1 (Approval):** Tishaura Jones **57%**, Cara Spencer **46%**, Lewis Reed **39%**, Andrew Jones **14%**. The shares sum to ~156% by design: 44,538 voters cast 69,607 approvals — about **1.56 approvals per ballot**.
- **Round 2 (head-to-head):** Jones **51.7%** — Spencer **47.8%**.

The approval order held, but an 11-point approval gap shrank to under 4 points head-to-head: the general asked a different question — *of these two, which?* — and nearly got a different answer. (In the [2025 rematch](https://en.wikipedia.org/wiki/2025_St._Louis_mayoral_election) it ran the other way: Spencer led the approval round 68%–33% and won the general comfortably.) The cost side is just as visible: every cycle needs **two campaigns, two election days, and two electorates that never quite match** — the March 2021 electorate that picked the finalists was about 13,500 voters *smaller* than the April one that picked the mayor.

## STAR: the same package, one trip

STAR *is* Approval + Top-Two folded into a single ballot — historically, not just conceptually. When the Unified Primary campaign ended in 2014, the Equal Vote Conference in Eugene kept its architecture — a broad, expressive first round, then a top-two majority check — and asked what round-1 ballot would let the runoff run **automatically** ([STAR voting — Wikipedia](https://en.wikipedia.org/wiki/STAR_voting)). The answer was to replace the checkmark with a **0–5 score**. The score round finds the two strongest candidates (the primary's job), and because every ballot now records *degrees* of support, the runoff reads each voter's preference between the finalists off the ballot they already cast (the general's job) — [Score Then Automatic Runoff](../STAR_Voting/STAR_Automatic_Runoff.md). One trip, one electorate, no second campaign; ballots that scored the finalists equal are counted openly as Equal Support ([Two Denominators, One Winner](../STAR_Voting/runoff_percentages.md)). And unlike the approval echo above, STAR's runoff has real information to consult — it can even overturn the scoring-round leader, which is the whole point of having it ([the runoff reversal](../../01_STAR/_main/_main_pages/bv2182_tg4779_faq_runoff_reversal.md)).

| | Choose-One + Top-Two | Approval + Top-Two | STAR |
|---|---|---|---|
| Round-1 ballot | pick one | approve any number (0/1) | score each 0–5 |
| Vote-splitting in round 1 | severe | largely solved | solved |
| Finalists picked by | top two vote counts | top two approval counts | top two score totals |
| The runoff | second election | second election | **automatic — same ballots** |
| What the runoff learns | new head-to-head votes | new head-to-head votes | each ballot's finalist preference (Equal Support counted openly) |
| Trips to the polls | 2 | 2 | **1** |
| Electorates | two different turnouts | two different turnouts | identical by construction |

The [fidelity ladder](../scores_and_ranks/fidelity_ladder.md) says the same thing in one line: Approval is Score at 1-bit resolution — and one bit is one bit too few for a runoff.

## See also

- [Approval Voting](approval_voting.md) — the overview, including the stepping-stone argument (the [Equal Vote Approval page](https://www.equal.vote/approval) advocates exactly this primary + top-two package; advocacy lean disclosed)
- [Approval — Honest Limits](approval_honest_limits.md) — the gaps the runoff patches (§2 the threshold, §4 the missed majority favorite)
- [`approval_101_c3_b5`](../../04_Approval/_main/_main_pages/approval_101_c3_b5.md) — the featured election (BV-backed, frozen ballots)
- [Alternate ballot styles](../topics/ballot_styles.md) — one voter, every ballot style, side by side
- [Unified primary (Wikipedia)](https://en.wikipedia.org/wiki/Unified_primary) · [St. Louis Prop D (Ballotpedia)](https://ballotpedia.org/St._Louis,_Missouri,_Proposition_D,_Approval_Voting_Initiative_%28November_2020%29) · [2021 St. Louis mayoral election (Wikipedia)](https://en.wikipedia.org/wiki/2021_St._Louis_mayoral_election)

# file: approval_top_two.md
