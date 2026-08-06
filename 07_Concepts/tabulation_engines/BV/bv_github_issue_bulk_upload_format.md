<!--
Ready-to-paste GitHub issue for  github.com/Equal-Vote/bettervoting.

STATUS: filed 2026-08-06 as #1486 —
  https://github.com/Equal-Vote/bettervoting/issues/1486
  Pointer comment left on #810 itself:
  https://github.com/Equal-Vote/bettervoting/issues/810#issuecomment-5203454260

Origin: Adam asked whether #810 ("Allow election admins to bulk upload ballots")
should be CLOSED because it is CSV-based. ANSWER: NO — it is a maintainer's own
open feature request (ArendPeter, 2025-02), still live (jacksonloper commented
2025-12), and closing another team's roadmap item over a format preference would
be wrong. The useful move is a separate, narrowly-scoped issue about the FORMAT,
cross-referenced to it.

Everything asserted below was read from the BV repo, not assumed:
  * packages/frontend/src/components/UploadElections.tsx — PapaParse; the NOTE
    "this assumes rank_column_csv, may not work with other formats"; base race
    hard-coded `voting_method: 'IRV'`, `num_winners: 1`; candidate names
    harvested from the rank* columns; sentinels 'skipped' / 'overvote';
    max_rankings = count of rank* columns.
  * packages/frontend/src/components/ElectionSettingInference.ts — takes the
    FILE NAME, splits `jurisdiction_date_race`, throws if the jurisdiction isn't
    a known state/city.
  * packages/frontend/src/components/public_archive_settings.yaml — the YAML
    sidecar holding voting_method + exhaust_on_N_repeated_skipped_marks per
    jurisdiction. This is the strongest single point in the issue and it is
    entirely BV's own code: they already put the un-inferable settings in YAML.
-->

---

**Title:** Bulk ballot upload needs a defined ballot format — the parser #810 plans to reuse is rank-only and takes the method from the filename

### Summary

[#810](https://github.com/Equal-Vote/bettervoting/issues/810) proposes reusing the `UploadElections` logic for admin ballot upload. I went and read that code, and I don't think it transfers — not because it's bad, but because it was built for a different job: importing public-archive CVRs of real ranked elections. Three specific things would have to be decided before it can accept an admin's ballots for an arbitrary BetterVoting election.

This isn't a request to change the public-archive importer, which works fine for what it does. It's a request to **define the upload format** before the feature is built, since that decision is hard to walk back once people have files.

### 1. The parser is rank-only

`UploadElections.tsx` carries its own warning:

```js
// NOTE: this assumes rank_column_csv, may not work with other formats
const rankFields = parsed_csv.meta.fields.filter((field) => field.startsWith('rank'));
```

Candidate names are then harvested out of the `rank*` cells. That shape can express a ranked ballot and nothing else — there is no way to write a STAR `0–5` score, an Approval `0/1`, or a Plurality mark in it. #810's target is any election an admin owns, and BetterVoting supports STAR, STAR_PR, Approval, Plurality, RankedRobin, IRV and STV. So the format question is unavoidable, not incidental.

### 2. The method comes from the filename, not the file

```js
voting_method: 'IRV',   // base race, before inference
…
inferences = inferElectionSettings(cvr.name);   // <- the FILE NAME
```

and `ElectionSettingInference.ts` splits that name into `jurisdiction_date_race`, then throws if the jurisdiction isn't a known state or city:

```js
if(state == undefined) throw `Couldn't infer state from ${file_name}`
```

That's reasonable for archive imports of `Burlington_20090303_Mayor.csv`. It can't work for an admin uploading `ballots.csv` into their own election — and it shouldn't have to, because in #810's flow the **election already exists and already knows its races**. Which is the good news: for this feature the method doesn't need to be inferred *or* declared, it needs to be **checked**. The upload should validate the file against the race it's being loaded into and reject a mismatch, rather than guess.

That check is only possible if the file's shape is defined in the first place. `0,0,1,1` is a valid Approval ballot, a valid STAR ballot, and an **invalid Plurality** ballot — two votes in a one-vote race. Nothing about those eight characters says which.

### 3. There's no vocabulary for the non-votes

The current parser recognises two sentinels in a rank cell, `skipped` and `overvote`. A score ballot needs more than that, and the distinctions are exactly the ones already being argued about on the download side:

- a real `0` (an active low score) vs. a blank vs. a deliberate abstention vs. a spoiled ballot — all tabulate as 0, all mean different things. See [#791](https://github.com/Equal-Vote/bettervoting/issues/791), [#1090](https://github.com/Equal-Vote/bettervoting/issues/1090), [#1160](https://github.com/Equal-Vote/bettervoting/issues/1160), and the policy question in [#884](https://github.com/Equal-Vote/bettervoting/issues/884).

If upload can't express a distinction that download exports, the two ends don't match.

### The constraint that resolves most of this: make it round-trip

The natural source of an upload file is a **previous export**. So: *whatever the export writes, the upload should accept, and re-uploading an export should reproduce the election.* Adopting that one rule settles most of the format questions for free, gives an obvious test case, and makes #1160's processed-vs-raw split meaningful in both directions rather than just one.

### One observation, from your own repo

`public_archive_settings.yaml` opens with:

```yaml
# This file is used to infer election settings when elections are uploaded to public archive
```

…and holds `voting_method` and `exhaust_on_N_repeated_skipped_marks` per jurisdiction. That file exists **because a ballot CSV can't carry the election's configuration** — the conclusion is already drawn here, it's just implemented as a lookup table keyed on the filename instead of as fields in the file. That's the whole argument for a richer upload format, and it's yours, not mine.

### Happy to help

I maintain a public library of ~500 runnable elections in a format built for exactly this problem — the ballots, the method, the seats, the tie-break order and a per-cell marker vocabulary (`-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled and re-issued) in one plain-text file, with an engine that validates ballots *against* the declared method and refuses mismatches. MIT licensed, free to copy:

- [Eight lines of CSV, eight questions](https://masiarek.github.io/star-voting-library/YAML_library/csv_ambiguity.html) — the ambiguity worked through on eight real ballots
- [Why YAML, and not CSV or JSON](https://masiarek.github.io/star-voting-library/YAML_library/why_yaml_test_cases.html) — including why the method has to be in the file for anything to be validated
- [The format, field by field](https://masiarek.github.io/star-voting-library/YAML_library/YAML_authoring_template.html)
- [~500 elections in it](https://masiarek.github.io/star-voting-library/07_Concepts/YAML_test_case_index/index.html), across 17 methods

Related: [#810](https://github.com/Equal-Vote/bettervoting/issues/810) (the feature), [#778](https://github.com/Equal-Vote/bettervoting/issues/778) (the general file-standard discussion), [#349](https://github.com/Equal-Vote/bettervoting/issues/349) (ballot multiplier — bulk upload is where weighted rows would naturally arrive), [#1236](https://github.com/Equal-Vote/bettervoting/issues/1236) (restricting the ballot source), [#1485](https://github.com/Equal-Vote/bettervoting/issues/1485) (recording the abstention policy).
