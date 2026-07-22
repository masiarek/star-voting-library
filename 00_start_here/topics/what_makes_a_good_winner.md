# What makes a "good" winner? — the correct winner, the consensus candidate, and why there's no single ideal

*When we say a voting method "gets it right" or "elects the wrong winner," what do we actually mean? There is no single **correct** winner handed down from on high — "good winner" is a **design choice** about what we value. This page lays out the competing ideals, shows them disagreeing on real elections in this repo, and pins down the vocabulary (consensus candidate, strong candidate, utilitarian winner) so the rest of the docs can use it precisely.*

→ **Level: Voting 201** — Curriculum [201.6](../CURRICULUM.md) (deeper theory — VSE, Arrow — at 301). Related topic hubs: [Condorcet efficiency](condorcet) · [Center squeeze](center_squeeze) · [Majority criterion](majority_criterion) · [Why STAR](Why_STAR_Voting.md) · [STAR's honest limits](../STAR_Voting/properties_and_limits/STAR_honest_limits.md).

## The trap: "the winner should have won"

**Surprisingly, once more than two candidates are involved, there is no single universally-accepted definition of who *should* win.** It's tempting to say a method failed because "obviously candidate X should have won" — but *obviously by what standard?* Almost every argument about voting methods is really an argument about which of a few **different, reasonable ideals** of a good winner you're using. They usually agree — and when they don't, that disagreement *is* the whole subject.

This isn't a gap waiting to be filled; it's a **theorem**. Arrow's impossibility theorem shows no ranked method can satisfy a short list of obviously-reasonable fairness conditions at once, and majority preference can even **cycle** (A beats B beats C beats A), so "the candidate a majority prefers" need not exist. Every method augments majority rule with *some* extra rule to always name a winner — and that choice is where methods differ.

## Four ideals of a "good" winner (single-winner)

| Ideal | The winner is… | Also called | The criterion |
|-------|----------------|-------------|---------------|
| **Most first choices** | whoever leads the first-preference count | the plurality leader / front-runner | (plurality) |
| **Majority's choice** | someone a majority ranks first / prefers | the majority winner | [Majority criterion](majority_criterion) |
| **Beats everyone head-to-head** | who wins every one-on-one matchup | the **consensus candidate** / **Condorcet winner** / a "strong" candidate | [Condorcet criterion](condorcet) |
| **Highest overall support** | who the electorate rates highest in total | the **utilitarian** / best-liked winner | (utilitarian efficiency) |

These are *different questions*. "Who has the most passionate first-choice base?" is not "who could beat any rival in a runoff?" is not "who is rated highest by everyone?" A **polarizing front-runner** can lead first choices while losing every head-to-head; a **consensus candidate** can be almost nobody's favorite yet everybody's acceptable second choice and beat all rivals one-on-one.

## The key words

- **Consensus candidate** — broadly acceptable; the compromise a majority would take over any single rival. Formally, when one exists, this is the **Condorcet winner** (beats every opponent head-to-head). Often *few first choices* but *wide second-choice support*.
- **Strong candidate** — loosely, one who holds up under scrutiny: wins pairwise matchups, or has deep and wide support. The Condorcet winner is the strongest in the pairwise sense.
- **Utilitarian winner** — maximizes total voter satisfaction (e.g. the highest score sum). The strongest in the "greatest overall happiness" sense.
- **Spoiler / vote-split victim** — a good winner who *loses* only because similar candidates divided the vote (see [spoiler effect](spoiler_effect.md)).

## They disagree — on real elections in this repo

**[Tennessee (BV2131)](../../05_Ranked_Robin/rr_vs_irv_plurality/bv2131_tennessee_condorcet_center_vqyqkr.md).** One ballot set, three "good winners":

- Plurality → **Memphis** (most first choices — but 58% rank it *last*).
- RCV-IRV → **Knoxville** (last one standing after eliminations).
- Ranked Robin / Condorcet → **Nashville** — the **consensus candidate**, beats every city head-to-head, yet holds few first choices.

Which is "correct"? Memphis is the plurality answer; Nashville is the consensus answer. The center-squeeze critique of IRV is precisely that it discards the consensus candidate — but that critique only bites if you *value* the consensus candidate.

**[Pet poll II (BV2133)](../../method_comparisons/pet_poll_four_winners/bv2133_dyxrbr_pet_poll_four_winners.md).** Four methods, **four different winners** on the same 32 voters: Dog (plurality front-runner), Fish (IRV), Bird (broadly approved), Cat (STAR / the consensus Condorcet winner). Each is the "right" winner under *some* ideal.

**A real one — Alaska's 2022 special U.S. House election.** Begich was the **Condorcet winner**: head-to-head he beat Palin (101,229 to 63,621) *and* Peltola (93,052 to 79,558) — he'd have won a runoff against either. But RCV-IRV eliminated Begich in an earlier round (too few first choices — the center squeeze) and elected **Peltola**. That's a **Condorcet failure**: a real election with a consensus candidate the method didn't pick (Graham-Squire & McCune, [arXiv:2301.12075](https://arxiv.org/abs/2301.12075)). Whether you call it a "failure" depends entirely on whether you hold the consensus-candidate ideal — which is the point of this page.

**Burlington, VT 2009 mayor (IRV, later repealed).** Three viable candidates; the Democrat was the **Condorcet winner** (preferred head-to-head over both rivals) but was eliminated early for too few first choices, and the Progressive won — a Condorcet failure, and the city repealed IRV soon after. Note the honest nuance: with only rankings we *can't tell* whether the Republican voters who preferred the Democrat were nearly-indifferent between Democrat and Progressive or strongly preferred the Democrat — which is exactly the case for wanting **level-of-support** data, not just order.

### The deepest split: majoritarian vs. utilitarian

The two ideals that most often pull apart are the **majoritarian** winner (whom a majority prefers, e.g. the Condorcet/pairwise winner) and the **utilitarian** winner ([electowiki](https://electowiki.org/wiki/Utilitarian_winner) — who maximizes total voter satisfaction). A candidate loved intensely by 51% and hated by 49% can be the *majoritarian* winner while a broadly-liked compromise is the *utilitarian* winner.

A tiny illustration (Range Voting's "three brothers split one fruit," utilities on an arbitrary happiness scale):

| | apple | orange | banana |
|---|:---:|:---:|:---:|
| boy 1 | 2 | 7 | **8** |
| boy 2 | 3 | 9 | **10** |
| boy 3 | 4 | **11** | 0 |
| **average** | 3 | **9** | 6 |

A **majority** (boys 1 & 2) rank *banana* top → the **majoritarian** winner is banana. But *orange* maximizes **total satisfaction** (avg 9) because banana is worthless to boy 3 → the **utilitarian** winner is orange. Neither is "wrong"; they optimize different things. Ranked methods can only see order — [**preference**, not **support**](../scores_and_ranks/preference_vs_support.md) — so they chase the majoritarian/Condorcet ideal; scored methods (STAR, Score) can see *intensity*, so they can weigh the utilitarian one — and STAR's automatic runoff then checks the utilitarian leader against majority preference.

In practice the Condorcet and utilitarian (VSE) answers **usually agree**; they diverge only in close elections — where Condorcet favors the majority's first choice and VSE the broadest compromise. And a Condorcet winner is only as trustworthy as the ballots: with rankings you can't tell honest from strategic votes, or see *how much* a voter liked each candidate — which is the argument for an expressive (scored) ballot.

## So is there a "best" method / an ideal winner?

**No method optimizes all four ideals at once** — that's not a bug in any particular method, it's a theorem. When a Condorcet winner exists, most well-regarded methods elect them and the ideals line up; the disagreements happen exactly when majority-rule, consensus, and total-support *pull apart* (cycles, center squeezes, polarized electorates). Different methods make a considered choice about what to prioritize:

- **Ranked Robin / Condorcet methods** target the **beats-everyone** ideal (the consensus candidate), and name someone even when a cycle means none strictly exists.
- **STAR** targets **high, broad support** (score) and then confirms it against **majority preference** (the automatic runoff) — a blend of the utilitarian and majority ideals.
- **Approval** rewards **broad acceptability**.
- **Plurality / IRV** center on **first-choice** support (all at once, or round by round), which is why they can miss the consensus candidate.

*(Which ideal one **should** prioritize is a values question — this page deliberately doesn't pick a favorite. It gives you the vocabulary and the worked cases to reason about the trade-off yourself. For the case that STAR strikes a good balance, see [Why STAR](Why_STAR_Voting.md); for where STAR itself doesn't elect the Condorcet winner, see [STAR's honest limits](../STAR_Voting/properties_and_limits/STAR_honest_limits.md).)*

## A theorist's "best": the candidate at the center

The ideals above are values choices — but there's one framing where theory *does* pin down a single "best" candidate, **independent of any voting rule** (which matters, because "whoever the rule elects" is circular — rules disagree as the field changes; that's Arrow). It's the [spatial model](spatial_voting_model.md): place every voter's ideal at a point in issue-space. Then "best," per Tideman & Plassmann (*"Which voting rule is most likely to choose the 'best' candidate?"*, *Public Choice* 158 (2014): 331–357), has two natural readings — and they agree:

- **Voters as disinterested judges** (each estimating what's best for society): the best candidate is the one **closest to the mean** of all the ideal points — the electorate's center of gravity.
- **Voters as self-interested advocates**: the best candidate **minimizes the total distance** to every voter — the smallest aggregate compromise, the utilitarian least-unhappiness pick.

As the electorate grows, **these two definitions converge**: the minimize-total-distance candidate *is* the one at the mean. So a procedure-independent "best" exists after all — **the candidate nearest the center of the electorate** — even if no voting rule is guaranteed to elect them. That candidate is precisely the "optimal winner" the **VSE** score below measures methods against, and the operational cousin of the [utilitarian](#the-deepest-split-majoritarian-vs-utilitarian) ideal. And it's no accident that this is where **STAR and Ranked Robin aim** — scores and head-to-heads both pull toward the center — and the candidate **Choose-One and IRV can eliminate for lacking first-choice support** (the [center squeeze](center_squeeze/); Alaska's Begich is a real one).

## Measuring it empirically: VSE / Bayesian Regret

If there's no single definition of the *correct* winner, how do reformers compare methods? By **simulation**. **Voter Satisfaction Efficiency (VSE)** — the modern form of what earlier work called **Bayesian Regret** — models an electorate (usually a [spatial model](https://en.wikipedia.org/wiki/Spatial_model_of_voting): voters and candidates as points, closer = more preferred), runs thousands of simulated elections, and scores each method by *how satisfied the average voter is with the winner it produces* — 100% = the utility-maximizing winner every time, 0% = a random winner.

This sidesteps the "which winner is correct?" argument by asking a measurable question: **which method makes the most voters happiest, most often, across many plausible electorates?** The score is a normalized ratio — the older "Voter Satisfaction Index" writes it `(U − R) ÷ (O − R)`, where **U** = utility of the method's winner, **R** = utility of a *random* winner (0%), **O** = utility of the *optimal* winner (100%). Random draw = 0%; the utilitarian best = 100%; a method can even score *negative* (worse than a coin flip).

In these studies the ordering is consistently roughly **STAR ≳ Approval > RCV-IRV > Plurality**, plurality falls sharply as the field grows past two candidates, and STAR's edge is *largest in big, competitive fields* (score-plus-runoff was in fact *predicted* to top the list by Bayesian-Regret work around 2000). Caveats that keep it honest: the result **depends on the voter model and on how strategic voters are** (honest vs. fully strategic reshuffles the middle of the pack; STAR stays near the top across both), and every simulation is only as good as its assumptions. VSE is the closest thing to an objective score, but it's why "STAR tops the accuracy charts" is a claim about *simulated voter satisfaction under a model*, not a claim that its winner is metaphysically "correct."

VSE measures only *accuracy*. Its companion metric, **[PVSI](pvsi_strategic_incentive.md)** (Pivotal Voter Strategic Incentive), measures the other axis — how much a method **rewards voting dishonestly** — and the two are judged together, since a method that invites strategy erodes its own accuracy in practice.

*(Related: the "Yee diagram" visualizes the same idea in 2-D — for a given method, it colors each point of a policy space by who would win if the electorate centered there; good methods elect near the center of the voters, and the pictures show where plurality/IRV veer away. How these synthetic electorates are generated — Impartial Culture, spatial, Mallows, urn models — and why the results depend on that choice: [Election simulation models](election_simulation_models.md).)*

## Multi-winner: "good" changes meaning

For a *body* of seats, "good winner" becomes "good **body**," and a new ideal appears: **proportionality** — the winners should mirror the electorate's factions, not just repeat its majority. See the [Pets Governance set](../../method_comparisons/pets_governance): the same voters give a **majority sweep** under Bloc STAR/Approval but **minority representation** under STAR-PR and STV. Neither is "wrong" — they answer different questions ("who does the majority want?" vs. "does everyone get represented?").

## Takeaway

"Good winner," "correct winner," "the candidate who *should* have won" are never absolute — they're shorthand for one of a few reasonable ideals: **most first choices, the majority's choice, the consensus (Condorcet) candidate, or the highest-support (utilitarian) candidate** — plus **proportionality** for multi-winner. Methods differ because they weigh these differently, and the interesting elections are exactly the ones where the ideals disagree. The test cases in this repo exist to make those disagreements concrete.

## The other half of the question

A good *winner* is only half of it. The rest is whether the *method* is practical: simple to vote and count, transparent and auditable, summable by precinct, resistant to strategy, and good for competition (third parties, no spoilers). And "a perfect election system will never exist" — every method trades these against each other. That's the companion page: **[What makes a voting *method* good?](what_makes_a_voting_method_good.md)**.

## See also

- [What makes a voting *method* good? (criteria & practicality)](what_makes_a_voting_method_good.md)
- [Condorcet efficiency (topic hub)](condorcet) · [Ranked Robin vs. "the Condorcet winner"](../RCV_Ranked_Robin/ranked_robin_vs_condorcet.md)
- [Center squeeze](center_squeeze) · [Majority criterion](majority_criterion) · [Spoiler effect](spoiler_effect.md)
- [Why STAR Voting](Why_STAR_Voting.md) · [STAR's honest limits](../STAR_Voting/properties_and_limits/STAR_honest_limits.md) · [Glossary](../GLOSSARY.md)

**External references:** [Utilitarian winner (electowiki)](https://electowiki.org/wiki/Utilitarian_winner) · [Condorcet winner criterion (electowiki)](https://electowiki.org/wiki/Condorcet_winner_criterion) · [Voter Satisfaction Efficiency](https://electionscience.github.io/vse-sim/) · Graham-Squire & McCune, *RCV in the US*, [arXiv:2301.12075](https://arxiv.org/abs/2301.12075) (the Alaska Condorcet failure).
