# A Rust tabulation kernel — scope, and whether it is worth building

**Level: reference · deep dive**

**One line:** a Rust *kernel* — ballots in, winners and audit trail out — is worth building for two things this library cannot do today (count in the reader's browser, and search ballot space exhaustively); rewriting the *test cases* in Rust would be a straight loss.

This is a strategy note, not a plan of record. Nothing here has been built. It exists so that the question gets answered once, with the repo's actual numbers in front of it, instead of being re-litigated every time Rust comes up.

**Read the companion first if you are starting cold.** [Goals, requirements, and how to get ready](rust_kernel_requirements.md) works the prior question — what a kernel would be *for* — across nine candidate goals, and derives requirements from the answer. Scope without a goal is just a list.

---

## Two questions that get confused

**"Should the voting test cases be Rust?"** — No, and the reasoning is short enough to finish here. The 615 case files are the library's most valuable asset precisely *because* they are language-neutral: a YAML election with an `expected_winners:` line is a claim about arithmetic, not about Python. Six engines already consume them — the [LH engine](LH_starvote/README.md), [BetterVoting](BV/README.md), [`pyrankvote`](RCV_IRV/README.md), [`pref_voting`](cross_checking_with_pref_voting.md), [RCTab](rctab.md), and [rcv-lab.org](rcv_lab_irv_crosscheck.md) — and every one of them was wired up *without* touching a case file. Re-authoring those elections as `#[test]` functions would convert a shared asset into one implementation's private fixtures, and the next engine would have to convert them back.

So the case library stays exactly where it is. Rust, if it happens, is a **consumer** of the case library on equal footing with the other five.

**"Should there be a Rust tabulation kernel?"** — That is the real question, and the answer is conditional. It depends entirely on whether the goal is *a faster engine* (no) or *the two capabilities in the next-but-one section* (yes).

---

## What the library already has

The porting cost is low because the hard part is already done — not the code, the **specification by example**.

| | count |
|---|---|
| tracked `.yaml` files | 649 |
| of those, carrying a `ballots:` or `grades:` block | 615 |
| carrying `expected_winners:` (the machine-checkable answer key) | 567 |
| ballot-carrying, **no** `expected_winners:` at the time of writing — see item 2 below: only 4 were real cases, keyed 2026-08-20 | 48 |
| `_tabulated.txt` mirrors | 782 |
| Python in the main engine | 4,257 lines — **1 class, 57 functions** |

Two observations that shape everything below.

**The engine is procedural, not object-oriented.** One class in 4,257 lines. That is not an accident or a defect: tabulation is data in, result out, and the code reads well that way. It also means a port carries almost no object-model baggage — there is no hierarchy to redesign into Rust's trait system, because there is no hierarchy.

**Most of those 4,257 lines are the report, not the count.** The pairwise matrix renderer, the self-reconciling runoff summary, the [Smith set](../topics/smith_set.md) block, the RCV-IRV transfer block, the divergence comparison — that is where the bulk of the file lives, and it is where most of the *teaching* value lives too. A Rust port that chases those is porting a text formatter.

---

## Scope

### Tier 1 — the kernel (build this or nothing)

Pure functions. No file I/O, no printing, no CLI. Ballots and a method in; winners, per-round tallies, pairwise matrix, and elimination order out.

- STAR, single-winner
- Bloc STAR
- Approval, single- and multi-winner
- Ranked Robin (Copeland)
- RCV-IRV
- Plurality / SNTV
- Score / Range

**Coverage: 560 of the 615 ballot-carrying cases — 91%.** Estimated at well under 2,000 lines of Rust, because the arithmetic of every method on that list is genuinely simple; the difficulty in all of them is tie handling, which is discussed below.

### Tier 2 — defer until Tier 1 is green

- **STV** (11 cases) and the **STAR-PR family** — allocated score (27), SSS (8), RRV (6). Fractional surplus transfers, quota arithmetic, and reweighting. This is where a naive port silently disagrees rather than obviously failing; the [allocated-score count-vs-weight bug](../../STARVote_LH_tabulation_engine/BUG_allocated_count_vs_weight.md) is a live example of a defect that survived in a published engine precisely because the number it produced was plausible.
- **Combined Approval (CAV)** and **3-2-1** — one case each, trivial arithmetic, add them when convenient.
- **The grade methods** — 7 `grades:` cases (Majority Judgment, Range on foreign scales). Not LH-runnable at all today, so a Rust implementation would *add* coverage rather than duplicate it. Cheap and tempting; also the least important.

### Out of scope, permanently

- The report renderer and the 782 `_tabulated` mirrors. Byte-identical text reproduction is 10× the kernel's work and delivers none of its value.
- Page generation, the divergence ledger, the hygiene checks, BetterVoting integration, the [website build](../about_this_repo/website_build.md). Rust improves none of these.
- The YAML dialect's forgiving edges — bare `title:` as an alias, method names with trailing `#` comments, the negative-fixture error messages. Let the Rust side be strict and read a normalized input.

---

## The case for building it

Ranked by how much they actually justify the effort.

**1. WebAssembly — counting in the reader's browser.** This is the one that would make the project worth doing on its own. A pure kernel compiles to WASM at a few hundred kilobytes, and the published site could then let a reader edit a ballot and watch the runoff flip live, on the page, with no server. That is a *new capability for the teaching mission*, not a re-implementation of an existing one. Every other item on this list is a variation on "we could check our work better"; this one changes what the library can show.

**2. Exhaustive and property-based search.** With a fast kernel you can enumerate ballot space rather than hand-craft examples: *does any 3-candidate, ≤7-voter STAR election exhibit a monotonicity failure?* — asked by brute force, answered with a witness or a proof of absence. Python can do this in principle and cannot do it at interesting sizes. This feeds directly into the [research-topics companion repo](https://github.com/masiarek/star-voting-research-topics), where "we searched the whole space" is a publishable result and "we found an example" is not.

**3. A genuinely independent third implementation.** This library's entire method is cross-checking — the [engines README](README.md) is mostly a list of engines refereeing each other. A Rust kernel written **from the written spec** rather than transliterated from the Python is another referee, and re-deriving the rules in a language that refuses to be vague is exactly the process that surfaces semantic bugs. Note the qualifier: a line-by-line translation of [`starvote_larry_hastings.py`](../../STARVote_LH_tabulation_engine/starvote_larry_hastings.py) would inherit its bugs and prove nothing. If it is not written from the spec, it is not a cross-check.

**4. A path to encrypted, publicly verifiable tallying.** The longest-range reason, and the only one where Rust is close to the *correct* language rather than a preference — the applied-crypto ecosystem there is best-in-class and targets WASM well. [Counting under encryption](../topics/homomorphic_tallying.md) already establishes that score methods admit additively homomorphic tallying and that IRV does not, for the same reason one is [summable](../topics/summability/README.md) and the other is not. The first two rungs of that ladder — a toy Approval tally, then range proofs — are *the same WASM work as reason 1*, which is why choosing the modest goal does not foreclose the ambitious one. Bounds and staging in the [requirements page](rust_kernel_requirements.md#g8-in-detail-end-to-end-verifiability).

**5. Speed.** Listed for completeness and then dismissed. House convention is [the fewest ballots that make the point](../tips/TIPS_choosing_voter_counts.md) — often nine voters. Nothing in this repo is slow. Speed matters only as an enabler of reason 2.

---

## The case against

**1. Two implementations is a drift surface, and this repo's whole hygiene apparatus exists to prevent drift.** Generated mirrors, pages, and indexes are all kept honest by tests that compare a file to its regenerated form. A second engine cannot be checked that way — only its *outputs* can be compared, and only on the cases that exist. Every case the library does not have is a place the two can silently disagree.

**2. The 48 unanswered cases are a cheaper win.** 48 ballot-carrying files have no `expected_winners:` line, which means 48 elections in this library currently assert nothing that any engine can check. Closing that gap improves every present and future cross-check, costs a weekend, and requires no new language.

**3. Maintenance falls on one person.** A Rust kernel is a second codebase with a second toolchain, second CI, and second set of dependency updates, maintained alongside an already-large Python repo, [open upstream bug reports](../about_this_repo/upstream_bug_reports.md), and the actual teaching content — which is the point of the project.

**4. The interesting part of the engine is not portable.** See above: the reporting layer is where the pedagogy is. Porting the kernel moves the least interesting 20% of the code.

**5. Rust's headline advantages barely apply.** Memory safety is not a live concern for a program that reads a small YAML file and prints integers; Python was never the source of a wrong answer here. The bugs this repo has actually found were *semantic* — a quota filled by ballot count instead of ballot weight — and a type system does not catch those.

---

## Verdict

**Build the kernel if — and only if — the goal is WASM in the browser or exhaustive ballot-space search.** Both are real, both are out of Python's reach, and both are served by the same 1,500-line pure library. Under that framing the scope question answers itself: kernel plus JSON in and out, no CLI, no filesystem, no reporting.

**Do not build "the engine, but in Rust."** As a general-purpose replacement it is a large amount of work to arrive at the same winners, plus a permanent drift liability, in exchange for speed nobody needs.

---

## Prerequisites — all of them in Python, all useful anyway

None of this requires deciding about Rust. All of it should happen regardless, and doing it first is what would make a port start with a green test harness instead of an argument about what "correct" means.

1. **Add a `--json` result mode to the LH engine.** Today the CLI is hand-rolled `sys.argv` parsing with `--save` and `--full`, and the only machine-readable output is the `expected_winners:` line in the input. A JSON *result* — winners, per-round tallies, pairwise matrix, elimination order, exhausted counts — is richer than the answer key, far cheaper than the text mirror, and is the natural conformance-fixture format for any second implementation. It would also let the divergence ledger and the page generator stop re-parsing rendered reports.
2. **Backfill the 48.** Every ballot-carrying case gets an answer key. **Done 2026-08-20 — by dissolving, mostly.** The 48 was the raw case-count arithmetic, and on inspection only **4** were ordinary teaching cases missing keys (the Alabama-paradox pair, the bloc-vs-PR pair) — keyed and engine-verified. The other 44 were never backfillable: 34 deliberately-malformed negative fixtures (machine-checked the other way, by [`tests/test_negative_validation.py`](../../STARVote_LH_tabulation_engine/tests/test_negative_validation.py) asserting exit 1 and the right error), 3 engine/tool demo inputs, a drift of 5 in the count itself through ordinary churn since the note was written (cases keyed, moved or retired), and **2 cases whose entire point is that no winner exists** — the quorum-fail demo elects nobody, and BV2269 (three seats, three candidates) is refused outright. Those last two are the real residue: `expected_winners:` has no way to say *"nobody"* or *"this file must not tabulate,"* which is a gap in the answer-key format, not in the corpus.
3. **Write down the method-alias table.** `STAR` / `star` / `bloc` / `rr` / `RCV_IRV` / `RCV-IRV` / `IRV` / `RCV` are all live in the corpus, along with values carrying trailing `#` comments. Python is forgiving by accident; anything else will be strict by construction.
4. **Write down the tiebreak ladders** — per method, per engine, as prose. This is the single largest source of legitimate disagreement between correct implementations, *and* — as the 2026-08-19 Ranked Robin correction showed — the place a single implementation quietly stops matching the method it claims to count. **Done 2026-08-20:** [tiebreak_ladders.md](tiebreak_ladders.md) states every ladder side by side, code-verified per engine; the per-method stories stay on [the ladder itself](../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md) and [the engine-by-engine comparison](../../05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md), which it links rather than restates.

---

## Hazards a port will actually hit

Not the ones people expect. In rough order of how much time each would cost.

**Ties and lots.** The LH engine breaks a Copeland tie by Ranked Robin's published [degrees of ties](../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md) — the **1st Degree** (greatest sum of win margins over the other finalists), then the **2nd Degree** (the same sum over the whole field), then a published `lot_numbers:` draw; BetterVoting implements the 1st Degree for a two-way tie only and sends anything larger to a seeded shuffle. Two implementations can agree on every tally and still disagree on winners across a meaningful share of cases. A port must replicate the *ladder*, rung by rung, or its disagreements will be unreadable — and the ladder is also the part of this engine that was most recently **wrong**: until 2026-08-19 it had no 1st Degree rung, ranking ties by total margin over the whole field, and correcting that changed the winner on 11 of the library's 100 Ranked Robin cases. A port written against those winners would have inherited the bug and passed.

**IRV elimination order.** [`rcv_irv_tabulation.py`](../../06_Other/RCV_IRV/RCV_IRV_tabulation_engine/rcv_irv_tabulation.py) deliberately reads eliminations back out of `pyrankvote` rather than recomputing them, specifically so the transfer block cannot contradict the round table on a tie settled by the second-choices ladder. A Rust kernel has nothing to read back from — it must reproduce `pyrankvote`'s tie rule independently, and that rule is a behaviour of a specific library, not a property of IRV.

**Blanks and markers.** `-` `~` `&` `?` `%` all tabulate as 0 but mean different things, and the distinction is the whole subject of several teaching cases. Any type that models a ballot entry as a plain integer has thrown away information the library cares about.

**Floating point in the PR family.** Allocated score, SSS, and RRV carry fractional weights. Both languages are IEEE 754, so the values agree; *summation order* need not, and reweighting amplifies it. Decide early whether the kernel uses rationals or floats, and if floats, whether comparisons get an epsilon.

**The 0–5 score cap is a teaching guardrail, not an engine limit.** Larry's underlying `starvote` is range-parametric. Do not bake `0..=5` into a Rust type; make the maximum a parameter, as the original is.

**Licensing.** `starvote` is MIT ([LICENSE](../../STARVote_LH_tabulation_engine/LICENSE)) — a derived port is fine with attribution. Worth settling before anything is published rather than after.

---

## Interface sketch

Deliberately small. The shape matters more than the details, and the shape is: *no I/O anywhere in the library*.

```rust
pub struct Election {
    pub candidates: Vec<String>,
    pub ballots:    Vec<Ballot>,   // weighted; blanks and markers preserved
    pub method:     Method,
    pub seats:      usize,
    pub lot:        Option<Vec<usize>>,  // published draw, for reproducible tiebreaks
}

pub struct Outcome {
    pub winners:      Vec<String>,
    pub rounds:       Vec<Round>,        // scoring, runoff, or IRV rounds
    pub pairwise:     Option<Matrix>,
    pub tie_resolved: Option<TieRung>,   // which rung of the ladder decided it
}

pub fn tabulate(e: &Election) -> Result<Outcome, TabulationError>;
```

One entry point, one error type, serde derives for the JSON contract, and a separate thin crate for the CLI and for the WASM binding. The conformance harness is then a loop over the case files comparing `Outcome` to the fixture — which is the thing worth building first, before any method is implemented.

---

## Open questions

- Is the WASM demo actually wanted on the site, and where would it live? The answer decides whether this project happens at all.
- From-spec or from-code? From-spec is the only version that is a real cross-check, and it is meaningfully slower to write.
- Does the kernel own tiebreaks, or take a resolved order as input? Taking it as input makes the kernel a pure function of its arguments and pushes the messiest disagreement out to the caller.
- Rationals or floats for the PR family?

*Up: [Tabulation engines](README.md) · [07_Concepts](../README.md).*
