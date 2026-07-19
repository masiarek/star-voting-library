# Why STAR Voting

### Voting 101 → 301 · the case for STAR — for voters, presenters, and debaters

The case for **STAR Voting** — *Score Then Automatic Runoff* — laid out as regular reading. This page makes the argument in **eleven plain points**, then answers the objections it tends to draw, sorted from the unshakeable to the genuinely contested. A better ballot, a fairer winner, and a count anyone can verify: that's the whole promise, and the sections below unpack each part with the honest caveats attached.

*Prefer it spoken or on slides? The narrated companion is [What's so good about STAR](../STAR_Voting/reference/whats_so_good_about_STAR_Voting.md); the scannable benefit list is [The benefits of STAR Voting](../STAR_Voting/getting_started/STAR_benefits.md).*

---

## The case in eleven points

### 1. STAR in one sentence

STAR stands for **Score Then Automatic Runoff**. You score every candidate from 0 to 5 by how much you support them; the two highest-scored candidates become finalists; and then every ballot counts as a full vote for whichever finalist it scored higher. That's it — a ballot that lets you say *how much* you support each candidate, a winner who genuinely beats the runner-up, and a count any citizen can re-add by hand. It isn't a tweak to how votes are counted so much as a better ballot to count.

### 2. The problem isn't just spoilers

Choose-One Plurality forces your whole opinion into a single name. That one act is the root of a whole family of failures: vote splitting, the [spoiler effect](spoiler_effect.md), and lesser-evil voting — and winners who take office without ever beating anyone head-to-head. But the deeper failure is upstream of all of those: the ballot itself won't let voters say what they think, so the result can't reflect what voters actually want. Fixing "spoilers" alone misses the point — the goal is a ballot expressive enough that the electorate's real preferences survive the count. (This is why STAR advocates lead with expressiveness rather than spoilers: [RCV-IRV](rcv_irv_vs_star.md) also claims to reduce spoilers, but it doesn't give voters a way to express degree of support.)

### 3. What STAR Voting is

A STAR ballot has two simple steps. In the **scoring round**, you score every candidate 0 to 5 — like rating movies — and the two highest-scored candidates become the finalists. In the **automatic runoff**, your ballot counts as a full vote for whichever of those two finalists you scored higher. Degree of support first, then a clear head-to-head finish. Anyone can watch the two rounds turn on a three-candidate example: add up the scores to find the top two, then see which finalist each ballot preferred.

### 4. You never have to betray your favorite

