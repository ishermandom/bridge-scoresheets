# Tasks

Status key: `[ ]` not started · `[~]` in progress · `[x]` done · `[-]` dropped

---

## Recurring maintenance

**Goal:** keep what this repo depends on current, on a chosen cadence rather
than by surprise. Entries here never complete — a finished run leaves the task
in place for its next turn — so never prune them.

- [ ] **Refresh pinned dependencies** {#dependency-refresh} — about monthly, run
      `uv lock --upgrade && uv sync`, so everything this repo pins picks up
      improvements on a chosen schedule instead of drifting. `--dry-run`
      previews what would move, and the Stop checks report within one turn
      whether the new versions object to anything — read those before committing
      the lockfile.
  - Note: use `git log -1 --format=%as -- uv.lock` to determine when this last
    ran.
  - Note: a refresh that moves `playwright` can leave the shared browser install
    behind — the Python package expects a specific Chromium build and does not
    fetch it. Re-run the browser install from the README when `playwright`
    itself moves.
