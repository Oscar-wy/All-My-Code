from flask import Flask, url_for, request, render_template, redirect, make_response
from markupsafe import escape
import Handler

app = Flask(__name__)
global user
user = Handler.User()
Handler.Initialise()

@app.route("/")
def Index():
    try:
        userID = request.cookies.get("UUID")
        if userID:
            user.GetUser(userID)
            if user.Got:
                return render_template("Main.html")
            else:
                return redirect("/login")
        else:
            return redirect("/signup")
    except:
        return render_template("Error.html")
# def Home():

@app.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        return "Logging In"
    else:
        return "Hello"
    
@app.route("/signup", methods=["GET", "POST"])
def Signup():
    if request.method == "POST":
        try:
            if user.CreateUser(Username=request.form["Username"], FName=request.form["FName"], LName=request.form["LName"], Email=request.form["Email"], Password=request.form["Password"]):
                resp = make_response(redirect("/"))
                resp.set_cookie("UUID", str(user.UUID))
                return resp
            else:
                return redirect("/signup", Error="Username Already Exists")
        except Exception as err:
            return render_template("Error.html", Error=err)
    else:
        return render_template("SignUp.html")
    
@app.route("/user/@<username>")
def Profile(username):
    return f"{username}\'s profile"

@app.errorhandler(404)
def pageNotFound(error):
    return render_template("PageNotFound.html")