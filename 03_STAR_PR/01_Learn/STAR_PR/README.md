# STAR-PR — proportional STAR, and its methods

**One line:** STAR-PR fills **several seats proportionally** using ordinary STAR **score ballots** (0–5). After each seat is awarded, the ballots that helped win it are **reweighted** (their remaining influence is reduced), so the next seat reflects the voters who haven't been represented yet. Same scored ballot as single-winner STAR — different counting, run as many times as there are seats.

→ STV (the ranked-ballot proportional method) side by side with STAR-PR: [STV vs STAR-PR](../stv/proportional_stv_vs_star.md) · Glossary: [`Proportional STAR`](../../../07_Concepts/GLOSSARY.md) · Curriculum: [`301.1`](../../../07_Concepts/CURRICULUM.md) · Level: **Voting 301**

---

## The core idea: quota + reweighting

A proportional method shares the seats among coalitions in proportion to their support, instead of letting the largest group take everything. Two ingredients:

1. **A quota** — the share of support that earns one seat. STAR-PR uses the **Hare quota**, `votes / k` — for 3 seats, one third. (The other standard formula, the **Droop quota** `⌊votes / (k+1)⌋ + 1`, is what STV normally uses; it is smaller, so it is easier to reach. Hare-with-greatest-remainders is the *unbiased* one; Droop tilts toward larger factions but resists strategic voting better. (The shorthand "Hare helps small factions" is only true *relative to Droop* — see [seat bias](../../../07_Concepts/GLOSSARY.md).) Don't mix them up when quoting a threshold: the engine prints `Hare quota is …` for `allocated` and `Hare score quota is …` for `sss`, and the [Hare Quota Criterion](../what_proportional_means.md) is named after this one.)
2. **Reweighting** — once a candidate is seated, the ballots that scored them highly have "spent" some of their weight, so they count for less when the next seat is decided. That is what stops a 58% majority from sweeping all the seats.

This is the whole difference from **[Bloc STAR](../../../02_STAR_Bloc/01_Learn/bloc_star.md)**, which runs the ordinary STAR count once per seat with no reweighting — and is therefore *majoritarian*, not proportional (see the contrast below). (It is *not* "the top N score-leaders": each seat is settled by its own runoff, so the point leader can [win no seat at all](../../../02_STAR_Bloc/01_Learn/score_leader_no_seat.md).)

## The three STAR-PR methods

All three use the same score ballots and differ only in *how* a ballot's weight is spent after each seat. The LH engine runs each via `voting_method:` plus `num_winners: k`.

| Method | `voting_method` | How it reweights, in a line |
|---|---|---|
| **Allocated Score** | `allocated` | Seat the top scorer, then fully **spend a quota's worth** of the ballots that supported them most (those ballots are "used up"); repeat. This is the Equal Vote Coalition's recommended "STAR-PR." |
| **Sequentially Spent Score** (SSS) | `sss` | Like Allocated Score, but each supporting ballot **spends score proportionally** toward the quota rather than being fully exhausted — a smoother allocation. |
| **Reweighted Range Voting** (RRV) | `rrv` | Don't spend ballots; instead **divide each ballot's weight** by a growing factor based on how much score it has already given to winners (a D'Hondt/Jefferson-style divisor). |

**The trade between these families cuts both ways.** Classical apportionment theory (Pukelsheim, ch. 9) proves a **Coherence Theorem**: a method is coherent — meaning every subset of the winners, re-solved on its own, gives the same answer — *if and only if* it is a **divisor** method. Quota methods are not coherent, and they are also not house-size monotone or vote-ratio monotone, which is why they are the family historically prone to the **Alabama paradox** (add a seat, someone loses one), the **population paradox**, and the **no-show paradox**. The German Bundestag abandoned Hare-quota-with-greatest-remainders in 2008 for precisely this reason.

So the honest framing is a genuine [Balinski–Young](the_math_behind_proportional_star.md) trade, not a winner: **Allocated Score is a quota method** — it guarantees a quota-sized group a seat, and buys that guarantee from the family with the monotonicity problems. **RRV is a divisor method** — coherent and monotone, and it pays for that by not guaranteeing quota. Neither is simply better.

**Does this actually bite STAR-PR? Nobody here has checked, and it is very much checkable.** Allocated Score is *not* literally a classical quota method: it is sequential, it works on a ballot matrix rather than party vote totals, and its "residual fit" hands back **ballot weight** rather than awarding whole seats. The theorems are proved for the one-shot party-list setting, so they do not transfer automatically. The concrete open question, and a good one for this library: **run a STAR-PR election at N seats and at N+1, and see whether anyone loses a seat.** If Allocated Score is Alabama-free, that is worth knowing and worth publishing; if it is not, that is worth knowing more.

**They are not equally proportional, and it's worth being precise about that.** Allocated Score and SSS are quota-based allocation methods. RRV is a *divisor* method and **does not pass the [Hare Quota Criterion](../what_proportional_means.md)** — a faction holding a quota's worth of voters cannot always force a seat by voting as a bloc — which is why some classify it as **semi-proportional** rather than proportional. Equal Vote's own summary of the trade: RRV is the mathematically simplest tabulation and the oldest cardinal-PR proposal, but tends toward more utilitarian and less diversified winners, and is less transparent to non-mathematicians. SSS they describe as innovative, easy to explain, and promising, but newer and still a proposal for further study. (Their assessment of methods they advocate — the criterion itself is standard and checkable.)

In practice, on a clean two-coalition electorate all three tend to **agree on the slate** (see the worked example below); they diverge on closer or more fragmented races, which is exactly where the criterion difference bites.

### Allocated Score, step by step

The recommended method, in the three moves the count actually makes:

1. **Winner selection** — for each seat, elect the highest-scoring candidate.
2. **Allocating voters** — mark **one quota's worth** of that winner's strongest supporters as represented. Supporters are sorted into groups by the score they gave the winner: the 5-star group is allocated first, then 4-star, and so on until the quota is filled.
3. **Fractional surplus** — the last group added is usually a little larger than the quota needs. The "extra votes" are returned to that group and shared evenly among them, so those voters keep partial influence over later seats.

Subsequent rounds include everyone not yet *fully* represented — partial representation is real here, which is the point of a scored ballot: it records not just whether a voter is represented but **to what degree**.

Fractional surplus is what makes step 3 fair rather than arbitrary: voters who gave the winner the *same* score are treated the same, instead of an alphabetical or random cut deciding which of them gets used up. ([electowiki](https://electowiki.org/wiki/Allocated_Score) adds that it preserves independence of irrelevant alternatives and monotonicity, though that claim carries a `citation needed` there — treat it as unverified.)

**Three variants worth recognizing**, since they get named in the same discussions:

- **Droop-quota Allocated Score** — swapping Hare for Droop mitigates free-riding but biases toward larger factions.
- **Sequential Monroe** — Allocated Score with a different *selection* rule (highest-scoring quota rather than highest-scoring candidate). One of the committee's three finalists; **the LH engine does not implement it**.
- **Allocated STAR** — adds a runoff on the **final** seat, so the last seat is decided the way single-winner STAR decides one: two finalists, the one more voters prefer. Intended to keep voters expressing a full preference order.

*Provenance:* Allocated Score is the consensus method of the Equal Vote 0–5 STAR Proportional Representation Research Committee, which spent roughly two years from 2018 comparing options at each stage of the tabulation (credited to Parker Friedland, Keith Edmonds, Jameson Quinn, Sara Wolk and others). That is an advocacy body selecting among methods it favors — the *procedure* is precisely specified and independently reimplementable, which is what makes it checkable here regardless.

## The majoritarian contrast: Bloc STAR

`voting_method: bloc` runs STAR's score-then-runoff *N* times with **no reweighting**, so the largest bloc can win **every** seat. It's useful when you *want* an at-large majority result, and it's the method to **avoid when you want proportionality**. Keep it in the comparison precisely to show what reweighting buys you.

## Run them

```
voting_method: allocated   # or: sss | rrv   (proportional)
num_winners: 3
```

Worked examples in [`03_STAR_PR/`](../../README.md):

- [Allocated Score](../../02_Examples/cases/cases_pages/02a_c5_b63_proportional-allocated-score.md) — the same 63 ballots, seat by seat ([yaml](../../02_Examples/cases/02a_c5_b63_proportional-allocated-score.yaml))
- [SSS](../../02_Examples/cases/cases_pages/02b_c5_b63_proportional-sss.md) — same ballots, budget-spending reweight ([yaml](../../02_Examples/cases/02b_c5_b63_proportional-sss.yaml))
- [RRV](../../02_Examples/cases/cases_pages/02c_c5_b63_proportional-rrv.md) — same ballots, D'Hondt divisor ([yaml](../../02_Examples/cases/02c_c5_b63_proportional-rrv.yaml))
- [STAR-PR, 3 seats](../../02_Examples/cases/cases_pages/03b_star_pr_3seats.md) — the same race as the STV file ([yaml](../../02_Examples/cases/03b_star_pr_3seats.yaml))
- [Bloc STAR, 2 seats](../../../02_STAR_Bloc/02_Examples/cases/cases_pages/01_c4_b2_bloc-star-2-seats.md) — the majoritarian contrast ([yaml](../../../02_STAR_Bloc/02_Examples/cases/01_c4_b2_bloc-star-2-seats.yaml))

The head-to-head with STV, on one shared electorate, is in [STV vs STAR-PR](../stv/proportional_stv_vs_star.md): STV and all three STAR-PR methods land on the same proportional slate; Bloc STAR doesn't.

## Why proportional representation? (pros & cons)

Proportional representation elects candidates *in proportion to their support*: if a faction is a fifth of the electorate and votes together, it earns roughly one of five seats. The goal is a "round table" where any faction with enough support has a seat — in direct contrast to Bloc STAR, which lets the majority take **every** seat. This mirrors the public-facing framing on [starvoting.org/star-pr](https://www.starvoting.org/star-pr), condensed for reference.

**Pros:**

- **Diversity of representation** — smaller factions win seats even without a majority, so more voters end up genuinely represented.
- **Coalition-building** — factions must band together to pass anything, which rewards negotiation over winner-take-all.
- **Breaks two-party lock-in** — minor parties can gain a foothold where they'd never win a single-winner seat.
- **Mitigates gerrymandering** — multi-member districts are far harder to draw for advantage (though solving districting directly is better where possible).

**Cons:**

- **Less accountability over a specific incumbent** — with *k* seats, it can take roughly `k/(k+1)` of voters opposing someone to unseat them; smaller districts (fewer seats each) raise that bar back up. STAR-PR's expressive ballot softens this by surfacing less-polarizing candidates.
- **More complex to tally and less transparent** than single-winner or Bloc — voters may not fully follow how winners are determined (STAR-PR is still simpler than STV, but it's not trivial).
- **Possible stagnation** — hard-line factions can refuse to coalition and block legislation as leverage.
- **Not batch-summable** — STAR-PR ballots can't be tallied precinct-by-precinct and summed; they must be **centrally tabulated and audited** per election. That makes it best suited to local elections, or to regional multi-member districts at larger scale.

**The case for STAR-PR specifically:** the same 0–5 ballot works for single-winner, Bloc, and proportional races, so voters learn one ballot. The expressive scores give the method more to work with — it can favor broadly-supported candidates over polarizing ones — while keeping the tally simpler than ranked proportional methods like STV. It's non-partisan by default, though it can back a party-list system if desired, and pairs well with small/local districts to preserve accountability.
