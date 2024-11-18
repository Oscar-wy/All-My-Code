from flask import *
import Server

app = Flask(__name__)
user = Server.User()

def CheckUser():
    SessionID = request.cookies.get("SessionID")
    if user.Got:
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

@app.route("/auth/signup")
def Signup():
    if CheckUser():
        return redirect("/")
    return render_template("Auth.html", ShowMain="Hidden", ShowSignup="Show", ShowLogin="Hidden")

@app.route("/auth/login")
def Login():
    if CheckUser():
        return redirect("/")
    return render_template("Auth.html", ShowMain="LogHidden", ShowSignup="Hidden", ShowLogin="Show")

@app.errorhandler(404)
def pageNotFound(error):
    return render_template("PageNotFound.html", Error=error)