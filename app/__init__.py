from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="views", static_folder='static')
    app.secret_key = 'sla_qualquer_coisa'

    #importar o Blueprint do controller
    from app.controllers.controller import tarefasbp
    #registra o blueprint do controller na aplicação
    app.register_blueprint(tarefasbp)

    return app