from flask import abort, render_template, send_file, request
from jinja2 import TemplateNotFound
from markupsafe import escape

from . import app_bp

# Send Home page
@app_bp.route('/')
def getIndexPage():
    session = request.cookies.get('session')
    if session:
        return render_template("chat.html")
    return render_template("index.html")

# 404 error handler
@app_bp.errorhandler(404)
def pageNotFound(err):
    _ = err
    return render_template('404.html'), 404

# Send Favicon
@app_bp.route('/favicon.ico')
def getFavIcon():
    return send_file('../static/assets/favicon.ico', as_attachment=False)


# Route users
@app_bp.route('/users/<name>')
def getUsersPage(name):
    try:
        return render_template(f'users/{escape(name)}.html')
    except TemplateNotFound:
        abort(404)

