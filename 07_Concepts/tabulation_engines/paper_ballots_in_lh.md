# What paper ballots would mean for the LH engine — a requirements sketch

**Level: reference · deep dive** Companions: [Election systems at organization scale](../topics/election_systems_at_org_scale.md) · [Run a paper-ballot STAR demo](../../01_STAR/01_Learn/hands_on/running_a_paper_ballot_demo.md) · [What would it take to certify STAR software?](certifying_star_software.md). Nothing here is implemented — this is a design document.

**Scope, stated up front.** This is about **private elections run with private software**: a co-op board, a union local, an HOA, a club AGM, a party committee. Not state elections. That scope removes most of the government requirement set — no VVSG certification, no ballot-on-demand printing, no jurisdiction-wide ballot-style inventory, no risk-limiting audit at scale, no accessibility mandate under HAVA. What it does **not** remove: ballot secrecy, double-vote prevention, and reconciliation. Those are not federal impositions — they are what makes a vote a vote, and an organization that skips them has run a survey.

The specific case worth designing for is the one that's actually common: a **hybrid** election, where some members vote electronically and some on paper.

---

## The one change everything follows from

Today a YAML case file's `ballots:` block **is** the election. It is the original record, and the only one. There is nothing behind it to check it against, which is exactly right for a teaching library.

Introduce paper and the YAML is demoted: it becomes a **transcript of a record that lives somewhere else**. The paper is the [ballot of record](../topics/election_systems_at_org_scale.md) — the original, human-readable, voter-verified statement of intent — and the file is a derivative representation of it. Every requirement below is a consequence of that single demotion.

## The requirements

### R1 — Provenance, per ballot

Every ballot row must say which channel produced it. Today all rows are identical in kind; in a hybrid election a row is either a transcription of a physical object or a record born digital, and those have different failure modes, different marker vocabularies (R4), and different custody.

Without it, a discrepancy cannot be localized: you know the totals disagree and nothing more. A row comment (`# paper 014`) is *nearly* free, since the ballot-art drawer already reads row comments — but a comment is not data and the engine must not depend on one. This wants a real field.

### R2 — One roll across both channels *(the hard one, and not the engine's job)*

If a member can vote online **and** drop a paper ballot, nothing downstream can detect it. Both ballots are anonymous, both look valid, and the tabulator has no way to know. There is no clever counting rule that recovers from this.

So: **hybrid voting requires a single marked roll — one poll book covering both channels — and no tabulator can substitute for it.** The engine's only honest contribution is to make the failure *visible* at the reconciliation layer (R3), never to prevent it. State this in any documentation, because it is the requirement an organization is most likely to assume the software handles.

### R3 — Reconciliation arithmetic, printed

Three identities, checked and shown:

```text
ballots counted   = paper transcribed + online cast
ballots counted  ≤ voters checked in
voters checked in ≤ eligible roll
```

The engine already owns the last line — `eligible_voters` is an *external* number precisely because it comes from the roll, not from the ballots, and it is what drives the quorum report. Extending that into a funnel is a natural fit and the repo already has the pattern: the runoff summary is deliberately **self-reconciling**, and the `_tabulated` mirror expands it into a `461 − 98 = 363` funnel. Same shape, three lines higher up.

### R4 — The two channels do not have the same ballot space

