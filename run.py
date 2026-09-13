from app import create_app

#executa a função do objeto central
app = create_app()

#Liga o servidor local e atualiza a cada save
if __name__ == '__main__':
    app.run(debug=True)