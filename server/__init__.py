from flask import Flask
from .routes import main_bp
from .models import db
from .test import test


def createApp():
    app = Flask(__name__, template_folder="../templates",
                static_folder="../static/")

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat_app.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()
        test()

    app.register_blueprint(main_bp)
    return app
