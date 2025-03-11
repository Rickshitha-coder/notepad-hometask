from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/")
def form():
    return render_template("11 mar hometask.html")
@app.route("/submit", methods=["post"])
def submit():
    name=request.form.get("name")
    email=request.form.get("email")
    tech=request.form.get("Tech")
    commmuni=request.form.get("Communi")
    roll=request.form.get("roll")
    msg=request.form.get("msg")
    return f"<h2>Thank You {name}!</h2> Submitted From {email} And Roll No is {roll}"
if __name__=="__main__":
    app.run(debug=True)