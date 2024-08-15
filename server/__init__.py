from flask import Flask, url_for
from .config import config
from .models import db
from .routes import app_bp


def createApp():
    app = Flask(__name__, template_folder="../templates", static_folder="../static/")
    app.json.sort_keys = False
    app.config.from_object(config["development"])  # or 'testing', 'production'

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(app_bp)
    return app
