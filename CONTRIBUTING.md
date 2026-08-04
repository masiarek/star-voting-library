# Contributing

Thanks for helping! This page is the short front door; the depth lives in three
documents linked below.

## Setup (once)

```bash
git clone https://github.com/masiarek/star-voting-library
cd star-voting-library
uv sync
git config core.hooksPath STARVote_LH_tabulation_engine/tools_adam/scripts/git-hooks
```

## The loop

1. **Find your way around** — the [Repository & Engine Guide](07_Concepts/about_this_repo/repository_guide.md)
   has the repo map, quick-start commands, and how the voting methods dispatch.
2. **Adding or editing an election case?** Copy from the
   [YAML authoring template](07_Concepts/about_this_repo/YAML_authoring_template.md) —
   it documents every allowed key (a schema lint enforces the list). After
   editing a case's YAML, re-run it through the engine so its `_tabulated`
   mirror stays fresh, then regenerate the derived pages:

   ```bash
   uv run python STARVote_LH_tabulation_engine/starvote_larry_hastings.py path/to/case.yaml
   uv run python STARVote_LH_tabulation_engine/tools_adam/scripts/regen_all.py
   ```

   On a checkout you haven't edited, `regen_all.py` is a **no-op** — it should
   leave `git status` clean. Anything it reports is either drift someone forgot
   to commit or a bug in a generator; either way, don't commit around it. The
   generated CSVs are stored **LF**, per `.gitattributes`, so every builder that
   writes one passes `lineterminator="\n"` — Python's `csv` module defaults to
   RFC 4180 CRLF, which git would then flag on every rebuild forever.

3. **Follow the house conventions** — terminology, naming, options defaults,
   and the one-door-per-method rule are all in [CLAUDE.md](CLAUDE.md) (it
   doubles as the standing guidance for the repo's AI tooling; the conventions
   apply to humans equally).
4. **Run the tests** — the same suite CI runs on every push:

   ```bash
   uv run pytest
   ```

Every claim in this library is backed by a runnable election, and the test
suite is what keeps that promise honest — if your change flips a winner or
strands a generated page, a test will name it.
