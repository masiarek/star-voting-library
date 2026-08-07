# Concepts — by topic (cross-method view)

This folder holds the library's **cross-method concept pages** — the ideas that don't belong to any single method — in two forms: the flat **concept pages** (below) and the **topic hubs** (subfolders): thin index pages that gather one cross-method idea and link out to each method's authoritative treatment. Method-specific concept pages stay in the per-method folders under [07_Concepts](../README.md) (STAR_Voting/, RCV_IRV/, RCV_Ranked_Robin/…), because that's how most people arrive.

**The hubs don't duplicate content** — the detailed write-ups stay in the per-method folders. A hub is just the shared definition plus a "which methods, and where" table, so there's almost nothing to keep in sync. Browse by method *or* by topic, whichever fits.

## Start here — the meta-question

Before the per-topic criteria: **what are we even optimizing for?**

- [**What makes a good winner?**](what_makes_a_good_winner.md) — the "correct" winner, consensus/Condorcet vs. utilitarian vs. majority, and why there's no single ideal.
- [**What makes a voting *method* good?**](what_makes_a_voting_method_good.md) — the criteria beyond the winner (simplicity, summability, auditability, honesty/strategy, competition), VSE, and "a perfect system will never exist."
- [**Election simulation models**](election_simulation_models.md) — how VSE studies generate synthetic electorates (Impartial Culture, spatial, Mallows, urn…), and why results depend on the model.
- [**AI advice — a verdict, on the record**](ai_advice.md) — the one page that *does* pick: asked to play all-knowing and all-powerful, the library's AI names STAR by a nose over Ranked Robin, shows the reasoning, states where the pick flips — and discloses its own leans first.

## Topic hubs

| Topic | What it compares | Hub |
|-------|------------------|-----|
| **Summability** | which counts add up from precinct subtotals (STAR ✅, Ranked Robin ✅, IRV ❌) | [Summability](summability/README.md) |
| **Monotonicity** | where more support can backfire (all elimination methods ❌; STAR ✅, Ranked Robin ✅) | [Monotonicity](monotonicity/README.md) |
| **Center squeeze** | who eliminates the moderate (Hare/Contingent ❌; whole-ballot methods ✅) | [Center squeeze](center_squeeze/README.md) |
| **Condorcet efficiency** | who elects the head-to-head winner (Ranked Robin/BTR ✅, STAR ⚠️, IRV ❌) — and [how often, measured](condorcet/condorcet_efficiency_measured.md) | [Condorcet efficiency](condorcet/README.md) |
| **Ties & tie-breaking** | where ties arise and how the lot order settles them | [Ties & tie-breaking](ties/README.md) |
| **Majority Criterion** | must a majority's favorite win? + the Relaxed Majority Criterion & the Later-No-Harm link (IRV ✅; STAR ❌ but mild; Score/Approval ❌) | [Majority Criterion](majority_criterion/README.md) |
| **"Majority" / "minority" candidate** | the *words*, not the criterion — five senses of "majority candidate", what "majority" means on a *score* ballot, why "minority winner" is nearly automatic in a big field, and what makes it a real indictment | [Majority & minority candidates](majority_criterion/majority_and_minority_candidates.md) |
| **Participation** | can showing up to vote ever hurt you? the no-show/Twin paradoxes, live (Score/Approval/Choose-One ✅; STAR ❌ rare; IRV ❌ readily; Condorcet methods ❌ provably) | [Participation](participation/README.md) |
| **Districting** | when the *lines* decide, not the count — the reinforcement paradox, the candidate who wins no district, seats vs. votes, and why a better ballot cannot fix any of it (no method is immune) | [Districting](districting/README.md) |
| **Burial** | sinking a rival you actually like, so they lose a comparison they'd win (Ranked Robin/Copeland ❌ its named risk; Borda ❌ notoriously; STAR ⚠️ rarely pays; IRV ✅ later-no-harm) | [Burial](burial/README.md) |

