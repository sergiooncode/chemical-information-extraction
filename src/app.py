import os

from flask import Flask

from config import config, DEFAULT_CONFIG_NAME
from config.routes import api
from src.infrastructure.persistence.mongoengine.model import db


def create_app(config_name=os.getenv("ENVIRONMENT") or DEFAULT_CONFIG_NAME):
    """Initialize the core application."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    with app.app_context():
        # Show API swagger or not depending on env
        if config_name == DEFAULT_CONFIG_NAME:
            api.init_app(app)
        else:
            api.init_app(app, add_specs=False)

        db.init_app(app)

        # CLI commands
        from bin.cli import patents
        from bin.cli import documents
        from bin.cli import ner_entities

        app.register_blueprint(patents.patents_blueprint)
        app.register_blueprint(documents.documents_blueprint)
        app.register_blueprint(ner_entities.entities_blueprint)

    return app


app = create_app()
