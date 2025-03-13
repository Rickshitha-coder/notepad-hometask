from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/", methods=["GET"])
def form():
    return render_template("12 mar home.html")
    
@app.route("/submit", methods=["POST"])
def submit():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        phone=request.form.get("phone")
        age=request.form.get("age")
        dob=request.form.get("dob")
        interview=request.form.get("interview")
        Years=request.form.get("Years")
        level=request.form.get("level")
        position=request.form.get("position")
        pos=request.form.get("pos")
        country=request.form.get("country")
        msg=request.form.get("msg")
        return f"""
        <h2 style="color:green;">Form Submitted Successfully!</h2>
        <p><b>Name:</b> {name} <br><br>
        <b>Email:</b>{email} <br><Br>
        <b>Contact:</b> {phone} <br><Br>
        <B>Age:</b> {age} <br><br>
        <b>Date of Birth:</b> {dob} <br><br>
        <b>Appointment Time:</b> {interview} <br><br>
        <b>Years of Experience:</b> {Years} <br><br>
        <b>Satisfaction Level:</b> {level} <br><Br>
        <b>Selected Position:</b> {pos} <br><Br>
        <b>Country:</b> {country} <br><BR>
        <b>Your Queries:</b> {msg} <br></p>"""
        
if __name__=="__main__":
    app.run(debug=True)