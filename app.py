from flask import Flask,render_template, request
import sqlite3
app= Flask(__name__)
@app.route("/", methods=["GET" ,"POST"])
def index ():
    db= sqlite3. connect("anxiety.db")
    result=None
    feedback=None
    if request.method == "POST":
        q1=request.form.get("q1")
        q2=request.form.get("q2")
        q3=request.form.get("q3")
        q4=request.form.get("q4")
        q5=request.form.get("q5")
        db.execute("INSERT INTO responses(q1,q2,q3,q4,q5) VALUES (?,?,?,?,?)",(q1,q2,q3,q4,q5))
        db.commit()
        average=(int(q1) + int(q2) + int(q3) + int(q4) + int(q5))/5
        result=round(average,1)
        if result <=2.3:
            feedback="you response suggest exam anxiety is not a major factor for you."
        elif result <=3.6:
            feedback="you exam anxiety level is moderate,suggested structured planning or taking a small break."
        else:
            feedback="you exam stress is more.suggested talking to your mentor,teacher,family or friends."

    count=db.execute("SELECT COUNT(*) FROM RESPONSES").fetchone()[0]
    db.close()
    return render_template("index.html", user_count=count,result=result,feedback=feedback)
