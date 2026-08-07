# Why more candidates make every method miss

→ Topic hub: [Condorcet efficiency](README.md) · the rates this explains: [Condorcet efficiency, measured](condorcet_efficiency_measured.md) · the worked election: [the crowded field](../../../method_comparisons/crowded_field/README.md) · the simulation: [`condorcet_efficiency_simulation.py`](../../../06_Other/simulations/condorcet_efficiency_simulation.py) · **Level: 301 · deep dive**

[Condorcet efficiency, measured](condorcet_efficiency_measured.md) reports the fact in a single line — *"more candidates hurt everyone except the control"* — and moves on. It is the most robust finding on that page: it holds for every method, in every electorate model, at both electorate sizes, with no exceptions. It also gets quoted a lot and explained almost never.

This page does the explaining. **The answer is not one mechanism but four, they hit different methods, and they are measurable** — so all four are measured here rather than asserted, on the same harness that produced the rates.

The short version: as the field grows, the candidate the electorate actually prefers holds a smaller share of first choices, wins their head-to-heads by thinner margins, and becomes harder to distinguish from their nearest rival on a fixed-resolution ballot. Every method reads *some* of that degraded signal. Only a method that reads the pairwise margins directly is immune, which is why the [Ranked Robin](../../../05_Ranked_Robin/01_Learn/ranked_robin.md) control never moves.

---

## 1. The finding, drawn

Each bar is the share of elections in which that method elected the [Condorcet winner](README.md), out of the elections that had one. Ranked Robin is the **control** — [Copeland](../../../05_Ranked_Robin/01_Learn/ranked_robin.md) is Condorcet-efficient by construction, so it *must* read 100%, and any bar of its that fell short would mean the harness was broken and every other number worthless.

```text
spatial1d — 501 voters          (voters and candidates on a single left-right spectrum)
            3 candidates        5 candidates        7 candidates
RankedRobin ████████████ 100%  ████████████ 100%  ████████████ 100%
STAR        ████████████  97%  ██████████··  87%  ██████████··  79%
Score       ██████████··  84%  █████████···  72%  ████████····  68%
Approval    ██████████··  83%  ████████····  67%  ███████·····  56%
RCV-IRV     ██████████··  87%  ███████·····  61%  ██████······  47%
Plurality   ████████····  70%  █████·······  42%  ████········  30%
            3 → 7 candidates, percentage points lost: STAR 18, Score 17, Approval 28, RCV-IRV 40, Plurality 40

faction2d — 501 voters          (voters clustered around three group centres)
            3 candidates        5 candidates        7 candidates
RankedRobin ████████████ 100%  ████████████ 100%  ████████████ 100%
STAR        ████████████  99%  ███████████·  95%  ███████████·  92%
Score       ███████████·  90%  ██████████··  84%  ██████████··  82%
Approval    ███████████·  92%  ██████████··  80%  █████████···  74%
RCV-IRV     ███████████·  96%  ██████████··  85%  █████████···  76%
Plurality   ███████████·  90%  █████████···  73%  ███████·····  61%
            3 → 7 candidates, percentage points lost: STAR 7, Score 8, Approval 18, RCV-IRV 19, Plurality 29

noise — 501 voters              (impartial culture: every opinion independent and random)
            3 candidates        5 candidates        7 candidates
RankedRobin ████████████ 100%  ████████████ 100%  ████████████ 100%
STAR        ███████████·  90%  ██████████··  83%  ██████████··  83%
Score       ██████████··  83%  █████████···  75%  █████████···  77%
Approval    █████████···  77%  ████████····  66%  ███████·····  60%
RCV-IRV     ████████████  96%  ███████████·  90%  ██████████··  85%
Plurality   █████████···  76%  ███████·····  57%  ██████······  46%
            3 → 7 candidates, percentage points lost: STAR 7, Score 7, Approval 17, RCV-IRV 12, Plurality 30
```

Reproduce all eight blocks (four models × two electorate sizes) with:

```bash
uv run 06_Other/simulations/condorcet_efficiency_simulation.py --chart
```

Three things are worth reading off the bars before any explanation:

