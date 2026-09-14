from flask import Blueprint, render_template, redirect
from app.models.tarefa import Tarefa

#Inicializao do Blueprint
tarefasbp = Blueprint('tarefas', __name__)

@tarefasbp.route('/')
def index():
    lista_tarefas = [
        Tarefa(1, "Estudar Flask"),
        Tarefa(2, "Praticar MVC", estado=True),
    ]
    return render_template("index.html", tarefas=lista_tarefas)