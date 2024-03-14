from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from models import User
from flask import flash
from custom_fields import ButtonField

def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(error,'error')


class SignupForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20), EqualTo("password_confirm", message="Passwords must match!")], render_kw={"placeholder": "Password"})
    password_confirm = PasswordField(validators=[InputRequired()], render_kw={"placeholder": "Confirm Password"})

    submit = SubmitField("Sign up")

    def validate_username(self, username):
        existing_user_name = User.query.filter_by(username=username.data).first()
        if existing_user_name:
            raise ValidationError("This username already exists, choose a different one!")


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Log in")

    def validate_username(self, username):
        existing_user_name = User.query.filter_by(username=username.data).first()
        if not existing_user_name:
            raise ValidationError("We couldn't find that username!")
        



class CreateGroupchatForm(FlaskForm):

    name = StringField(validators=[InputRequired()],
                        render_kw={"placeholder":"Name"})
    create_submit = SubmitField("CREATE ROOM")

class JoinGroupchatForm(FlaskForm):

    id = StringField(validators=[InputRequired()],
                        render_kw={"placeholder":"Name"})
    join_submit = SubmitField("JOIN ROOM")


class ChatMessageForm(FlaskForm):
    message = StringField(validators=[Length(max=100)], render_kw={"placeholder":"Message"}, id="message")
    button = ButtonField("SEND", name="send")
