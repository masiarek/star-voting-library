# 04_Approval — Approval Voting

*Mark **every** candidate you approve. Whoever collects the most marks wins.*

<img src="01_Learn/img/approval_ballot_single_bubble.png" width="460" alt="An Approval ballot: one bubble per candidate — Andre, Blake, Carmen, David, Erin — under the instruction 'Vote for ALL candidates you approve of'. This voter has filled the bubbles for Andre, Carmen and David.">

*The ballot ([Equal Vote](https://www.equal.vote/approval)) — it can look identical to a traditional ballot. Only the "vote for only one" instruction changes.*

**Approval hands every voter a checklist instead of a single choice.** Approve as many candidates as you like — one, three, all of them — and each approval is worth one point. Add up the checkmarks; whoever has the most wins. No ranking, no scores, no runoff.

That one change fixes Choose-One's core failure. Under Choose-One, marking your sincere favorite (a long shot) *costs* you a vote against the front-runner you'd settle for — the [spoiler / vote-splitting](../07_Concepts/topics/spoiler_effect.md) trap. Under Approval you simply approve **both** your favorite and the acceptable compromise, so supporting a new candidate never splits your own side.

It also asks one genuinely hard thing of you. Because the ballot is binary, Approval forces exactly one call: **where to draw your approval line.** Approve too few and you can't help a compromise; approve too many and you help a rival beat your favorite. And a checkmark can never say *how much* you approve, or in what order — which is precisely the information [STAR](../01_STAR/README.md)'s 0–5 ballot keeps. Approval is Score voting at **one-bit resolution**: an enormous gain in expressiveness over choose-one, for near-zero ballot complexity.

This page is the folder's front door: the method, one worked election, and the index of runnable examples below. The full concept treatment lives next door — **[Approval Voting](01_Learn/approval_voting.md)** (the ballot variants, reading a result, where it fits in the scored family), **[honest limits](01_Learn/approval_honest_limits.md)** (where it struggles), **[Approval + Top-Two](01_Learn/approval_top_two.md)** (the St. Louis package), **[in the theory literature](01_Learn/approval_in_the_literature.md)**, and the [full concept index](01_Learn/README.md).

---

## How it counts — a worked election

Five voters, three candidates — Ann, Bob and Cal. Here is every ballot twice over: as the voter marked the paper, and as the count reads it, one column per candidate.

<!-- ballots:approval_101_c3_b5 -->
The ballots as marked — a filled **Yes** is a `1` in that candidate's column, a filled **No** a `0`:

| Ballot as marked | Ann | Bob | Cal |
|:--|:--:|:--:|:--:|
| <img src="02_Examples/cases/img/approval_101_c3_b5_ballot_1.png" width="330" style="min-width:330px" alt="A Yes/No Approval ballot — Voter 1 — approves Ann and Bob: Ann Yes, Bob Yes, Cal No."> | 1 | 1 | 0 |
| <img src="02_Examples/cases/img/approval_101_c3_b5_ballot_2.png" width="330" style="min-width:330px" alt="A Yes/No Approval ballot — Voter 2 — approves Bob and Cal: Ann No, Bob Yes, Cal Yes."> | 0 | 1 | 1 |
| <img src="02_Examples/cases/img/approval_101_c3_b5_ballot_3.png" width="330" style="min-width:330px" alt="A Yes/No Approval ballot — Voter 3 — approves Ann and Bob: Ann Yes, Bob Yes, Cal No."> | 1 | 1 | 0 |
| <img src="02_Examples/cases/img/approval_101_c3_b5_ballot_4.png" width="330" style="min-width:330px" alt="A Yes/No Approval ballot — Voter 4 — approves only Bob: Ann No, Bob Yes, Cal No."> | 0 | 1 | 0 |
| <img src="02_Examples/cases/img/approval_101_c3_b5_ballot_5.png" width="330" style="min-width:330px" alt="A Yes/No Approval ballot — Voter 5 — approves Ann and Cal: Ann Yes, Bob No, Cal Yes."> | 1 | 0 | 1 |
<!-- /ballots -->

Now add up the columns — a `1` is a point, a `0` is nothing:

<!-- report:approval_101_c3_b5 -->
```text
--- Approval Voting (single winner) ---
 Tabulating 5 ballots (any non-zero score = approval).

Ballots:
   columns = Ann, Bob, Cal      (1 = approve; 0 = not approved)
     2 × 1,1,0
     1 × 0,1,1
     1 × 0,1,0
     1 × 1,0,1

   Bob -- 4 (80%) -- Elected
   Ann -- 3 (60%)
   Cal -- 2 (40%)

[Approval Distribution] (how many candidates each ballot approved)
   9 approvals across 5 ballots — average 1.8 of 3 (range 1–2).
     approved 1: 1 ballot
     approved 2: 4 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
        |  Bob   |  Ann   |  Cal   |
   ---------------------------------
   Bob  |   --   |  50%   |  25%   |
   Ann  |  67%   |   --   |  33%   |
   Cal  |  50%   |  50%   |   --   |

Winner — Approval Voting (single winner)
  Bob
```
<!-- /report -->

**Bob wins with 4 of 5.** He is nobody's *only* choice, yet four of five voters approve him — the broadest support in the field, and the honest headline is exactly that: *80% of voters approve Bob*, not a share of some contested denominator. Two further numbers come with every approval count, and they're the ones people forget to ask for:

- **The approval distribution — the strategy signal.** How many candidates *each ballot* approved (here 9 approvals across 5 ballots, average 1.8 of 3). If most voters had **bullet-voted** — approved exactly one — the electorate would be behaving like Choose-One and the "approve as many as you like" freedom would have gone unused.
- **The co-approval matrix — the coalitions.** Of the voters who approved the row candidate, the share who *also* approved the column candidate. It exposes structure the totals hide: Ann's approvers back Bob 67% of the time, while Cal's split evenly.

Both are unpacked on [Approval Voting → reading a result](01_Learn/approval_voting.md#reading-an-approval-result). Want the whole count? → the full report: [`approval_101_c3_b5.md`](02_Examples/cases/cases_pages/approval_101_c3_b5.md) · run it yourself: [`.yaml`](02_Examples/cases/approval_101_c3_b5.yaml) · live on BetterVoting: [`ff6mk3` results ↗](https://bettervoting.com/ff6mk3/results)

## How it compares

| | **Choose-One** | **Approval** | **STAR** |
|---|---|---|---|
| Ballot | pick **one** | approve **any number** (0/1) | score each **0–5** |
| Approve favorite **and** compromise? | ❌ | ✅ | ✅ |
| Preference **strength**? | ❌ | ❌ | ✅ |
| **Order** among the ones you like? | ❌ | ❌ | ✅ |
| Spoiler / vote-splitting resistant? | ❌ | ✅ largely | ✅ |

*(The fuller version of this table — the threshold decision, [precinct-summability](../07_Concepts/topics/summability/README.md) — is on the [method page](01_Learn/approval_voting.md#how-it-compares).)*

Approval's virtue is **simplicity**: no ballot redesign, nothing to spoil (every combination of marks is a valid ballot), a trivial hand count, and it's precinct-summable on existing equipment — which makes it the cheapest reform to actually adopt, and a strong first step for anyone leaving plurality behind. Its ceiling is the binary ballot. The [Black Curtain](../method_comparisons/black_curtain/README.md) set makes the trade-off concrete: on identical ballots, Approval elects the broadly-approved consensus candidate while STAR's runoff hands the seat to the majority's favorite — same voters, different question.

---

## The worked examples

Runnable elections, each isolating one idea. Tabulate any of them yourself.

| Where | What |
|---|---|
| [Approval 101 — most approvals wins](02_Examples/cases/cases_pages/approval_101_c3_b5.md) | the full report for the election above — Bob takes 4 of 5 approvals without being anyone's only choice. A real BetterVoting election (`ff6mk3`), which agrees exactly ([folder](02_Examples/README.md)) |
| [Multi-winner (bloc) Approval](02_Examples/multiwinner/README.md) | the same 0/1 ballot for several seats: top-`N` approved win. Three cases — the plain 3-seat count, the **majority sweep** (a 4-voter majority takes *both* seats and the minority gets nothing), and Lackner & Skowron's running example, where the proportional rules seat a different committee |
| [Lackner & Skowron — approval and its shadow STAR](02_Examples/multiwinner/lackner_skowron_shadow_star.md) | the same profile run through the STAR family: Bloc STAR / Allocated Score / SSS all seat D, and only **RRV** recovers F, matching PAV |
| [The Black Curtain](../method_comparisons/black_curtain/README.md) | the same five voters counted by Approval vs STAR vs RCV-IRV vs Score — Approval flips the winner in election 1 |
| [The BV Library](../method_comparisons/BV_Library/README.md) | a real BetterVoting approval election |

The proportional approval rules the LH engine doesn't carry (SPAV, PAV, seq-Phragmén) run on the same YAML files through the [`abcvoting` engine](../06_Other/abcvoting_tabulation_engine/README.md) — they break the bloc sweep and give the minority its seat.

So does **[Satisfaction Approval Voting (SAV)](01_Learn/Multiwinner_Approval/satisfaction_approval_voting.md)**, by a different route: one vote per *ballot*, split evenly among your marks, so approving four gives each a quarter. On Brams & Kilgour's own ten-voter example it elects a committee with **no candidate in common** with bloc Approval's — and bloc STAR and Ranked Robin, run on the same electorate, both side with bloc Approval.

**Where it stands on the criteria** — Approval's pass/fail row beside STAR, Ranked Robin and RCV-IRV, each ✗ linked to a runnable election: [Criteria at a glance](../07_Concepts/topics/criteria_at_a_glance.md). **Where it has actually been used** — papal conclaves, Venice and Greece long before anyone named it; Fargo and St. Louis recently, and Fargo's repeal in 2025: [the record, from Wikipedia](01_Learn/approval_voting.md#where-it-has-actually-been-used).

**The three-option variant** — [Combined Approval Voting (CAV)](../06_Other/Combined_Approval/README.md) adds an explicit **Against** to the ballot: For (+1) / abstain (0) / Against (−1), highest net wins. It lives in `06_Other/` because it isn't an EVC method, but it belongs to this family, and it carries the sharpest lesson about what a blank is worth — CAV reads an unmarked row as the *middle* grade where every other score ballot here reads it as the *lowest*, and a runnable pair of elections shows the same twelve voters reversing end-to-end on that one word.

House rule: Approval ballots accept only `0`/`1`; the engine errors on 0–5 scores under `voting_method: Approval`. A blank cell counts as **not approved**, and so does any of the five [abstention markers](../01_STAR/01_Learn/properties_and_limits/abstention_vs_zero_vs_nota.md) — `-` blank, `~` race abstention, `&` candidate abstention, `?` spoiled, `%` spoiled and re-issued. The report echoes all of them as `0`, and names the ones a file actually used in a legend beneath the ballots.

**Conversation scripts:** the Larry ↔ Adam series (STAR + RCV-IRV) is indexed in [Conversation scripts — index](../07_Concepts/about_this_repo/conversation_scripts.md).

# file: README.md
