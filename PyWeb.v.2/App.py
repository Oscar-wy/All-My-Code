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
        return render_template("Home.html")
    else:
        return redirect("/auth")

@app.route("/auth", methods=["GET", "POST"])
def Auth():
    if CheckUser():
        return redirect("/")
    return render_template("Auth.html", ShowMain="Show", ShowSignup="Hidden", ShowLogin="Hidden")

@app.route("/auth/signup", methods=["GET", "POST"])
def Signup():
    if CheckUser():
        return redirect("/")
    if request.method == "POST":
        if user.CreateUser(Username=request.form["Username"], FName=request.form["FName"], LName=request.form["LName"], Email=request.form["Email"], Password=request.form["SignPassword"]):
            resp = make_response(redirect("/"))
            resp.set_cookie("SessionID", user.SessionID)
            return resp
    return render_template("Auth.html", ShowMain="Hidden", ShowSignup="Show", ShowLogin="Hidden")

@app.route("/auth/login", methods=["GET", "POST"])
def Login():
    if CheckUser():
        return redirect("/")
    if request.method == "POST":
        if user.Login(UserEmail=request.form["UserEmail"], Password=request.form["Password"]):
            resp = make_response(redirect("/"))
            resp.set_cookie("SessionID", user.SessionID)
            return resp
    return render_template("Auth.html", ShowMain="LogHidden", ShowSignup="Hidden", ShowLogin="Show")

@app.route("/logout/<UUID>")
def Logout(UUID):
    CheckUser()
    print(UUID, "UserId: ", user.UUID)
    if UUID == user.UUID:
        resp = make_response(redirect("/"))
        resp.delete_cookie('SessionID')
        return resp
    return redirect("/")

@app.errorhandler(404)
def pageNotFound(error):
    return render_template("PageNotFound.html", Error=error)