# Testing Log

# Approach

I tested the website myself while I was making it. I tried different answer fixations and checked if the result matched the right scoring range. I didn't use automated tests because they weren't really needed for this project. Every test below was done on the live website.

# Scoring Range Tests

**Lowest possible score**

* Answers: 1, 1, 1, 1, 1
* Expected average: 1.0
* Expected result: Low anxiety
* Result: Pass

**Top of Low Range**

* Answers: 2, 2, 2, 3, 2
* Expected average: 2.2
* Expected result: Low anxiety
* Result: Pass

**Start of Moderate Range**

* Answers: 2, 3, 2, 3, 2
* Expected average: 2.4
* Expected result: Moderate anxiety
* Result: Pass

**Middle of Moderate Range**

* Answers: 3, 3, 4, 3, 3
* Expected average: 3.2
* Expected result: Moderate anxiety
* Result: Pass

**Start of High Range**

* Answers: 4, 4, 4, 4, 3
* Expected average: 3.8
* Expected result: High anxiety
* Result: Pass

**Highest possible score**

* Answers: 5, 5, 5, 5, 5
* Expected average: 5.0
* Expected result: High anxiety
* Result: Pass

## Database and Count Tests

* I checked that every submission added one new row to the `responses` table by using `SELECT * FROM responses;` in SQLite.

* I also checked that the student count on the website matched `SELECT COUNT(*) FROM responses;` after a few submissions.

* I checked that just opening or refreshing the page didn't add a new row. The count stayed the same after refreshing without submitting.

# Bugs I Found

**Form submitted as GET instead of POST**

I found this after checking Flask's terminal when I clicked Submit. It showed a GET request instead of POST. I had forgotten the opening `<` on the `<form>` tag. After I added it everything worked.

**405 Method Not Allowed**

After fixing the form I got a 405 error. I checked `app.py` and found I forgot to add `methods=["GET", "POST"]` to the route.

**500 Error on the Live Website**

I checked the PythonAnywhere error log and found a `sqlite3.OperationalError`. The Working Directory didn't match the Source Code directory so the app couldn't find the database. I fixed the paths and it worked.

**Homepage Missing the Heading and Disclaimer**

After I deployed the website I noticed the heading and disclaimer were missing. I added the missing HTML back in PythonAnywhere. Later I checked my local copy and it already had it.

**CSS Wasn't Working**

The page opened but the styling wasn't showing. I used `find` and found that `style.css` had been made as a folder instead of a file. I fixed it with `mv` and the CSS worked.

# Cross-Environment Check

I checked the project in both my Codespace and on the live PythonAnywhere website. Both worked the same. The only difference was the database because each one has its own `anxiety.db` file, so the number of submissions is different on each one.

