from flask import render_template, Blueprint

bp = Blueprint('home_page', __name__)

@bp.route("/")
def home():
    print(3)
    return render_template("home_page.html", name=None)