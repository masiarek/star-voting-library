# The STAR reference package — requirements at a scope one person can finish

**Level: reference · deep dive**

**One line:** a certified STAR tabulator running in a county *is* a moonshot — but the moonshot is only moon-sized because approval is bundled into the goal; **unbundle it and what remains is a six-document reference package that needs nobody's permission, is useful the day it exists, and makes the eventual certified product dramatically cheaper.**

This page is deliberately short. It is the working requirements document for the small scope; the reasoning that led here is in [certifying STAR software](certifying_star_software.md) and the long exploration in [goals and requirements](rust_kernel_requirements.md).

---

## The unbundling

Two things keep getting treated as one goal:

| | The product | **The reference package** |
|---|---|---|
| What | A certified STAR tabulator a county runs on election night | The specification, test, and documentation set any implementer would need |
| Gated by | A sponsoring organization, a VSTL budget, a vendor pairing, state approval, and **a jurisdiction that wants it** | Nothing |
| Timeline | Years, and only after demand exists | Evenings |
| Who can do it | An organization | **One person with 615 verified elections and six engines' worth of divergence knowledge** |
| Value if the other never happens | Zero | Teaching content, a publishable conformance suite, and an answer ready when someone asks |

**A moonshot is something where you cannot do a useful fraction.** This is not one. The documentation *is* the fraction, it stands alone, and it happens to be the part that no amount of funding shortens — because it needs someone who knows the method cold, not someone who knows procurement.

**And the approval gate is demand-gated, not effort-gated.** Nobody certifies a tabulator nobody asked for. Waiting on R5 is therefore correct rather than defeatist; the job in the meantime is to be *ready when asked*, and readiness is a documentation state.

---

## Scope

**In scope.** A tabulator that consumes anonymous cast vote records from an already-certified scanning system and produces a canvass-ready STAR result — and, for now, only the *documents* that specify, test, and describe such a thing.

**Explicitly out of scope, permanently:** voter registration, pollbooks, ballot issuance, authentication, credentialing, chain of custody, scanners, ballot-marking devices, operating systems, hardware. The jurisdiction owns all of it. The tabulator is blind to identity by design, and that blindness is a security property rather than a limitation.

**Out of scope for now:** the software itself, the VSTL engagement, and any vendor conversation. Those begin at R5.

---

## The six deliverables

Each is a document. Each is finishable. Each is worth having on its own.

### D0 — The vocabulary map

**Do this before anything else, because every other document uses the words.** This library, and BetterVoting, say **race**; the standard term is **contest**. That single slip is enough to mark an implementation statement as amateur to a lab reviewer, and there are a dozen more like it.

A one-page table mapping this repo's teaching vocabulary to the standard vocabulary used by NIST and the EAC:

| Here | Standard |
|---|---|
| race | **Contest** (specifically a `CandidateContest`) |
| the thing a voter marks | `Candidate` + `ContestSelection` |
| a ballot, as cast | **`CastVoteRecord`** |
| the score a voter gave | `SelectionPosition` (its value) |
| precinct | `GpUnit` / `ReportingUnit` |
| voting method | **`VoteVariation`** |
| winner | the contest result; a candidate is *elected* |

Authoritative sources exist to align against — NIST's [election glossary](https://pages.nist.gov/ElectionGlossary/) and the [CVR common data format](https://pages.nist.gov/CastVoteRecords/). This is cheap, it is a day's work, and it buys credibility that no amount of correct arithmetic will.

**It does not mean changing the teaching pages.** "Race" is the word readers use, and the [voice rules](../../CONTRIBUTING.md) say meet people where they are. It means the *certification-facing* documents speak the reviewer's language, and that the map between the two is written down once so neither drifts.

### D1 — The clause-numbered specification

Enough to implement STAR correctly **without reading any implementation**. Every tie rung, every ballot-marking edge case, every reporting obligation. Each clause numbered, each clause citing the case file that pins it.

**Done when:** a competent stranger could implement from it and pass the conformance suite. **Why first:** everything else references clause numbers.

### D2 — Rule-space coverage, and the gap list

Tag every existing case with the clauses it exercises; generate the list of clauses no case would catch a violation of; write the missing cases.

**This is the deliverable that changes what the library *is*.** The 615 cases currently prove *agreement between engines*. They do not yet prove *rule coverage* — a corpus can hold 615 elections and still have no case where the runoff pair is itself tied. Coverage of rule space and coverage of election space are different claims, and case count measures the wrong one.