- **Every method's bar shrinks, and the control's does not.** That asymmetry is the whole subject of this page. Ranked Robin is not "better at crowded fields"; it is reading a quantity that a crowded field does not degrade.
- **The size of the fall is not the same for everyone.** Under `spatial1d`, Plurality and RCV-IRV lose about 40 points between three and seven candidates while STAR loses 18. Different mechanisms, different exposure.
- **The model changes the answer as much as the method does.** Under `noise`, RCV-IRV declines least of any non-control method and beats STAR at every field size; under `spatial1d` it falls off a cliff. Any single number quoted without its model is a model choice being passed off as a result — which is the standing rule of [this repo's simulations folder](../../../06_Other/simulations/README.md) and the reason four models are run rather than one.

---

## 2. How this was tested

Nothing above is a survey of real elections. It is a brute-force simulation, and the honest way to read it is to know exactly what was randomised.

**The harness.** [`condorcet_efficiency_simulation.py`](../../../06_Other/simulations/condorcet_efficiency_simulation.py) samples an electorate, computes each method's winner from that *same* electorate, and records whether each elected the Condorcet winner. 4,000 elections per bar; `numpy`'s `default_rng` seeded at 20260727, so every figure is reproducible from the command above. Field sizes 3, 5, 7; electorate sizes 51 and 501.

**Utilities first, ballots derived.** Each voter gets a numeric opinion of each candidate, and every ballot is computed from those opinions — the ranking is the opinions in order, the 0–5 score ballot is the voter's own min-max scaling of them, the approval ballot is that thresholded at 4. Ballots are never drawn at random directly; doing so would build the answer into the sampling ([simulate utilities, not ballots](../simulate_utilities_not_ballots.md)).

**The four randomness models** — this is the part to quote alongside any number:

| Model | What is random | What it is good for |
|---|---|---|
| **`noise`** — impartial culture | every voter's opinion of every candidate is an independent uniform draw. No structure at all: `5,5,5,5,5` is as likely as any real-looking ballot. | The adversarial stress test, and the standard baseline in the literature. It manufactures far more [cycles](../smith_set.md) than any real electorate shows — at seven candidates **more than a third** of its elections have no Condorcet winner at all. Treat its numbers as a bound, not a forecast. |
| **`spatial1d`** | voters and candidates are points on one line; opinion = minus the distance, plus a little noise. | The classic left-right spectrum, and precisely where [center squeeze](../center_squeeze/README.md) lives. This is the model that punishes elimination methods hardest. |
| **`spatial2d`** | the same, in two dimensions. | Two issues instead of one. Worth running because the squeeze softens when "the moderate" stops being a single well-defined position — a caution against reading any one spatial result as *the* answer. |
| **`faction2d`** — groups | voters cluster around three group centres, then scatter. | Simulating **groups**: a polarised or tribal electorate rather than an evenly spread one. Closest of the four to how real electorates actually lump together. |

**The conditional, and why it matters.** Condorcet efficiency is *P(elects the Condorcet winner | one exists)*. Elections with a cycle have no Condorcet winner, so no method could elect one; folding them into the denominator would drag every method down by the cycle rate and end up measuring the electorate rather than the method. Cycle elections are therefore excluded, and the share that had a Condorcet winner is reported separately in [the sibling page's table](condorcet_efficiency_measured.md#the-measured-table).

**What holds it honest.** The Ranked Robin control must read exactly 100% — [`tests/test_condorcet_efficiency_sim.py`](../../../STARVote_LH_tabulation_engine/tests/test_condorcet_efficiency_sim.py) fails the suite if it ever does not. STAR is not re-implemented here; the script imports the engine-faithful model from [`star_vs_rr_divergence.py`](../../../06_Other/simulations/star_vs_rr_divergence.py), which is held to the real tabulation engine by its own test. And `--selftest` runs known-answer checks on a hand-verifiable center-squeeze profile before any of this is believed.

**What it is not.** Sincere ballots only — no strategy anywhere. Four models are not the world. And Approval's numbers move with the cutoff, which is a modelling choice rather than a fact about Approval.

---

## 3. Why: what a bigger field does to the election itself

Here is the part that actually answers the question. Before asking what happens to any *method*, measure what happens to the *election*. Three quantities, all properties of the electorate alone:

```text
model       C     V |   CW 1st %  CW margin  pairs tied
------------------------------------------------------
spatial1d   3   501 |      48.6%      21.5%        6.3%
spatial1d   5   501 |      28.9%      11.9%       11.3%
spatial1d   7   501 |      19.7%       7.9%       13.9%

faction2d   3   501 |      60.9%      34.8%        5.9%
faction2d   5   501 |      46.3%      24.9%       10.8%
faction2d   7   501 |      38.1%      20.6%       13.3%

noise       3   501 |      35.3%       2.5%        6.7%
noise       5   501 |      21.8%       1.8%       11.4%
noise       7   501 |      15.9%       1.6%       13.3%
```

```bash
uv run 06_Other/simulations/condorcet_efficiency_simulation.py --why --voters 501
```

- **CW 1st %** — the Condorcet winner's share of first choices.
- **CW margin** — their *narrowest* head-to-head win, in percentage points.
- **pairs tied** — the share of candidate pairs an average 0–5 ballot cannot separate.

All three move the wrong way, and they move a lot. On a single spectrum, going from three candidates to seven **halves the Condorcet winner's first-choice share (48.6% → 19.7%), cuts their thinnest winning margin by two-thirds (21.5 → 7.9 points), and more than doubles the fraction of the score ballot that goes tied (6.3% → 13.9%).** Those three columns are the whole explanation. Each method is exposed to a different one.

### Mechanism 1 — first choices fragment, so elimination methods lose the candidate early

This is the one that hits **Choose-One and RCV-IRV**, and it is nearly pure arithmetic. Each new candidate stands *somewhere*, and wherever they stand they take the first-choice votes of everyone now closer to them. A broadly-acceptable candidate near the middle is surrounded on both sides, so they lose votes to every entrant.

The `CW 1st %` column is that effect measured: the person who beats everyone head-to-head is down to **19.7% of first preferences at seven candidates** on a single spectrum. Choose-One counts nothing but that number, and RCV-IRV uses it to decide who dies first — so a candidate at 19.7% is a candidate the count is about to throw away, however many head-to-heads they win.

This is [center squeeze](../center_squeeze/README.md), and field size is its accelerator: three candidates squeeze a centrist from two sides, seven squeeze them from six. It explains why RCV-IRV's fall is steepest exactly where the geometry is sharpest — 40 points in `spatial1d`, 19 in `faction2d`, 12 under structureless `noise` where there is no "middle" to be squeezed out of.

### Mechanism 2 — margins thin out, so the signal any ballot must carry gets fainter

The `CW margin` column is the Condorcet winner's *closest* call. With three candidates on a spectrum they win their tightest matchup by 21.5 points; with seven, by 7.9. Nothing has gone wrong — a crowded field simply means a rival standing nearer, and a nearer rival is a closer contest.

This one hits **everybody**, because every method has to recover that margin through some ballot. Twenty-one points survives rounding, noise and coarse ballots easily. Eight points does not. It is the reason the other mechanisms bite harder at seven candidates than the same mechanisms do at three: they are eroding a smaller signal.

Ranked Robin is the exception, and precisely here is why: it reads the margins themselves off a full ranking. An 8-point margin and a 21-point margin are both simply *a win*, so nothing about the crowd degrades what it needs. That is the control's 100% — not skill, but immunity to the quantity that changed.

### Mechanism 3 — the ballot runs out of rungs, so score methods stop being able to tell candidates apart

This is the one that hits **STAR, Score and Approval**, and it is where the explanation usually goes wrong.

A 0–5 ballot has **six rungs**. Six rungs can hold at most six distinct ranks, so from seven candidates onward *every* voter's ballot must tie at least one pair — a pigeonhole, not a tendency. Long before that hard limit, rounding is already flattening the near-calls: the `pairs tied` column runs 6.3% → 11.3% → **13.9%** as the field grows.

Now combine that with mechanism 2. The pairs a coarse ballot flattens first are the *close* ones — and the crowded field has made the Condorcet winner's decisive matchups close. The ballot is losing resolution exactly where the answer now lives.

**The surprise in the data is which half of STAR this lands on.** A Condorcet winner who *reaches* STAR's runoff wins it — they beat anyone head-to-head — so STAR can only miss two ways, and the sibling page counts them separately:

| | 3 cands | 5 cands | 7 cands |
|---|:--:|:--:|:--:|
| `spatial1d`, top-two miss — the CW never reached the runoff | 0.0% | 5.2% | 11.2% |
| `spatial1d`, **grid loss** — the CW reached the runoff and lost | **5.2%** | **9.8%** | **14.9%** |

Both grow with the field, but **grid loss is the larger of the two at every field size**, and roughly two-thirds of grid losses are outright reversals rather than exact ties ([the mechanism breakdown](condorcet_efficiency_measured.md#why-star-misses-and-the-surprise-in-the-answer)). So the popular story — *a crowded field squeezes the compromise candidate out of STAR's top two* — is real, and is the smaller half. The bigger half is the ballot's resolution giving out.

Read that in both directions, as the sibling page insists. It is **not** a defence that clears STAR: a real STAR election really is counted on a 0–5 ballot, so the loss is real and it lands on STAR. But it is **not a property of the automatic runoff** either, and it is inherited by every score-ballot method here. It also means the comparison is structurally generous to Ranked Robin, which reads a full-resolution ranking — the single biggest caveat on both pages.

### Mechanism 4 — the approval cutoff drifts, so Approval dilutes

**Approval** gets mechanisms 2 and 3 plus one of its own. A voter approving "everyone I'd rate 4 or 5" is drawing a line at a fixed *height*, but a wider field puts more candidates above any fixed line and rearranges who is near it. The broadly-liked compromise — everyone's solid second choice, nobody's favourite — is the candidate a widening field pushes below the line first, because the newcomers standing nearer each voter take the top rungs.

Approval falls 28 points in `spatial1d` and 18 in `faction2d`, in both cases faster than STAR or Score. It is also the column to quote most carefully: change the cutoff and the number changes. There is no such thing as "Approval's Condorcet efficiency" without the rule attached.

### A fifth thing that is *not* a mechanism — cycles

More candidates means more pairs to be intransitive about: three candidates have 3 head-to-heads, seven have 21. Cycles duly become far more common, and under impartial culture at seven candidates more than a third of elections have no Condorcet winner at all.

This does **not** contribute to anything above, and the distinction is worth keeping straight. A cycle election has no Condorcet winner to elect, so it is excluded from the denominator entirely. Rising cycle rates make the *question* less often answerable; they do not make any method worse at answering it when it is. Conflating the two is the most common way these numbers get mangled.

---

## 4. Watch it happen: one electorate, three ballot sizes

The mechanisms above are rates over thousands of sampled elections. Here is a single election you can run, where the same effects are visible one at a time.

**Sixty-five voters who never change their minds.** They sit in seven blocs along one spectrum. Seven candidates stand at fixed points. **Diego beats every rival head-to-head at every rung** — the electorate's answer is the same in all three elections. The only thing that changes is how many names are on the ballot.

| Field | Ranked Robin | STAR | Score | Approval | RCV-IRV | Choose-One |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| **3 candidates** | Diego | Diego | Diego | Diego | Diego | Diego |
| **5 candidates** | Diego | Diego | Diego | Diego | **Elsa** | **Bruno** |
| **7 candidates** | Diego | **Clara** | **Clara** | **Felix** | **Clara** | **Greta** |

- **At three**, Diego holds an outright majority of first choices (34 of 65) and every method elects him.
- **At five**, two candidates join — one on each side. Diego's first choices collapse from 34 to **9**, purely because two people now stand between him and voters who previously had nobody closer. Choose-One and RCV-IRV leave. *(Mechanism 1.)*
- **At seven**, two more join. Diego still beats all six rivals — including Clara, 36–29 — but on the 0–5 ballot **25 of the 65 voters cannot separate them at all**, and Clara takes the runoff 23–17. *(Mechanisms 2 and 3, and note that Diego was **in** the runoff: this is a grid loss, not a top-two miss.)*

Every ballot in it is derived from the candidates' positions by the rules in §2, not hand-written, and no result at any rung is settled by a tie-break. The full worked election, all twelve engine reports, and the caveats: **[the crowded field](../../../method_comparisons/crowded_field/README.md)**.

---

## 5. Where this lands

**For anyone quoting a Condorcet-efficiency number:** say how many candidates. The field size moves these figures by more than the choice of method does in most rows, and "STAR is 97% Condorcet-efficient" and "STAR is 79% Condorcet-efficient" are the same simulation, same model, same electorate size — three candidates and seven.

**For STAR specifically**, the honest statement has two halves and the second is not optional. The good half: STAR degrades *slowly* — 18 points over `spatial1d`'s 3→7 range against RCV-IRV's 40 and Plurality's 40, and it is the most Condorcet-efficient non-Condorcet method measured in every structured model. The other half: it does degrade, most of the degradation is the 0–5 ballot running out of resolution, and that is a real cost of a real ballot, not an artifact. If a crowded field is your expected case and electing the head-to-head winner is your priority, the method that guarantees it is [Ranked Robin](../../../05_Ranked_Robin/01_Learn/ranked_robin.md), and STAR's [honest limits page](../../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md) says so.

**For RCV-IRV**, the finding is sharper and deserves to be stated as carefully as it is stated plainly. On a single-issue spectrum with seven candidates, instant runoff elects the head-to-head winner **less than half the time**, and mechanism 1 says exactly why. But the same simulation shows it *beating* STAR at every field size under impartial culture, and that belongs in the same breath — see [keeping method comparisons fair](../../../method_comparisons/README.md).

**And the reform-design point that falls out of all of this:** every argument here gets weaker as the field gets smaller, and none of these methods is in trouble at three candidates. Reforms that also shape *how many people run* — primaries, qualifying rounds, ballot access thresholds — are changing the same variable this page is about, in the same direction. That interaction is the subject of [does the qualifying round throw away the consensus winner?](../../../method_comparisons/qualifying_round_primary_method.md).

---

**See also:** [Condorcet efficiency, measured](condorcet_efficiency_measured.md) (the rates) · [the crowded field](../../../method_comparisons/crowded_field/README.md) (the worked election) · [center squeeze](../center_squeeze/README.md) · [the Smith set](../smith_set.md) · [what makes a good winner](../what_makes_a_good_winner.md) · [simulations folder](../../../06_Other/simulations/README.md) · [Condorcet reading list](condorcet_reading_list.md) · [topic hub](README.md)
