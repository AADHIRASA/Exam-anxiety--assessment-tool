# Challenges and Problem-Solving

## Overview

Most of the work on this project wasn't writing new code — it was figuring out why something wasn't working and fixing it. Here are the main challenges faced and how each was solved.

## 1. Getting the Logic Right in Python

The scoring logic broke a few times because of how Python code is structured using indentation. Once this was understood properly, the scoring worked reliably.

## 2. A Git Merge Conflict

Editing code from two different places at once caused a real conflict in Git, where two versions of the same file didn't match. This was resolved by choosing the correct version and completing the merge properly — and led to a simple rule afterward: only edit code from one place.

## 3. Code Getting Overwritten

A couple of times, working code was accidentally replaced by an older or default version. Each time, it was recovered using Git's history, which keeps a record of every earlier version of the project.

## 4. A Server Error After Deployment

After putting the app online, it briefly stopped working with a server error. Checking the server's error log showed the real issue — a settings mismatch — which was fixed directly in the hosting configuration.

## 5. Choosing the Right Hosting Option

A couple of free hosting options were compared before deciding. One was more convenient but would have quietly lost saved data over time. The one chosen keeps data safe, at the small cost of a monthly check-in to keep it active.

## 6. File and Folder Mix-ups

While adding styling, a file got created in the wrong format (as a folder instead of a file), which quietly stopped the styling from working. This was fixed by locating the file properly and moving it to the right place.

## What This Showed

Almost every problem here came down to something small — a setting, a file location, a version mismatch — not a big design flaw. Learning to read error messages carefully and check the details rather than guess was the most useful skill that came out of this project.

## Future Improvements

- Show each person their own answers alongside their score, not just the final average.
- Add basic checks so a submission can't go through unless every question is answered.
- Track a person's responses over time, rather than only one-off submissions.
- Move to a hosting plan that doesn't need monthly maintenance, if this continues being used long-term.
