from flask import *
import random
import Backend.Server

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def Index():
    SessionID = request.cookies.get("SessionID")
    if SessionID:
        UserID = None
        return redirect("/App")
    return render_template("Landing.html")

@app.route("/App", methods=["GET", "POST"])
def App():
    pass