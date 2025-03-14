from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def form():
    if request.method=="POST":
        data={
        "name":request.form.get("name"),
        "email":request.form.get("email"),
        "phone":request.form.get("phone"),
        "dob":request.form.get("dob"),
        "address":request.form.get("address"),
        "gender":request.form.get("gender"),
        "state":request.form.get("state"),
        "district":request.form.get("district"),
        "id_proof":request.form.get("id_proof"),
        "file":request.files.get("file").filename if request.files.get("file") else "No file uploaded",
        "agree":request.form.get('agree','NO')
        }
        return render_template("14mar home result.html",data=data)
    return render_template("14 mar home.html")
if __name__=="__main__":
    app.run(debug=True)