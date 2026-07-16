# `generate_dead_rung_scenarios.py` — build STAR "dead rung" tie-break elections

A generator for the trickiest STAR tie-break fact, the one that keeps causing confusion: **STAR's second tiebreaker counts only score-5 votes — "most five-star votes" — and it never steps down to the 4s.** If the tied candidates have equal (or zero) 5s, that rung reads `0–0`, can't separate them, and the tie falls straight through to the **lot**. Piling up 4s does nothing.

You give it a round, a rung state, and (optionally) a score cap; it prints a ready-to-tabulate YAML election that lands on exactly that situation. It generalizes the checked-in cases in [The "dead rung" — when STAR's five-star tiebreaker can't fire](../../01_STAR/tie_break_dead_rung/README.md) (cases 01–09).

---

## Remembering the name: "dead rung"

Picture STAR's tiebreaker as a **ladder** you climb only as far as you need:

```
SCORING ROUND   finalists:  pairwise  →  five-star  →  lot
AUTOMATIC RUNOFF winner:     score     →  five-star  →  lot
```

The **five-star rung** is the step that counts votes equal to the scale max (5). If nobody scored a 5, there's no one standing on that step — a **dead rung** — so you fall through to the lot.

**Mnemonics**

- **"No fives, no rung — drop to the lot."**
- **"It counts fives, not fours."** — the whole surprise in five words.
- **"Fives or dice"** — either a 5 decides it, or the lot (the dice) does; the 4s never get a vote.
- Ladder image: a **rung with nobody standing on it** won't hold your weight — you fall past it to the lot.

