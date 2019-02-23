import connexion

def create_app():
    app = connexion.FlaskApp(__name__)
    app.add_api('api.yaml')

    return app
