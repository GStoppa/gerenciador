from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="view", static_folder='static')

    app.secret_key = 'sla_qualquer_coisa'

    return app