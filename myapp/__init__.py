import connexion

app = connexion.FlaskApp(__name__)
app.add_api('my_api.yaml')

