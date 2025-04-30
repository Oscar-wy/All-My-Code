from flask import *
import random
import Backend.Server

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def Index():
    return render_template("Landing.html")