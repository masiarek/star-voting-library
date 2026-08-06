<!--
Ready-to-paste GitHub issue for  github.com/Equal-Vote/bettervoting.

STATUS: filed 2026-08-06 as #1485 —
  https://github.com/Equal-Vote/bettervoting/issues/1485

Origin: the one idea from the #778 "YAML File standard" sketch that has no home
anywhere — `race abstention allowed` / `candidate abstention allowed`. Those
describe what the ELECTION'S RULES permitted, not what a voter did, and neither
the election object, the export, nor the CSV records them.

Checked for duplicates before filing:
  * #699 "Election setting for requiring races" — the UI half of the RACE level,
    open since 2024-10, maintainer says "we don't have a use case for this yet".
    This issue is deliberately scoped to the RECORDING side and cites #699 rather
    than restating it, and supplies the use case #699 asked for. A comment saying
    so was left on #699 itself 2026-08-06 (conceding we have no strong case for
    the SETTING, only for storing its value):
    https://github.com/Equal-Vote/bettervoting/issues/699#issuecomment-5203410021
  * #627 (can't abstain from the last race) is a bug in the current behavior —
    cited as evidence that intended and actual policy already differ.
  * #778 / #1160 / #791 / #1090 / #884 are the format, export and policy
    neighbours; all cross-referenced.
-->

---

**Title:** Record the abstention policy on the race, so an export says what was *allowed* — not just what voters did

### Summary

An exported BetterVoting election cannot distinguish **"nobody abstained"** from **"abstaining was impossible."** Both look identical: no `null`s, `nAbstentions: 0`. Whoever re-counts or audits the election later has no way to tell which one they are looking at, and no way to reproduce the election's actual rules.

This is a small, additive request: **store the abstention / undervote policy on the race, and carry it into the export.** It's the recording half — separate from, and cheaper than, the admin UI in #699.

### What's there today

`Election.races[]` carries only:

```json
{
  "title": "…",
  "race_id": "…",
  "num_winners": 1,
  "voting_method": "STAR",
  "candidates": [ … ],
  "description": ""
}
```

and `Election.settings` is election-wide, with nothing about undervotes:

```json
{
  "voter_access": "open",
  "voter_authentication": { "ip_address": false, "voter_id": false, "email": false },
  "ballot_updates": false,
  "public_results": true,
  "time_zone": "America/Los_Angeles",
  "random_candidate_order": false,
  "require_instruction_confirmation": true
}
```

So the policy that governed the ballots is nowhere in the artifact the ballots ship in.

### Two distinct levels

They're worth separating, because a system can plausibly allow one and not the other:

1. **Race-level** — may a voter skip the whole race? (This is what #699's setting would control.)
2. **Candidate-level** — may a voter leave an individual candidate unscored on a STAR or Approval ballot, or must every line be marked?

### Why it matters — the use case #699 asked for

> *"We could add an election setting to require a vote for every race, but we don't have a use case for this yet so it's not a high priority"* — [#699](https://github.com/Equal-Vote/bettervoting/issues/699)

Fair, for the *setting*. But the **recording** has a use case that doesn't depend on the setting ever shipping:

- **Audit and recount.** A third party re-tallying a frozen export has to interpret every `null`. Whether zero abstentions is a fact about the voters or a fact about the ballot changes what that export means — and today the file is silent, so the auditor guesses.
- **Reproducing a count in another engine.** This is the case I hit constantly. When a count is re-run outside BetterVoting, the abstention rule has to be supplied by hand from outside the file, which is exactly the class of ambiguity [#778](https://github.com/Equal-Vote/bettervoting/issues/778) is about.
- **Intended vs. actual already differ.** [#627](https://github.com/Equal-Vote/bettervoting/issues/627) reports that a voter *can't* abstain from the last race. So there is already at least one election where the effective policy isn't the documented one — and nothing in the export would ever show it.
- **It's the cheap half.** A recorded default costs one field and no UI. If #699 ever ships, the field is already there to hold its value; if it never ships, the export still stops being ambiguous.

### Suggested shape

Whatever fits the schema best — the specific spelling matters much less than having the value somewhere. One option, per race:

```json
"undervotes": {
  "race_may_be_skipped": true,
  "candidates_may_be_left_unscored": true
}
```

Both defaulting to today's behavior, so nothing changes for existing elections. Then:

- echo it in the JSON export (`Election.races[]`), and
- name it in the CSV download's header or sidecar, alongside whatever comes of [#1160](https://github.com/Equal-Vote/bettervoting/issues/1160)'s processed-vs-raw split — a CSV of scores is where the ambiguity bites hardest ([#791](https://github.com/Equal-Vote/bettervoting/issues/791), [#1090](https://github.com/Equal-Vote/bettervoting/issues/1090)).

### Relation to the other abstain tickets

This one is deliberately **not** about what *counts* as an abstention — that's [#884](https://github.com/Equal-Vote/bettervoting/issues/884), and it's a policy argument I've made elsewhere. This is the layer underneath: whatever the counting rule is, the file should say what the voter was permitted to do, so the rule can be applied — or audited — by someone who wasn't there.

Background and the neighbouring tickets, cross-referenced to reproducing cases: [BV abstain / blank / zero — issue index](https://masiarek.github.io/star-voting-library/07_Concepts/tabulation_engines/BV/abstain_issues_index.html).
