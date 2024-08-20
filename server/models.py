from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    username = db.Column(db.String(16), nullable=False, primary_key=True)
    display_name = db.Column(db.String(40), nullable=False)
    about = db.Column(db.String(100), nullable=False, default="")
    email = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    profile_pic = db.Column(db.String(16), nullable=False, default="profile.jpg")
    is_active = db.Column(db.Boolean, nullable=False, default=False)
    status = db.Column(db.String(16), nullable=False, default="Offline")
    last_seen_time = db.Column(db.String(16), nullable=True, default="Unknown")
    created_time = db.Column(db.DateTime, nullable=True, default=datetime.now())

    chats = db.relationship('Chat', backref='user', lazy=True)
    sessions = db.relationship('Session', backref='user', lazy=True)
    # blocks = db.relationship('BlockedUsers', backref='blocked', lazy=True)


class Chat(db.Model):
    chat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    primary_username = db.Column(db.String(80), nullable=False)
    secondary_username = db.Column(db.String(80), db.ForeignKey('user.username'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    last_message_sent = db.Column(db.String(120), nullable=True)
    is_last_message_seen = db.Column(db.Boolean, default=False)


class Session(db.Model):
    session_id = db.Column(db.String(16), primary_key=True, nullable=False)
    username = db.Column(db.String(16), db.ForeignKey('user.username'), nullable=False)
    ip_address = db.Column(db.String(45), nullable=True)
    device_info = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    last_accessed_at = db.Column(db.DateTime, default=datetime.now, nullable=False)


class Message(db.Model):
    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.chat_id'))
    sender_id = db.Column(db.String(16), db.ForeignKey('user.username'))
    content = db.Column(db.Text, nullable=False)
    message_type = db.Column(db.String(50), default='text')
    attachment_url = db.Column(db.Text, nullable=True)
    forwarded_from = db.Column(db.String(16), db.ForeignKey('user.username'), nullable=True)
    replied_to_message_id = db.Column(db.Integer, db.ForeignKey('message.message_id'), nullable=True)
    sent_at = db.Column(db.DateTime, default=datetime.now)
    edited_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)


# class BlockedUsers(db.Model):
#     blocker_id = db.Column(db.String(16), db.ForeignKey('user.username'), primary_key=True)
#     blocked_id = db.Column(db.String(16), db.ForeignKey('user.username'), primary_key=True)
#     blocked_at = db.Column(db.DateTime, default=datetime.now)

