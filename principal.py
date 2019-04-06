#Filipe Fernandes
#RA: 21800169

from flask import Flask, render_template,request
from flaskext.mysql import MySQL
from bd import *


app = Flask(__name__)
#instanciando o objeto MySQL
mysql = MySQL()
#Ligando o MySQL ao Flask
mysql.init_app(app)

#configurando o acesso ao MySQL
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = "root"
app.config['MYSQL_DATABASE_DB'] = "faculdade"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/listarProfessores")
def listarProfessores():
    cursor = mysql.get_db().cursor()
    professores = get_listar_prof(cursor)
    return render_template("listar_professores.html", professores=professores)

@app.route("/exibirProfessor/<id_prof>")
def exibirProfessor(id_prof):
    cursor = mysql.get_db().cursor()
    exibir_professor = get_exibir_prof(cursor, id_prof)
    return render_template("exibir_professor.html", detalhes=exibir_professor[0], disciplinas=exibir_professor[1])

@app.route("/consultarPorTitulacao")
def consultarPorTitulacao():
    return render_template("consultar_titulacao.html")

@app.route("/titulacao", methods=["GET","POST"])
def retornoTitulacao():
    if request.method == "POST":
        valor_titulacao = request.form["valor"]

        cursor = mysql.get_db().cursor()
        retorno_titulacao = get_titulacao(cursor, valor_titulacao)
        return render_template("retorno_titulacao.html", retorno_titulacao=retorno_titulacao)

@app.route("/consultarCursos")
def consultarCursos():
    return render_template("apenas_computacao.html")

@app.route("/consultarApenasComputacao",  methods=["GET","POST"])
def consultarComputacao():
    if request.method == "POST":
        computacao = request.form["valor"]

        cursor = mysql.get_db().cursor()

        retorno_computacao = get_computacao(cursor, computacao)
        print(retorno_computacao)

        return render_template("retorno_computacao.html", retorno_computacao=retorno_computacao)

if __name__ == "__main__":
    app.run(debug=True)