**Synonyms / alternate names** (if "dead rung" doesn't stick): *broken rung, missing step, empty rung, phantom rung,* or plainly *"the five-star tiebreaker that can't fire."* Related jargon you'll see nearby: the **five-star rung** (the step itself) and **falling through to the lot** (what happens when it's dead).

> The deeper point behind all the names: STAR's tiebreak rungs are **discrete tests**, not a smooth countdown. It checks 5s, and if that's inconclusive it does **not** check 4s, then 3s — it jumps to the lot. So a candidate can be buried in 4s and still lose the tiebreak to the lot.

---

## What it produces

A single YAML election in the `tie_break_dead_rung/` house **flat schema** (top-level keys, matching cases 01–09), with a `lot_numbers:` line (when the lot is involved) and an `expected_winners:` assertion — so each file is auto-discovered by `test_single_winner_positive.py` and doubles as a positive test. By default it prints to the **screen only** — pass `--out` to save.

---

## Parameters

| Flag | Meaning | Default |
|------|---------|---------|
| `--round {scoring,runoff,full}` | where the tie sits: 3-candidate scoring (a leader wins, two tie for the 2nd slot), a 2-candidate automatic-runoff tie, or **`full`** — a fully symmetric `k`-candidate tie (see below) | `scoring` |
| `--rung {alive,dead,tied}` | what the five-star rung finds (see below); ignored for `--round full` | `alive` |
| `--candidates N` | number of candidates for `--round full` (≥2); any of the `k` can win by lot | `3` |
| `--cap {4,3,2}` | score ceiling for a **dead** / **full** rung — the *"what about the 4s?"* knob | `4` |
| `--adversarial-lot` | pin the lot to favor the *wrong* candidate, so the winner only comes out right if the ladder runs in the correct order (a strict regression test) | off |
| `--scale N` | duplicate the ballot block N times (bigger electorate, identical result) | `1` |
| `--theme {letters,classic,fruits,flavors,capitals}` | candidate names (`classic` = Ann/Ben/Cara, matching the case docs) | `letters` |
| `--title "…"` | override the generated title | auto |
| `-o`, `--out PATH` | save to a file (or DIR, auto-named); omit → screen only | — |
| `--run` | tabulate with the LH engine after writing | off |

### The three rung states

| `--rung` | What the ballots do | Who decides |
|----------|---------------------|-------------|
| `alive` | one tied candidate has a **5** the other lacks | **five-star** (the ballots) |
| `dead` | **nobody** scored a 5 (all capped at `--cap`) → rung reads `0–0` | **the lot** |
| `tied` | **both** tied candidates have equal, non-zero 5s → rung runs but `1–1` | **the lot** |

`alive` vs `dead` is the same tie **one point apart** (a 5 capped down to a 4). That single point is the whole difference between "ballots decide" and "the lot decides." `tied` is the subtle third case: the rung *runs and counts real votes* and still resolves nothing.

### `--round full` — a fully symmetric `k`-candidate tie

`--round full --candidates k` builds the `k`-candidate generalization of the BetterVoting `jfk7pd` case: `k` candidates and `k` ballots forming an identity matrix × `--cap`, so ballot *i* gives candidate *i* the cap and everyone else 0:

```
A,B,C,D
4,0,0,0
0,4,0,0
0,0,4,0
0,0,0,4
```

Every candidate totals the same, every pairwise is 1–1, and (cap < 5) nobody has a 5 — a **dead rung**. Nothing separates them, so the lot alone decides and **any of the `k` can win** (the file asserts the lot favorite, candidate A). This is the knob for exploring how the phenomenon scales: a random draw diverges from a published order **`(k−1)/k`** of the time — 50% at `k=2`, 67% at 3, 75% at 4, 80% at 5 — and the generated `election_description` states that fraction for you.

```
python generate_dead_rung_scenarios.py --round full --candidates 4 --run   # A wins by lot; reorder → any of A–D
```

(`--rung` and `--adversarial-lot` don't apply here — a full tie is inherently a symmetric dead rung. Use `--theme letters` for more than five candidates.)

### `--pad N` — "less obvious" ties (bury it in noise)

By default the full-tie ballots are a tidy identity matrix — obvious at a glance. `--pad N` (with `--seed` for reproducibility) makes the tie look like a messy real election **without changing the result**. Each pad block appends the **orbit** of a noise vector — its distinct permutations under all candidate relabelings. That orbit treats every candidate identically, so totals, pairwise, **and** five-star all stay exactly equal (the tie is preserved), and the rows are shuffled so the identity ballots don't stand out.

```
python generate_dead_rung_scenarios.py --round full --candidates 3 --pad 4 --seed 7
```

**Why "shorter but not obvious" is a real tension — and how to control it.** The orbit has to include *all* relabelings, because the scoring round's first tiebreaker is **pairwise** (head-to-head): a Latin square or a handful of cyclic shifts equalizes totals and five-star counts but can leave one head-to-head tilted, which would break the tie at the pairwise rung and never reach the lot. So the block size is the orbit size — and that is governed entirely by how many **repeated scores** the noise vector has:

| Noise vector (k = 6) | Distinct permutations | Effect |
|---|---:|---|
| all-distinct `[0,1,2,3,4,cap]` | `6! = 720` | huge — the old default |
| `[4,4,4,0,0,0]` | `6!/(3!·3!) = 20` | varied-looking, readable |
| `[4,0,0,0,0,0]` | `6!/(1!·5!) = 6` | shortest, still non-identity |

The tool now **defaults to a repeated-score vector** (roughly half the candidates at `--cap`, half at 0), so `--candidates 6 --pad 1` produces **12** ballots instead of 726. To dial it yourself use `--pad-vector`:

```
# 26 ballots (6 identity + 20-permutation orbit), clearly varied but short:
python generate_dead_rung_scenarios.py --round full --candidates 6 --pad 1 --pad-vector 4,4,4,0,0,0
```

`--pad-vector` takes comma-separated scores of length `--candidates`, each `0..cap`. Fewer distinct values ⇒ shorter file; more distinct values ⇒ messier but longer. The tool warns past ~1000 ballots and suggests a more-repeated vector. This is the knob for demonstrating that a lot-decided tie needn't be an obvious toy — it can hide in a normal-looking ballot set — while keeping the file short enough to read.

(`--scale N`, by contrast, just *clones* the whole block N times — bigger, but still visually obvious. Use `--pad` for genuinely varied ballots.)

---

## Worked example 1 — the core lesson (scoring, dead rung → lot)

```
python generate_dead_rung_scenarios.py --round scoring --rung dead --theme classic --run
```

Generated ballots (Ann leads and wins; Ben and Cara tie for the second finalist slot; every score capped at 4 so **no 5 exists**):

```yaml
lot_numbers: [Ann, Ben, Cara]
ballots: |-
  Ann,Ben,Cara
  4,4,1
  4,0,3

expected_winners:
  - Ann
```

The engine's report shows the rung firing and finding nothing, then falling to the lot:

```
Scoring Round
   Ann           -- 8 -- First place
   Ben           -- 4 -- Tied for second place
   Cara          -- 4 -- Tied for second place
 Ann advances, but there's a two-way tie for second.

Scoring Round: First tiebreaker
 The candidate preferred in the most head-to-head matchups advances.
   Ben           -- 1 -- Tied for second place
   Cara          -- 1 -- Tied for second place        ← pairwise 1–1, no help

Scoring Round: Second tiebreaker
 The candidate with the most votes of score 5 advances.
   Ben           -- 0 -- Tied for second place
   Cara          -- 0 -- Tied for second place        ← DEAD RUNG: 0–0

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ben', 'Cara']
  Resolved: ['Ben'] (selected by lot-number priority).   ← the lot decides

Winner — STAR Voting Method (single winner)
 Ann
```

Note Ben's and Cara's **4s never enter the tiebreak** — the second rung asks only "most votes of score 5," gets `0–0`, and hands off to the lot. Run the same command with `--rung alive` and Ben (who now holds a 5) advances **by the ballots**, no lot needed. Same tie, one point apart.

**"What about the 4s?"** Lower the cap and nothing changes — it's still dead:

```
python generate_dead_rung_scenarios.py --round scoring --rung dead --cap 3
python generate_dead_rung_scenarios.py --round scoring --rung dead --cap 2
```

Only an actual **5** revives the rung.

---

## Worked example 2 — the winner actually flips (runoff, adversarial lot)

The scoring example above elects the leader (Ann) either way — good for teaching, but it can't *catch a bug*, because the winner is the same whether or not the engine consults the rung. `--adversarial-lot` fixes that: it pins the lot to the "wrong" candidate, so the **elected winner changes** depending on whether the five-star rung fires.

**Rung alive** — five-star must OUTRANK the lot (lot favors Ben; Ann holds a 5):

```
python generate_dead_rung_scenarios.py --round runoff --rung alive --adversarial-lot --theme classic --run
```

```
Automatic Runoff Round: Second tiebreaker
 The candidate with the most votes of score 5 wins.
   Ann           -- 1 -- First place
   Ben           -- 0
 Ann wins.                    ← ballots (five-star) beat the lot
```

**Rung dead** — cap the 5 to a 4 and *only the lot is left* (which favors Ben):

```
python generate_dead_rung_scenarios.py --round runoff --rung dead --adversarial-lot --theme classic --run
```

```
[Tiebreaker: Lot Number Priority]
  Resolved: ['Ben'] ...
 Ben wins.                    ← nothing on the ballots separates them; the lot decides
```

Same two voters, **one point of enthusiasm** (a 5 vs a 4) flips the winner from Ann to Ben. If an engine ever consulted the lot early, or stepped down to 4s, the `alive` case would elect Ben and its `expected_winners` assertion would fail — which is exactly what makes these good regression tests.

---

## All the combinations

Verified against the engine (exit 0, engine winner == asserted winner):

| `--round` | `--rung` | plain winner | with `--adversarial-lot` |
|-----------|----------|:--:|:--:|
| scoring | alive | leader (A) — five-star advances the 2nd finalist | **B** (five-star beats lot) |
| scoring | dead  | leader (A) — lot advances the 2nd finalist | **A** (lot advances the loser) |
| scoring | tied  | leader (A) — lot advances the 2nd finalist | *(n/a)* |
| runoff  | alive | A — five-star wins the runoff | **A** (five-star beats lot) |
| runoff  | dead  | A — lot wins the runoff | **B** (lot wins) |
| runoff  | tied  | A — lot wins the runoff | *(n/a)* |

The adversarial `scoring/alive` → **B** vs `scoring/dead` → **A**, and `runoff/alive` → **A** vs `runoff/dead` → **B**, are the winner-flips that prove the cascade order.

---

## Implementation notes

- **Verified ballots.** Each `(round, rung, adversarial)` uses a ballot template taken from the checked-in cases 01–09, generalized over the cap, electorate scale, and names. The tied pair's totals and pairwise are exactly equal by construction, so the tie genuinely lands on the five-star rung.
- **Cap generalization.** For a non-adversarial dead rung the filler adjusts with `--cap` so the two candidates stay tied at any ceiling (4, 3, or 2). The adversarial dead template is fixed at cap 4 (other caps would unbalance the bloc totals); `--cap` is ignored there with a note.
- **`--scale`** just repeats the ballot block, which preserves every total, pairwise, and 5-count — so the winner is unchanged, the electorate just looks bigger.
- **Engine discovery for `--run`** walks up from the output file and from this script's own location, so it works even when the YAML is a temp file outside the repo.

---

## Related

- The hand-built case set this generalizes: [The "dead rung" — when STAR's five-star tiebreaker can't fire](../../01_STAR/tie_break_dead_rung/README.md) (cases 01–09).
- Canonical concept page: [STAR Tie-Breaking — The Full Chain](../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md) (Level 301) — has the "dead rung" section.
- Why one point of scale can flip a winner: [Scale granularity can flip the winner](../../00_start_here/scores_and_ranks/scale_granularity_flips_the_winner.md).
- The runoff and scoring rounds themselves: [The Automatic Runoff Round](../../00_start_here/STAR_Voting/the_count/STAR_Automatic_Runoff.md) · [reporting true ties](../../00_start_here/STAR_reporting/reporting_ties.md).
