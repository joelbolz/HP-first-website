from flask import Blueprint, render_template

bp = Blueprint("general", __name__, static_folder="general/static", template_folder="templates")

@bp.route("/")
def home():
    return render_template("home.html")