import connexion

from . import utils

__all__ = ['utils']


def create_app():
    app = connexion.FlaskApp(__name__)
    app.add_api('api.yaml')

    return app
