from flask import request, jsonify
from typing import Optional

from server.models import User
from .login import getNewSessionID
from . import app_bp

def addNewUser(email: str, username: str, password_hash: str) -> Optional[User]:
    pass

@app_bp.route('/api/reset', methods=['GET'])
def handlePasswordReset():
    "Reset Password api"

    request_data = request.get_json()
    request_email = request_data["email"]
    request_username = request_data["username"]
    request_password_hash = request_data["password_hash"]

    if User.query.filter_by(email=request_email).first():
        return jsonify({"error": "Email Address already used"}), 404

    if User.query.filter_by(username=request_username).first():
        return jsonify({"error": "Username unavailable"}), 404

    new_user:Optional[User] = addNewUser(request_email, request_username, request_password_hash)
    if new_user:
        session_id = getNewSessionID(new_user)
        return jsonify({"session_id": session_id})

    return jsonify({"error": "Unable to create account. Please try again"}), 404

