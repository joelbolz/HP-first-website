from flask import Blueprint
bp = Blueprint("chat", __name__, url_prefix="/chat", static_folder="static", template_folder="templates")
