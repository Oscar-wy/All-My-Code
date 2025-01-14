from flask import *
import Server

app = Flask(__name__)
user = Server.User()
Server.InitialiseTables()

def CheckUser():
    SessionID = request.cookies.get("SessionID")
    if user.AssignUser(SessionID):
        return True
    return False

@app.route("/", methods=["GET", "POST"])
def Index():
    if CheckUser():
        return render_template("Home.html", Profile=user.ProfilePic)
    else:
        return redirect("/auth")

@app.route("/auth", methods=["GET", "POST"])
def Auth():
    if CheckUser():
        return redirect("/")
    return render_template("Auth.html", Profile=user.ProfilePic, ShowMain="Show", ShowSignup="Hidden", ShowLogin="Hidden", ShowDock="Hidden")

@app.route("/auth/signup", methods=["GET", "POST"])
def Signup():
    if CheckUser():
        return redirect("/")
    if request.method == "POST":
        if user.CreateUser(Username=request.form["Username"], FName=request.form["FName"], LName=request.form["LName"], Email=request.form["Email"], Password=request.form["SignPassword"]):
            resp = make_response(redirect("/"))
            resp.set_cookie("SessionID", user.SessionID)
            return resp
    return render_template("Auth.html", Profile=user.ProfilePic, ShowMain="Hidden", ShowSignup="Show", ShowLogin="Hidden", ShowDock="Hidden")

@app.route("/auth/login", methods=["GET", "POST"])
def Login():
    if CheckUser():
        return redirect("/")
    if request.method == "POST":
        if user.Login(UserEmail=request.form["UserEmail"], Password=request.form["Password"]):
            resp = make_response(redirect("/"))
            resp.set_cookie("SessionID", user.SessionID)
            return resp
    return render_template("Auth.html", Profile=user.ProfilePic, ShowMain="LogHidden", ShowSignup="Hidden", ShowLogin="Show", ShowDock="Hidden")

@app.route("/logout/<UUID>")
def Logout(UUID):
    CheckUser()
    if UUID == user.UUID:
        resp = make_response(redirect("/"))
        resp.delete_cookie('SessionID')
        return resp
    return redirect("/")

@app.route("/chat")
def Chat():
    if CheckUser():
        return render_template("Chat.html", Profile=user.ProfilePic, Username="", UserProfile=url_for('static', filename="PFP.png"))
    else:
        return redirect("/")
    
@app.route("/feed")
def Feed():
    if CheckUser():
        return redirect("/")
    else:
        return redirect("/")
    
@app.route("/profile")
def Profile():
    if CheckUser():
        return redirect("/")
    else:
        return redirect("/")

@app.errorhandler(404)
def pageNotFound(error):
    return render_template("PageNotFound.html", Error=error)