# What would it take to certify STAR Voting software?

**Level: reference · deep dive**

**One line:** federal certification of a whole voting system — scanners, operating systems, hardware, the lot — genuinely is a monster, but **the method-specific part of it is a small stack of documents**, the EAC writes none of them, and a nonprofit has already walked the entire path for a new voting method.

This page sizes the problem honestly and then names the pieces one person or a small organization could actually produce. It is a research summary, not legal or compliance advice, and it describes the US federal and state landscape only.

---

## The two facts that shrink the monster

### 1. There is no federal standard defining any voting method — the vendor supplies it

This is the surprising one. The EAC's own explanation of how RCV systems get certified says plainly that certified systems **may** support RCV but are not required to, and that because methods vary, there are *no* EAC guidelines setting out requirements a system supporting RCV must meet. What the manufacturer must do instead is **document how the method works in their implementation statement**, and for the older guidelines, in the Technical Data Package.

VVSG 2.0 adds requirements, but read what they actually are: record the voter's selections faithfully into the cast vote record, aggregate the first-choice totals, **process the CVRs each round according to the method stated in the implementation statement**, and be able to report totals for the contest and for each round.

That is a *procedural* frame, not a *substantive* one. The standard does not know what IRV is. It requires that you say what your method is, and then behave that way, verifiably.

**The consequence for STAR is large: STAR does not need a new federal standard.** It needs an implementation statement — a document — plus evidence that the software does what the document says. Every one of the VVSG 2.0 bullets has a STAR analogue, and each is *simpler* than its ranked counterpart: the ballot records scores rather than an ordering, aggregation is a sum, "each round" means two well-defined stages (the scoring round and the automatic runoff), and both are reportable.

### 2. The EAC has already stated STAR's structural advantage — while describing IRV

In the same document, explaining why RCV complicates system architecture, the EAC notes that all ballots in a contest must be available to tabulate, because each round depends on the totals from every ballot cast — and therefore, in their words, **"a single precinct tabulator cannot tabulate RCV vote results by itself."**

That is [summability](../topics/summability/README.md), stated by the federal certification body, as a *system architecture constraint with certification consequences* — not as a theoretical criterion. It is why a third-party tabulator has to enter the picture for RCV at all.

**STAR sits on the other side of that sentence.** A precinct device can produce everything a STAR count needs — per-candidate score totals and the pairwise preference matrix — and those precinct results combine to the correct statewide answer. See [STAR's summability](../../01_STAR/01_Learn/properties_and_limits/STAR_summability.md) against [IRV's lack of it](../../06_Other/RCV_IRV/concepts/RCV_IRV_lack_of_summability.md).

This is the most citable argument on this page, and it is worth using carefully rather than triumphantly: the EAC is describing a fact about elimination methods, not endorsing an alternative.

---

## The existence proof: RCTab

The strongest reason not to treat this as impossible is that it has been done, recently, for a new voting method, by an organization that is not a voting-system vendor.

[RCTab](rctab.md) — the Universal RCV Tabulator — is open-source software from the Ranked Choice Voting Resource Center, a nonprofit. It was tested by **Pro V&V**, a voting system test laboratory accredited by the EAC, and it has been approved at state level: Virginia's Department of Elections approved it in May 2023 for use in RCV contests in the Commonwealth, describing it as the first open-source software to meet VVSG standards.

Two details matter for anyone thinking about STAR:

- **Scope.** RCTab is tabulation software. It is not a scanner, a ballot-marking device, or an operating system. The certified voting systems from the established vendors do the scanning and produce the CVRs; the tabulator consumes them. The hardware-and-OS burden stays with the vendor whose system it is paired with. The EAC's framing is that where a system relies on a third-party application to determine the winner, **that application is evaluated as part of the voting system configuration** — so it is not a loophole around certification, but it *is* a much smaller surface than a whole system.
- **Producer.** A 501(c)(3), not ES&S. The analogous actor for STAR is the Equal Vote Coalition and the surrounding community, not a large vendor.

---

## What a state actually asked for

Virginia's published approval memo is the most useful document in this whole area, because it enumerates exactly what was reviewed. The evaluation ran in three phases — the Pro V&V test report, a review of the security documentation package, and the state's own test elections — and the documentation package consisted of:

