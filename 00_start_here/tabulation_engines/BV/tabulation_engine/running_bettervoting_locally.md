# Running BetterVoting locally — the two setups, and the gotchas

Notes-to-self so the next local run isn't a struggle. There are **two** ways to run BetterVoting on the Mac; they are for different jobs. Picking the wrong one is what cost the time.

## TL;DR — which setup?

| I want to… | Use | Why |
|---|---|---|
| **Click through the UI** (vote, create an election, test a results page) | **Dev flow** (`localhost:3000`) | `localhost` is a *secure context* → browser crypto works; hot reload; runs your branch |
| Run the **Playwright E2E suite** / check the fully-built app | **Docker compose** (`docker compose up`) | It's an E2E harness: builds the app + runs the tests inside the Docker network |
| Unit tests / `tsc` / lint only | neither — just `npm` | pure Node, no services needed |

The Docker compose is **not** meant for host-browser manual use (see the `crypto.randomUUID` gotcha below). For clicking around, use the dev flow.

---

## Setup A — Dev flow (use this for manual UI testing)

Hot-reloading dev servers on `localhost`, backed by Docker Keycloak + local Postgres. This is the one to use day-to-day.

- Frontend → **http://localhost:3000**
- Backend → **http://localhost:5001**
- Keycloak (Docker) → localhost:8080
- Postgres (Homebrew) → localhost:5432

**Steps** (all from the repo dir `/Volumes/T7/Voting/BetterVoting/BV/bettervoting`, in `fish`):

```fish
# 0. If the Docker E2E stack is running, stop it first (frees 5432/8080):
docker compose down

# 1. Local Postgres (usually already running):
brew services start postgresql@16
#    First time only, or after schema changes:
npm run migrate:latest -w @equal-vote/star-vote-backend

# 2. Keycloak in Docker (the dev flow still uses it):
docker compose up -d --build keycloak

# 3. If you edited anything under packages/shared/, REBUILD it (see gotcha #4):
npm run build -w @equal-vote/star-vote-shared

# 4. Backend — terminal 1 (leave running):
npm run dev -w @equal-vote/star-vote-backend      # wait for "Server started on port 5001"

# 5. Frontend — terminal 2 (leave running):
npm run dev -w @equal-vote/star-vote-frontend     # opens http://localhost:3000
```

Then open **http://localhost:3000**, sign in, and go.

---

## Setup B — Docker E2E stack (use this to run the test suite)

```fish
docker compose up --build      # first time; later just `docker compose up`
```

Builds the `web` image (frontend + backend), starts Postgres/Keycloak/nginx, and the **Playwright container auto-runs the E2E suite** (you'll see e.g. `19 passed`). The app is served inside the Docker network at `web:5000` — reaching it from a host browser needs a hosts hack *and* still breaks browser crypto (gotcha #3). So use this for **tests**, not clicking.

---

## The gotchas (each cost time today)

**1. Port 5000 is taken → `bind: address already in use`.**
macOS **AirPlay Receiver** (process `ControlCe`) squats on port 5000.
Check: `lsof -i :5000`. Fix: **System Settings → General → AirDrop & Handoff → AirPlay Receiver → Off.**
(The dev flow sidesteps this by using 5001/3000, which is why `DEV_START.md` puts the backend on 5001.)

**2. Keycloak login "Invalid username or password".**
`admin` / `admin` is the Keycloak **master console** login — *not* a user in the app's **Dev** realm, so it always fails.
Use the seeded Dev-realm user: **username `PlayWrightTest`, password `test`** (capital P/W/T). Or click **Register** (self-registration is on).

**3. `Uncaught TypeError: crypto.randomUUID is not a function` → Create-Election wizard does nothing.**
`crypto.randomUUID()` (and most Web Crypto) is only exposed in a **secure context**: HTTPS, or `http://localhost` / `127.0.0.1`. Viewing the Docker stack at **`http://web:5000`** (plain HTTP, non-localhost host) is *insecure* → the API is missing → the wizard's `onClick` throws → nothing happens (and **no** network request fires — the tell is an empty Network tab + a red Console error).
Fix: use the **dev flow** at `http://localhost:3000` (secure). Quick alt if you must use the Docker stack: `chrome://flags/#unsafely-treat-insecure-origin-as-secure` → add `http://web:5000` → relaunch.
Not a bug and nothing to do with any code change — production (HTTPS) and localhost work fine.

**4. `Module not found: Can't resolve '@equal-vote/star-vote-shared/utils/exportFormat'`.**
The frontend/backend import `@equal-vote/star-vote-shared` from its **compiled `dist/`**, not its source. If you add/edit a file under `packages/shared/`, `dist/` is stale until you rebuild.
Fix: `npm run build -w @equal-vote/star-vote-shared`, then restart the dev server. (Docker doesn't hit this because it builds everything fresh.)

**5. `npm error … Could not read package.json` (ENOENT at `/Users/amasa/package.json`).**
You ran `npm run … -w …` from your **home dir**, not the repo. Every workspace command must run from the repo root. `cd` in first.

**6. `node: command not found` in a fresh terminal.**
node@20 is keg-only. `fish_add_path /usr/local/opt/node@20/bin`.

**7. `EADDRINUSE :5001`** — a stray backend `tsx watch` is still running. `pkill -f "tsx watch"` (keep only one backend terminal).

---

## Quick reference

- **Repo:** `/Volumes/T7/Voting/BetterVoting/BV/bettervoting`
- **Dev URLs:** frontend `localhost:3000` · backend `localhost:5001` · keycloak `localhost:8080` · postgres `localhost:5432`
- **Dev-realm login:** `PlayWrightTest` / `test`
- **Env files (don't overwrite from sample.env):** `packages/backend/.env` → `BACKEND_PORT=5001`; `packages/frontend/.env` → `REACT_APP_BACKEND_URL=http://localhost:5001`
- **`__META_TITLE__` placeholder** in the browser tab under the dev flow is normal — meta-tag injection only runs in the backend-served build, not the RSBuild dev server.

Contribution/PR flow (fork → PR, "when is Docker needed"): see [contributing_to_bettervoting.md](contributing_to_bettervoting.md). The repo's own `DEV_START.md` has the canonical dev-server steps.
