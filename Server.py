from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_cors import CORS
from dao import PessoaDao, UsuarioDao
from models import Pessoa, Usuario
import os, regra_score,configparser, mysql.connector


app = Flask(__name__)
app.secret_key = 'SauloJanuzzi'
cors = CORS(app, resource={r"/*":{"origins": "*"}})


config = configparser.ConfigParser()
config.read("db.config")

db = mysql.connector.connect(
  host=config.get("DB", "host"),
  user=config.get("DB", "user"),
  passwd=config.get("DB", "passwd")
)
pessoa_dao = PessoaDao(db)
usuario_dao = UsuarioDao(db)

@app.route('/teste')
def teste():
    return "<h1>Hello World!</h1>"


@app.route('/')
def index():
    return render_template('lista.html', titulo='Constrole de Cadastro', pessoas=lista1)

@app.route('/consultacadastros')
def consultacadastro():
    lista = pessoa_dao.listar()
    return render_template('lista.html', titulo='Constrole de Cadastro', pessoas=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Cadastro')

@app.route('/criar', methods=['POST',])
def criar():
    score = regra_score.defini_score()
    nova_pessoa = Pessoa(request.form['cpf'], request.form['nome'], request.form['renda'], request.form['logradouro']
                         , request.form['numero'], request.form['bairro'],score,
                         regra_score.gerar_credito(request.form['renda'], score))


    pessoa_dao.salvar(nova_pessoa)
    flash('Cadastro realizado com sucesso!')
    return redirect(url_for('consultacadastro'))


@app.route('/deletar/<string:cpf>')
def deletar(cpf):
    pessoa_dao.deletar(cpf)
    flash('Cadastro removido com sucesso!')
    return redirect(url_for('consultacadastro'))


@app.route('/menu')
def menu():
    return render_template('menu.html', titulo='Controle de Cartão de Crédito')


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()