| Document | What it covers |
|---|---|
| Secure USB processes | Encrypted distribution media, PIN-authenticated, to federal standards |
| System hardening procedures | An offline machine, sealed ports, no network, UPS, physical security |
| **Software design and specifications** | The code, the design, coding standards, quality tooling |
| **System test and verification specification** | Acceptance criteria, processing accuracy, data quality, **ballot interpretation logic**, exception handling, audit and security |
| **Logic & accuracy test procedures** | The step-by-step pre-election check, including hashing results for integrity |
| **Quality assurance plan** | Defect and regression testing across vendors, large contests, real-life scenarios, with public defect tracking |

**Three of those six are already substantially built in this library, under different names.** The system test and verification specification is a [conformance suite](../YAML_test_case_index/README.md) — 615 elections, 567 with machine-checkable answers, cross-verified across six independent engines. The quality assurance plan describes regression testing across multiple vendors, large contests, and real-world scenarios with public defect tracking — which is a fair description of the existing pytest suite, the imported real elections, and the upstream bug reports. The software design and specifications document is the per-method specification already proposed as stone S-2 in [the requirements page](rust_kernel_requirements.md).

The other three — secure media, system hardening, and the VSTL test itself — are operational and financial, not intellectual. They need an organization and a budget, not insight.

---

## The stepping stones, smallest first

Each of these is a document. None requires building a voting system, and none requires anyone's permission to start.

### C-1. A model VVSG 2.0 implementation statement for STAR

**The highest-leverage document nobody has written.** Since the EAC defines no method requirements and instead tests a system against its own stated implementation, this statement *is* the method-specific certification content. Writing a model one — what the ballot records, how scores aggregate, what the two stages are, what gets reported at each, how ties resolve, what a blank or an abstention means, what an overvote is on a 0–5 ballot (and whether the concept even applies) — hands any future vendor or nonprofit the hardest part of their paperwork, pre-drafted.

It is a handful of pages. It is squarely within the competence of someone who has run 615 STAR elections through six engines. And it is the artifact that makes STAR *procurable*, because a jurisdiction cannot write a contract for a method nobody has specified.

### C-2. A system test and verification specification — i.e. publish the test deck as one

Reframe the existing corpus for a reviewer rather than a learner: what each case proves, which rule it pins, what a pass means, how to run your own engine against it. The **ballot interpretation logic** line in Virginia's review is precisely the marker/abstention/blank handling this library already treats as a first-class subject.

### C-3. A logic-and-accuracy test deck for a STAR contest

Every jurisdiction runs L&A before every election. For plurality this is routine and for RCV it now exists; for STAR nobody has written what the deck contains or what the expected output is. A small, deliberately-designed set of ballots with a hand-verifiable expected result — exactly this library's house style.

### C-4. The canvass and reporting question

What must a STAR count report, per precinct and in total, for the result to be publicly checkable? This is where summability stops being a virtue and becomes a reporting requirement — and it is also the argument that a precinct-level STAR count is *more* transparent than a centralized RCV one.

### C-5. Recount, tie, and audit procedure

What does a recount of a STAR contest do, given the runoff pair depends on the scoring round? How does statutory tie resolution interact with the engines' tiebreak ladders? These are drafts for practitioners to argue with, and should say so.

---

---

# "A STARTab" — the goal that finally has a shape

The natural conclusion from all of the above: **build for STAR what RCTab is for RCV.** An open-source, offline, auditable tabulator that consumes cast vote records produced by an already-certified scanning system and produces a canvass-ready result.

This is the best-scoped goal in this whole line of thinking, for reasons that have nothing to do with enthusiasm:

- **The category already exists.** RCTab defines the shape, the deliverable set, the review process, and the approval precedent. There is no need to invent what the thing is.
- **It is identity-blind by construction.** Registration, pollbooks, ballot issuance, and chain of custody belong to the jurisdiction. The tabulator receives anonymous CVRs and never sees a voter, holds a credential, or stores a name. That is a security property, and it removes the entire authentication problem from scope.
- **It is small.** RCTab is a desktop application. The tabulation itself is the easy part; this library has had it working for a long time.
- **Most of the documentation burden is already half-built here.**

## Where Rust would finally earn its place — and it is not the tabulation

