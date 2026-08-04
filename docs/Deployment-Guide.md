# Deployment Guide

## Live Link

**https://aadhirasa.pythonanywhere.com**

## Hosting Service Used

PythonAnywhere (free "Beginner" tier) was chosen because it supports Python/Flask directly and, unlike some free alternatives, provides persistent storage — meaning the SQLite database (and the running user count) is preserved even when the site is temporarily paused. This mattered because the project relies on an accurate, growing count of real submissions over time.

## Deployment Steps

1. Created a free PythonAnywhere account.
2. Opened a Bash console and cloned the GitHub repository directly:
   ```
   git clone https://github.com/AADHIRASA/Exam-anxiety--assessment-tool.git
   ```
3. Confirmed Flask was already available in the environment.
4. Created a new web app via the Web tab, selecting Flask and Python 3.10, and pointed it to the cloned project's `app.py`.
5. Set the Working Directory to match the project's Source Code directory, so relative file paths (like the SQLite database) resolve correctly.
6. Recreated the SQLite `responses` table directly on the server, since the database file itself is excluded from Git via `.gitignore` (by design, since database files shouldn't be version-controlled).
7. Reloaded the web app and tested the live link.

## Problems Encountered and Fixes

- PythonAnywhere's setup wizard initially overwrote `app.py` with its own default "Hello World" template, since the wizard offers to generate a starter file at the chosen path. Fixed by running `git checkout -- app.py` to restore the committed version from the project's own Git history.
- The homepage template (`index.html`) on the deployed copy was missing its heading and disclaimer section (a leftover from an earlier, incomplete commit). Fixed by manually restoring the missing HTML directly in the PythonAnywhere file editor.
- A 500 Internal Server Error occurred because the app's Working Directory did not match its Source Code directory, causing it to look for the database in the wrong location. Fixed by aligning the two paths in the Web app configuration.

## Known Limitation: Free Tier Maintenance

PythonAnywhere's free tier requires logging in at least once a month and clicking "Run until 1 month from today" to keep the site active; otherwise it automatically pauses (PythonAnywhere sends an email reminder beforehand). Importantly, pausing does not delete any data — the SQLite database and all saved responses remain intact and are restored the moment the site is reactivated. A recurring monthly reminder is used to ensure the site stays available for ongoing and future reference.

## Data Persistence

The deployed database is separate from the local development database (used in the GitHub Codespace). Submissions made via the live public link accumulate independently on PythonAnywhere's server and are not affected by local development work.

## Keeping the Codespace and the Live Site in Sync

The Codespace and the live PythonAnywhere site are two separate copies of the project, not one shared thing. Editing code in the Codespace — changing colours, wording, anything — only changes that copy. It does not automatically appear on the live site.

The change actually reaches the live site in three steps:

1. Push the change from the Codespace to GitHub, as usual.
2. On PythonAnywhere, open a Bash console, move into the project folder, and run `git pull` to bring that update in.
3. Go to the Web tab and click **Reload** — this is the step that actually makes the live site use the new code.

Skipping any one of these three steps means the live site keeps showing the old version, even though the Codespace looks correct. This came up directly during development, when a fix made in the Codespace didn't show up on the live link until it was manually pulled and reloaded on PythonAnywhere.

This exact process was used again later to deploy an update to the page's design, including a custom colour theme. The same push, pull, and reload sequence deployed the change successfully, confirming the workflow holds for ongoing updates, not just the initial deployment.