This is the subtle one, and it is specific to this engine. Paper can produce states an online form usually prevents at input: two bubbles filled in one row, an illegible mark, a ballot spoiled and reissued. The engine already has vocabulary for exactly these — `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — and it is worth noticing that **that is paper vocabulary**. It exists to record what was physically on a sheet.

The consequence for reporting: a hybrid election's marker distribution will be lopsided by channel, and pooling the two invites a wrong inference — *"paper voters are sloppier"* when the truth is that only paper voters **can** be. Requirement: **markers reported per channel, never pooled.**

### R5 — Transcription is a trusted step; make it reviewable *(before OCR, not after)*

A human reads marks and types digits. That is one person's judgement standing exactly where an audit trail should be, and it is the weakest link in the current demo loop.

The cheap fix is not OCR. It is **double entry**: two people transcribe the same stack independently into two files, the tool diffs them, and only the disagreements go to adjudication in front of witnesses. That converts an unmeasurable trust assumption into a measured disagreement rate, it is perhaps twenty lines of code, and it is how double-key data entry has worked for a century. Requirement: **a diff-and-adjudicate path ships before any scanning.**

### R6 — Secrecy is the weaker of the two channels

Online ballots usually arrive through an identity-bound link; paper is anonymous once it is in the box. A hybrid election's secrecy property is the **minimum** of the two, not the average — and most small-org platforms retain the member-to-ballot mapping and protect it by access control rather than discarding it.

Two rules follow: **do not publish a running tally** during a hybrid election (a ballot landing in a quiet window *is* the movement in the totals, and a 0–5 delta exposes the voter's rating of every candidate, not one bit), and **discard the link-to-member mapping once reconciliation is done**.

### R7 — One close time, no partial publication

Electronic votes are instant; paper arrives late — mailed proxies, absentee envelopes, the stack someone forgot in a tote bag. Two failure modes: announcing before the paper lands, and publishing a preliminary electronic-only tally that then moves and looks like tampering.

Requirement: **a single close time and no partial publication.** Worth flagging that this is the place where this library's [summability](../topics/summability/README.md) argument is honestly *irrelevant* — the constraint is ballot **arrival**, not the arithmetic of addition. Summability buys you nothing against a late envelope.

### R8 — What the report must print

For a member in the room to check the count without trusting anyone, the report needs four things it does not print today: ballots **by channel** · markers **by channel** · the R3 reconciliation funnel · and the transcription provenance (who transcribed, whether double-entered, how many rows were adjudicated). The engine's whole culture is "print the entire audit"; this is that culture extended by four lines.

## What it would cost in the file format

Not implemented — a sketch, so the shape is arguable before anything is built. The current schema's top-level keys are fixed and checked (`check_top_level_keys`), so additions are deliberate, not incidental:

| Proposed | Holds | Note |
|---|---|---|
| `ballot_source:` | `digital` (default) \| `paper` \| `hybrid` | Absent ⇒ `digital`, so all 500+ existing cases stay valid and unchanged. |
| `transcription:` | transcriber(s), double-entered y/n, adjudicated row count, date | The provenance R8 prints. Prose, not arithmetic — the engine records it, never validates it. |
| `checked_in:` | count of voters who were issued a ballot | Sits between `eligible_voters` and the ballots; completes the R3 funnel. |
| a per-row channel mark | `paper` / `online` on each ballot | The only one that touches the ballot grammar, which is why it is the one to argue about hardest. |

The default matters: **`digital` unless stated** keeps paper an opt-in claim. A file should never *appear* to be paper-backed because someone forgot a key.

## What not to build

- **Not OCR as the source of truth.** Scanning before double entry builds the harder half first, and an unverified OCR pass is worse than a tired human because it is confidently wrong *at scale and uniformly*. The existing spec's gate is the right one — a synthetic-ballot round trip (render ballots with known scores → read them back → assert equality) before it is trusted on anything real.
- **Not certification.** State certification is a different universe and [certifying STAR software](certifying_star_software.md) covers why. Private software for private elections does not need it and must not imply it.
- **Not cryptographic end-to-end verifiability.** [Counting under encryption](../topics/homomorphic_tallying.md) and the [Rust kernel requirements](rust_kernel_requirements.md) already argue that this belongs to a funded team with a professional audit, and that the hard problems there are social rather than mathematical.
- **Not a claim that any existing case is paper-backed.** None is, and none should acquire the appearance of being so.

## A staged path

1. **`checked_in:` and the reconciliation funnel.** Pure arithmetic on numbers the engine already handles, no ballot-grammar change, and it is the requirement organizations most often skip. Cheapest real integrity gain available.
2. **`ballot_source:` and `transcription:`.** Recording, not validating. Makes the provenance claim explicit and falsifiable.
3. **Per-channel reporting** (R1, R4, R8). Needs the ballot-grammar decision, which is the genuinely contentious one.
4. **Double-entry diff** (R5). Small tool, large trust gain.
5. **OCR.** Only after 4, and only behind the round-trip self-test.

Steps 1–2 are afternoons. Step 3 is a schema argument. Steps 4–5 are the only real projects, and 5 should stay parked until someone actually needs it.

## See also

- [Election systems at organization scale](../topics/election_systems_at_org_scale.md) — where paper sits in the wider architecture, and what this library has versus what it hasn't.
- [Run a paper-ballot STAR demo](../../01_STAR/01_Learn/hands_on/running_a_paper_ballot_demo.md) — the loop as it exists today, including the honest note that reading the paper is manual.
- National Academies, [*Securing the Vote*](https://www.nationalacademies.org/projects/PGA-STL-16-02/publication/25120) (2018), Box 3-2 — the ballot-of-record definition, and a level-headed account of paper's own failure modes.
