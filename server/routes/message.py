from . import app_bp
from server.models import User,
from flask import request, jsonify

def getUserContactList(user: User)->list[User]:
    "Get User contact list from database"
    pass

@app_bp.route('/api/message', methods=['GET'])
def handleMessageAPI():
    "Return chat messages of username in JSON format"

    request_data = request.get_json()
    request_primary_username = request_data["primary_username"]
    request_secondary_username = request_data["secondary_username"]
    # request_session_id = request_data["session_id"]

    user = User.query.filter_by(username=request_primary_username).first()
    msg = Message.query.filter_by(sender_username=request_secondary_username).all()

    if msg:
        messages = [{
            "username": message.sender_username,
            "message_id": message.message_id,
            "message": message.message,
        } for message in msg]
    else:
        messages = []

    if user:
        return jsonify({
            "username": user.username,
            "is_active": user.status,
            "name": user.name,
            "last_online_time": user.last_seen_time,
            # "last_seen_id": TODO:,
            "message": messages
        })
    return jsonify({"error": "No chat history found"}), 404
