from flask import Blueprint, render_template, jsonify, request
from markupsafe import escape
from .models import User, Contact, Message

main_bp = Blueprint("main", __name__)

# Contact list API
@main_bp.route('/api/contact_list/<username>', methods=['GET'])
def getContactList(username: str):
    "Return contact lists of username in JSON format"

    user = User.query.filter_by(username=username).first()
    if user:
        contacts = Contact.query.filter_by(current_username=username).all()

        contact_list = [{
            "username": contact.username,
            "is_active": _usr.is_active,
            "name": _usr.name,
            "last_seen_time": _usr.last_seen_time,
            "is_last_message_seen": contact.is_last_message_seen,
            "last_message_sent": contact.last_message_sent
        } for contact in contacts if
            (_usr := User.query.filter_by(username=contact.username).first())]

        return jsonify({
            "username": user.username,
            "status": user.status,
            "name": user.name,
            "contact": contact_list
        })

    return jsonify({"error": "User not found"}), 404


# Chat message API
@main_bp.route('/api/chat_message/<username>/<username1>', methods=['GET'])
def getChatMessage(username: str, username1: str):
    "Return chat messages of username in JSON format"

    user = User.query.filter_by(username=username).first()
    msg = Message.query.filter_by(sender_username=username).all()

    if msg:
        messages = [{
            "username": message.sender_username,
            "message_id": message.message_id,
            "message": message.message,
        } for message in msg]

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


# Send message API
@main_bp.route('/api/send_message', methods=['POST'])
def sendMessage():
    data = request.json
    sender = data.get("username")
    recipient = data.get("recipient")
    message = data.get("message")

    if sender and recipient and message:
        new_message = {
            "username": sender,
            "message_id": str(len(messages.get(recipient, [])) + 1),
            "message": message
        }
        messages.setdefault(recipient, []).append(new_message)
        return jsonify({"status": "Message sent"}), 200
    return jsonify({"error": "Invalid data"}), 400

# Home page
@main_bp.route('/')
def getIndexPage():
    return render_template("chat.html")

@main_bp.route('/<name>')
def getNormalPage(name):
    return render_template(escape(name)+".html")
