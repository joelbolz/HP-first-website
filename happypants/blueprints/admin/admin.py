from flask import Blueprint, render_template
from models import User

bp = Blueprint("admin", __name__, url_prefix="/admin", static_folder="static", template_folder="templates")


@bp.route("/dashboard")
def admin_dashboard():
    user_data = User.query.all()
    print(user_data[0])
    return render_template("admin_dashboard.html", user_data=user_data, content_type="admin")