**Done when:** every clause has at least one case that fails if the clause is violated.

### D3 — The conformance suite, published for implementers

The existing corpus, re-fronted for a reviewer rather than a learner: the format, how to run your own engine against it, what a pass means, what each case proves. Plus the JSON result contract that makes engine comparison mechanical.

**Started 2026-08-10.** The result contract half is built — [the result contract page](result_schema.md), a published [JSON Schema](../../STARVote_LH_tabulation_engine/star_result.schema.json), and `--json` on the engine, covering all six method families the engine counts. The tiebreak ladders — every method, every engine, as prose — are written too ([tiebreak_ladders.md](tiebreak_ladders.md), 2026-08-20): that is the D1 clause set an implementer could least afford to reverse-engineer from cases. The "48 unanswered cases" also closed 2026-08-20: on inspection only 4 were real teaching cases (now keyed and engine-verified); the rest were negative fixtures, demo inputs, and two no-winner-by-design cases the key format cannot express — the accounting is in [the scope note's item 2](rust_kernel_scope.md). The answer-key form for *"no winner"* is done too (2026-08-21): `expected_outcome:` — `elected` / `no_winner` / `rejected` — is a documented, linted, engine-enforced key. Still open: per-case *what this proves* notes, and the rest of the executable specification (D1).

**The input half is built too, 2026-08-21** — [the election contract](input_schema.md), a published [`star_election.schema.json`](../../STARVote_LH_tabulation_engine/star_election.schema.json) with one worked illustration per method, and `--emit-election-json` on the engine. All 593 case files emit a valid document (including the 7 grade files, which the result contract cannot express at all), and on the 586 with countable ballots the ballots rebuilt from the JSON are **identical** to the ones the engine parsed. It exists because the result contract compares two counts while silently assuming the two engines read the same election — an assumption §2 below shows does not survive a second YAML parser.

**Done when:** someone else's tabulator can be scored against it without asking us anything.

### D4 — A logic-and-accuracy test deck

Every jurisdiction runs L&A before every election. For plurality this is routine; for RCV it now exists; for STAR nobody has written what the deck contains or what output to expect. A small, deliberately-designed set of ballots with a hand-verifiable expected result — exactly this library's house style.

### D5 — A model VVSG 2.0 implementation statement

The highest-leverage document nobody has written. Because the EAC defines no requirements for *what a voting method is* and instead tests a system against its own stated implementation, this statement **is** the method-specific certification content. A handful of pages that hands any future vendor or nonprofit the hardest part of their paperwork, pre-drafted — and that makes STAR procurable, since a jurisdiction cannot write a contract for a method nobody has specified.

### D6 — The CVR mapping

How a 0–5 score ballot is represented in a cast vote record — NIST CDF, and whatever the vendor exports look like.

**Partly unblocked already, and the news is good.** NIST's CVR common data format defines a `VoteVariation` enumeration for how a contest is tabulated, and **`range` is one of its values** — alongside approval, cumulative, RCV, plurality, and `other` (paired with `OtherVoteVariation` for anything unlisted). The format also allows **multiple `SelectionPosition` instances per candidate**, explicitly for vote variations where a voter marks more than one option per candidate — which is the structure a score grid needs.

The clean way to state it, and the reason this matters: **a CVR records the ballot, not the tabulation.** A STAR ballot *is* a range ballot; the automatic runoff is a downstream counting rule the format never needs to know about — exactly as a ranked CVR is neutral between IRV, Ranked Robin, and STV. So the likely mapping is `VoteVariation: range` at the record layer, with STAR named in the implementation statement, and `other` available if a reviewer wants the contest labelled explicitly.

**What remains genuinely unknown is not the format but the product:** whether any certified scanner *emits* such a CVR today. That is a vendor question, and it is the pivotal one below.

---

---

## "But we use YAML" — the format is not the lesson, and there is a trap underneath

Worth separating three things that ride together here.

### 1. The lesson is separation, and this library does the opposite — correctly

RCTab's config file names the rules, the candidates, the output metadata, and **the paths to the CVR files**. The ballots are somewhere else, because on election night they arrive from a scanner by the thousand.

This library puts the ballots *inside* the same file as the configuration. That is right for what it is — one file is one complete, readable, self-contained election, which is what makes a case file teachable and testable. It is a **fixture format**, and fixture formats should be self-contained.

A production tabulator needs the split, for a reason that is procedural rather than aesthetic: **the configuration is authored, reviewed, approved, and hashed *before* election day; the ballot data does not exist until after the polls close.** They have different lifecycles, different signers, and different audit trails, so they cannot live in one artifact. So: adopt the separation in the reference package's design, and do **not** propagate it back into the case library.

### 2. YAML versus JSON barely matters for *emitting* — and matters a great deal for *ingesting*

YAML 1.2 is a superset of JSON, and emitting JSON from the existing files is one line of code. If a lab or a vendor wants JSON, generate it. Migrating 649 case files would be work for no benefit.

**But that symmetry breaks the moment a second implementation reads the same file.** PyYAML is YAML **1.1**; every YAML parser in the Rust, Go and modern JS ecosystems is YAML **1.2 core schema**. Probed directly (PyYAML 6.0.3 vs `serde_yaml` 0.9.34), `No` → `False` on one side and `"No"` on the other, `12:30` → `750` vs `"12:30"`, `007` → `7` vs `"007"`. The port is *more correct* every time, which is exactly the problem: conformance means agreeing with the reference, so the correct implementation is the one scored as divergent. That is not a style question — it is the same certification-context determinism argument as §3 below, arriving through a different door, and `source.sha256` cannot see it because the **bytes** are identical.

The fix is not to migrate the corpus. It is to generate a normalized JSON document from the reference reader and let every other engine consume that, so the bespoke ballot DSL keeps exactly one implementation, forever, in Python. Design, with one illustration per method: [the election contract](input_schema.md).

### 3. But YAML's implicit typing is a genuine certification-context hazard

This is the part worth knowing, and it is not hypothetical — probed against this repo's own `yaml.safe_load`:

| Written | Parsed as |
|---|---|
| `No` | `False` (bool) |
| `Yes` | `True` (bool) |
| `Off` | `False` (bool) |
| `1.10` | `1.1` — the trailing zero is gone |
| `12:30` | **`750`** — YAML 1.1 reads it as base-60 |
| `null` | `None` |

For a configuration file whose scalars include **candidate names and contest titles**, that is a live category of defect. JSON has no implicit typing: a string is a string. Where a reviewer must be certain that two independent parsers read the same bytes the same way, JSON's much smaller grammar is a real, defensible advantage — an attack-surface and determinism argument, not a style preference.

**This repo is accidentally hardened against most of it, and a plausible "cleanup" would break that.** Candidate names and scores live inside the `ballots: |-` block literal, which YAML hands over as a single opaque string for the engine's own parser to read — so the scalar resolver never sees a candidate name. A tidier-looking redesign that promoted candidates to a proper YAML list would introduce the bug it currently avoids by construction. Worth writing down before someone improves it.

**One exposure does remain.** `expected_winners:` *is* a YAML list, so a candidate named `No` would parse as `False`, and a **correct** result would fail the test harness — a false failure that looks like an engine bug. Checked across all 649 tracked files: **zero currently trigger it**, so this is latent rather than live. But note how easily it stops being latent: the natural way to add a ballot-measure case is a contest whose options are *Yes* and *No*.

### 4. This was already solved once, and the solution was lost

The trap above is not a new discovery. **The project used StrictYAML, deliberately, for exactly this reason — and it was dropped.**

Commit `996016b` (2026-05-03) carries `from strictyaml import load, YAMLError` in live Python. The README of that era stated the rationale in as many words: StrictYAML *"securely handles the string-to-dictionary parse to avoid type coercion,"* handing the result to **Pydantic** for cross-field validation, with the pipeline *"serializing validated cases into strict JSON baselines for secondary systems."*

Today: no `strictyaml` dependency anywhere in `pyproject.toml` or the lockfile, no import in any source file, no mention in any tracked document, and the engine parsing with `yaml.safe_load`. The code went first; the README paragraph was removed later in `26a8758`. Neither removal appears deliberate — this looks like drift as the project turned from "Better Voting Test Library" into a teaching library, not a decision anyone made.

**Note what that earlier design already anticipated.** "Strict JSON baselines for secondary systems" is precisely the D3 conformance contract, and precisely the answer to *"a future implementation will want a JSON interface."* The May 2026 architecture had the right shape for a question this page took a long conversation to re-derive.

### What to actually do about it

Three options, and the cheapest two are not exclusive.

| | Guarantee | Cost |
|---|---|---|
| ~~A hygiene check~~ — **built 2026-08-10**: `check_yaml_name_types()` rejects any `expected_winners` entry or `election_title` that parses as a non-string | Closes the known hole | done |
| **Pydantic models over `safe_load`** — validate types and cross-field rules after parsing | Same practical guarantee, plus cross-field validation, **plus JSON Schema generation for free** | A day; but it *is* D3 |
| **Restore StrictYAML** — no implicit typing at the parse boundary at all | The strongest guarantee, and the original intent | A schema, a dependency, and reformatting **32 files** |

That last number is worth having measured: StrictYAML forbids flow style, so `expected_winners: [Ben]` would have to become a block list — and **only 32 of the 569 files use flow style; 537 are already block style.** The migration everyone assumes is expensive is two dozen mechanical edits.

**Done: the hygiene check.** `check_yaml_name_types()` in [`check_repo_hygiene.py`](../../STARVote_LH_tabulation_engine/tools_adam/scripts/check_repo_hygiene.py), gated by [`test_md_links.py`](../../STARVote_LH_tabulation_engine/tests/test_md_links.py) with a non-vacuous companion that proves it fires on `No`, `Yes`, `12:30` and `null` while sparing a quoted `"No"` and the string `Nan`. All 649 tracked files pass, so the class is now closed going forward rather than merely known.

**Still recommended: Pydantic when D3 is built.** Pydantic covers the same hole, adds the cross-field validation the original design wanted, and emits the JSON Schema that the conformance contract and any non-Python implementation both need — one tool serving three items on this page. StrictYAML remains the purist answer and is cheaper than it looks; it is just narrower in what it buys.

## Sequencing

**D1 → D2 → D3** is the spine, in that order, because D2 needs D1's clause numbers and D3 is D2 made presentable. D4 and D5 can be written at any point and are the two most likely to be read by someone outside this project. D6 waits on an answer nobody here can produce.

**Before any of it: ask the one question.** *Can a certified scanner and its CVR export represent a 0–5 score ballot at all?* It is a question, not a project — a conversation with a vendor or an election official — and the answer reshapes D6 and possibly the whole path. RCTab could exist as an add-on precisely because certified systems already record and export rankings. Whether they can do the same for a score grid is the pivotal unknown, and it is cheap to find out.

**And the actual first action is smaller than any of this:** run the 48 ballot-carrying cases that still have no `expected_winners:` line and write the answers in. Mechanical, one evening, no decisions, and it takes the corpus to fully machine-checkable — which every deliverable above rests on.

---

---

## Who actually does the certification — and what they need from us

The right instinct: **we are not trying to get certified. We are trying to make STAR the cheapest new method anyone could add.** Somebody else owns the certification relationship — and they own it *already*, as a going concern.

An established vendor has the VSTL relationship, the lab budget, the implementation-statement template, the technical data package apparatus, the QA and regression machinery, and staff who have done this before. What they do not have is a reason to care about STAR and a pre-solved definition of it. A vendor adds a method when a customer asks, or when it is nearly free. **We cannot manufacture the first. We can move the second a long way** — the specification, the conformance suite, the L&A deck, and a drafted implementation statement together represent a large share of the internal cost of adding a method, handed over at no charge, already argued through.

There are **two paths, and the package serves both identically**, which is why there is no need to bet on one:

- **Vendor-native.** A vendor implements STAR inside their certified system and carries it through their own certification. Their language, their toolchain, their liability.
- **The RCTab path.** A nonprofit builds the adjunct tabulator; a *state* procures it — Virginia purchased RCTab rather than a vendor adopting it — and it is evaluated in configuration with the certified system. Note this is procurement by a jurisdiction, not adoption by a vendor: a different door, same paperwork.

### On "give them ready software"

Worth being realistic about how that lands. Vendors are generally reluctant to take outside code into a certified baseline — licensing, liability, their own coding standards, and a certification baseline they do not want to disturb. What they will actually use, in descending order of eagerness:

1. **The test deck.** The thing they most want and least want to build themselves.
2. **The specification.** It removes the argument about what STAR is.
3. **A reference implementation — as an oracle to diff against, not as code to ship.**

That third point resolves the language question that has been circling this whole discussion. **If the software's job is to be an oracle rather than a product, Python is entirely appropriate — and it already exists.** The single-static-binary argument applies only to a *shipped* adjunct tabulator on an air-gapped machine. Build the oracle in the language that already works; defer the packaging question to the path that actually needs it.

### On licensing — MIT is the least of the obstacles

The worry that a vendor would object to an open-source, MIT-licensed library is worth answering directly, because it points at the wrong risk.

**MIT is the license a vendor wants**, if they are going to take code at all: permissive, no copyleft, no obligation to publish their own source, no viral scope. The license vendors object to is the GPL. And **the precedent runs the other way** — RCTab is open source and was approved; Virginia's review described it as the first open-source software to meet VVSG standards, noted its third-party modules as original, unmodified, and likewise open source, and treated open source as a **transparency virtue** rather than a liability.

The real objections are not about the license text:

- **Warranty and accountability.** MIT disclaims all warranty, and a vendor carrying certification liability cannot lean on "AS IS". This — not copyleft — is the reason they would rather reimplement from a specification than adopt code. It also reinforces the point above: sell the spec and the test deck, offer the implementation as an oracle.
- **Certification baseline disturbance.** Any code entering a certified baseline triggers retesting, at a cost unrelated to licensing.
- **Provenance.** Who wrote each line, and did they have the right to contribute it? A clean history and a DCO or CLA matter more to corporate counsel than the license name, and are worth putting in place *before* there are outside contributors rather than after.
- **Coding standards.** Virginia's review examined design and coding standards explicitly. Outside code rarely matches a vendor's, and rewriting to match is often cheaper than reviewing.

**What RCTab actually chose is worth knowing: MPL-2.0**, not MIT — the Mozilla Public License, a *file-level* copyleft. Modifications to MPL-licensed files must be published under MPL, but those files can be combined with proprietary code in a larger work without infecting it. For election software that is a deliberate and rather good bargain: **the counting logic stays inspectable no matter who ships it, while commercial integration stays possible.** MIT would let a vendor fork the tabulator and never show what they changed about how votes are counted — which, for voting software specifically, is the wrong default. One caveat on the precedent: RCTab was *procured by a state*, not incorporated by a vendor, so its license has not actually been tested against commercial integration.

**Three artifacts, three different answers — pick per artifact, not once for everything:**

1. **The specification and the case corpus: maximally permissive** (CC0 or CC-BY). They are documents and data, not software; the entire point is that a vendor, a lab, or a competing implementer can lift them without a conversation or an attribution obligation buried inside a certification package. **These are the artifacts most likely to actually be used**, and they carry none of the objections above.
2. **A shipped tabulator: MPL-2.0, following RCTab.** Same niche, same reasoning, and a reviewer has already seen it approved once — which is worth something on its own.
3. **A library or oracle intended for adoption: MIT or Apache-2.0.** Apache-2.0 adds an explicit patent grant that corporate counsel prefers and MIT lacks; dual `MIT OR Apache-2.0` is the Rust ecosystem convention for exactly this reason.

The inherited obligation applies throughout: the engine derives from Larry Hastings' MIT-licensed `starvote`, and MIT's attribution travels into any of these (MIT being permissive, relicensing a derivative under MPL is allowed as long as that notice survives).

### The follow-up question worth asking directly

The certification bodies and labs are approachable, and the cheapest possible research step is to ask them rather than infer. The EAC publishes explanatory guidance and a clearinghouse address; an accredited VSTL will discuss scope and rough cost. Two questions worth putting to them, in writing, early:

- Given that the EAC sets no method-specific requirements and tests against the manufacturer's implementation statement, **what would an implementation statement for a score-then-runoff method need to contain** to be testable?
- **Can a currently certified scanner's CVR export represent a 0–5 score per candidate**, or would that require a change to a certified component?

The second is the pivotal unknown from the previous section. Both are questions, not projects, and either answer is worth having before writing D6.

## What this is not

- **Not a promise.** Nothing here is announced, roadmapped, or offered to anyone.
- **Not compliance advice.** These would be drafts for practitioners to argue with, and should say so on their face.
- **Not a reason to write software yet.** The language question — and the observation that an air-gapped, hash-verified deployment argues for a single self-contained binary — is [parked](certifying_star_software.md) until R1–R4 are real.
- **Not urgent.** Certification becomes the bottleneck the day *after* a jurisdiction says yes. Having the documents already written is worth something precisely because that day cannot be scheduled.

*Up: [Tabulation engines](README.md) · the landscape: [certifying STAR software](certifying_star_software.md) · the reasoning: [goals and requirements](rust_kernel_requirements.md) · [07_Concepts](../README.md).*
