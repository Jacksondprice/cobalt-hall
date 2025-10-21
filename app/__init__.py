from flask import Flask

from .config import Settings
from .routes import bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Settings())
    app.register_blueprint(bp)
    return app