Worth stating clearly, because it inverts the usual argument. RCTab runs on **Java**, and nothing in Virginia's review required otherwise — the review looked at design documents, coding standards, quality tooling, and test evidence, all language-agnostic.

But look at what the security package actually describes: an **offline machine with sealed ports, software delivered on encrypted USB, hash values recorded to prove the running software matches the original**, and physical security around the box. That deployment model wants a **single, self-contained, hashable binary**. It does not want a Python environment with a dependency tree that a security reviewer has to enumerate and a jurisdiction has to reproduce byte-for-byte on an air-gapped laptop.

So: **the argument for Rust here is distribution and auditability, not performance and not safety-as-slogan.** One static binary, one hash, no interpreter, no site-packages. That is the first concrete, non-hypothetical reason to reach for it that has come up — and it is worth noting it argues equally well for Go, or for anything that produces a single binary. The language is still open; the *packaging requirement* is the real finding.

The counterweight, stated honestly: fewer reviewers read Rust than read Java or Python, and a nonprofit has to maintain the thing for a decade. Reviewability by strangers is itself a certification asset.

## When could we say we are ready?

Readiness is not "the tabulation is correct" — that has been true here for a long time. Five gates, each independently checkable:

| Gate | Ready when | Status today |
|---|---|---|
| **R1 — Specification** | Someone can implement STAR correctly from our documents **without reading our code**, including every tie rung and every ballot-marking edge case | not started; this is stone C-1/S-2 |
| **R2 — Conformance** | Every clause of that specification has at least one case that fails if the clause is violated | **unknown, and this is the important gap** — see below |
| **R3 — Real data** | The tool reads an actual CVR export from a certified vendor system, unmodified | not started; blocked on Q1 |
| **R4 — Determinism** | Same input produces byte-identical output across platforms and runs, with a published hash and an audit log | partially — the engine is deterministic, but nothing is hashed or logged for audit |
| **R5 — Institutional** | A sponsoring organization, a budget for a VSTL, a vendor pairing, and a jurisdiction that wants it | not in an individual's control |

**R1 through R4 are achievable by one person. R5 is not, and pretending otherwise is how this kind of effort dies.** The useful posture is to make R1–R4 true and leave R5 to the moment a jurisdiction asks.

## The uncomfortable truth about the existing test cases

The 615 cases are a real asset, and they are **not yet evidence of conformance readiness**, because they answer a different question than R2 asks.

What they prove: *this engine agrees with five other independent engines on 567 elections.* That is agreement testing, and it is genuinely valuable — it is why the arithmetic can be trusted.

What they do not prove: *every rule of STAR has a case that would catch its violation.* Those are different claims. A corpus can contain 615 elections and still have no case where two candidates tie for second place in the scoring round, or where a ballot scores every candidate identically, or where the runoff pair is itself tied. Coverage of *rule space* is not the same as coverage of *election space*, and case count measures the wrong one.

**So the first real question the library must be asked is: which specification clauses have no case?** And that question cannot be asked until the specification exists — which is exactly why C-1 comes before everything, and why "write the spec" is not bureaucratic throat-clearing but the thing that makes the existing corpus measurable.

The practical form of this: write the spec, number every clause, tag every case with the clauses it exercises, and generate the gap list. The gaps become new cases. That is a bounded, mechanical, and genuinely valuable project — and it is the one that converts a teaching corpus into a certification artifact.

## The questions to ask first, and who can answer them

Ordered by how much they would change the plan if the answer is bad.

**Q1. Can a certified scanner and its CVR export represent a 0–5 score ballot at all?** *(Answer needed from a vendor or an election official — not from us.)* This is the pivotal unknown and everything downstream depends on it. RCTab could exist as an add-on precisely because certified systems already record rankings and export them in a CVR. Do they record a score grid? The physical marking is structurally similar — a candidate × value bubble grid, much like a candidate × rank grid — so the scanning capability plausibly exists; the real question is whether the **exported CVR represents it faithfully and whether the implementation statement can say so**. If the answer is no without firmware or software changes, the STARTab path stalls until a vendor moves, and the correct response is to know that now rather than after writing six documents.

