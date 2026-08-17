# Re-scoping the BPML sheet, and the columns that follow

**Level: reference · deep dive**

A proposal, written after running [the reconciliation](RECONCILIATION.md). It answers one question — *what is the BPML sheet's job?* — because the answer determines what columns it needs, and getting that order backwards would mean adding 162 rows to a sheet that shouldn't have them.

## The finding that forces the question

The sheet references **one** of the library's 163 BV-backed elections. The instinct is that this is neglect and the fix is to add the other 162. It isn't, and it isn't.

Split the sheet's own rows by what they are actually about:

| | rows | share |
|---|---:|---|
| BPML rows about **the application** | 102 | 91% |
| BPML rows about **counting votes** | 9 | 8% |
| Library elections, every one about **counting votes** | 163 | 100% |

The sheet is an **application** inventory: create an election, change a race, upload voters, download a CSV, log in, archive, preserve ballot secrecy. The library is a **tabulation** inventory: given these ballots under this method, is this the right winner.

Those are two different testing activities. The join returned 1 not because anyone neglected it, but because the two documents are about almost disjoint subject matter. No single test-id column can be the coverage map for both.

**The clearest illustration** is the row *"Ranked Robin Voting - Single Winner."* It cites `BV1550`, which exists in neither inventory, so the sheet reads as a coverage gap. Meanwhile the library holds **41 Ranked Robin elections**, each cross-verified three ways. The row isn't uncovered — it's *mis-pointed*. It's pointing at one id when the honest answer is a whole family.

## The re-scope

**Two inventories, each owning one question, with a named seam between them.**

| | Owns the question | Verified by | Size |
|---|---|---|---|
| **BPML sheet** | *Does the application do the thing?* | the Drive QA log (`BVxxx` functional tests) | 102 rows |
| **The library** | *Given these ballots, is this the right winner?* | runnable YAML cases with published answer keys | 163 elections |

The seam is those nine counting rows. **A counting row's verification is a method family, not a test id** — so it links to the library's by-method index, and the library's own count is the coverage number.

**The sheet does not gain 162 rows. It gains nine links.**

That also fixes the thing that made the sheet feel wrong to sort: today its Test Case column silently means two different things depending on which kind of row you're on. Naming the scope per row makes every other column unambiguous.

### The nine seam rows, and what each should point at

| BPML row | Currently cites | Should point at | Library has |
|---|---|---|---|
| Voting Methods → Ranked Robin, single winner | `BV1550` (nonexistent) | RankedRobin cases | **41** |
| Voting Methods → Single-winner Approval | — | Approval cases | **15** |
| Voting Methods → STAR scoring/runoff divergence | `BV90` (QA log only) | STAR cases | **122** |
| Voting Methods → Plurality, single-winner | — | Plurality cases | **22** |
| Voting Methods → Multi-winner Bloc STAR | — | Bloc STAR cases | **23** |
| Voting Methods → Multi-winner Plurality | *(process name repeated)* | Plurality multi-winner | subset of 22 |
| Establish Election Procedures → Handling ties | — | the tie-behaviour cases | tie cases across methods |
| Tabulation → Distribution of Equal Support | — | Equal Support cases | STAR subset |
| Election → Verify Preference Matrix | `BV705` (nonexistent) | matrix cases | STAR subset |

Every "nonexistent" id above becomes a live link under the re-scope. Three rows that read as gaps today are in fact the best-covered things in the project.

**Six of the nine resolve cleanly; three do not, and the generator says so.** Ranked Robin, Approval, STAR, Plurality, Bloc STAR and multi-winner Plurality each map onto a method family, so they come out `covered` with a count. The remaining three — *Verify Preference Matrix*, *Handling ties*, *Distribution of Equal Support* — are **cross-cutting concerns rather than method families**: the relevant cases are scattered across several methods, so a by-method index is the wrong target and they come out `unchecked` instead of being given a link that doesn't answer the question. Those three need a curated case list, which is the one piece of this that can't be generated.

## The column spec

Only now does this make sense. Seven columns, replacing six.

| # | Column | Values | Notes |
|---|---|---|---|
| 1–3 | `L1` / `L2` / `L3` | unchanged | the process hierarchy |
| 4 | **`Scope`** | `Application` · `Counting` | **new, and the load-bearing one** — it decides how columns 6 and 7 are read |
| 5 | **`Help URL`** | a docs.bettervoting.com URL, or blank | blank = not published. This is the coverage dashboard the sheet was missing |
| 6 | **`Spec`** | Drive design doc / functional spec link | split out of today's combined column |
| 7 | **`Verified by`** | `Application` → a `BVxxx` from the QA log · `Counting` → a link to the library's by-method index | one column, two readings, disambiguated by `Scope` |
| 8 | **`Status`** | `covered` · `gap` · `n/a` · `unchecked` | kills the ambiguous blank |
| 9 | `Additional info` | unchanged | keeps `EB-phase0` and similar cohort tags |

**Why `Status` matters more than it looks.** Today an empty cell could mean *not needed*, *not written*, or *nobody has checked* — three very different things that sort identically. That is why the sheet can't produce a percentage. With an explicit value it can, and `gap` becomes the filter that drives the work.

**Why splitting column 4 matters.** Today one column is headed *"Functional Specification or BPML details or Training Document."* Three artifact types in one cell means you cannot ask "which processes have user-facing help?" separately from "which have a spec" — and the first of those is the actual docs backlog.

## Six defects to fix in the same pass

Found while reading the sheet; all cheap, none contentious.

1. **`Voter` and `Electors (Voters)` are the same L1**, split into two branches, both carrying Create / Change / Delete rows. Merge them.
2. **Two rows have `co to` as the L3 process name** — placeholder text that shipped.
3. **A row about the sheet, inside the sheet**: `BPML - Overview → BPML - Overview → BPML - Overview`.
4. **`Election State / Status - Test`, annotated *"Same as Open?"*** — no. `validElectionStates` is `['draft','finalized','open','closed','archived']`; there is no test state, and **draft** is the test mode. Verified from source in [bv_draft_state_test_votes.md](../bv_draft_state_test_votes.md). Delete the row.
5. **A stray row** — `follow up on this` sitting in the L1 column with a starvoting.org link in L2.
6. **`Multi-winner Plurality` cites its own process name as a test case.** It looks like coverage and isn't; under the re-scope it becomes a library link.

## What this does not change

The sheet stays a **backlog**, not navigation. That verdict is unchanged and is argued in [the docs information architecture](../bv_docs_information_architecture.md): the L3 names are system functions, not the questions users type, and one user question scatters across several rows. Re-scoping makes the backlog *sortable*; it does not make it a site map.

---

Related: [the reconciliation](RECONCILIATION.md) · [docs information architecture](../bv_docs_information_architecture.md) · [BV registry](../../../YAML_test_case_index/BV_registry.md) · [all cases by method](../../../YAML_test_case_index/README.md)
