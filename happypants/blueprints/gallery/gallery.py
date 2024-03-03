from flask import Blueprint
bp = Blueprint("gallery", __name__, url_prefix="/gallery", static_folder="static", template_folder="templates")
