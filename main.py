from flask import Flask, render_template, redirect, url_for, request
import db
app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

@app.route("/", methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)

        elif request.form['username'] == 'admin' or request.form['password'] == 'admin':
            print("Passou aqui2")
            return redirect(url_for('posts'))

    if request.method == 'GET':
        return render_template('login.html', error=error)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'GET':
        return render_template('registro.html')

    if request.method == 'POST':
        colunas = '"nome", "matricula", "curso", "admin", "senha"'
        valores = (request.form['nome'], request.form['matricula'], request.form['curso'], 'false', request.form['senha'])
        conexao = db.connect() 
        cursor = conexao.cursor()
        db.inserir(cursor, "estudantes", colunas, valores)

        # Commit modificações
        conexao.commit()

        # Retornar para página de login
        return redirect(url_for('login'))

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'GET':
        cursor = db.connect().cursor()
        avaliacoes = db.selectAll(cursor, "avaliacoes")
        return render_template('posts.html', avaliacoes = avaliacoes)

    if request.method == 'POST':
        print("Passou aqui")

@app.route('/denuncias', methods=['GET', 'POST'])
def denuncias():
    if request.method == 'GET':
        cursor = db.connect().cursor()
        avaliacoes = db.selectAll(cursor, "denuncias")
        return render_template('denuncias.html', avaliacoes = avaliacoes)

    if request.method == 'POST':
        pass


@app.route('/avaliacoes', methods=['GET'])
def avaliacoes():
    if request.method == 'GET':
        cursor = db.connect().cursor()
        avaliacoes = db.selectAll(cursor, "avaliacoes")
        return render_template('avaliacoes.html', avaliacoes = avaliacoes)

@app.route('/avaliar/<avaliado>', methods=['GET', 'POST'])
def avaliar(avaliado):
    if request.method == 'GET':
        print(avaliado)
        return render_template('avaliar.html', avaliado = avaliado)

    if request.method == 'POST':
        colunas = '"avaliacao", "avaliado", "nome", "comentario"'
        valores = (request.form['avaliacao'], avaliado.replace("'", "").strip('][').split(', ')[0], avaliado.replace("'", "").strip('][').split(', ')[1], request.form['comentario'])

        print("---------------------------------")
        print(colunas)
        print(valores)
        print(avaliado.strip('][').split(', '))
        print(type(avaliado.strip('][').split(', ')))
        print("---------------------------------")

        conexao = db.connect() 
        cursor = conexao.cursor()

        db.inserir(cursor, "avaliacoes", colunas, valores)

        # Commit modificações
        conexao.commit()

        return redirect(url_for('posts'))

@app.route('/departamentos', methods=['GET', 'POST'])
def departamentos():
    if request.method == 'GET':
        cursor = db.connect().cursor()
        departamentos = db.selectAll(cursor, "departamentos")
        return render_template('departamentos.html', departamentos = departamentos)

@app.route('/disciplinas', methods=['GET', 'POST'])
def disciplinas():
    if request.method == 'GET':
        cursor = db.connect().cursor()
        disciplinas = db.selectAll(cursor, "disciplinas")
        return render_template('disciplinas.html', disciplinas = disciplinas)

@app.route('/turmas', methods=['GET', 'POST'])
def turmas():
    if request.method == 'GET':
        cursor = db.connect().cursor()
        turmas = db.selectAll(cursor, "turmas")
        return render_template('turmas.html', turmas = turmas)

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)