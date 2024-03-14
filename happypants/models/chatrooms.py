from db import db
from sqlalchemy.sql import func

class Chatroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    messages = db.relationship("Message", backref="chatroom")


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    chatroom_id = db.Column(db.Integer, db.ForeignKey("chatroom.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
