# Distributed voting — the measured price of counting by district

*A 301 theory page. [Distortion](distortion.md) asks what a **ballot** costs you by recording order instead of degree. This page asks a different question with the same instrument: what does the **architecture** cost you? When voters are partitioned into districts that each elect a representative alternative, and the winner is chosen from among those representatives, the welfare loss is multiplied by **k, the number of districts** — and that factor is there even if every district counts perfect cardinal utilities. It is a cost of the map, not of the paper.*

**Level: 301 · deep dive** Builds on [distortion](distortion.md) (301). Reads naturally after the library's own two-district cases, which turn out to be exactly this model.

Companions: [Distortion](distortion.md) — the parent metric and its two models · [The reinforcement paradox, counted](../../method_comparisons/reinforcement_paradox/) — the same slicing, as a criterion failure rather than a welfare ratio · [Exercise 1 — two districts, one mayor](../../01_STAR/05_Practice/ex01_two_districts.md) — the runnable companion used below · [Multiple districts / consistency](../voting_paradoxes/multiple_districts.md) · [Summability](summability/) — the *other* thing precincts do to a count, and the one this is constantly confused with.

---

## The model, in one paragraph

Take the usual utilitarian setup — `n` agents with hidden values for `m` alternatives, social welfare is the sum of values, the optimum is the welfare-maximizing alternative. Now partition the agents into `k` disjoint **districts**. Each district runs a local election under some in-district rule and declares a **representative alternative**. A second, over-arching rule then picks the winner **from among those representatives**. Mechanisms are named `f_over`-of-`f_in`: Plurality-of-Plurality, Plurality-of-Range-Voting, Uniform-of-Range-Voting.

That is the Electoral College, near enough; it is also a party caucus system, a federated standards body, and any two-stage "each unit picks one, then we pick among the picks" procedure. And it is precisely the shape of [Exercise 1](../../01_STAR/05_Practice/ex01_two_districts.md), which is why that exercise does double duty below.

The literature's question: **how much welfare does the partition itself destroy?**

## The bounds — districting multiplies

The centralized column is standard [distortion](distortion.md); the distributed column is the same quantity once the electorate is sliced into `k` districts.

| Information the mechanism has | Centralized | **Distributed (k districts)** |
|---|:--:|:--:|
| cardinal values, deterministic | 1 (just pick the max) | **Θ(km)** |
| cardinal values, randomized | 1 | **O(k)** — and Ω(k) for any unanimous rule |
| rankings only, deterministic | Θ(m²) | **Θ(km²)** |
| rankings only, randomized | Θ(√m) | **O(k√m)** |
| strategyproof, deterministic | — | **Θ(nm)** (First-of-First) |

Read the pattern down the column: **every row is its centralized counterpart times k.** Slicing the electorate into districts costs a factor equal to the number of districts, and it costs it *on top of* whatever the ballot was already costing.

The row that carries the argument is the first one. With **perfect cardinal information in every district** — every voter's exact utilities, no compression at all — a deterministic districted mechanism still has distortion Θ(km), and no unanimous mechanism of any kind escapes Ω(k). Centralized, that same information gives distortion 1. So the k is not a ballot problem and no ballot reform touches it: it is the structural consequence of requiring that the winner be *somebody's district winner*. The globally best alternative can be a strong second everywhere and win nothing.

**Where the tight bounds come from:** Filos-Ratsikas, Micha & Voudouris (SAGT 2019 / AIJ 2020) established the model and bounded a specific class of deterministic plurality-based mechanisms. Filos-Ratsikas & Voudouris (ToCS 2024, open access) closed it out — asymptotically tight bounds for the *whole* class of deterministic mechanisms, plus the first treatment of randomized ones.

## The one piece of good news, and it is about the ballot

Compare two rows: deterministic districted with cardinal in-district information is **Θ(km)**; with rankings only it is **Θ(km²)**.

The over-rule is identical. The map is identical. The number of districts is identical. The only thing that changed is what the **in-district ballot** records — and it is worth a factor of **m**. Plurality-of-Range-Voting is asymptotically optimal among cardinal mechanisms; Plurality-of-Plurality is asymptotically optimal among ordinal ones, a full factor of m worse.

