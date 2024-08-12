from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    username = db.Column(db.String(80), primary_key=True, nullable=False)
    status = db.Column(db.String(16), nullable=False, default="Online")
    name = db.Column(db.String(120), nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    last_seen_time = db.Column(db.String(16), nullable=True, default="Unknown")
    contacts = db.relationship('Contact', backref='user', lazy=True)
    messages_sent = db.relationship('Message', backref='user', lazy=True)


class Contact(db.Model):
    username = db.Column(db.String(80), primary_key=True, nullable=False)
    current_username = db.Column(
        db.String(80), db.ForeignKey('user.username'), nullable=False)
    last_message_sent = db.Column(db.String(120), nullable=True)
    is_last_message_seen = db.Column(db.Boolean, default=False)


class Message(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    message_status = db.Column(db.Text, nullable=False, default="sent")
    sender_username = db.Column(db.String(80), nullable=False)
    receiver_username = db.Column(db.String(80), db.ForeignKey(
        "user.username"), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
