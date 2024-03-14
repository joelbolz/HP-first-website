from flask_login import UserMixin
from db import db

room_user = db.Table('room_user',
                    db.Column('chatroom_id', db.Integer, db.ForeignKey('chatroom.id')),
                    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
                    )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    chatrooms = db.relationship('Chatroom', secondary=room_user, backref='users')

