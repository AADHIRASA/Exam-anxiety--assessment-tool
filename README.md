# Exam-anxiety--assessment-tool
Exam Anxiety Assessment — README

About This Project:

Exam Anxiety Assessment is an educational self analysis web tool built with Flask, SQLite, HTML, and Jinja. The users will answer 5 questions about their exam anxiety by selecting through 5 given options (On a scale of 1-5) and then they receive an average score along with feedback based on what to do according to their score. The tool also displays a count of the total amount of students who have used the website.

DISCLAIMER! 

This is purely an educational tool, not a medical or psychological test. Results are for personal knowledge only and cannot be used as a substitute for professional advice and help.

The questions asked: 
1. How often do you feel anxious before an exam
2. How often have you forgotten your answers due to exam anxiety
3. How often do you have trouble sleeping before exams
4. How often have you lost confidence due to exam anxiety
5. How often has anxiety affected your studies before exams

You can answer the question from a scale of 1 (Not really) to 5 (Absolutely)

Score system:

The average values from each input is taken and then classified into seperate ranges
- 1.0 – 2.3: Low anxiety
- 2.4 – 3.6: Moderate anxiety
- 3.7 – 5.0: High anxiety

I have used:

- Python and Flask — for web application and routing
- SQLite — storing each submission and counting total users
- HTML and Jinja — the page structure 
- CSS — a custom brownish colour theme (static/style.css)
- Git and GitHub — version control, developed directly through GitHub Codespaces

How do you Run This Project?

1. Open the repository in a GitHub Codespace.
2. Install Flask 
3. Run : python3 -m flask --app app run --debug
4. Open the forwarded port (5000) in the browser from the Ports tab.

Live Deployment
https://aadhirasa.pythonanywhere.com
See docs/Deployment-Guide.docx for complete details

Project Status Right now:

The main functionality is finished. The form collects answers, saves them to a database, calculates the score, shows feedback, and shows the user count. The app is customised and deployed to a public link.
Right now 135 students have used this tool.

Background
Built after completing CS50x (from Harvard), as a personal project to apply what was learned.
