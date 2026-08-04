# Exam Anxiety Assessment — README

## About This Project

Exam Anxiety Assessment is an educational self-reflection web tool built with Flask, SQLite, HTML, and Jinja. Users answer 5 questions about their exam-related anxiety by selecting an option from 1 to 5, and receive an average score along with educational feedback based on that score. The tool also displays a running count of how many people have used it.

**This is an educational self-reflection tool, not a medical or psychological diagnostic instrument. Results are for personal awareness only and are not a substitute for professional advice.**

## The 5 Questions

1. How often do you feel anxious before an exam?
2. How often have you forgotten your answers due to exam anxiety?
3. How often do you have trouble sleeping before exams?
4. How often have you lost confidence due to exam anxiety?
5. How often has anxiety affected your studies before exams?

Each question is answered by selecting one option from a fixed scale of 1 (never) to 5 (always).

## Scoring

The average of all 5 selected values is calculated and mapped to one of three feedback bands:

- 1.0 – 2.3: Low anxiety
- 2.4 – 3.6: Moderate anxiety
- 3.7 – 5.0: High anxiety

## Technology Used

- Python and Flask — the web application and routing
- SQLite — storing each submission and counting total users
- HTML and Jinja — the page structure and dynamic content
- CSS — a custom terracotta colour theme (`static/style.css`)
- Git and GitHub — version control, developed directly via GitHub Codespaces

## How to Run This Project

1. Open the repository in a GitHub Codespace.
2. Install Flask if not already installed: `pip install flask`
3. Run the app: `python3 -m flask --app app run --debug`
4. Open the forwarded port (5000) in the browser via the Ports tab.

## Live Deployment

**https://aadhirasa.pythonanywhere.com**

See `docs/Deployment-Guide.md` for full deployment details.

## Project Status

Core functionality is complete: the form collects answers, saves them to a database, calculates a score, displays feedback, and shows a live user count. The app is styled and deployed to a public link.

## Background

Built after completing Harvard's CS50x, as a personal project to apply what was learned.
