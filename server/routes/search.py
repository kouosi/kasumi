from flask import request
from rapidfuzz import process

from server.models import User
from .util import sendSuccess
from . import app_bp


@app_bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower()

    users:list[User] = User.query.all()
    names = [user.display_name for user in users]
    results = process.extract(query, names, limit=10, score_cutoff=63)

    matched_items = []
    seen_ids = set()
    for name, score, _ in results:
        for user in users:
            if user.display_name == name and user.username not in seen_ids:
                matched_items.append({
                    'name': user.display_name,
                    'username': user.username,
                    'about': user.about,
                    'profile': user.profile_pic,
                    'score': score,
                })
                seen_ids.add(user.username)
    matched_items.sort(key=lambda x: x['score'], reverse=True)

    return sendSuccess({"users": matched_items})
