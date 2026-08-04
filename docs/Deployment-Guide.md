# Deployment Guide

## Live Link

**https://aadhirasa.pythonanywhere.com**

## Hosting Service Used

I used PythonAnywhere's free Beginner plan because it works really well with Python and Flask. Unlike some other free hosting websites it keeps the SQLite database even if the website gets paused. That was important because I wanted the number of submissions to keep increasing instead of getting reset.

## Deployment Steps

1. Made a free PythonAnywhere account.
2. Opened the Bash console and cloned my GitHub repository.

   ```
   git clone https://github.com/AADHIRASA/Exam-anxiety--assessment-tool.git
   ```
3. Checked that Flask was already installed.
4. Created a new Flask web app with Python 3.10 and linked it to my project's `app.py`.
5. Set the Working Directory to the same folder as the project so files like `anxiety.db` could be found properly.
6. Made the `responses` table again on the server because `anxiety.db` isn't on GitHub. It's in `.gitignore` so it doesn't get uploaded.
7. Reloaded the website and tested if everything was working.

## Problems I Ran Into

* PythonAnywhere replaced my `app.py` with its own Hello World file when I first made the web app. I fixed it by running `git checkout -- app.py` to get my file back.

* The deployed website was missing the heading and disclaimer because the `index.html` file wasn't fully updated. I fixed it by adding the missing HTML back using the PythonAnywhere editor.

* I got a 500 Internal Server Error because the Working Directory wasn't the same as the Source Code directory. The app was looking for the database in the wrong place. Once I changed the paths to match everything worked.

## Free Tier Limitation

The free PythonAnywhere plan needs me to log in once every month and click **"Run until 1 month from today"**. If I don't do that the website gets paused. They send an email reminder before it happens. The good thing is none of the data gets deleted. The database stays the same and starts working again once I reactivate the website. I also keep a monthly reminder so I don't forget.

## Data Storage

The database on the website is separate from the one in my GitHub Codespace. Any responses from the live website stay on PythonAnywhere and don't affect the local database I use while developing.

## Keeping the Codespace and the Live Site in Sync

The Codespace and the live website are two separate copies of the project. If I change something in the Codespace it won't automatically show up on the website.

To update the live website I do three things:

1. Push the changes from the Codespace to GitHub.
2. Open a Bash console in PythonAnywhere and run `git pull`.
3. Go to the Web tab and click **Reload**.

If I skip one of these steps the website keeps showing the old version. I found this out while working on the project because one of my fixes didn't show up until I pulled the changes and reloaded the website.

I used the same steps later when I changed the website design and added a custom colour theme. It worked the same way and updated the live website without any problems.
