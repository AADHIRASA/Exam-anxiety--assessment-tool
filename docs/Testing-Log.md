# Testing Log

## Approach

Testing was done manually throughout development, by submitting the form with different answer combinations and checking the result against the expected scoring band, rather than through automated tests (outside the scope of CS50x). Each test below was run on the live, deployed version.

## Scoring Band Tests

| Test | Selected Options (q1-q5) | Expected Average | Expected Band | Result |
|---|---|---|---|---|
| Lowest possible score | 1, 1, 1, 1, 1 | 1.0 | Low anxiety | Pass |
| Boundary: top of Low | 2, 2, 2, 3, 2 | 2.2 | Low anxiety | Pass |
| Boundary: start of Moderate | 2, 3, 2, 3, 2 | 2.4 | Moderate anxiety | Pass |
| Mid-range Moderate | 3, 3, 4, 3, 3 | 3.2 | Moderate anxiety | Pass |
| Boundary: start of High | 4, 4, 4, 4, 3 | 3.8 | High anxiety | Pass |
| Highest possible score | 5, 5, 5, 5, 5 | 5.0 | High anxiety | Pass |

## Database and Count Tests

- Verified each submission creates exactly one new row in the `responses` table, checked directly with `SELECT * FROM responses;` in the SQLite command line.
- Verified the displayed user count matches `SELECT COUNT(*) FROM responses;` after multiple submissions.
- Confirmed a normal page visit (no submission) does not insert a row, and does not error, by checking the count stays the same after simply refreshing without submitting.

## Bugs Found During Testing

| Bug | How It Was Found | Fix |
|---|---|---|
| Form submitted as GET instead of POST | Checked Flask's terminal request log after clicking Submit; saw GET instead of POST | Found a missing opening `<` on the `<form>` tag, breaking it entirely |
| 405 Method Not Allowed | Same terminal log check, after fixing the form tag | `app.py` route was missing `methods=["GET", "POST"]` |
| 500 error on live deployment | Checked PythonAnywhere's error log, found `sqlite3.OperationalError` | Working directory did not match source code directory on the server |
| Homepage missing heading/disclaimer on live site | Visual check after deployment — page loaded but looked incomplete | Restored missing HTML directly; later confirmed local copy was already correct |
| CSS not applying after styling was added | Visual check — page loaded correctly but with no colour or layout changes | Traced with `find` to discover `style.css` had been created as a folder, not a file; corrected the path with `mv` |

## Cross-Environment Check

Confirmed the app behaves the same way in both environments: the development Codespace (local testing) and the live PythonAnywhere deployment (public link). Each environment has its own separate database, so submission counts differ between them by design — this was verified rather than assumed.
