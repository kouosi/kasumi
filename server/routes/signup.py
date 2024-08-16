from flask import request
from typing import Optional

from server.models import User, db
from .login import getNewSessionID
from .util import sendError, sendSuccess
from . import app_bp

def addNewUser(name: str, email: str, username: str, password_hash: str) -> Optional[User]:
    user = User(username=username, display_name=name, email=email, password_hash=password_hash)
    if user:
        db.session.add(user)
        db.session.commit()
        return user
    return None

@app_bp.route('/api/signup', methods=['POST'])
def handleSignupAPI():
    request_data = request.get_json()
    request_email = request_data["email"]
    request_name = request_data["name"]
    request_username = request_data["username"]
    request_password_hash = request_data["password_hash"]

    if User.query.filter_by(email=request_email).first():
        return sendError("Email Address already used")

    if User.query.filter_by(username=request_username).first():
        return sendError("Username unavailable")

    new_user:Optional[User] = addNewUser(request_name, request_email, request_username, request_password_hash)
    if new_user:
        session_id = getNewSessionID(new_user)
        new_response = sendSuccess({"message": "Sign up completed"})
        new_response.set_cookie("session", session_id)
        new_response.set_cookie("username", request_username)
        return new_response

    return sendError("Unable to create account. Please try again", 401)
