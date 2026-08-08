# What "test votes" means in BetterVoting's draft state

BetterVoting's *"Draft" State* help draft says **"All votes cast during this state will be counted as test votes,"** and then leaves an explicit note to itself: *"Follow up: create a document explaining what it means."* This page is that follow-up, answered from BetterVoting's source rather than from inference — every claim below cites the file that makes it true.

The headline: **draft *is* BetterVoting's test mode.** There is no separate test state — the [BPML use-case sheet's](bv_docs_information_architecture.md) row *"Election State / Status - Test → Same as Open?"* is right to carry a question mark, and the answer is "neither: it's draft." That is the same shape as the two findings already written up here — [there is no demo flag](bv_voter_authentication_modes.md), and there is no `demo_title` — where something that looks like a mode turns out to be a derived condition.

## What is true of a draft election

**Voters can reach it and cast ballots.** A draft election is *not* invisible to voters, which is the one thing the current help draft gets wrong when it says "The election is not yet live or accessible to voters." BetterVoting will send invitation and message emails while the election is in draft, and stamps them with a banner (`EmailTemplates.ts`):

> ⚠️This {election|poll} is still in test mode. All ballots during test mode will be removed once the election is finalized, and at that time you will need to vote again.⚠️

**Those ballots are deleted automatically when you finalize** — the email's promise is kept, and it is not a manual step. `finalizeElectionController.ts` sets the state and then calls `innerDeleteAllBallotsForElectionID(req)` in the same request. (There is also a manual ballot reset, but it is gated to draft too: *"Ballots can only be reset while in draft mode or if it's a public_archive election."*)

**Finalizing is a one-way door, and it is the only way out of draft.** The controller rejects any election that isn't in draft with *"Election already finalized."* So the draft→finalized transition happens exactly once, and everything below stops being true at that moment.

**Finalizing also stamps a default on you.** If the election never set `max_rankings`, finalize writes one — `DEFAULT_BALLOT_RANKS`, defaulting to **6**. Worth knowing for a ranked election: the ranking limit your voters get is decided at finalize, not at build time, if you never touched it.

## What a test vote does *not* exercise — the part that matters

This is the substance of the follow-up, and it is the part a help page has to say out loud, because the natural reading of "test mode" is *"a rehearsal of the real thing."* It isn't. Two of the checks that define a real BetterVoting election are **skipped entirely** while in draft.

**1. Voter authentication and the voter roll are skipped.** From `castVoteController.ts`, with the comment in the source:

```ts
// skip voter roll & validation steps while in draft mode
if (targetElection.state !== 'draft' && req.election.ballot_source !== 'prior_election') {
    const missingAuthData = checkForMissingAuthenticationData(req, targetElection, req, voter_id)
    if (missingAuthData !== null) throw new Unauthorized(missingAuthData);
    roll = await getOrCreateElectionRoll(req, targetElection, req, voter_id, true);
    const voterAuthorization = getVoterAuthorization(roll, missingAuthData)
    assertVoterMayVote(voterAuthorization, targetElection, req);
}
```

Everything in that block — the authentication check, the roll lookup, and `assertVoterMayVote` — is inside the `state !== 'draft'` guard. So while an election is in draft, **its security settings are not being enforced**, whatever they say on the Manage Voters screen. A test vote from someone not on your voter list will succeed. So will a second test vote from the same person.

That is the single most important thing for a help page to say, because it inverts what an admin is trying to learn. If you test a restricted election in draft and the ballot goes through, **you have learned nothing about whether your restriction works** — you have confirmed that draft skips the check. The [six voter-authentication modes](bv_voter_authentication_modes.md) are exactly the thing a draft test cannot exercise.

**2. Editable ballots are off.** Also from `castVoteController.ts`:

```ts
if (targetElection.settings.ballot_updates && targetElection.state !== 'draft') {
```

The lookup that finds a voter's prior ballot and updates it in place only runs outside draft. So in draft, a voter who votes twice produces **two ballots**, not one revised one — even on an election configured for editable ballots. Vote-changing cannot be rehearsed in draft either.

## So what *is* a draft test good for?

Stated positively, which is how the help page should put it — a draft test genuinely verifies:

- **the ballot itself** — that the races, candidates, and wording render the way you meant, on the device the voter will actually use;
- **the voting method** — that scores or ranks behave as expected and the results page draws;
- **the email text** — what your invitation actually looks like when it lands;
- **the whole flow end to end**, from link to receipt.

And it verifies none of:

- **who can vote** (auth and roll checks skipped);
- **one-person-one-vote** (`assertVoterMayVote` skipped);
- **vote-changing** (`ballot_updates` disabled);
- anything about the **live ballot set**, since finalize deletes it.

## Why this matters for the docs

The current help draft describes draft state in generic terms — *"the initial planning phase,"* *"changes and edits are freely allowed"* — which is true and matches every election system ever built. The BetterVoting-specific facts are the four above, and they're the ones an admin gets wrong: that voters *can* be invited during draft, that their ballots *will* vanish at finalize, that the security settings *aren't live yet*, and that finalize is *once only*.

Same failure mode as the *Poll vs Election* draft, which answers with textbook political science (*"a poll is a survey or sampling of opinions…"*) when BetterVoting's own answer is much smaller and much more useful — see the [IA proposal](bv_docs_information_architecture.md#the-first-question-election-or-poll). Both drafts hedge where the code is definite. A help page can afford to be definite; that's most of its value.

## Related

- [Organizing docs.bettervoting.com — an IA proposal](bv_docs_information_architecture.md) — where this page fits, and the Election-vs-Poll answer
- [BetterVoting's six voter-authentication modes](bv_voter_authentication_modes.md) — the settings a draft test does *not* exercise
- [Creating BetterVoting elections via the API](bv_api_election_creation_notes.md) — the admin URL map
- [BV — BetterVoting (the live web app)](README.md)
