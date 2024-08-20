from flask import Blueprint

app_bp = Blueprint("app", __name__)

from server.routes import contact, website, login, signup, newmsg, search #, message
