from flask import Blueprint, render_template
from flask_login import current_user

bp = Blueprint("general", __name__, static_folder="general/static", template_folder="templates")

@bp.route("/")
def home():
    if current_user.is_authenticated:
        welcome_message = current_user.username
    else:
        welcome_message = "Welcome to happypants."
    return render_template("home.html", welcome_message=welcome_message)

@bp.route("/about-us")
def aboutus():
    return render_template("about-us.html")