from flask import Flask,render_template, request
import sqlite3
app= Flask(__name__)
@app.route("/", methods=["GET" ,"POST"])
def index ():
    db= sqlite3. connect("anxiety.db")
    if request.method == "POST":
        q1=request.form.get("q1")
        q2=request.form.get("q2")
        q3=request.form.get("q3")
        q4=request.form.get("q4")
        q5=request.form.get("q5")
        db.execute("INSERT INTO responses(q1,q2,q3,q4,q5) VALUES (?,?,?,?,?)",(q1,q2,q3,q4,q5))
        db.commit()
    count=db.execute("SELECT COUNT(*) FROM RESPONSES").fetchone()[0]
    db.close()
    return render_template("index.html", user_count=count)
    