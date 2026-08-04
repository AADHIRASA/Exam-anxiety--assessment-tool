# Database Design!


# Why SQLite

I used SQLite because it was the easiest option. It doesn't need a server or any setup. The whole database is just one file called `anxiety.db` with the rest of the project. Since this project is pretty small it was more than enough. I had already used SQLite in CS50x for the Finance problem set so I already knew how it worked.

# The `responses` Table

I only needed one table to store all the submissions. Every row is one person's completed assessment.

**id** - INTEGER, PRIMARY KEY, AUTOINCREMENT. This gives every submission its own ID.

**q1** - INTEGER. Stores the answer to "How often do you feel anxious before an exam?" The answer is from 1 to 5.

**q2** - INTEGER. Stores the answer to "How often have you forgotten your answers due to exam anxiety?" The answer is from 1 to 5.

**q3** - INTEGER. Stores the answer to "How often do you have trouble sleeping before exams?" The answer is from 1 to 5.

**q4** - INTEGER. Stores the answer to "How often have you lost confidence due to exam anxiety?" The answer is from 1 to 5.

**q5** - INTEGER. Stores the answer to "How has anxiety affected your studies before exams?" The answer is from 1 to 5.

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

* **When someone submits the form:** I add the five answers into the database as one new row using an `INSERT` query. I use parameterized queries so people can't try SQL injection.

* **When someone opens the website:** I count how many rows are in the database using `SELECT COUNT(*)` and show that as the live "students have used this tool" count.

* I work out the average score in Python right after the form is submitted. I don't save it in the database because I can always work it out again from the answers.

## Why the Database File Isn't on GitHub

I don't keep `anxiety.db` on GitHub. It's in `.gitignore` because it changes every time someone submits the form. It isn't really part of the code anyway. If I uploaded it Git would keep tracking all those changes and the commits would just get messy. So my Codespace and the PythonAnywhere website both have their own `anxiety.db` file and each one stores its own submissions.

