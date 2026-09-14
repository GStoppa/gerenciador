from flask import Blueprint, render_template, redirect, session, request, url_for
from app.models.tarefa import Tarefa

#Inicializao do Blueprint
tarefasbp = Blueprint("tarefas", __name__)

@tarefasbp.route('/')
def index():
    dados_sessao = session.get("tarefas", [])
    #traformar o dicionario em objetos
    lista_objetos = []
    for item in dados_sessao:
        objeto = Tarefa.from_dict(item)
        lista_objetos.append(objeto)

    return render_template("base.html", tarefas=lista_objetos)

@tarefasbp.route('/criar-tarefa', methods=['GET', 'POST'])
def criar_tarefa():
    if request.method == 'POST':
        descricao = request.form.get("descricao")

        if descricao:
            #Pegar a lista de tarefas criada na sessao
            tarefas = session.get("tarefas", [])
            #len serve para retornar o número de itens de uma lista
            novo_id = len(tarefas) + 1
            nova_tarefa = Tarefa(novo_id, descricao)

            #guardando a tarefa na sessao
            tarefas.append(nova_tarefa.para_dict())
            session["tarefas"] = tarefas

        return redirect(url_for("tarefas.index"))

    return render_template('criar.html')

