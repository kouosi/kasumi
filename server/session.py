import base64, os

from .models import User, Session, db
from flask import request

def getNewSessionID(user: User) -> str:
    random_bytes = os.urandom(16)
    session_id = base64.urlsafe_b64encode(random_bytes).rstrip(b'=').decode('utf-8')
    new_session = Session(session_id=session_id,
                          username=user.username,
                          ip_address=request.remote_addr,
                          device_info=request.headers.get('User-Agent')
                    )
    if new_session:
        db.session.add(new_session)
        db.session.commit()
    return session_id

def isSessionValid(username: str, session_id: str) -> bool:
    sessions:list = Session.query.filter_by(username=username, session_id=session_id).first();
    return True if sessions else False
