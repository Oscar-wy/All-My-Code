from flask import *
import random
import Backend.Server as Server

app = Flask(__name__)

# user = Server.User()

# def CheckUser():
#     SessionID = request.cookies.get("SessionID")
#     if user.AssignUser(SessionID):
#         return True
#     return False

account = False

@app.route("/", methods=["GET", "POST"])
def Index():
    if account:
        #return redirect("/App")
        return render_template("Landing.html", HasAccount="", NoAccount="Hidden")
    return render_template("Landing.html", HasAccount="Hidden", NoAccount="")

@app.route("/App", methods=["GET", "POST"])
def App():
    pass

if __name__ == "__main__":
    app.run(debug=True)