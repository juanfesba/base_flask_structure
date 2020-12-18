from . import app
from flask import render_template


@app.route("/")
def home():
    return render_template("home_page.html", name=None)

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
            "hello_there.html",
            name=name
    )