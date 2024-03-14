from flask import Blueprint
from forms import CreateGroupchatForm, JoinGroupchatForm, ChatMessageForm, flash_errors
from models import Chatroom, User, Message
from db import db
from sio import socketio
from flask_socketio import leave_room, join_room, send
from flask import render_template, redirect, url_for
from flask_login import current_user, login_required
bp = Blueprint("chat", __name__, url_prefix="/chat", static_folder="static", template_folder="templates")


@bp.route("/", methods=["POST", "GET"])
def chat_home():
    send_form = ChatMessageForm()

    create_form = CreateGroupchatForm()
    join_form = JoinGroupchatForm()


    if create_form.create_submit.data and create_form.validate():
        new_chatroom = Chatroom(name=create_form.name.data)
        new_chatroom.users.append(current_user)
        db.session.add(new_chatroom)
        db.session.commit()
        return redirect("#")
    
    if join_form.join_submit.data and join_form.validate():
        room = Chatroom.query.filter_by(id=int(join_form.id.data)).first()
        room.users.append(current_user)
        db.session.commit()
        return redirect("#")

    groups=current_user.chatrooms
    flash_errors(join_form)
    return render_template("chat_home.html", groups=groups, create_form=create_form, join_form=join_form, send_form=send_form, content_type="chat")




@socketio.on("connect")
def connect(auth):
    for room in User.query.filter_by(username=current_user.username).first().chatrooms:
        join_room(room.id)

@socketio.on("message")
def message(data):
    room = Chatroom.query.filter_by(id=int(data["origin_room"])).first()
    new_msg = Message(content=data["data"])
    room.messages.append(new_msg)
    content = {"message": data["data"], "origin_room": data["origin_room"]}

    print(data["origin_room"])
    send(content, to=int(data["origin_room"]))

