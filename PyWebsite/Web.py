from flask import Flask, url_for, request, render_template, redirect, make_response
from markupsafe import escape
import Handler

app = Flask(__name__)
global user
user = Handler.User()
Handler.Initialise()

@app.route("/", methods=["GET", "POST"])
def Index():
    SessionID = request.cookies.get("SessionID")
    print(SessionID)
    if SessionID:
        UserID = user.GetUserIDFromSession(SessionID)
        user.GetUser(UserID)
        if user.Got:
            if request.method == "POST":
                print(request.form["Logout"])
                if request.form["Logout"] == "True":
                    if request.cookies.get('SessionID'):
                        resp = make_response(redirect("/"))
                        resp.set_cookie('SessionID', expires=0)
                        return resp
            return render_template("Index.html")
        else:
            return redirect("/login")
    else:
        return redirect("/signup")
# def Home():

@app.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        if user.Login(Username=request.form["UserEmail"], Password=request.form["Password"]):
            resp = make_response(redirect("/"))
            resp.set_cookie("SessionID", str(user.SessionID))
    else:
        return render_template("Login.html")
    
@app.route("/signup", methods=["GET", "POST"])
def Signup(Error=None):
    if request.method == "POST":
        if user.CreateUser(Username=request.form["Username"], FName=request.form["FName"], LName=request.form["LName"], Email=request.form["Email"], Password=request.form["Password"]):
            resp = make_response(redirect("/"))
            resp.set_cookie("SessionID", str(user.SessionID))
            return resp
        else:
            return redirect("/signup", Error="Username Already Exists")
    else:
        return render_template("SignUp.html")
    
@app.route("/user/@<username>")
def Profile(username):
    return f"{username}\'s profile"

@app.errorhandler(404)
def pageNotFound(error):
    return render_template("PageNotFound.html")