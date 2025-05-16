from flask import *
import random
import Backend.Server as Server

app = Flask(__name__)

Server.InitialiseTables()

# user = Server.User()

# def CheckUser():
#     SessionID = request.cookies.get("SessionID")
#     if user.AssignUser(SessionID):
#         return True
#     return False

@app.route("/", methods=["GET", "POST"])
def Index():
    if 'username' in session:
        return redirect("/App")
    return render_template("Landing.html", HasAccount="Hidden", NoAccount="")

@app.route("/App", methods=["GET", "POST"])
def App():
    if 'username' not in session:
        return redirect("/")

    username = session['username']
    user = Server.User()
    user_data = user.fetchUserData(username)
    
    if user_data:
        return render_template("App.html", user=user_data)
    else:
        return "User not found."
    
@app.route("/auth", methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        # Handle login
        if 'login' in request.form:
            username = request.form['username']
            password = request.form['password']
            user = Server.User()

            if user.Login(username, password):
                session['username'] = username
                return redirect("/App")
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
            
    return render_template("Auth.html", error_message=None, success_message=None, login=True)
    
@app.route("/logout", methods=["GET"])
def logout():
    session.pop('username', None)  # Remove session on logout
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)