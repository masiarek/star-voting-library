# A Rust voting kernel — goals, requirements, and how to get ready

**Level: reference · deep dive**

> **Decision, 2026-08-10: no Rust kernel for this library. Python stays.**
>
> The reasoning is in [Why Python is the right language for a test library](#why-python-is-the-right-language-for-a-test-library) below, and it is short: a teaching-and-test library's dominant costs are authoring speed, readability, and staying inside the Python social-choice ecosystem that supplies its cross-checks. Rust's advantages buy nothing there and its costs land on the thing done most often.
>
> **What survives the decision is Track A** — the JSON result contract, the 48 missing answer keys, the alias table, the written tiebreak ladders. Those were always worth doing in Python, and they are now the whole recommendation.
>
> **What Rust keeps a real claim to is a different project:** software that counts a real, high-stakes election under verifiable encryption. That is not this repo's job, it needs a funded independent audit, and it would have a different owner. The analysis below is kept because it is the argument for why — and so the question does not get re-opened from scratch.

> **Superseded in scope, kept for the reasoning.** The exploration on this page converged on a much smaller and better-defined target: [the STAR reference package](star_reference_package.md), with the certification landscape in [what would it take to certify STAR Voting software?](certifying_star_software.md). Read those two first; this page is the argument that got there.
>
> **If this page looks like a monster: it is a register of opportunities, not a backlog with a due date.** Nothing here is blocking anything. Most of the "requirements gathering" it describes is **harvesting, not authoring** — the requirements are already encoded in 615 case files and six engines' worth of recorded disagreements, and the job is transcription, one method at a time.
>
> **The smallest real first step takes an evening and needs no decisions:** run the 48 ballot-carrying cases that have no `expected_winners:` line, check the results, and write the answers in. No schema, no spec, no document. That is the largest single chunk of rung 1, it is mechanical, it finishes, and it takes the corpus to 100% machine-checkable. Everything else on this page can wait indefinitely.

**Status: analysis retained; decision recorded above.** This is a working document, not a plan of record. Its companion [A Rust tabulation kernel — scope](rust_kernel_scope.md) argues *what* such a kernel should and should not contain; this page works the step before that, which is deciding what the thing is **for**, and then deriving requirements from the answer instead of inventing them.

Nothing below should be built yet. Part 3 is the only section with work in it that is worth doing regardless of how the decision goes.

---

## How to use this page

Three passes, in order, and the order matters:

1. **Goals** — pick exactly one primary goal. Everything downstream is a consequence.
2. **Requirements** — derived from that goal, not brainstormed independently.
3. **Readiness** — what must be true in this repo, and in the author's head, before the first line of Rust.

The failure mode this page exists to prevent is starting with a scope ("port the engine") and reverse-engineering a justification. That produces a library that does everything adequately and nothing well.

---

# Part 1 — Goals

## The discipline: one primary goal

Each candidate below produces a **materially different library**. Not a different emphasis — a different public API, a different dependency set, a different definition of done. Two co-primary goals is the same as no goal.

Rank all five. Only the top one gets to constrain the design; the rest are allowed to happen for free or not at all.

### G1 — Live tabulation in the reader's browser (WASM)

**Success looks like:** a reader on the published site edits a ballot on a teaching page, and the runoff result updates without a page load or a server.

**Demands:** a kernel compiled to WebAssembly, a JSON in/out contract, no filesystem, no threads, a small binary, and a JavaScript shim on the site. Ties must be deterministic client-side.

**Makes irrelevant:** CLI ergonomics, batch throughput, reading YAML at all (the page hands it structured data).

**Verdict:** the strongest goal on the list, because it is the only one that gives the *library's readers* something they cannot have today. Everything else on this list benefits the maintainer.

### G2 — Exhaustive and property-based search over ballot space

**Success looks like:** a statement of the form *"no 3-candidate, ≤7-voter STAR election exhibits a monotonicity failure"* — proved by enumeration, with a witness when one exists.

**Demands:** raw speed, an allocation-light kernel, `proptest` or a hand-rolled enumerator, and a way to emit a discovered counterexample **as a YAML case file** so a finding lands back in the library.

**Makes irrelevant:** WASM, pretty output, most of the method coverage — a search tool that only knows STAR and IRV is already useful.

**Verdict:** the most *interesting* goal, and the one that could produce results worth publishing in the [research-topics companion repo](https://github.com/masiarek/star-voting-research-topics). Also the one most likely to eat unbounded time.

### G3 — A genuinely independent third implementation

**Success looks like:** all 567 answered cases agree, and the disagreements found while getting there are written up as bugs in one engine or the other.

**Demands:** breadth over depth — every method the library uses — and the hard constraint that it is written **from the written rules, never transliterated** from the Python. A translation inherits the original's bugs and proves nothing.

**Makes irrelevant:** speed, WASM, ergonomics. Only agreement matters.

**Verdict:** honest but weak on its own. The library already has five engines refereeing each other; a sixth has diminishing returns, and this goal is better treated as a *by-product* of G1 or G2 than as the reason to start.

### G4 — Faster regeneration of the library's artifacts

**Success looks like:** the full mirror-and-page rebuild drops from minutes to seconds.

**Verdict:** **reject.** The bottleneck is not tabulation, it is page generation and Markdown rendering, which is out of scope for a kernel. Nine-voter elections do not need Rust.

### G5 — Learning Rust, with a domain the author already knows cold

**Success looks like:** fluency in ownership, traits, enums, and `serde`, acquired on a problem where the correct answers are already known.

**Demands:** almost nothing from the repo. Small scope, fast feedback, permission to throw it away.

**Verdict:** entirely legitimate, and worth stating out loud if it is the real driver. It is the *best* domain for the purpose — 567 known-correct answers is a rare luxury for a learning project. But if this is the primary goal, the repo should not be reorganized around it, no page should promise it, and the scope should be one method, not seven.

### G6 — A shared conformance suite that other projects adopt

**Success looks like:** a second project — BetterVoting, a student implementation, a new engine — runs this library's case files against its own tabulator and finds a bug, without anyone here being involved.

**Demands:** the JSON result contract, a published schema, a stable case format, and a `README.md` aimed at implementers rather than learners. The Rust kernel's role is to be the **reference implementation** that proves the suite is implementable by someone who did not write the Python.

**Makes irrelevant:** WASM, speed, breadth beyond what the suite covers.

**Verdict:** quietly the highest-leverage goal on this list, and the least glamorous. The 615 cases are the thing this project has that nobody else does; a kernel is one more engine, but a conformance suite is infrastructure. Note that most of the value here is **Track A work in Python** — the Rust part is almost incidental.

### G7 — Audit artifacts and risk-limiting audits for STAR

**Success looks like:** given a set of ballots, the tool emits a tamper-evident audit artifact — a hash-chained ballot manifest plus a deterministic tally — and, further out, computes a risk-limiting audit sample size for a STAR contest.

**Demands:** determinism above all (NFR-2), a stable canonical ballot serialization, and for the RLA half, real statistics.

**Verdict:** the RLA half is a genuine research gap — [SHANGRLA](https://arxiv.org/abs/1911.10035)-style methods are well developed for plurality and thin for score methods — and it belongs in the [research-topics companion repo](https://github.com/masiarek/star-voting-research-topics) before it belongs in code. The hash-chain half is a weekend and needs no Rust at all.

### G8 — Moonshot: publish the encrypted ballots, count them without opening them

This is the one worth taking seriously, so it gets its own treatment below.

### G9 — Rebuild BetterVoting in Rust

**Verdict: reject.** Reasoning in its own section below, because the *reason* it is wrong points at what is right.

---

## G8 in detail — end-to-end verifiability

**The idea:** every cast ballot is published, encrypted. Anyone can verify that the announced result is the sum of exactly those published ballots. Nobody can read any individual ballot. Voters can confirm their own ballot is in the set.

**The good news is that the analysis is already done, in this repo.** [Counting under encryption](../topics/homomorphic_tallying.md) works the whole argument through: the tally is addition, so *additively* homomorphic encryption suffices (not FHE); STAR's scoring round is exactly [ElectionGuard](https://github.com/Election-Tech-Initiative/electionguard)'s construction with a 0–5 range instead of 0/1; the automatic runoff is **not** additive, because it is a comparison against a pair not known until after the scoring round decrypts; and the fix is to have each ballot also carry an encrypted indicator per ordered pair, with a zero-knowledge proof that those indicators are consistent with the scores.

**Why this matters strategically, and not just technically:** that fix is the [summability](../topics/summability/README.md) property wearing a different hat. A method is homomorphically tallyable for essentially the same reason it is precinct-summable — the tally is a fixed-size sum. So the methods this library advocates ([STAR](../../01_STAR/01_Learn/properties_and_limits/STAR_summability.md), Approval, [Ranked Robin](../../05_Ranked_Robin/01_Learn/RCV_RR_summability.md)) are precisely the ones that admit efficient encrypted tallying, and the method it critiques is precisely the one that [does not](../../06_Other/RCV_IRV/concepts/RCV_IRV_lack_of_summability.md) — IRV's sequential elimination needs ballot-level data, so encrypted IRV needs mixnets or heavy multiparty computation instead. That is a real argument, it is already half-written across the [summability demo](../../method_comparisons/summability_demo/README.md), and it is the kind of claim this library exists to make runnable.

**Why Rust specifically, here and nowhere else on this list:** the applied-cryptography ecosystem is genuinely best-in-class in Rust — the `dalek` curve libraries, Bulletproofs, `arkworks` — and it targets WASM well. This is the one goal where the language choice is not arbitrary. Everywhere else, Rust is a preference; here it is close to the right answer.

### The moonshot decomposes — that is the whole point

Treat it as a ladder where each rung ships something standalone. It stops being a moonshot the moment you notice rung 0 is already built.

| Rung | Deliverable | Effort | Standalone value |
|---|---|---|---|
| **M0** | The teaching page: why score methods can be counted encrypted and IRV cannot | **done** — [`homomorphic_tallying.md`](../topics/homomorphic_tallying.md) | already has it |
| M1 | Toy additive tally for **Approval** — exponential ElGamal, single trustee, no proofs, WASM demo on the site | days | a reader watches encrypted ballots become a verified total |
| M2 | Range proofs — prove each encrypted score is in 0–5 without revealing it | weeks | ballots become well-formedness-verifiable |
| M3 | **Full STAR**: encrypted scores *plus* pairwise indicators *plus* a consistency proof | months | the novel piece; a paper, not a feature |
| M4 | Threshold decryption across *k* of *n* trustees | months | no single party can open anything |
| M5 | Bulletin board, cast-as-intended challenge, receipts | open-ended | a system, and one nobody should trust unaudited |

**M1 and M2 are a WASM demo, which is G1.** That is the key planning insight: the moonshot's early rungs and the most defensible near-term goal are *the same work*. Choosing G1 does not defer G8; it starts it.

### How valuable is this to STAR, actually?

Worth separating, because the four audiences give four different answers and only one of them is "very".

**To STAR adoption in US government elections: near zero, and possibly negative.** No election official has ever declined STAR because the ballots weren't encrypted. The live obstacles are awareness, equipment certification, state law, and FairVote's head start. Worse, US election administration is moving deliberately *toward* hand-markable paper and risk-limiting audits and *away* from anything that sounds like cryptographic online voting — and the election-security research community is, with good reason, hostile to internet voting after a decade of broken deployments. Attaching STAR to that association could cost more than it gains with exactly the constituency that decides.

**To STAR in online and organizational elections: moderate and real.** Unions, co-ops, HOAs, student governments, professional societies, party conventions — these already vote online, usually with no verifiability whatsoever beyond trusting the vendor. That is where [BetterVoting](BV/README.md) already plays, and "publish the encrypted ballots and verify the count yourself" is a genuine differentiator in a field that currently offers nothing. Modest market, real value.

**To STAR's intellectual standing: high — and it is the cheapest value to capture.** STAR is close to absent from the cryptographic-voting literature. A worked scheme for homomorphically tallying a score-plus-runoff method would put it there, and the second-order effect matters more than the first: it makes STAR look like a method serious people study rather than a campaign. Note that **this value comes from the argument and the write-up, not from shipping code.** The [existing page](../topics/homomorphic_tallying.md) already captures most of it; a paper would capture the rest; an implementation adds surprisingly little on top.

**To this library: high early, then a cliff.** M0 and M1 are an excellent teaching artifact — a reader watching encrypted ballots become a verified total learns something no prose delivers. M3 onward serves a research goal, not a teaching one, and should be honest about which it is.

**The comparison that matters.** If the question is *"what research-shaped moonshot would most help STAR?"*, the answer is probably not this one — it is **G7, risk-limiting audits for STAR**. The moment a real jurisdiction seriously considers STAR, someone asks how you audit it, and the honest current answer is thin: RLA methods are mature for plurality and under-developed for score methods. That question will be asked; "can it be tallied under encryption?" will not. G8 is the better moonshot for STAR's *profile*; G7 is the better one for STAR's *adoption*. They are both papers before they are code, and the cheap move is to write both up in the [research-topics companion repo](https://github.com/masiarek/star-voting-research-topics) before a line of Rust exists.

### The honest bounds — state these on every page that touches this

The repo's credibility rests on claim-checking other people's overreach, so it cannot overreach here.

- **This is a teaching demonstration, not election infrastructure.** Nothing built here should ever count a real vote without professional cryptographic audit. The field is littered with academic E2E systems broken after deployment.
- **Homomorphic tallying does not make internet voting safe.** It addresses tally integrity. It does nothing about malware on the voter's device, coercion in the voter's living room, or denial of service.
- **Verifiable ≠ receipt-free.** Letting a voter prove their ballot was counted, without also letting them prove *how* they voted to a coercer, is a separate and harder problem.
- **Publishing plaintext ballots — the thing encryption avoids — is itself a live hazard.** A full ranked ballot in a large field is close to a unique fingerprint, which is what makes coercion by "vote this exact unusual pattern and show me" possible. That is a real argument *for* this work, and worth stating plainly rather than assuming.
- **Novelty is narrower than it looks — and the search has now been done once.** No published scheme tallies STAR's score-plus-runoff shape, so the gap is real; but the *machinery* is well covered. The tally-hiding line of work — [Ordinos](https://eprint.iacr.org/2020/405) (IEEE EuroS&P 2020), [Cortier, Gaudry and Yang's toolbox](https://eprint.iacr.org/2021/491) (ESORICS 2022, with worked D'Hondt / Condorcet / STV / Majority Judgment schemes), and [Kryvos](https://eprint.iacr.org/2022/1132) (ACM CCS 2022) — computes exactly the encrypted comparison a STAR runoff needs, under multi-party computation rather than additive encryption. So the defensible claim is **"nobody has instantiated this for STAR,"** not "nobody knows how" — and a paper opening with the second would be refereed straight into the ground. One reason the gap *looks* larger than it is: [STAR-Vote](https://arxiv.org/abs/1211.1904) (Benaloh et al., 2012) is *Secure, Transparent, Auditable, Reliable*, an unrelated polling-place architecture that swamps any acronym search. The encryption page carries all four.

---

## G9 in detail — why not rebuild BetterVoting in Rust

Worth working through, because the reason it fails points directly at the version that works.

**The case for, such as it is:** tabulation correctness matters most where real elections are run, and that is BetterVoting, not here. A Rust core would be memory-safe, fast, and shareable between server and browser. And the crypto ecosystem argument from G8 applies to any future verifiability work.

**The case against, which wins:**

1. **It is not your project.** BetterVoting is an active Equal Vote codebase with maintainers. Your leverage there is already real and already working — PRs, [QA findings, and filed upstream bugs](../about_this_repo/upstream_bug_reports.md). A unilateral rewrite is a fork nobody asked for and nobody merges.
2. **The language is not the hard part.** BV's difficulty is election lifecycle, auth, email, migrations, i18n, and UI. Rust makes none of those easier, and the Rust web-frontend ecosystem is meaningfully weaker than React for the part of BV users actually touch.
3. **Rewrites of working products are the canonical failure.** Day one delivers zero new user value; the finish line moves for years.
4. **It splits a tiny community.** There is one open-source STAR election platform. Two half-maintained ones is strictly worse than one maintained one.
5. **Capacity.** This is a large repo maintained alongside a full-time job.

**The version that works — G10, in effect: build the kernel, and offer it to BV.** BV already carries tabulation logic in shared TypeScript. A Rust kernel compiled to WASM is a *drop-in for that layer specifically* — one verified implementation callable from BV's frontend and backend both, cross-checked against 615 cases, with an upgrade path to encrypted tallying that TypeScript will never have. That is contribution rather than competition, it is a plausible upstream PR rather than a fork, and it needs none of BV's auth, email, or UI.

Note this changes nothing about the scope in [the companion page](rust_kernel_scope.md). It is the same kernel, with a second consumer.

### Could the encrypted-tally work go back to BetterVoting too?

Plausibly, and it is the right ambition — but on a much longer fuse than the kernel, and the blocker is not code.

**What makes it attractive:** BetterVoting is an *online* platform, which is exactly where "trust us, we counted it right" is weakest. End-to-end verifiability is the strongest available answer, and the niche is under-served — [Helios](https://heliosvoting.org/) has held it for fifteen years and shows its age. A STAR platform that could say *"the encrypted ballots are published; verify the count yourself"* would have something no competitor has.

**What makes it hard has nothing to do with Rust:** threshold decryption needs **trustees**, and trustees are people. Who holds the key shares for a housing co-op board election? Who convenes them if one loses a laptop? Helios stayed niche largely because that ceremony is heavy for exactly the small-organization elections these platforms serve. Solve the trustee problem and the cryptography is the easy half; leave it unsolved and a perfect implementation is unusable.

**So the staged path, in ascending order of commitment:**

1. **Documentation, now.** The summability-implies-encryptable argument is a help-site page, not a code change — and the [`bv-docs`](../about_this_repo/repository_guide.md) workflow already exists. Free, immediate, and it seeds the idea with the people who would have to build it.
2. **The WASM kernel, next.** No crypto at all. Replaces shared tabulation logic with one implementation cross-checked against 615 cases. A normal PR.
3. **An experimental, clearly-labelled encrypted race type, eventually.** This is a design conversation with Equal Vote, opened *before* any code exists — not a surprise pull request. The same etiquette the QA work already follows: raise it with the maintainers first.

**And the standing caution applies doubly here.** A demo on this library's teaching site can be labelled a toy. The same code inside a platform people run real elections on cannot, and must not ship without an independent cryptographic audit. If that audit is not fundable, the honest answer is that step 3 stops at a prototype — which is still worth building, and should say so on its own front page.

---

## Why Python is the right language for a test library

This is the conclusion the goal menu above arrives at, so it belongs before the table rather than after it.

**A test-and-teaching library's dominant cost is authoring, not running.** The things done weekly here are: add a case, add a method, change a report's wording, write a one-off cross-check script, regenerate 782 mirrors. Python is close to optimal for every one of those, and Rust's compile-edit cycle taxes exactly the operation performed most. The things Rust is good at — memory safety, throughput, fearless concurrency — describe risks this project does not have. Python has never produced a wrong winner here; the bugs that were found were *semantic* (a quota filled by ballot count instead of ballot weight), and no type system catches those.

**The code is teaching material, and Python reads like pseudocode.** A reader can follow [`starvote_larry_hastings.py`](../../STARVote_LH_tabulation_engine/starvote_larry_hastings.py) and see the runoff happen. The same logic in Rust, wrapped in lifetimes and `Result` plumbing, is a worse artifact for the audience this library exists to serve — and legibility of the count is not incidental to the argument this repo makes, it *is* the argument.

**The cross-check ecosystem is Python, and that is the methodology.** `pref_voting`, `abcvoting`, `pyrankvote` — the independent referees that make a result here trustworthy rather than self-confirming are all Python libraries, callable in one import. A Rust kernel would move the engine away from its own referees and turn a function call into a subprocess and a serialization format. For a project whose entire credibility rests on engines checking each other, that is the wrong direction.

**Where Rust does keep a claim: real elections, not test libraries.** High-stakes tabulation under verifiable encryption is a genuinely different problem, with different requirements (auditability of the *implementation*, memory safety as a security property, a crypto ecosystem Python lacks) — and it is bigger than a moonshot, not smaller. It needs a funded independent audit before it counts a single real vote. It is not this repo's job, and pretending otherwise would be the kind of overreach this library exists to call out in other people's claims.

### One honest amendment

The strongest argument for Rust above was G1 — counting in the reader's browser — on the premise that WASM is the only route. **That premise is not quite true.** [Pyodide](https://pyodide.org/) runs CPython in WebAssembly today and could load the existing engine essentially unchanged. The cost is size: a multi-megabyte runtime against a few hundred kilobytes for a purpose-built Rust kernel. That is a real difference for a documentation site, but it is a *tradeoff*, not an impossibility — and the Python route reuses code that already exists and is already correct. **If in-browser counting is ever wanted, price Pyodide first.** Reaching for a second language to gain a capability the first language already has, more slowly, is the definition of a premature rewrite.

## Where Rust is actually the right tool

Since the honest starting position is "no idea where Rust could be helpful," here is the whole surface, scored.

| Candidate | Right tool? | Why |
|---|---|---|
| Tabulation kernel | **yes** | pure, deterministic, portable, compiles to WASM, and the one place correctness is load-bearing |
| In-browser counting on the teaching site | **yes** | WASM is the only way to do this without a server |
| Encrypted / verifiable tallying | **yes** | best-in-class crypto ecosystem, WASM-friendly |
| Exhaustive ballot-space search | **yes** | the only candidate where raw speed changes what is possible |
| Conformance harness | maybe | needs to run the kernel; otherwise Python is fine |
| Report rendering, page generation, mirrors | **no** | Python is better at it and the code already exists |
| BetterVoting as a whole | **no** | see G9 |
| Faster library rebuilds | **no** | the bottleneck is not tabulation |
| Anything touching YAML's forgiving dialect | **no** | strictness is a liability there |

The pattern: Rust earns its place where the code must be **pure, portable, and provably correct**, and loses everywhere the job is text wrangling. That is a narrow target — roughly 1,500 lines — which is a feature, not a disappointment.

## Goal statement — to be filled in

> The Rust kernel exists so that **\_\_\_\_\_\_**. We will know it worked when **\_\_\_\_\_\_**. We are explicitly *not* trying to **\_\_\_\_\_\_**. If it never does more than **\_\_\_\_\_\_**, it was still worth building.

The fourth blank is the honest one. If there is no acceptable minimum, the project has no scope.

## Success metrics — pick two, make them countable

| Metric | Serves | Target |
|---|---|---|
| Cases passing the conformance harness | G3 | e.g. 560 / 560 in Tier 1 |
| Methods implemented | G1, G3 | 7 |
| WASM binary size | G1 | < 500 KB gzipped |
| Teaching pages with a live counter | G1 | e.g. 3 |
| Ballot configurations searched per second | G2 | order of magnitude only |
| New case files generated from discovered counterexamples | G2 | ≥ 1 is a success |

A goal without a number attached tends to become "keep going."

---

# Part 2 — Requirements

Written as if G1 were chosen, with per-requirement notes where another goal would change the answer. Revise once the goal is locked.

## Non-goals (state these before the requirements — they do more work)

- **NG-1.** The kernel does not print human-readable reports. The [LH engine](LH_starvote/README.md) owns all rendering, permanently.
- **NG-2.** The kernel does not reproduce the 782 `_tabulated.txt` mirrors, byte-wise or otherwise.
- **NG-3.** The kernel does not replace the Python engine for any existing workflow. Nothing in the repo becomes dependent on it.
- **NG-4.** The kernel does not parse the library's forgiving YAML dialect — bare `title:` aliases, method names with trailing comments, the negative-fixture error messages. It reads a normalized structure.
- **NG-5.** The test cases are not ported. They stay language-neutral YAML, consumed by every engine equally.

## Functional requirements

| # | Requirement | Priority |
|---|---|---|
| FR-1 | Tabulate STAR (single-winner), Bloc STAR, Approval (single and multi), Ranked Robin, RCV-IRV, Plurality/SNTV, Score/Range | must |
| FR-2 | Return winners **and** an audit trail: per-round tallies, pairwise matrix where applicable, elimination order, exhausted-ballot counts | must |
| FR-3 | Preserve ballot-entry *meaning*, not just value — blank, race abstention, candidate abstention, spoiled, spoiled-and-reissued all tabulate as 0 but must remain distinguishable | must |
| FR-4 | Support weighted ballots (a leading `Count` on a row) | must |
| FR-5 | Accept a configurable maximum score; do not hard-code 0–5 | must |
| FR-6 | Report *which tiebreak rung* decided a result, not merely the winner | must |
| FR-7 | Accept a published lot order as input and replay it deterministically | must |
| FR-8 | Serialize the result to the repo's JSON result contract | must |
| FR-9 | Report a tie as a tie when no rung resolves it, rather than picking | must |
| FR-10 | STV and the STAR-PR family (allocated, SSS, RRV) | later |
| FR-11 | Grade methods (Majority Judgment, Range on foreign scales) | later |
| FR-12 | Emit a discovered counterexample as a valid YAML case file | G2 only |

## Non-functional requirements

| # | Requirement | Rationale |
|---|---|---|
| NFR-1 | The kernel is a pure library: no file I/O, no printing, no environment access, no threads | Required for WASM; also what makes it testable |
| NFR-2 | Deterministic — identical input yields identical output on every platform | A voting engine that is not reproducible is not evidence |
| NFR-3 | `no_std`-friendly if cheap; do not contort for it | WASM size |
| NFR-4 | Every fallible path returns `Result`; the library never panics on malformed input | A panic in WASM takes the page down |
| NFR-5 | Dependency budget: `serde` and little else | Audit surface, binary size |
| NFR-6 | MIT-compatible, with attribution to Larry Hastings' `starvote` ([LICENSE](../../STARVote_LH_tabulation_engine/LICENSE)) | Derived work |
| NFR-7 | Floating-point policy stated explicitly and applied uniformly | The PR family reweights; summation order is a real divergence source |

## The data contract is the actual deliverable

This is the requirement most likely to be under-weighted, so it gets its own section.

The JSON result schema — winners, rounds, pairwise matrix, eliminations, exhausted counts, tiebreak rung — is what makes two implementations comparable at all. Once it exists, the Python engine emits it, the Rust kernel emits it, and conformance is a diff. Without it, "do they agree?" is answered by eyeballing text reports.

Three consequences:

- **The schema is defined once, in the repo, in Python, before any Rust exists.** It is not a Rust artifact that Python later adopts.
- **It is versioned.** A field added later must not break a stored fixture.
- **It is not the `_tabulated` mirror.** The mirror is a rendering for humans; this is a result for machines. Confusing the two is how a kernel port turns into a formatter port.

## Acceptance criteria — definition of done for a first release

1. Every Tier 1 case in the library round-trips: YAML → kernel → JSON result, with winners matching `expected_winners:`.
2. Every disagreement with the Python engine is either fixed or written up as a documented divergence with a named cause.
3. Tiebreak behaviour is covered by explicit cases at every rung, including the unresolved-tie case.
4. The build produces a WASM artifact under the size budget *(G1)*, or a search harness that runs a bounded enumeration to completion *(G2)*.
5. A `README.md` states the goal, the non-goals, and the license attribution.

---

# Part 3 — How to prepare

Everything in Track A and Track B is worth doing whether or not the Rust project ever starts. That is the point of putting them first.

## Track A — repo work, in Python

| # | Task | Exit criterion | Status |
|---|---|---|---|
| A-1 | Define and document the JSON result schema | Written down, versioned, reviewed | **Done** (2026-08-10) — [`star_result.schema.json`](../../STARVote_LH_tabulation_engine/star_result.schema.json) + [the contract page](result_schema.md) |
| A-2 | Add a `--json` mode to the LH engine emitting it | Every Tier 1 case produces valid JSON | **Done** (2026-08-10) — 556 of 571 ballot-carrying cases emit valid JSON and match their answer key; 6 are methods this engine does not count, 9 have no key |
| A-3 | Backfill `expected_winners:` on the 48 ballot-carrying cases that lack it | 615 / 615 answered | Open |
| A-4 | Freeze the method-alias table | One documented list; the corpus normalized against it | **Mostly done** — `classify_method()` is now the single source, read by both the CLI dispatch and the contract; the corpus is not yet normalized against it |
| A-5 | Write the tiebreak ladders down, per method, per engine | Prose a stranger could implement from | Open — the contract *reports* the rung that fired; the ladders themselves are still undocumented |
| A-6 | Store a JSON fixture per case, generated and checked like the other mirrors | A drift test fails when one goes stale | Open — [`tests/test_result_json.py`](../../STARVote_LH_tabulation_engine/tests/test_result_json.py) currently rebuilds and re-validates every case rather than diffing stored fixtures, which catches drift but not silent contract changes |

A-1 and A-2 are the load-bearing ones. A-3 through A-5 are small.

**What building A-1/A-2 turned up**, since it bears on the rest of this page: the contract is not just packaging. Extending the answer key past the winner immediately found a real defect — multi-winner Choose-One counts *marks* while single-winner Choose-One *spoils an overvote*, and deriving one from the other elected the wrong slate on five block-voting cases. That bug was invisible to 567 winner-only answer keys because it was introduced in the new code, but it is exactly the shape of thing a second implementation would hit and the old suite could not have caught in *either* engine. The tie-break field is the same argument: `tiebreaks: []` is a positive claim that no rung fired, and a right-winner-wrong-path result fails it.

## Track B — write the rules in prose, before code

For each of the seven Tier 1 methods, one page answering: what the ballot is, how the tally works, what happens on a tie at each rung, what happens to blanks and abstentions, and what the engine reports. Much of this already exists scattered across the concept pages; the work is collecting it into something implementable.

This is the step that turns G3 from a slogan into a real cross-check. **A specification written from the code is not a specification** — if the prose is derived by reading [`starvote_larry_hastings.py`](../../STARVote_LH_tabulation_engine/starvote_larry_hastings.py), then a Rust kernel written from the prose is a transliteration with extra steps, and it will agree with Python about everything including the bugs.

## Track C — personal preparation

**Skip object-oriented Python entirely.** Rust has no inheritance; the transferable ideas are structural typing (→ traits), plain data records (→ structs), and immutability by default. The LH engine is 1 class and 57 functions across 4,257 lines — the codebase being ported has no object model to carry over.

**Read, in this order, and stop:** *The Rust Book* chapters 3–4 (ownership and borrowing), **6** (enums and `match` — this is where the voting domain lives: a ballot entry is an enum, not an integer), 8 (collections), 9 (`Result`), 10 (traits and generics), 13 (iterators and closures — most tabulation is an iterator chain), 18 (patterns). Then the `serde` guide. Everything else can wait for a real need.

**Build in this order.** The first thing to write is not a method — it is the harness:

1. **The conformance harness.** Read a case file, read its answer key, print the pair. No tabulation at all. Roughly 50 lines with `serde`, and it makes every subsequent step a red-to-green loop.
2. **Then one method at a time**, cheapest-with-the-most-coverage first:

| Order | Method | Cases | Cumulative | Coverage |
|---|---|---|---|---|
| 1 | Plurality / SNTV | 31 | 31 | 5% |
| 2 | Approval (+ multi) | 37 | 68 | 11% |
| 3 | Score / Range | 4 | 72 | 12% |
| 4 | **STAR** (incl. 9 defaulting cases) | 281 | 353 | **57%** |
| 5 | Bloc STAR | 33 | 386 | 63% |
| 6 | Ranked Robin | 101 | 487 | 79% |
| 7 | RCV-IRV | 73 | 560 | **91%** |

Plurality first not because it matters but because it is the smallest method that still has real tiebreak behaviour — it exercises the hardest part of the design on the easiest arithmetic. STAR at step 4 is where the coverage number stops being embarrassing. RCV-IRV last: it is the hardest of the seven, because elimination order under a tie is a behaviour of `pyrankvote` specifically rather than a property of IRV, and it must be re-derived rather than read back.

3. **Then** `proptest` *(G2)* or `wasm-bindgen` *(G1)* — never before Tier 1 is green.

---

# Part 4 — How to approach a project like this

## Six principles, before any schedule

A long solo side project alongside a full-time job has one dominant risk, and it is not technical: it stops. So the design constraint is **maximize the value already delivered at the moment it stops** — which changes the ordering in ways that feel wrong at first.

1. **Order by "what survives if I quit here", not by dependency and not by interest.** Every rung must leave the repo better even if it is the last one climbed.
2. **Front-load whatever is valuable regardless of the decision.** All of Track A is useful to a Python-only future. Doing it first means the project cannot fail to produce something.
3. **Build the harness before the engine.** Write the thing that can tell you you are wrong before the thing that can be wrong. In this project that inverts the intuitive order: the first Rust written tabulates nothing.
4. **Order the methods by coverage, not by interest.** Plurality → Approval → STAR reaches 57% of the case library quickly and keeps the feedback loop green. Starting with RCV-IRV because it is the interesting one reaches 12% slowly, on the hardest method, with the most obscure tie rules.
5. **Ship something visible early, even if it is small.** One teaching page with a live counter on it is worth more — to motivation and to the library — than a perfect kernel nobody can see.
6. **Cryptography goes last, and not merely because it is hard.** You cannot debug a crypto layer sitting on top of a tabulator you do not yet trust. Every encrypted-tally rung assumes a kernel whose answers are already boring.

And one rule that is not a principle but a practice: **write down the kill criterion for each rung before starting it.** A project with explicit permission to stop is more likely to finish the parts that matter.

## The ladder

Effort figures are honest orders of magnitude for evenings and weekends, not estimates.

| # | Rung | Effort | Exit criterion | Value if you stop here | Kill criterion |
|---|---|---|---|---|---|
| **0** | Lock one primary goal; fill in the goal statement | a day | D-1 answered in writing | clarity; this page stops being hypothetical | — |
| **1** | **Track A** — JSON result schema, `--json` mode, backfill the 48, alias table, tiebreak ladders written down | weeks | every case has a machine-readable answer | **large, and entirely in Python.** Better cross-checks, a cleaner corpus, a publishable conformance suite | none — do this regardless |
| **2** | **Track B** — prose rules for the first three methods | a week | a stranger could implement Plurality, Approval, and Score from the pages alone | the specs are teaching content in their own right | none — do this regardless |
| **3** | The Rust conformance harness — reads cases, reads answer keys, tabulates **nothing** | a weekend | it runs and reports 615 failures honestly | proof the toolchain and the data contract work | if `serde` plus the case format is a fight, the schema is wrong — go back to rung 1 |
| **4** | Methods 1–3: Plurality, Approval, Score | a weekend or two | 72 cases green (12%) | a real cross-check on three methods | if the tiebreak ladder cannot be reproduced, stop and fix rung 1's documentation |
| **5** | **STAR** | weeks | 353 green (57%) | the headline method independently verified | — |
| **6** | Bloc STAR, Ranked Robin | weeks | 487 green (79%) | — | — |
| **7** | RCV-IRV | weeks | 560 green (91%) — **Tier 1 complete** | a genuine sixth engine; G3 and G6 achieved | if reproducing `pyrankvote`'s tie behaviour turns into archaeology, ship at 79% and document the gap |
| **8** | **WASM demo on one teaching page** | a week | a reader edits a ballot and the result moves | **G1 achieved.** The first rung readers can see | if the site integration fights MkDocs, ship it as a standalone page |
| **9** | More live pages; offer the kernel to BetterVoting as a shared-tabulation PR | weeks | a PR opened | upstream contribution | maintainers uninterested → stop, no loss |
| **10** | *Branch A:* `proptest` and bounded exhaustive search | weeks | one bounded search runs to completion and emits any counterexample as a YAML case | **G2.** Potentially publishable results | unbounded scope → time-box it |
| **11** | *Branch B:* **M1** — toy encrypted Approval tally, exponential ElGamal, single trustee, WASM, labelled a toy | weeks | a reader watches encrypted ballots become a verified total | the best teaching artifact on this list | — |
| **12** | **M2** — range proofs, so ballots are well-formedness-verifiable | months | scores provably in 0–5 without revealing them | a credible demonstration rather than a toy | needs real crypto review; without a reviewer, stop at 11 |
| **13** | **M3** — full STAR under encryption: scores plus pairwise indicators plus a consistency proof | months | the runoff computes without opening a ballot | **the novel contribution.** Write the paper, then the code | if the write-up is not going to happen, the code is not worth it |
| **14** | M4–M5 — threshold trustees, bulletin board, cast-as-intended | open-ended | — | a system nobody should trust unaudited | **default: do not climb.** Requires funding and an independent audit |

**Yes — HE is at the very end, and correctly so.** Not only because it is hard: rungs 11–13 all assume a kernel that is already trustworthy and a WASM pipeline that already works, and both of those are rungs 7 and 8. Attempting crypto before them means debugging three unfamiliar things at once and being unable to tell which one is lying.

**The realistic ambition.** Rung 8 is a very good outcome and is reachable. Rungs 1–2 are the ones that pay off even if nothing else happens, which is why they come first and why they are Python. Rung 13 is a research project with a paper attached, and should be entered deliberately or not at all — the honest expectation is that it is written up long before it is implemented, and possibly instead.

---

# Part 5 — Stepping stones for a future professional implementation

The decision above says this library does not build election infrastructure. That is not the same as being unable to help build it. The question worth answering is: *what can one person produce, now, that makes a future funded team's job materially cheaper and their result more trustworthy?*

## The reframe: a professional team's bottleneck is not the code

Tabulating STAR is not hard. A competent team implements the count in a week. What takes years — and what kills projects — is everything around it:

- there is **no implementable specification** of STAR, only advocacy prose and reference code;
- there is **no published test deck**, so conformance has to be invented before it can be demonstrated;
- **edge cases are undocumented folklore** scattered across implementations that quietly disagree;
- **certification** wants evidence in formats nobody has produced for a score method;
- **auditability** for score methods is a thin literature.

Every one of those is a documentation-and-data problem, not a software-engineering problem. Every one of them is squarely within reach of one person with a large case library and six engines' worth of divergence knowledge. And — the key property — **every one of them is language-neutral**, so it serves a Rust team, a C++ team, or a vendor equally.

That is the whole strategy: **do not write the implementation; write the things that make anyone's implementation cheaper, and its correctness checkable by someone who did not write it.**

## For real elections, requirements are inherited, not gathered

Gathering requirements for a high-stakes election system genuinely is a monster — but only if you imagine starting from a blank page. You would not be. For actual elections the requirements already exist, in force, written by other people:

- **VVSG 2.0** (the federal Voluntary Voting System Guidelines) and the EAC-accredited test labs that administer it;
- **state certification statutes**, which differ per state and are the real gate;
- **HAVA and ADA accessibility** obligations;
- **ballot-secrecy, chain-of-custody, canvass, recount, and audit law**.

None of that is authored by a volunteer, and no individual should try. But here is the useful part: **those frameworks are method-agnostic, and every one of them has slots that must be filled in per voting method.** For plurality those slots were filled decades ago. For RCV-IRV they have been filled recently and painfully, jurisdiction by jurisdiction. **For STAR they are empty.**

That converts an unbounded task into an enumerable one. You do not invent the taxonomy — you take an existing framework's table of contents and answer, section by section, *"what would this say for a score ballot?"* For example:

- What does a **logic-and-accuracy test deck** for a STAR contest contain?
- What is an **overvote** on a 0–5 ballot — and is there such a thing?
- What does a **recount** of a STAR contest do differently, given the runoff depends on the scoring round?
- What does the **canvass report** show, and what must be reportable **per precinct**? (This is where [summability](../topics/summability/README.md) stops being a theoretical virtue and becomes a procurement requirement.)
- How is a **tie** resolved as a matter of law, and does the statutory procedure match what the engines do?
- What does a **risk-limiting audit** of a two-stage count look like? (S-5.)

That list is finite, it is knowable, and answering any single item is a page — not a program. It is also the exact material a future professional team would otherwise spend a year assembling, and the one contribution here that no amount of funding shortens, because it requires knowing the method deeply rather than knowing procurement.

**The honest boundary:** these pages would be *drafts for practitioners to argue with*, not authoritative guidance, and should say so on their face. That is not a weakness — a well-posed draft is how this kind of document gets written at all.

## Scope it as a tabulator and the identity problem disappears

The instinct that authentication and credentialing at scale — millions of records, privacy, security — is a monster is correct. The resolution is the one already reached: **think of it as a county-level tabulation engine, where the county manages everything else.** That is not a convenient dodge. It is how US election systems are actually architected, and the separation is deliberate.

A jurisdiction already owns, and does not want a vendor touching:

- voter registration and eligibility (the state voter database);
- authenticating the voter at the polling place (pollbooks — a solved, separate product);
- issuing ballots, and the procedures that keep them secret;
- chain of custody for paper.

**The tabulator sits downstream of all of it and is blind to identity by design.** Its input is a set of anonymous cast vote records from scanners; it never sees a voter, never holds a credential, never stores a name. That blindness is a *security property*, not a gap — a tabulator that could link a ballot to a voter would be disqualifying.

So the requirements shrink to a bounded, unglamorous list: integrity of the CVR set, deterministic and reproducible output, audit logging, logic-and-accuracy testability, and correct arithmetic. No identity system, no millions of records, no privacy architecture. That is a scope one person can meaningfully write specifications *for*, which is the whole of Part 5.

**And it explains why the encrypted-tally moonshot is a genuinely different animal.** End-to-end verifiability works by putting the voter *back* into the system — they need a tracker to confirm their own ballot was counted — which reintroduces exactly the identity, credentialing, and coercion problems that county tabulation architecture spent decades designing out. That is why G8 belongs to the online and organizational world ([BetterVoting](BV/README.md)'s ground), not to county election night, and why its hardest problems are social rather than mathematical.

Two different systems, two different scopes, and only one of them is a monster. Keep them apart.

## The stones, in order of leverage

### S-1. The conformance suite — mostly already built, badly framed

**What a team needs:** a published set of elections with known-correct results, broad enough to exercise every rule and every tie rung, that an implementation can be run against on day one.

**What exists:** 615 case files, 567 with machine-checkable answer keys, already cross-verified across [the LH engine](LH_starvote/README.md), [BetterVoting](BV/README.md), [`pref_voting`](cross_checking_with_pref_voting.md), [`pyrankvote`](RCV_IRV/README.md), [RCTab](rctab.md), and [rcv-lab.org](rcv_lab_irv_crosscheck.md). This is, as far as this repo knows, the largest cross-verified STAR conformance corpus anywhere — and it was, until 2026-08-10, presented as teaching material rather than as a test suite. **The result contract and the implementer-facing front page now exist**: [the result contract](result_schema.md), `--json`, and a published schema. What remains is A-3 through A-6 and the executable specification (S-2).

**The work:** finish Track A (the 48 missing answer keys, normalizing the corpus against the alias table, the tie-break ladders in prose). Weeks, in Python, and it is the same work already recommended.

**Why it is stone number one:** it is 90% done, it is unglamorous enough that nobody else will do it, and whoever holds the accepted test deck when a jurisdiction moves is in the room.

### S-2. The executable specification

**What a team needs:** a document precise enough to implement from, without reading anyone's source code.

**What exists:** the rules are distributed across concept pages, engine source, and commit messages. [Track B](#track-b-write-the-rules-in-prose-before-code) above is the seed of this.

**The work:** one page per method answering, exhaustively — what the ballot is; how the tally proceeds; **what happens at every tie rung, including when no rung resolves**; how blanks, abstentions, spoiled ballots, overvotes, equal scores, and truncated rankings are treated; and what the count must report. Each rule cites the case file that pins it. Ambiguities get written down *as ambiguities* rather than resolved silently.

**Why it matters more than it sounds:** a spec whose every clause has a runnable case attached is a rare object. It also does something no advocacy document can — it makes STAR *procurable*, because a jurisdiction cannot buy what it cannot describe in a contract.

### S-3. Interoperability with the formats real elections use

**What a team needs:** to read and write what actual jurisdictions exchange — NIST's Election Results Common Data Format and Cast Vote Records CDF ([SP 1500-100](https://www.nist.gov/publications/election-results-common-data-format-specification-version-10) and the CVR specification), which is what certified systems and audit tooling speak.

**What exists:** the repo already converts cases to [RCTab](rctab.md)'s CSV and [rcv-lab.org](rcv_lab_irv_crosscheck.md)'s format, so the pattern is established. Nothing speaks NIST CDF.

**The work:** an exporter from the case library to CVR CDF, and an importer back. Bounded, testable against the existing corpus, and it does something disproportionate — it makes 615 STAR elections readable by software that already exists, instantly.

**The open question worth answering publicly:** *does the CVR CDF even express a 0–5 score ballot cleanly?* If it does, say so with a worked example. If it does not, that gap is itself a finding, and a comment worth filing.

### S-4. The divergence catalog

**What a team needs:** the list of places correct implementations legitimately disagree, so they can choose deliberately instead of discovering it in production.

**What exists:** a great deal, scattered — the [upstream bug reports](../about_this_repo/upstream_bug_reports.md), the divergence ledger, the LH-versus-BV tiebreak comparison, the Minimax "worst loss" readings, the Majority Judgment tie-break disagreement, the allocated-score quota bug.

**The work:** one page per divergence: the two behaviours, the case that separates them, which engines do which, and whether either is *wrong* or both are defensible. This is the institutional memory of the whole project, and it currently lives in commit messages.

### S-5. Audit groundwork

**What a team needs:** an answer to *"how do you audit this?"* — asked by every election official, immediately, and currently answered thinly for score methods.

**The work:** start with the write-up, not the code — a risk-limiting-audit prospectus for STAR in the [research-topics companion repo](https://github.com/masiarek/star-voting-research-topics). What does an RLA of a scoring round look like? Of a runoff whose finalists depend on the scoring round? Is a two-stage audit sound? Then, if it goes anywhere, a reference sampling implementation.

**Why it ranks here rather than higher:** it is genuinely hard and genuinely open, so it is the one stone that might not be placeable. It is also the one a jurisdiction will ask for first.

### S-6. The administrative artifacts

**What a team needs, and nobody writes:** ballot layout that survives contact with real voters, instructions in plain language, the operational definition of an overvote or a damaged ballot on a score ballot, poll-worker procedure, and what the canvass report should show.

**Why include it:** none of this is code, all of it is required, and it is the part a software team is worst at. Some already exists in this library's [ballot art and voting-styles work](../../01_STAR/01_Learn/README.md).

## The rule that makes these stones and not pebbles

**Everything above is written to be consumed by an implementation that does not exist yet, in a language nobody has chosen.** JSON schemas, prose specs, NIST CDF, case files, papers. No stone should require the reader to run Python, and none should assume the eventual system is Rust either — that guess could easily be wrong, and it does not matter.

The corollary is the thing to resist: **do not build half of the eventual system as a demonstration.** A half-finished Rust kernel is not a stepping stone, it is a liability a professional team would delete on day one — while a conformance suite they can run against their own code on day one is something they will thank you for and cite.

## What this looks like in practice

Nothing new gets started. The next three things are already on the list:

1. **Track A**, reframed as S-1 — the JSON contract, the 48 answer keys, the alias table, the tiebreak ladders. In Python, useful immediately, and the foundation of every other stone.
2. **S-2**, one method at a time, starting with STAR, each clause citing its case.
3. **S-3**, one exporter, to find out whether the format even fits.

S-4 is continuous. S-5 begins as a prospectus. S-6 happens when the teaching content pulls it in.

**And the honest expectation:** the professional team may never materialize, or may arrive in fifteen years and ignore all of it. Every stone above is chosen so that it is worth having anyway — a better test corpus, a written specification, a wider set of readers, a real paper. That is the same principle as the ladder in Part 4: order the work so that stopping is never a loss.

## Prototyping in Python as preparation — what that actually means

The natural next thought is *"keep developing, in Python, but with Rust in mind."* That is right, and it is worth being precise about it, because "with Rust in mind" can mean two very different things and only one of them is useful.

**It does not mean writing Rust-flavoured Python.** No hand-rolled `Result` monad, no avoiding exceptions on principle, no rejecting comprehensions for explicit loops. Python that imitates Rust's syntax is worse Python and does not make the eventual port easier. Syntax does not port; **design does.**

**It means rehearsing the architecture, in Python, where mistakes are cheap.** Four things are worth prototyping, and each is a real improvement to the Python on its own terms:

1. **A pure kernel module, beside the existing engine rather than replacing it.** One `tabulate(election) -> Outcome` function with no printing, no file access, no module-level state. If that separation cannot be made cleanly in Python — where nothing is stopping it — it would not be made in Rust either, and discovering that costs a weekend here instead of a rewrite there. This is the single highest-value prototype, because **the kernel/reporting boundary is the entire portable idea.**
2. **A ballot entry that is an enum, not an integer.** Blank, race abstention, candidate abstention, spoiled, spoiled-and-reissued all tabulate as zero but mean different things, and this is precisely the place Python lets the distinction be quietly dropped and Rust would not. Making it an `Enum` in Python is both a rehearsal of Rust's `match` and, independently, a correctness improvement the library already wants (FR-3).
3. **Frozen, fully annotated dataclasses for `Election` and `Outcome`, checked under strict `mypy`.** Immutability by default, no `None`-as-sentinel, `Optional` spelled out. This is the design discipline Rust enforces, adopted voluntarily, and it makes the Python better regardless.
4. **The JSON result contract.** Language-neutral by construction, so it is the one artifact that ports at zero cost — which is why it is rung 1 of the ladder and stone S-1 both.

**The test for whether a "Rust prep" change is worth making:** *would this still be an improvement if Rust never happens?* Enum ballot entries — yes. A pure kernel boundary — yes. Frozen dataclasses and strict typing — yes. The JSON contract — yes. A custom `Result` type, or contorting the report renderer — no, and those are the ones to refuse. Anything justified *only* by a future port fails the ladder principle from Part 4, because the future port is the step most likely never to be taken.

Done this way, the prototype is not a detour on the road to Rust. It is stone S-1 and S-2 being placed, in the language best suited to placing them, with the side effect that a future implementer — in Rust or anything else — inherits a design that has already been tested against 615 elections.

---

## Open decisions

| # | Decision | Recommended default |
|---|---|---|
| D-1 | Primary goal | **DECIDED 2026-08-10 — none; no Rust kernel.** Python is the right language for a test-and-teaching library. Track A proceeds in Python. Had a goal been picked, it would have been G1 — and even that is weakened by the Pyodide amendment above |
| D-1c | If in-browser counting is wanted later | Price [Pyodide](https://pyodide.org/) against a Rust kernel before assuming a second language is needed |
| D-1a | Is G8 (encrypted tallying) announced as a roadmap item? | No. M0 exists as a concept page; M1 ships as a labelled toy or not at all |
| D-1b | Is anything offered to BetterVoting before it works here? | No — documentation first, kernel second, crypto only as a conversation |
| D-2 | Spec-derived or code-derived implementation | Spec-derived, or drop G3 and say so |
| D-3 | Does the kernel own tiebreaks, or take a resolved order as input? | Take it as input — keeps the kernel a pure function of its arguments |
| D-4 | Rationals or floats for the PR family | Defer with Tier 2; floats plus a stated epsilon if forced |
| D-5 | One repo or a separate one | Separate repo, referenced here — keeps this repo's CI and hygiene gates unentangled |
| D-6 | Does the Python engine ever consume the Rust kernel? | No. NG-3 |
| D-7 | Is any of this promised publicly before it exists? | No |

---

*Up: [Tabulation engines](README.md) · scope companion: [A Rust tabulation kernel — scope](rust_kernel_scope.md) · [07_Concepts](../README.md).*