*(Add a new hub when a topic is clearly treated in 2+ method folders. A candidate still open: **vote-splitting** — see [the split-voting set](../../method_comparisons/split_voting/README.md) for the worked examples.)*

## Concept pages in this folder

**The problem, and the case for reform:** [our voting system is broken](our_voting_system_is_broken.md) · [the problem, in four causes](the_problem_in_four_causes.md) · [the spoiler effect](spoiler_effect.md) · [wasted votes](wasted_votes.md) · [two-party dominance](two_party_dominance.md) · [false majorities — over half the seats on under half the votes](false_majorities.md) · [does a better ballot end polarization?](does_better_voting_end_polarization.md) · [plurality](plurality.md) · [strategic voting](strategic_voting.md) · [Why STAR Voting](Why_STAR_Voting.md) · [RCV-IRV vs STAR](rcv_irv_vs_star.md)

**Ballots & what they capture:** [what is a voting method?](what_is_a_voting_method.md) · [what a method reads — its informational basis](what_a_method_reads.md) · [a ballot and a count](voting_method_ballot_and_count.md) · [ballot & terminology basics](ballot_and_terminology_basics.md) · [alternate ballot styles](ballot_styles.md) · [same opinions, every method — the line-up](same_opinions_every_method.md) · [preference](preference.md) · [scoring methods vs. ranked voting](scoring-methods-vs-ranked-voting.md) · [the ranked-ballot method zoo](ranked_ballot_methods_zoo.md) · [3-2-1 voting (vs. STAR)](three_two_one_voting.md) · [tabulation, step by step](tabulation_star_vs_irv.md) · [pairwise counting & the preference matrix](pairwise_counting.md) · [central tabulation](central_tabulation.md)

**Evaluating methods:** [what makes a good winner?](what_makes_a_good_winner.md) · [what makes a voting method good?](what_makes_a_voting_method_good.md) · [criteria at a glance](criteria_at_a_glance.md) · [the strategic pathologies (five Molochs)](strategic_pathologies.md) · [PVSI — the strategic-incentive metric](pvsi_strategic_incentive.md) · [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) · [does Arrow's theorem apply to STAR?](arrow_theorem_and_star.md) · [the social welfare function — what Arrow's theorem is about](social_welfare_function.md) · [May's theorem](mays_theorem.md) · ["one person, one vote"](one_person_one_vote.md) · [the Smith set](smith_set.md) · [the uncovered set](uncovered_set.md) · [tournament solutions](tournament_solutions.md) · [the cycle–cocycle decomposition](cycle_cocycle_decomposition.md) · [election simulation models](election_simulation_models.md) · [simulate utilities, not ballots](simulate_utilities_not_ballots.md) · [the statistics you need](statistics_for_voting.md) · [the spatial voting model](spatial_voting_model.md) · [distortion — the formal price of a ranked ballot](distortion.md) · [misrepresentation — the measure that hands Borda the trophy](misrepresentation.md) · [distributed voting — the price of counting by district](distributed_voting_distortion.md) · [cardinal utility — the number a score ballot reaches for](cardinal_utility.md) · [ordinal vs. cardinal, as mechanism design](ordinal_vs_cardinal_mechanism_design.md) · [expert consensus & IRV](expert_consensus_and_irv.md) · [AI advice — a verdict, with disclosures](ai_advice.md) · [counting under encryption](homomorphic_tallying.md)

**Mechanics & multi-winner:** [electing more than one](electing_more_than_one.md) · [comparing multi-winner methods](comparing_multiwinner_methods.md) · [quorum](quorum.md) · [the YAML election file & its pipeline](../../YAML_library/README.md)

**People, orgs & learning paths:** [how to learn about voting methods](how_to_learn_about_voting_methods.md) · [books on voting methods](../books/README.md) · [choosing among the EVC methods](choosing_among_evc_methods.md) · [advocacy organizations](advocacy_organizations.md) · [who's who in voting reform](whos_who_voting_reform.md) · [in memoriam: Jameson Quinn](in_memoriam_jameson_quinn.md)