**Q2. What is an overvote — or an undervote — on a score ballot?** Does the concept exist? What should a scanner do with two marks in one candidate's row, or a mark outside the 0–5 range? This library already treats [blanks and markers](rust_kernel_requirements.md) as first-class, which is a head start, but "what the scanner does" is a different question from "what the tabulator does with what it receives." *(Partly answerable here; the scanner half is not.)*

**Q3. What exactly must be reported, per precinct and in total?** Score totals and the pairwise matrix suffice mathematically — but "sufficient" and "required by canvass law" are different standards. *(Answerable here as a draft; needs a practitioner to confirm.)*

**Q4. What is the complete tiebreak ladder, expressed as procedure rather than as code — and does it match what state tie statutes require?** The engines already disagree at rung 2, which is a documented divergence and would become a compliance question. *(Answerable here; the statutory half varies by state.)*

**Q5. What does a recount of a STAR contest do**, given that the runoff pair is itself determined by the scoring round? Is a recount that changes the scoring round but not the finalists a different event from one that changes the finalists? *(Genuinely open. Worth drafting.)*

**Q6. What is in a logic-and-accuracy test deck for a STAR contest?** *(Fully answerable here — this is exactly the house style, and stone C-3.)*

**Q7. Is there any jurisdiction that would use it?** *(Not ours to answer, and it determines whether R5 ever arrives.)*

## What we already have, what we can get, and what we cannot

| Answer | Source |
|---|---|
| STAR tabulation semantics, verified six ways | **have** — the engines and the corpus |
| Marker, blank, and abstention handling | **have** — a first-class subject here |
| Where correct implementations legitimately disagree | **have**, but scattered — stone S-4 collects it |
| The specification, clause-numbered | **can produce** — C-1, weeks of writing |
| Rule-space coverage and the gap list | **can produce** — once the spec is numbered |
| NIST CDF / vendor CVR import | **can produce**, once Q1 is answered |
| Determinism, hashing, audit logging | **can produce** — small engineering |
| An L&A deck | **can produce** — C-3 |
| Whether scanners can export a STAR CVR | **cannot** — Q1, needs a vendor |
| What state law requires for canvass, ties, recounts | **cannot** — varies, needs practitioners |
| VSTL cost and sponsorship | **cannot** — needs an organization |

**The shortest path to knowing whether any of this is real is Q1**, and it is a question, not a project. Ask it before writing a line of anything.

---

## The honest boundaries

- **Certification is a state-by-state question.** EAC certification is voluntary at the federal level; states decide what they require, and they differ. Virginia's approval binds Virginia.
- **The VSTL test costs real money** and requires a sponsoring organization. No volume of documentation substitutes for it.
- **A tabulator is certified in configuration with a system**, not in isolation — so at some point a vendor partnership is unavoidable.
- **None of this is the bottleneck for STAR today.** Adoption is blocked by awareness, state law, and the absence of jurisdictions asking. Certification becomes the bottleneck the day after a jurisdiction says yes — which is exactly why having the documents already written is worth something, and why writing them is not urgent.
- **This page is a research summary from primary sources, not compliance advice**, and the landscape changes; VVSG 2.0's first certified system was announced in 2025.

---

## Sources

- U.S. Election Assistance Commission, *Explanation on Federal Certification of Voting Systems Utilizing Ranked Choice Voting*, October 2023 — [PDF](https://www.eac.gov/sites/default/files/2023-10/RCV%20Voting%20Systems%20V3%20Final%2010.20.23.pdf)
- Virginia Department of Elections, *Ranked Choice Voting Tabulation Software Approval*, May 2023 — [PDF](https://www.elections.virginia.gov/media/formswarehouse/ranked-choice-voting/RCTab-Security-Approval-(4).pdf)
- [Voluntary Voting System Guidelines 2.0](https://www.eac.gov/sites/default/files/TestingCertification/Voluntary_Voting_System_Guidelines_Version_2_0.pdf) · [EAC VVSG hub](https://www.eac.gov/voting-equipment/voluntary-voting-system-guidelines)
- [Ranked Choice Voting Resource Center — RCTab](https://www.rcvresources.org/rctab) · [BrightSpots/rcv source](https://github.com/BrightSpots/rcv)

*Up: [Tabulation engines](README.md) · related: [RCTab](rctab.md) · [stepping stones for a future implementation](rust_kernel_requirements.md) · [07_Concepts](../README.md).*
