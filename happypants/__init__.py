from flask import Flask
from flask_socketio import SocketIO
from sio import socketio
from os.path import exists, dirname, join


def create_app(test_config=None):
    # create and configure the app
    app="this function is used with flask run!" 
    return app






 # if test_config is provided, use that instead of default
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")
socketio.init_app(app)

# initialize database
from db import db
db.init_app(app)

from encrypt import bcrypt
bcrypt.init_app(app)


from blueprints.auth.auth import login_manager
login_manager.init_app(app)
login_manager.login_view = "login"

# register blueprints
from blueprints import bps
for bp in bps:
    app.register_blueprint(bp.bp)

# a simple page that says hello
@app.route("/dashboard")
def dashboard():
    return "<h1>Wow du bist eingeloggt!</h1>"
    

if not exists(join(dirname(__file__),"/instance/database.db")):
    from models import User, Chatroom, Message
    with app.app_context():
        db.create_all()

if __name__ == "__main__":

    socketio.run(app, debug=True)