That is a genuinely useful thing for a reform argument in a country that is not going to stop using districts: **you cannot fix the k from inside a district, but you can fix the m² — and the fix is the ballot.** It is also unusually clean evidence, because it comes from peer-reviewed CS with no stake in the American reform fight. Note carefully what it does *not* say: it does not say a score ballot beats a ranked one at the same task (in the [metric model](distortion.md#model-2-metric-rankings-are-surprisingly-cheap), rankings do fine, and approval-style input is *unbounded*). It says that in this unit-sum setting, richer in-district information buys back one of the two multiplied factors.

## Counted, on ballots the library already has

[Exercise 1 — two districts, one mayor](../../01_STAR/05_Practice/ex01_two_districts.md) is this model with k = 2: eighteen voters, five candidates, nine voters per district, each district running STAR and declaring a winner. Both districts elect **Avery**, so any `f_over`-of-STAR mechanism elects Avery. Counted centrally, STAR elects **Carmen**. Treat the 0–5 scores as the voters' values and the welfare numbers fall straight out of the scoring round:

```text
Scoring Round (all 18 ballots — this IS the utilitarian tally)
   Avery         -- 70 -- First place
   Carmen        -- 64 -- Second place
   Elena         -- 50
   Blake         -- 33
   Diego         -- 33
```

[full report → `cases/cases_pages/ex01_district_combined.md`](../../01_STAR/05_Practice/cases/cases_pages/ex01_district_combined.md)

| Winner under… | Who | Welfare (raw) | Distortion | Welfare (unit-sum) | Distortion |
|---|---|:--:|:--:|:--:|:--:|
| **the districted mechanism** | Avery | **70** | **1.00** | 5.2168 | **1.00** |
| centralized STAR | Carmen | 64 | 1.09 | 4.5967 | 1.13 |
| the [Condorcet winner](condorcet/) | Elena | 50 | 1.40 | 3.3333 | 1.57 |

(Both columns shown because distortion is defined on unit-sum-normalized values, not raw scores; here the ordering is the same either way, so nothing turns on the normalization. Elena's 1.57 is comfortably inside the [metric model's factor-of-3 guarantee](distortion.md#how-is-a-bound-of-3-even-possible-the-triangle-inequality-is-smuggled-in-cardinal-information) for a Condorcet winner, as it must be.)

**And the districted mechanism wins this one outright.** It elects the utilitarian optimum; centralized STAR does not. That is the honest result on the library's own case, and it is worth more than a confirming example would be. The theorem says districting costs up to a factor of k *in the worst case*; it does not say districting costs you anything in particular on any given electorate, and here it cost nothing while the centralized count gave up 13%. The three winners are the [three defensible notions of "best"](../../01_STAR/01_Learn/properties_and_limits/STAR_three_winner_notions.md) pulling apart — score says Avery, majority logic says Elena, STAR's runoff says Carmen — and the districted procedure happened to land on the one distortion is scored against.

## Reading this fairly

Apply the usual [severity × frequency](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md) discipline, because the caveats here are unusually strong and two of them come from the authors' own experiments:

- **Real electorates are homogeneous, and homogeneity is what saves you.** On the Jester dataset the deterministic district effect was real but far milder than the worst-case bounds, and on synthetic data it was milder still — the authors attribute this directly to homogeneity. When districts don't differ much, the winner doesn't either. The k in the bound is a *worst case* over adversarial partitions, and a gerrymander is exactly an adversarial partition, but an ordinary map is not.
- **Randomization looks great in theory and worse in practice.** The randomized mechanisms hold constant distortion as k grows — the headline theoretical win — yet on homogeneous real-world data they had *worse absolute* distortion than the deterministic ones. A bound that doesn't degrade is not the same as a number that is small.
- **This measures welfare and nothing else.** Districts exist for representation, local accountability, and federalism; distortion scores none of that. "Districting has distortion Θ(km)" is an argument about one axis, and treating it as a verdict on districts as such is the same overreach this library flags everywhere else.
- **It is the unit-sum model.** Per the [parent page](distortion.md#two-models-and-the-model-decides-the-verdict), that is the adversarial end. Nobody has run this analysis in the metric model, where ordinal rules do far better; expect the k to survive (it is architectural) and the m² not to.

## The distinction that trips everyone

**Districting is not [summability](summability/).** They both involve precincts and they are unrelated:

- **Summability** asks whether the *count* adds up from precinct subtotals. STAR's score totals and preference matrix both do; IRV's rounds don't. This is a property of the tabulation.
- **Districting** asks what happens when each precinct declares a *winner* and you aggregate the winners. What you cannot add up is a declared winner — and that is true of every method, summable or not.

[Exercise 1's own scenario note](../../01_STAR/05_Practice/ex01_two_districts.md) makes the point on the same ballots: the citywide result is a consistency failure, *not* a summability failure, because the score totals and the matrix added across the two districts perfectly well. What broke was the architecture. Distortion is just the price tag on the break. The criterion-shaped version of the same event is the [reinforcement paradox](../../method_comparisons/reinforcement_paradox/); this page is its welfare-shaped twin.

## Sources

**Academic — the right tier for theorems.**

- Filos-Ratsikas, Micha & Voudouris, [*The Distortion of Distributed Voting*](https://link.springer.com/chapter/10.1007/978-3-030-30473-7_21) (SAGT 2019; journal version *Artificial Intelligence* 286:103343, 2020) — introduces the model; tight worst-case and best-case bounds for plurality-based deterministic mechanisms, plus the first real-data experiments.
- Filos-Ratsikas & Voudouris, [*Revisiting the Distortion of Distributed Voting*](https://link.springer.com/article/10.1007/s00224-024-10171-1) (*Theory of Computing Systems* 68:1138–1159, 2024; **open access**; [arXiv:2301.03279](https://arxiv.org/abs/2301.03279)) — asymptotically tight bounds for the whole deterministic class, the randomized results, and the synthetic + Jester experiments quoted above.
- Anshelevich, Filos-Ratsikas, Shah & Voudouris, [*Distortion in Social Choice Problems: The First 15 Years and Beyond*](https://www.ijcai.org/proceedings/2021/0589.pdf) (IJCAI 2021) — the survey; puts distributed voting in context with the rest of the metric.

**Lean disclosure:** peer-reviewed CS/economics, no stake in the US reform fight — the same neutral tier as the [parent distortion page](distortion.md#sources), with the same blind spot: it optimizes a welfare ratio over models chosen for tractability and says nothing about why districts exist in the first place.

## See also

- [Distortion — the formal price of a ranked ballot](distortion.md) — the parent metric, both models, and the cardinal-query results
- [The reinforcement paradox, counted](../../method_comparisons/reinforcement_paradox/) · [Multiple districts / consistency](../voting_paradoxes/multiple_districts.md)
- [Exercise 1 — two districts, one mayor](../../01_STAR/05_Practice/ex01_two_districts.md) — the runnable companion
- [Summability](summability/) · [Central tabulation](central_tabulation.md) — the two things this is confused with
- [One person, one vote](one_person_one_vote.md) · [False majorities](false_majorities.md) — the political-science framing of the same architecture
- [What makes a good winner?](what_makes_a_good_winner.md) · [Reading these fairly](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md)
