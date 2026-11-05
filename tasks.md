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

---

## Backlog

- [ ] **Evaluate open-licensed fonts for the scoresheet** {#ofl-fonts} — the
      sheet sets its text in Helvetica Neue and its vulnerability markers in
      Menlo, both macOS system fonts, so a macOS update can shift `latest.pdf`,
      as macOS 27 did. Try fonts under the SIL Open Font License (OFL) that keep
      the sheet's fit and legibility, and compare printouts at the table.
  - Note: the current fonts are fine to keep meanwhile. Both allow unrestricted
    embedding, which macOS's license requires before a system font may be
    embedded in a distributed document, and the repo only ever carries their
    subsets inside `latest.pdf`.
  - Note: candidates to start from — Liberation Sans, which matches classic
    Helvetica's character widths (within 0.3% of Helvetica Neue's on a sample
    line); Source Sans 3, which the sibling `bridge` repo already carries; and
    IBM Plex Mono or Liberation Mono for the markers. `bridge`'s
    `fonts/README.md` has the checklist for adopting an OFL font.