Under Choose-One, backing a long-shot you love means abandoning the front-runner you also like — the two split your own side. Under STAR, you score both high and neither choice costs the other: no forced ranking, no "wasted" vote. You express *how much* you support each candidate rather than surrendering everyone but one. The upshot is the line worth remembering — **honesty is your best ballot.** (STAR isn't formally [favorite-betrayal](../STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md)-proof — no method that also has a majority runoff can be — but you can always give your true favorite a 5, and betraying them almost never pays. Point 12 handles this claim in full.)

### 5. Every winner earns a majority

The automatic runoff guarantees the winner beats the runner-up head-to-head: among all voters who expressed a preference between the two finalists, the winner has majority support. This is what answers the worry that scoring is "just an average" — the very last step is a real majority test, not a mean. Contrast a plurality winner who takes office on 30–40% while most voters opposed them. STAR pairs the expressiveness of scoring with the legitimacy of a final round, so there are **no more [10%-plurality winners](plurality.md#show-me-a-minority-winner-worked).**

### 6. Simple to vote

The 0–5 scale is the familiar five-star rating — movies, rideshares, now elections. Two features make it forgiving. **Equal scores are allowed:** rate two candidates the same when you feel the same about them, so you're never forced to invent a preference you don't have ([Equal Support](../GLOSSARY.md)). And you can't accidentally spoil your ballot the way a ranked overvote can — ballot-error rates are low, and there are no [exhausted](../RCV_IRV/exhausted_ballots_301.md) (discarded) ballots in the runoff. A real filled-in ballot looks familiar, not novel.

### 7. Easy to count and verify

STAR is **precinct-[summable](summability/)**: each precinct reports its score totals and a small For / Equal / Against pairwise matrix, and you add those up like sports scores. No shipping every ballot to one central computer to run sequential eliminations, and no central tabulation required at all. Any precinct's numbers can be checked and re-added independently, so any citizen can confirm the winner. Transparent, auditable, and fast — this is the point for the election officials and skeptics in the room, and it's the one thing sequential-elimination methods structurally can't match.

### 8. Better incentives for candidates

To win under STAR, you want to be the high score of your *opponents'* supporters too — which rewards broad appeal over base-energizing and mudslinging, because the people you attack can lower your score. The predicted result is healthier campaigns: more outreach, less trashing of rivals, a tendency toward broadly supported consensus winners. State this honestly as *what the incentives reward*, not as a proven outcome — the empirical record is thin because adoption is recent (see point 11).

### 9. An equal vote

Every voter has the identical 0–5 range for every candidate, and therefore identical maximum influence in both the scoring round and the runoff — the total number of points you hand out doesn't matter. This is what answers the "but some people give out more points!" objection. STAR passes the **Test of Balance**: any support a ballot can express can be met by an equal and opposite opposition, which is the precise version of "equal weight." The equality is structural, built into the ballot ([equally weighted vote](../STAR_Voting/properties_and_limits/equally_weighted_vote.md)).

### 10. What STAR does — and doesn't — claim

Honesty about the boundaries is what makes the rest trustworthy, so state them plainly. STAR **does** end favorite betrayal as a forced move, guarantee a majority finish, and stay easy to count. It **dramatically reduces** vote splitting — though no method eliminates all strategic incentive. It **usually** elects the [Condorcet winner](condorcet/) — at a very high rate, but not as a guarantee. And it's **resistant** to strategy, not strategy-proof — because no method can be. A reformer who states the boundary lines earns the trust to be believed on everything else.

### 11. What you can do

Try a STAR ballot for yourself at **[BetterVoting.com](https://bettervoting.com)**. Then the bigger step: run your next club, board, HOA, or local-org election with STAR — small real elections are how the method spreads. And the [Equal Vote Coalition](https://www.equal.vote) is the place to go for anyone who wants to get involved or go deeper.

---

## Answering the hard questions

Every point above draws objections. Here they are grouped by how solid your footing is — the claim in precise, defensible wording, the rebuttal it tends to draw, and the honest response. Lead with the first group; know the tradeoff cold before you wade into the last.

### The strongest points — lead with these

**[Expressiveness](../scores_and_ranks/scores_vs_ranks.md) — no forced favorite betrayal.** *Claim:* you score every candidate 0–5, so backing a new favorite never costs a candidate you also like. *Rebuttal:* "Ranked ballots let you express more than one choice too." *Response:* ranked ballots force a strict order and can't express equal or degree of support; STAR lets you score two candidates the same and say how much more you prefer one. And [IRV](center_squeeze/)'s later rounds can still punish your favorite via center squeeze — STAR's scoring round can't.

**The [automatic runoff](../STAR_Voting/the_count/STAR_Automatic_Runoff.md) → a guaranteed [majority finish](../GLOSSARY.md#core-vocabulary).** *Claim:* the two highest-scored candidates advance, and every ballot then counts fully for whichever finalist it scored higher, so the winner has majority support in that head-to-head. *Rebuttal:* "Score voting just elects the highest average — a small, enthusiastic minority can win." *Response:* that's exactly why STAR *has* the runoff. Pure score is vulnerable to that; the runoff guarantees the winner beats the runner-up among everyone who expressed a preference. STAR is the synthesis, not pure score.

**Summability, transparency, auditability.** *Claim:* STAR is precinct-summable — report each precinct's score totals and its For/Equal/Against matrix and add them up, no central tabulation needed. *Rebuttal:* "Modern RCV-IRV is auditable too; the software handles it." *Response:* RCV-IRV is not additively summable. Eliminations are sequential and depend on the full ballot set, so precincts can't be tallied independently and combined — you need the complete cast-vote record centrally. STAR's two summable data structures let any precinct's totals be verified on their own. It's a structural property of the method, not a software feature.

**Usability.** *Claim:* 0–5 scoring is the familiar five-star rating, equal scores are allowed, error rates are low, and there are no exhausted ballots in the runoff. *Rebuttal:* "RCV-IRV is already widely used; voters handle it fine." *Response:* ranked ballots have measurably higher overvote/error rates and produce exhausted (discarded) ballots when a voter doesn't rank a finalist. STAR ballots aren't exhausted in the runoff the same way, and allowing equal scores removes the cognitive load of a forced strict order.

### Points that need precise framing — true, with the right words

**Reduces vote splitting and the spoiler effect.** *Claim:* STAR dramatically reduces vote splitting. *Rebuttal:* "You admit it doesn't eliminate it — so it's not solved." *Response:* no deterministic method with three or more candidates eliminates strategic incentive entirely (Gibbard). STAR removes the ordinary spoiler dynamic — running a similar candidate doesn't split support, because voters can score both highly — and shrinks the residual to a narrow, hard-to-coordinate edge case ([residual vote splitting](../STAR_Voting/properties_and_limits/residual_vote_splitting.md)). "Dramatically reduces, doesn't claim to eliminate" is honest and still winning.

**Condorcet compliance.** *Claim:* STAR elects the [Condorcet winner](condorcet/) in the large majority of realistic elections. *Rebuttal:* "STAR isn't Condorcet-compliant — it can fail to elect the candidate who beats all others head-to-head." *Response:* correct, and we don't claim otherwise. STAR isn't Condorcet-compliant, but its Condorcet efficiency is very high in simulation; when it diverges, the winner is someone with very high overall support who lost one pairing narrowly. And Condorcet methods buy compliance by sacrificing other properties — the Condorcet winner can be a weakly supported compromise nobody is enthusiastic about. It's a tradeoff, not a clean loss.

**Strategy resistance.** *Claim:* a voter's best play is usually sincere or near-sincere scoring. *Rebuttal:* "STAR is manipulable — min/max (bullet) scoring is a strategy." *Response:* every method is manipulable — Gibbard–Satterthwaite for ranked methods, Gibbard's 1978 result for cardinal ones. (This is Gibbard, not Arrow — Arrow is about aggregating rankings, a different result.) The real question is how often strategy pays and how risky it is. Under STAR, min/maxing can backfire: collapsing your scores can hand the runoff to a worse candidate and forfeits your say in choosing the finalists. Resistant, not proof — and more resistant than Choose-One or RCV-IRV on realistic electorates.

**Consensus winners.** *Claim:* STAR rewards broad appeal and tends to elect consensus winners. *Rebuttal:* "'Consensus' is vague — define it." *Response:* operationalize it: STAR picks a runoff-moderated maximizer of total expressed support. It avoids both the plurality winner (narrow base) and the pure-average winner (manipulable), and the runoff then ensures that consensus winner also wins a majority head-to-head against the strongest rival.

### The contested, values-based points — win on framing, know the tradeoff

**Later-no-harm — feature, not bug** *(the central RCV-IRV attack).* *Claim:* later-no-harm is not a property we should want; honestly supporting a compromise candidate *should* be able to help them win. *Rebuttal:* "Under STAR, giving any points to your second choice can cause your first choice to lose. RCV-IRV guarantees ranking later choices never hurts your favorite." *Response:* Woodall proved later-no-harm is provably incompatible with other desirable criteria — it isn't free. The price RCV-IRV pays for it is [center squeeze](center_squeeze/): a broadly liked candidate can be eliminated early precisely because few rank them *first*, handing the win to a more polarizing candidate the majority actually opposed. STAR's design says that if enough voters genuinely support a compromise, that support should count. Reframe it: not "your vote hurt your favorite," but "your honest support helped elect someone a majority preferred."

**Equality and the Test of Balance.** *Claim:* STAR gives every voter equal weight and passes the Test of Balance — any support a ballot can express can be exactly countered by an equal and opposite opposition. *Rebuttal:* "Score/STAR violates one-person-one-vote — some voters hand out more total points." *Response:* total points are irrelevant to influence; every voter has the identical 0–5 range for every candidate and identical maximum leverage in both rounds. The Test of Balance is the precise version of equal weight. One caution: don't claim other methods violate the *constitutional* one-person-one-vote doctrine — the *Reynolds v. Sims* line governs district population equality, not ballot expressiveness. The equal-weight argument is structural and strong; the constitutional-violation claim is a stretch a lawyer will call.

**Reduces polarization and negative campaigning.** *Claim:* because candidates want to be the high score of rivals' supporters, STAR rewards broad outreach over base-energizing attacks. *Rebuttal:* "That's speculative — where's the evidence?" *Response:* it's an incentive-structure argument, well-grounded in theory and consistent with limited real-world use, but the large-scale empirical record is thin because adoption is recent. Present it as a predicted incentive effect, not a proven outcome — conceding that boundary protects your credibility on everything else.

**"Only RCV avoids favorite betrayal"** *(the deep dive behind point 4).* *Claim:* in STAR you can always give your true favorite a 5 and never have to abandon them — and in the competitive races that actually matter, STAR protects your favorite better than RCV-IRV does. *Rebuttal:* "Only Ranked Choice guarantees supporting your favorite never backfires. STAR isn't favorite-betrayal-proof — you admit it." *Response:* correct that STAR isn't formally **Favorite-Betrayal-Criterion (FBC)** compliant — but *neither is RCV-IRV.* The property the advocate is actually invoking is **later-no-harm** (ranking lower choices can't hurt your favorite), which RCV-IRV *does* satisfy — a *different* criterion. RCV-IRV **fails** FBC. The textbook case is Alaska 2022: voters who ranked Palin first were punished for it — that ranking helped elect their *last* choice, Peltola; they'd have done better betraying Palin and ranking Begich first. FBC and later-no-harm are **provably incompatible** — no method can have both. Cardinal methods (Approval, Score) satisfy FBC and fail later-no-harm; RCV-IRV satisfies later-no-harm and fails FBC; STAR satisfies *neither* by design, trading a sliver of each for a majority-backed, exaggeration-resistant result. (A brute-force check — [`06_Other/simulations/fbc_simulation.py`](../../06_Other/simulations/fbc_simulation.py) — finds STAR and RCV-IRV fail FBC at *about the same low rate*; STAR's real edge is that attempting favorite-betrayal **backfires ~98% of the time**, several times more reliably than under RCV-IRV. So don't quote a "98% FBC-compliant" figure — the sim doesn't support it. Claim instead that *betrayal doesn't pay.*) The honest one-liner: *"Neither of us is favorite-betrayal-proof, and on paper we fail about equally often — but in STAR betraying your favorite almost always backfires, while your center-squeeze failure is predictable enough that a whole wing has a reason to. And what you're calling 'no favorite betrayal' is later-no-harm — a different criterion."* <!-- terminology-ok: bare "RCV" is inside a quoted opponent slogan; the response uses RCV-IRV -->

---

## Where to start, depending on who you're talking to

- **General public / first contact:** point 4 (no favorite betrayal) plus point 5 (majority finish). Emotional and unshakeable.
- **Election administrators / officials:** point 7 (summability) plus point 6 (usability). Concrete and operational.
- **RCV-IRV advocates:** open on the majority finish and summability (take majoritarianism and transparency), then be ready for the later-no-harm attack and reframe it as center squeeze.
- **Academics / skeptics:** the middle group throughout, stated with the precise caveats. Your willingness to say "resistant, not proof" and "not Condorcet-compliant" is what earns the room.

---

## Where this fits in the overall teaching

- **Level:** spans Voting 101 (the problem, the two rounds), 201 (majority finish, summability, usability), and 301 (the FBC / later-no-harm deep dive in point 12).
- **Pairs with:** [Our voting system is broken](our_voting_system_is_broken.md) (the diagnosis) and [What's so good about STAR](../STAR_Voting/reference/whats_so_good_about_STAR_Voting.md) (the narrated pitch). For the limits argued the other way, see [STAR's honest limits](../STAR_Voting/properties_and_limits/STAR_honest_limits.md).
- **Terminology:** public-facing copy can say "RCV" (clarified once as ranked ballots counted by instant runoff); the technical passages here use `RCV-IRV` / `IRV` on purpose — center squeeze, exhausted ballots, and later-no-harm are IRV-specific, not properties of every ranked method.

Cross-references:
- [GLOSSARY](../GLOSSARY.md) — "Equal Support," "Majority finish," "Summability," "Condorcet winner," "Center squeeze," "Later-no-harm," "Favorite Betrayal Criterion."
- [Favorite betrayal, untangled (301)](../STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md) — the full FBC vs. later-no-harm treatment behind points 4 and 12.
- [STAR benefits](../STAR_Voting/getting_started/STAR_benefits.md) · [What's so good about STAR](../STAR_Voting/reference/whats_so_good_about_STAR_Voting.md) — the scannable and narrated companions.
- [LINKS.md](../LINKS.md) → **Why STAR 1** / **Why STAR 2** (the public Google Docs this page mirrors), **Full Deck 2025**.
