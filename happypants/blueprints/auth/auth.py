from flask import redirect, render_template, url_for, flash, Blueprint
from flask_login import login_user, LoginManager, login_required, logout_user
from happypants.models.users import User
from happypants.db import db
from happypants.encrypt import bcrypt
from .forms import SignupForm, LoginForm


bp = Blueprint("auth", __name__, url_prefix="/auth", static_folder="static", template_folder="templates")
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    
@bp.route("/login", methods=["POST","GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("dashboard"))
    return render_template("login.html", form=form)


@bp.route("/sign-up", methods=["POST", "GET"])
def sign_up():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    flash(form.errors)

    return render_template("signup.html", form=form)


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
