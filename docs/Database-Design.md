# Database Design

## Why SQLite

SQLite was used because it requires no separate server or setup — the entire database lives in a single file (`anxiety.db`) alongside the rest of the project. This matches the project's scope (a small, single-purpose tool) and is the same database approach used throughout CS50x, particularly in the Finance problem set.

## The `responses` Table

A single table stores every submission. Each row represents one person's completed assessment.

| Column | Type | Purpose |
|---|---|---|
| id | INTEGER, PRIMARY KEY, AUTOINCREMENT | Uniquely identifies each submission |
| q1 | INTEGER | Answer to "How often do you feel anxious before an exam?" (1-5) |
| q2 | INTEGER | Answer to "How often have you forgotten your answers due to exam anxiety?" (1-5) |
| q3 | INTEGER | Answer to "How often do you have trouble sleeping before exams?" (1-5) |
| q4 | INTEGER | Answer to "How often have you lost confidence due to exam anxiety?" (1-5) |
| q5 | INTEGER | Answer to "How often has anxiety affected your studies before exams?" (1-5) |

## Table Creation Statement

```sql
CREATE TABLE responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    q1 INTEGER,
    q2 INTEGER,
    q3 INTEGER,
    q4 INTEGER,
    q5 INTEGER
);
```

## How the Database Is Used

- **On submission (POST request):** the five answer values are inserted as one new row using a parameterised query (`INSERT INTO responses (...) VALUES (?, ?, ?, ?, ?)`), which protects against SQL injection by never directly inserting raw user input into the query string.
- **On every page load:** the total number of rows is counted with `SELECT COUNT(*) FROM responses`, and displayed as the live "students have used this tool" count.
- The average score is calculated in Python from the five submitted values immediately after insertion, rather than being stored as its own column, since it can always be recalculated from the raw answers.

## Why the Database File Is Not on GitHub

`anxiety.db` is listed in `.gitignore` and is not committed to the repository. Database files change constantly and are not really "source code" — committing them would clutter the project's history with data changes instead of code changes. As a result, the database exists separately in each environment (the development Codespace and the live PythonAnywhere deployment), each accumulating its own submissions independently.
