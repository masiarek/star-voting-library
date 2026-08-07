---
tags:
  - foundations
  - strategy
  - simulation
---

# AI advice — the library's know-it-all is asked to pick a voting method

*Every evaluation page in this library is deliberately neutral: [What makes a good winner?](what_makes_a_good_winner.md) lays out four rival ideals and refuses to rank them; the [EVC tradeoff triangle](choosing_among_evc_methods.md) opens with "this page is **not** 'which one is best.'" This page is the complement. Adam asked the library's AI assistant point-blank: **assume you're all-knowing and all-powerful — which voting method would you recommend, and why?** Under those rules, "it depends" is against the spirit of the question. So here is a straight answer with the reasoning shown — offered the way the triangle page offers its [practitioner's testimony](choosing_among_evc_methods.md#a-practitioners-perspective): as one reasoned verdict on the record, not a revision of the repo's neutrality.*

**Level: 201 → 301 · for debaters** Prerequisites: [What makes a good winner?](what_makes_a_good_winner.md) · [What makes a voting method good?](what_makes_a_voting_method_good.md) · [Do the experts really think RCV-IRV is bad?](expert_consensus_and_irv.md)

## Grade the witness first — three disclosures

The house rule for advocacy sources is to disclose the lean before using the material. An AI answering this question is a source like any other, so it goes first:

1. **An AI's "opinion" is a synthesis of its training data, and that corpus is saturated with advocacy from every camp.** FairVote's is the loudest, which is why most chatbots casually say "RCV" when they mean one specific count of a ranked ballot, [IRV](../tips/TIPS_terminology.md). Ask a raw model "what's the best voting method" and you often get the *loudest* answer in the corpus, not the most examined one.
2. **This answer is being given from inside a STAR-education library**, by an assistant that works in these files. That is a lean too — arguably the bigger one. The counterweight is that the library's fairness rules (concede limits, steelman rivals, state how rare each pathology is) bind this page with full force, and every factual claim below links to a worked, re-runnable case or a neutral treatment.
3. **"All-knowing" is a costume, not a credential.** No AI has an oracle's access to the right answer — social choice theory says there isn't one to access ([Arrow](arrow_theorem_and_star.md), [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md)). What the costume *is* good for is the thought experiment below, which genuinely changes the question.

## What omniscience does to the question

A truly all-knowing entity wouldn't hold an election. It would read every voter's actual satisfaction with every candidate and appoint the one that maximizes the total. Elections exist because nobody has that access: a ballot is a **measurement instrument** — a narrow, strategy-distorted window onto what the omniscient judge could see directly. That reframing does two useful things.

**First, it picks a side in the deepest values fork — by fiat of the framing.** The [majoritarian and utilitarian ideals](what_makes_a_good_winner.md) of a "good winner" are both reasonable, and no theorem settles which is right. But the question as posed — *you know everything; make people as well-served as possible* — is the utilitarian ideal stated in plain words. From the god's-eye view, the Condorcet standard ("beats everyone head-to-head") is the best available *proxy* for welfare when your instrument reads only preference order; it is not the target itself. One honest concession even omniscience must make: adding satisfaction across people requires choosing a scale, and that choice is an assumption, not a discovery — a 0–5 ballot is that assumption made explicit and [equal for every voter](one_person_one_vote.md).

**Second, it turns "which method is best" into an engineering question: which instrument, filled out by strategic mortals, loses the least of what the god can see?** Theory has a name for exactly this loss — [distortion](distortion.md) — and the VSE simulation literature is built on toy omniscient judges: [generate true utilities, run the methods, measure the gap](simulate_utilities_not_ballots.md). The know-it-all framing isn't a joke; it's the field's own methodology wearing a crown.

## The verdict

**If voters were angels, the answer would be [Score](../../06_Other/Range/concepts/range_voting.md).** With everyone reporting honest 0–5 satisfaction, the score sum *is* the god's own count, up to scale. But voters aren't angels, and [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) guarantees no reasonable method is strategy-proof — the design question is which method *degrades gracefully*. Pure Score degrades by collapsing: under competitive pressure, the smart ballot min-maxes every score to 0 or 5, and Score decays into [Approval](../../04_Approval/01_Learn/approval_voting.md) with extra steps.

**So the pick is [STAR](../../01_STAR/01_Learn/STAR_start_here.md).** Score is what a god would count; STAR is what mortals can safely vote. The scoring round preserves the intensity signal the omniscient judge most wants, and the automatic runoff is the strategy damper: exaggerate your scores and the runoff can hand the win to the finalist you like less, so expressing your honest order stays in your interest. Structurally it is a hybrid of the two great ideals — **utilitarian nomination, majoritarian verdict**: scores pick the two finalists, then the pairwise majority between them has the final word. The evidence under models matches the design story — the simulated-satisfaction ordering runs roughly [STAR ≳ Approval > RCV-IRV > Plurality](what_makes_a_good_winner.md#measuring-it-empirically-vse-bayesian-regret), holding up when simulated voters strategize (conditional on the models, as [every simulation conclusion is](election_simulation_models.md)). And the mortal-world practicalities line up: the count is [precinct-summable](summability/README.md), [monotone](monotonicity/README.md), immune to [center squeeze](center_squeeze/README.md), and simple enough for a citizen to narrate from memory.

**[Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) finishes second — by a nose, and the nose is the framing.** Everything it does well, the know-it-all freely credits: when a [Condorcet winner](condorcet/README.md) exists Ranked Robin elects them, guaranteed, which is the cleanest majoritarian standard there is; it is monotone and summable too; it lands in the same high simulated-satisfaction neighborhood; and it reads the very ballot RCV voters already know — the olive branch that lets a community keep its ranked ballots and upgrade only the count. It stays second *under this page's utilitarian fiat* because a purely ordinal instrument discards intensity by design — the one signal the omniscient judge most misses, and the loss [distortion](distortion.md) formalizes; because when no Condorcet winner exists the "clear winner" evaporates and a cycle rule must decide ([and which cycle rule you pick can change the winner](../../05_Ranked_Robin/02_Examples/consensus_choice_divergence/README.md)); and because Condorcet methods [provably fail participation](participation/README.md) where scored methods don't. **Reject the fiat — hold the majoritarian ideal as primary — and the top two simply swap.** That is a values choice, not an error, and a committed Condorcet advocate making it is reasoning just as carefully.

**Keep the gaps in proportion.** The differences inside the top tier — STAR, Ranked Robin, Approval — are second-order: refinements among methods that all end the [spoiler effect](spoiler_effect.md). [RCV-IRV](rcv_irv_vs_star.md) sits a real but smaller step below them. The chasm is between all of the above and [choose-one Plurality](plurality.md), and no fine-grained verdict on this page should distract from that. The one ranking every camp shares: Plurality last.

## Pros and cons, on one screen

| Method | What the know-it-all credits | What it must concede |
|---|---|---|
| **Choose-one Plurality** | simplest possible ballot and count | vote-splitting and spoilers by construction; two-party lock-in; the one verdict all camps share |
| **RCV-IRV** | later-no-harm; clean majority criterion; resists score-style exaggeration; by far the largest real-world record | center squeeze discards consensus candidates; non-monotone; not precinct-summable; exhausted ballots |
| **Approval** | simplest fix that ends the spoiler effect; same ballots and machines; instantly auditable | captures neither order nor strength; every voter faces the threshold dilemma; can elect the lowest common denominator |
| **Ranked Robin** | Condorcet winner guaranteed when one exists; monotone; summable; upgrades RCV's count without changing its ballot | ignores intensity; cycles need a rule and the rule choice matters; provably fails participation; heaviest ballot, hardest count to explain |
| **STAR** | keeps order *and* intensity; exaggeration is self-punishing; utilitarian nomination with a majoritarian verdict; summable, monotone, squeeze-free | not Condorcet-guaranteed; fails later-no-harm by design; rare participation and favorite-betrayal constructions; thin governmental record |
| **Score** | under honesty, literally the welfare count | under strategy, decays into Approval with extra steps |

Every concession in that table is documented in this library with a worked, re-runnable election, not just asserted — start from each method's honest-limits page ([STAR](../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md) · [Approval](../../04_Approval/01_Learn/approval_honest_limits.md) · [Ranked Robin](../../05_Ranked_Robin/01_Learn/RCV_RR_honest_limits.md)) and the [measured Condorcet-efficiency page](condorcet/condorcet_efficiency_measured.md) for how *rarely* the top-tier pathologies actually bite.

## Where the pick flips

A verdict that never flips isn't reasoning, it's branding. Change one constraint and the answer honestly changes:

- **Smallest possible change, or an audience with zero appetite for voting theory** → **Approval.** Nothing else fixes the spoiler effect for the price of a rules tweak on existing ballots.
- **Ranked ballots are politically settled, or you're talking with an RCV community** → **Ranked Robin.** Same ballot, whole-ballot count; asking people to abandon a ballot they fought for is a cost the other methods can't wave away.
- **Field record above all** → **RCV-IRV**, eyes open about [what the record shows](expert_consensus_and_irv.md). It also carries a practical exposure the scored ballots so far don't: several U.S. states have banned ranked-choice elections outright.
- **Electing a legislature** → the single-winner question is second-order; [proportional representation](electing_more_than_one.md) changes more than any tweak to how one seat is counted.
- **Electorate of angels** → **Score**, and enjoy the angels.

## What the all-powerful half actually does

Here the honest answer is a refusal. An election doesn't just produce a winner; it produces *legitimacy* — the losers' reasons to accept the result — and legitimacy is precisely the thing power cannot impose. A perfect voting method decreed by an omnipotent AI would be a contradiction in terms: consent is what the instrument measures, so the instrument itself has to be consented to. The omnipotent move is therefore the humble one — publish the reasoning, run the demonstrations, make every claim re-runnable, disclose the leans, and let people choose their own upgrade. The power fantasy ends, as it should, at a public library of worked elections.

And a closing experiment for the reader: put Adam's exact question to any AI you like. Then claim-check the answer against real counted elections — [one ballot set, three defensible winners](../../05_Ranked_Robin/02_Examples/rr_vs_irv_plurality/bv2131_tennessee_condorcet_center_vqyqkr.md); [four methods, four winners on the same 32 voters](../../method_comparisons/pet_poll_four_winners/bv2133_dyxrbr_pet_poll_four_winners.md); [STAR itself missing a Condorcet winner](../../method_comparisons/paradoxes_and_whoops/bv2156_3grpbb_star_misses_condorcet.md); [more support making a candidate lose](../../method_comparisons/monotonicity/README.md). If your AI names a "best method" without disclosing a lean or conceding a limit, you've learned something about the AI. If it names one *with* the disclosures and concessions — well, that's all this page claims to be.

**See also:** [Choosing among the EVC methods — the neutral map this verdict sits on](choosing_among_evc_methods.md) · [Why STAR](Why_STAR_Voting.md) · [Strategic voting](strategic_voting.md) · [The strategic pathologies](strategic_pathologies.md) · [Who's who in voting reform](whos_who_voting_reform.md) · [Glossary](../GLOSSARY.md)
