from server.routes.util import sendError
from . import app_bp
from server.models import User
from flask import request, jsonify

def getUserContactList(user: User)->list[User]:
    "Get User contact list from database"
    pass

@app_bp.route('/api/contact', methods=['POST'])
def handleContactListAPI():
    "Return contact lists of username in JSON format"

    request_data = request.get_json()
    request_username = request_data["username"]
    request_session_id = request_data["session_id"]

    user:User = User.query.filter_by(username=request_username).first()

    if user:
    #     user_contacts:list[User] = getUserContactList(user)
    #     contact_list = []
    #
    #     for contact in user_contacts:
    #         contact_user:User = User.query.filter_by(username=contact.username).first()
    #
    #         contact_list.append({
    #             "username": contact_user.username,
    #             "is_active": contact_user.is_active,
    #             "display_name": contact_user.display_name,
    #             "last_seen_time": contact_user.last_seen_time,
    #             "is_last_message_seen": False, # TODO
    #             "last_message_sent": "Unknown" # TODO
    #         })
    #
    #     contact_list_api_data = {
    #         "username": user.username,
    #         "status": user.status,
    #         "display_name": user.display_name,
    #         "contacts": contact_list
    #     }
    #     return jsonify(contact_list_api_data) # return our data according to API
    #
    # else:
    #     return jsonify({"error": "User not found"}), 404

        contact_list_api_data = {
            "username": request_username,
            "status": user.status,
            "display_name": user.display_name,
            "contact": []
        }
        return jsonify(contact_list_api_data)
    return sendError("Unable to make this")


