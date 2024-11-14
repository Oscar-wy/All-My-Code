from flask import Flask, url_for
from markupsafe import escape
import Handler as Handler

app = Flask(__name__)
user = None

@app.route("/")
def Home(user):
    if user:
        return "<p>Home<p>"
    else:
        url_for("Login")

@app.route("/login")
def Login():
    pass