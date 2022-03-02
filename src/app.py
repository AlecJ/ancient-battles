"""
Main app module.

Contains the app factory function.
"""
from src.util import config, loggingFactory
# import logging
# import sys

from flask import Flask
# from extensions import db, migrate
from src.api import api_blueprint


_getLogger = loggingFactory('app')
logger = _getLogger('__main__')

def create_app():  # config_object="settings"):
    app = Flask(__name__.split(".")[0])
    # Set config
    # app.config.from_object(config_object)
    # Register Blueprints
    app.register_blueprint(api_blueprint)
    # Register extensions
    # db.init_app(app)
    # migrate.init_app(app, db)

    # configure_logger(app)
    logger.info('Running environment: {}'.format(config.ENVIRONMENT))
    return app


# def configure_logger(app):
#     """Configure loggers."""
#     handler = logging.StreamHandler(sys.stdout)
#     if not app.logger.handlers:
#         app.logger.addHandler(handler)

# app = create_app()
