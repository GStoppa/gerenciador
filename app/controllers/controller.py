from flask import Blueprint, render_template, redirect

#Inicializao do Blueprint
tarefasbp = Blueprint('tarefas', __name__)

@tarefasbp.route('/')
def index():
    return render_template("index.html")