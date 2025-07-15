from flask import *
import os
import random
import Backend.Server as Server
from flask_socketio import SocketIO, emit

Server.InitialiseTables()

app = Flask(__name__)
app.secret_key = "3c841f496de2c2b9fa5d197d7b5c2f44"

# user = Server.User()

def getUser():
    sessionID = session.get('sessionID')
    if not sessionID:
        return None
    user = Server.User()
    user.fetchUserData(sessionID)
    return user

# def CheckUser():
#     SessionID = request.cookies.get("SessionID")
#     if user.AssignUser(SessionID):
#         return True
#     return False

@app.route("/landing", methods=["GET", "POST"])
def Index():
    if 'sessionID' in session:
        return redirect("/")
    return render_template("Landing.html", HasAccount="Hidden", NoAccount="")

@app.route("/", methods=["GET", "POST"])
def App():
    if 'sessionID' not in session:
        return redirect("/landing")

    user = getUser()

    if user:
        return render_template("App.html", NID=user.NID)
    else:
        return "User not found."
    
@app.route("/auth", methods=["GET", "POST"])
def auth():
    if 'sessionID' in session:
        return redirect("/")
    if request.method == "POST":
        # Handle login
        if 'login' in request.form:
            username = request.form['username']
            password = request.form['password']
            user = Server.User()

            if user.Login(username, password):
                session['sessionID'] = user.SessionID
                return redirect("/")
            else:
                error_message = "Invalid username or password. Please try again."
                return render_template("Auth.html", error_message=error_message, login=True)

        # Handle sign-up
        elif 'signup' in request.form:
            username = request.form['username']
            password = request.form['password']
            fname = request.form['fname']
            lname = request.form['lname']
            email = request.form['email']

            user = Server.User()

            if user.Register(username, password, fname, lname, email):
                success_message = "Account created successfully. You can now log in."
                return render_template("Auth.html", success_message=success_message, login=True)
            else:
                error_message = "Username already exists. Please choose another."
                return render_template("Auth.html", error_message=error_message, login=False)
            
    form_type = request.args.get('signup')
    if form_type == 'true':
        return render_template("Auth.html", login=False)  # Show sign-up form
    return render_template("Auth.html", login=True)

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if 'sessionID' not in session:
        return redirect("/landing")
    user = getUser()
    NID = request.args.get("NID")
    if not user:
        return redirect("/landing")
    if NID:
        userProfile = user.getProfileFromNID(int(NID))
        if user.NID != int(NID):
            relationStatus = user.getUserRelations(int(NID))
        else:
            relationStatus = "Own Profile"
            print("Own Profile?")
        if isinstance(relationStatus, tuple):
            status, requesterID = relationStatus
        else:
            status = relationStatus
            requesterID = None
        if userProfile != "No User Found":
            return render_template("Profile.html", UserName=userProfile[0], FName=userProfile[1], LName=userProfile[2], Connection=status, NID=int(NID), requesterID=requesterID)
    return "User not found", 404

@app.route("/sendRequest<int:targetNID>", methods=["POST"])
def sendRequest(targetNID):
    user = getUser()
    if not user:
        return redirect("/landing")
    if user.NID == targetNID:
        return "You cannot friend Yourself", 400
    user.sendRequest(targetNID)
    return redirect(f"/profile?NID={targetNID}")

@app.route("/cancelRequest<int:targetNID>", methods=["POST"])
def cancelRequest(targetNID):
    user = getUser()
    if not user:
        return redirect("/landing")

    user.cancelRequest(targetNID)
    return redirect(f"/profile?NID={targetNID}")

@app.route("/acceptRequest<int:requesterNID>", methods=["POST"])
def acceptRequest(requesterNID):
    user = getUser()
    if not user:
        return redirect("/landing")

    user.acceptRequest(requesterNID)
    return redirect(f"/profile?NID={requesterNID}")

@app.route("/declineRequest<int:requesterNID>", methods=["POST"])
def declineRequest(requesterNID):
    user = getUser()
    if not user:
        return redirect("/landing")

    user.declineRequest(requesterNID)
    return redirect(f"/profile?NID={requesterNID}")

@app.route("/unfriend<int:targetNID>", methods=["POST"])
def unfriend(targetNID):
    user = getUser()
    if not user:
        return redirect("/landing")

    user.unfriend(targetNID)
    return redirect(f"/profile?NID={targetNID}")

    
@app.route("/logout", methods=["GET"])
def logout():
    NID = request.args.get("NID")
    user = getUser()
    if str(NID) == str(user.NID):
        session.pop('sessionID', None)
        return redirect("/landing")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)