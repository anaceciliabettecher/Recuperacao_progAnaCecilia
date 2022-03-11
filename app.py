from config.Config import Config
from config.Database import Database
from dao.alunoDao import AlunoDao
from flask import Flask, request, render_template

from model.Aluno import Aluno, Aluno

app = Flask(__name__)

dao = AlunoDao(Database(Config().config).conn)

@app.route('/', methods=["GET"])
def iniciar():
       return render_template(
        "main.html"
    )

@app.route('/aluno/novo', methods=["GET", "POST"])
def novo():
    aluno = Aluno 
    return render_template("inserir.html")

@app.route('/aluno', methods=["POST"])
def inserir():
    aluno = Aluno()
    aluno.nome = request.form.get("nome")
    aluno.email = request.form.get("email")
    aluno.idade = int(request.form.get("idade")) 

    dao.inserirAluno(aluno)

    lista = dao.selecionarAluno()
    return render_template(
        "listagem.html",
        lista=lista
    )

@app.route('/aluno', methods=["GET"])
def listar():
    lista = dao.selecionarAluno()
    return render_template(
        "listagem.html",
        lista=lista
    )

@app.route('/aluno/<pid>', methods=["GET"])
def editarPagina(pid):
    aluno = dao.selecionarAluno(pid)
    return render_template("editar.html", aluno=aluno)

@app.route('/aluno/editar', methods=["POST"])
def editar():

    aluno = Aluno()
    aluno.pid = request.form.get("pid")
    aluno.nome = request.form.get("nome")
    aluno.email = request.form.get("email")
    aluno.idade = int(request.form.get("idade")) 
    aluno = dao.alterarAluno(aluno)
    
    lista = dao.selecionarAluno()
    return render_template(
        "listagem.html",
        lista=lista
    )

@app.route('/aluno/remover/<pid>', methods=["GET"])
def remover(pid):
    aluno = Aluno()
    aluno.pid = pid
    dao.excluirAluno(aluno)
    
    lista = dao.selecionarAluno()
    return render_template(
        "listagem.html",
        lista=lista
    )


if __name__ == '__main__':
    app.run()