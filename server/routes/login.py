from server.models import User
from flask import request, jsonify

from . import app_bp
from .util import sendError, sendSuccess


def getNewSessionID(user: User) -> str:
    return "test"

@app_bp.route('/api/login', methods=['POST'])
def handleLoginAPI():
    "Return new session_id for username"

    request_data = request.get_json()
    request_email = request_data["email"]
    request_password_hash = request_data["password_hash"]

    user:User = User.query.filter_by(email=request_email).first()
    if user:
        if user.password_hash == request_password_hash:
            session_id = getNewSessionID(user)
            new_response = sendSuccess({"message": "Sign up completed"})
            new_response.set_cookie("session", session_id)
            new_response.set_cookie("username", user.username)
            return new_response
        else:
            return sendError("Incorrect Password")

    else:
       return sendError("No user found with matching email", 401)
