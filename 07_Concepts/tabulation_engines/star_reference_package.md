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

### D1 — The clause-numbered specification

Enough to implement STAR correctly **without reading any implementation**. Every tie rung, every ballot-marking edge case, every reporting obligation. Each clause numbered, each clause citing the case file that pins it.

**Done when:** a competent stranger could implement from it and pass the conformance suite. **Why first:** everything else references clause numbers.

### D2 — Rule-space coverage, and the gap list

Tag every existing case with the clauses it exercises; generate the list of clauses no case would catch a violation of; write the missing cases.

**This is the deliverable that changes what the library *is*.** The 615 cases currently prove *agreement between engines*. They do not yet prove *rule coverage* — a corpus can hold 615 elections and still have no case where the runoff pair is itself tied. Coverage of rule space and coverage of election space are different claims, and case count measures the wrong one.

**Done when:** every clause has at least one case that fails if the clause is violated.

### D3 — The conformance suite, published for implementers

The existing corpus, re-fronted for a reviewer rather than a learner: the format, how to run your own engine against it, what a pass means, what each case proves. Plus the JSON result contract that makes engine comparison mechanical.

**Done when:** someone else's tabulator can be scored against it without asking us anything.

### D4 — A logic-and-accuracy test deck

Every jurisdiction runs L&A before every election. For plurality this is routine; for RCV it now exists; for STAR nobody has written what the deck contains or what output to expect. A small, deliberately-designed set of ballots with a hand-verifiable expected result — exactly this library's house style.

### D5 — A model VVSG 2.0 implementation statement

The highest-leverage document nobody has written. Because the EAC defines no requirements for *what a voting method is* and instead tests a system against its own stated implementation, this statement **is** the method-specific certification content. A handful of pages that hands any future vendor or nonprofit the hardest part of their paperwork, pre-drafted — and that makes STAR procurable, since a jurisdiction cannot write a contract for a method nobody has specified.

### D6 — The CVR mapping

How a 0–5 score ballot is represented in a cast vote record — NIST CDF, and whatever the vendor exports look like. **Blocked on the pivotal open question** (see below), and honest about it: if the answer is that no certified scanner can export a STAR CVR without a firmware change, that fact belongs in this document rather than being discovered later.

---

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
