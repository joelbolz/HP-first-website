import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile("config.py")
    
    # if test_config is provided, use that instead of default
    if test_config is  not None:
        app.config.from_mapping(test_config)

    # initialize database
    from happypants.db import db
    db.init_app(app)

    from happypants.encrypt import bcrypt
    bcrypt.init_app(app)

    from happypants.socketio import socketio
    socketio.init_app(app)

    from happypants.blueprints.auth.auth import login_manager
    login_manager.init_app(app)
    login_manager.login_view = "login"

    # register blueprints
    from happypants.blueprints import bps
    for bp in bps:
        app.register_blueprint(bp.bp)

    # a simple page that says hello
    @app.route("/dashboard")
    def dashboard():
        return "<h1>Wow du bist eingeloggt!</h1>"
    
    return app