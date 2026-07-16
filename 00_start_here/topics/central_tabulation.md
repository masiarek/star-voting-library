# Central Tabulation — When Every Ballot Must Travel

*The operational price of a non-summable count: ballots (or full cast-vote records) must be gathered in one place before anyone can name the winner — a single point of failure, and a heavier, slower audit. This page expands the one-line cost bullet into what it actually means on the ground.*

→ **Level: Voting 201** — Curriculum [201.1](../CURRICULUM.md) (reading the results) · the math side: [Summability topic hub](summability/) · Glossary: [`summability`](../GLOSSARY.md)

---

## Two ways to count an election

- **Precinct (local) count:** each precinct tallies its own ballots into a small fixed-size table — score totals, approval counts, a [pairwise matrix](pairwise_counting.md) — publishes it, and the jurisdiction **adds the tables**. The ballots never have to leave. Any method whose count works this way is [**summable**](summability/).
- **Central tabulation:** the ballots themselves — or their electronic images, the **cast-vote records (CVRs)**, one record per ballot listing everything that voter marked — must be **gathered in one place** and run through one count, because no precinct subtotal can stand in for them.

Which one a jurisdiction *needs* is a property of the voting method's count. IRV (and STV, and every sequential-elimination variant) is the prominent method that structurally **requires** central tabulation: who gets eliminated in round 2 depends on the *combined* round-1 totals of every precinct, so the count can't start until every ballot's full ranking is in one system. The worked two-district demonstration — B wins both districts, B is eliminated when they merge — is on [IRV is not summable](../RCV_IRV/RCV_IRV_lack_of_summability.md); this page is about what the centralization itself costs.

The methods that *don't* need it publish an artifact that adds: [STAR](../STAR_Voting/properties_and_limits/STAR_summability.md) (score totals + the pairwise matrix), [Ranked Robin](../RCV_Ranked_Robin/RCV_RR_summability.md) (the pairwise matrix alone — the *same ranked ballots* IRV must pool), Approval and Plurality (one count per candidate).

## Cost 1 — a single point of failure

Everything converges: one facility, one tabulation system, one software configuration, one team. That concentration shows up three ways.

- **The transport becomes part of the security perimeter.** Ballots or memory devices now travel, so chain-of-custody — couriers, seals, transmittal forms, locked storage — is no longer a formality but load-bearing. Maine, the first state with statewide IRV, runs exactly this operation for every ranked count: a contracted courier (with law-enforcement escort) retrieves sealed memory devices and ballots from the affected municipalities and delivers them to one counting facility in the Augusta area ([Maine Secretary of State, RCV FAQ](https://www.maine.gov/sos/elections-voting/ranked-choice-voting-frequently-asked-questions) · [tabulation explainer](https://www.maine.gov/sos/sites/maine.gov.sos/files/content/assets/RCVTabulationExplainer.2020.pdf)). It works — but it is a real, recurring logistics-and-security operation that a summable count simply doesn't need.
- **One configuration error changes every race at once.** In Alameda County's November 2022 election, the central RCV tabulator was misconfigured in how it handled ballots with a skipped ranking. Every RCV race in the county ran through that one setting; in one of them — Oakland school board, District 4 — it certified the wrong winner, and the error was only caught **weeks after certification**, when an outside recompute of the published CVRs didn't match ([Ballotpedia news](https://news.ballotpedia.org/2023/01/26/tallying-error-in-oakland-calif-led-to-inaccurate-election-results/); the full post-mortem is an academic paper: [“Ranked Choice Bedlam” in a 2022 Oakland school director election](https://arxiv.org/abs/2303.05985)). (Fair note: the recompute that caught it came from FairVote — the leading IRV advocacy organization — checking its own method's counts; credit where due.)
- **One central operation is one place for a mistake to be big.** New York City's first RCV mayoral primary (June 2021) published a preliminary central tally with roughly **135,000 test ballots** accidentally included from a test run of the central system; it was caught and corrected within days, but only because the error was enormous ([Wikipedia](https://en.wikipedia.org/wiki/2021_New_York_City_Democratic_mayoral_primary)). A decentralized count has many small failure domains; a central count has one large one.

None of these incidents is an argument that IRV picks wrong winners — they're counting-operations failures, and two of the three were caught and fixed. The point is structural: the method's count *concentrates* the operation, so the failure modes concentrate with it.

## Cost 2 — a heavier, slower audit

With a summable method, verification is cheap and local: each precinct's published table can be recomputed from that precinct's own ballots by anyone, and the statewide result is just the sum — checking the addition is arithmetic. Batch- and precinct-comparison audits fall out for free, and a precinct can certify its own contribution to the outcome.

Central IRV gives that up. There is no precinct subtotal to check, so an audit has to engage the whole ballot set: a full CVR file, plus machinery that can handle the fact that small errors can matter only via some *intermediate* elimination round. Rigorous [risk-limiting audits](https://en.wikipedia.org/wiki/Risk-limiting_audit) for IRV do exist — [RAIRE](https://arxiv.org/abs/1903.08804) (Blom, Stuckey & Teague) turns an IRV outcome into a set of testable assertions and audits them by ballot comparison — but that is specialized, newer machinery with heavier prerequisites (complete, trustworthy CVRs from a central system), versus "publish the precinct tables and add them up."

And the *results themselves* are slower and murkier along the way: partial counts under IRV are easy to misread (the first-choice leader partway through can lose once transfers run), and the definitive count can't even begin until the last ballots arrive — in Maine's case, after the courier run, days after election night.

## The honest caveats

- **Plenty of jurisdictions centrally count anyway.** Vote-by-mail states run central-count scanners as a matter of logistics, whatever the voting method. The difference is *optionality*: with a summable method, central counting is a choice, and cheap public checks (precinct/batch subtotals that add) exist regardless of where the scanners sit. With IRV it's structural — no subtotal can stand in for the ballots, so the checks have to be rebuilt the heavy way.
- **Published CVRs are a real mitigation.** Alameda 2022 is simultaneously the cautionary tale *and* the proof that transparency works: the county published full CVRs, an outsider re-ran the count, and the error surfaced. But note what the check required — downloading every ballot record and re-running tabulation software — versus adding a column of published precinct tables by hand.
- **It's the count, not the ballot.** The same ranked ballots, counted by [Ranked Robin](../RCV_Ranked_Robin/RCV_RR_summability.md), tally locally into pairwise matrices that add — no ballot has to travel. "Ranked ballots require central counting" is the same myth as "ranked ballots can't be summed," and it's wrong for the same reason: this is a property of **IRV's elimination count**, not of ranking. ([electowiki](https://electowiki.org/wiki/Summability_criterion) has the formal criterion; it's an advocacy-adjacent wiki, fine for the definition.)

---

## Cross-references

- [Summability topic hub](summability/) — the mathematical property whose absence forces central tabulation (STAR / Ranked Robin / IRV side by side, and the multi-winner seat-capping story)
- [IRV is not summable](../RCV_IRV/RCV_IRV_lack_of_summability.md) — *why* no precinct subtotal exists, with the two-districts worked example this page leans on
- [STAR is summable](../STAR_Voting/properties_and_limits/STAR_summability.md) · [Ranked Robin is summable](../RCV_Ranked_Robin/RCV_RR_summability.md) — the methods that keep the local count
- [Pairwise counting — every ballot is a tiny matrix](pairwise_counting.md) — the artifact precincts publish instead of shipping ballots
- [What makes a voting method good?](what_makes_a_voting_method_good.md) — where auditability and summability sit among the criteria
- Glossary: [`summability`, `preference matrix`](../GLOSSARY.md)
