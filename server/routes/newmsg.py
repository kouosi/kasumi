from flask import request

from server.models import User, db, Chat
from server.session import isSessionValid
from .util import sendError, sendSuccess
from . import app_bp


@app_bp.route('/api/newmsg', methods=['POST'])
def handleNewMsgAPI():
    request_data = request.get_json()
    request_username = request_data["username"]
    request_new_username = request_data["new_username"]
    request_session_id = request_data["session_id"]

    user:User = User.query.filter_by(username=request_username).first()
    user1:User = User.query.filter_by(username=request_new_username).first()
    if not user:
        return sendError("Critical: Current User not found in server", to_home=True)
    if not user1:
        return sendError("User not found")

    if not isSessionValid(user.username, request_session_id):
        return sendError("Critical: Session ID Not valid", to_home=True)

    test1 = Chat.query.filter_by(primary_username=user.username, secondary_username=user1.username).first()
    test2 = Chat.query.filter_by(primary_username=user1.username, secondary_username=user.username).first()
    if test1 or test2:
        return sendSuccess({});

    contact = Chat(primary_username=user.username, secondary_username=user1.username,
                    last_message_sent="Implement", is_last_message_seen=True)

    if contact:
        db.session.add(contact)
        db.session.commit()
        return sendSuccess({});

    return sendError("Unable to make contact. Please try again")
