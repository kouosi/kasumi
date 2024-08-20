from server.routes.util import sendError, sendSuccess
from server.session import isSessionValid
from . import app_bp
from server.models import Session, User, Chat
from flask import request

def getUserContactList(username: str)->list[Chat]:
    "Get User contact list from database"
    return Chat.query.filter_by(primary_username=username).all()

@app_bp.route('/api/contact', methods=['POST'])
def handleContactListAPI():
    "Return contact lists of username in JSON format"

    request_data = request.get_json()
    request_username = request_data["username"]
    request_session_id = request_data["session_id"]

    if not request_username or not request_session_id:
        return sendError("Either username or session id is null")

    if not isSessionValid(request_username, request_session_id):
        return sendError("Session id invalid", to_home=True)

    user:User = User.query.filter_by(username=request_username).first()
    if user:
        user_contacts:list[Chat] = getUserContactList(request_username)
        contact_list = []

        print(user_contacts)

        for contact in user_contacts:
            contact_user:User = User.query.filter_by(username=contact.secondary_username).first()

            contact_list.append({
                "username": contact_user.username,
                "is_active": contact_user.is_active,
                "display_name": contact_user.display_name,
                "profile_pic": contact_user.profile_pic,
                "last_seen_time": contact_user.last_seen_time,
                "is_last_message_seen": False, # TODO
                "last_message_sent": "TODO" # TODO
            })

        contact_list_api_data = {
            "username": user.username,
            "status": user.status,
            "display_name": user.display_name,
            "profile_pic": user.profile_pic,
            "contact": contact_list
        }
        return sendSuccess(contact_list_api_data) # return our data according to API

    else:
        return sendError("User not found", to_home=True)
