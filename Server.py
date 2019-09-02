from flask import Flask, render_template, request, redirect, flash, url_for, jsonify, json
from flask_cors import CORS
from dao import PessoaDao, UsuarioDao
from models import Pessoa, Usuario
import os, regra_score,configparser, mysql.connector,json, jsonpickle



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

@app.route('/')
def index():
    return render_template('menu.html', titulo='Constrole de Cadastro')


@app.route('/consultacadastros',  methods=['GET',])
def consultacadastro():
    lista = pessoa_dao.listar()
    return render_template('lista.html', titulo='Constrole de Cadastro', pessoas=lista)


@app.route('/api/consultacadastros', methods=['GET', ])
def consultacadastro_api():
    lista = pessoa_dao.listar()
    return jsonpickle.encode(lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Cadastro')


@app.route('/criar', methods=['POST', ])
def criar():
    if request.form['cpf'].isdigit() and request.form['renda'].isdigit():
        score = regra_score.defini_score()
        nova_pessoa = Pessoa(request.form['cpf'], request.form['nome'], request.form['renda'], request.form['logradouro']
                            , request.form['numero'], request.form['bairro'],score,
                             regra_score.gerar_credito(request.form['renda'], score))
        pessoa_dao.salvar(nova_pessoa)
        flash('Cadastro realizado com sucesso!')
        return redirect(url_for('consultacadastro'))
    else:
        flash('Digite apenas número nos campos de CPF e Renda!')
        return redirect(url_for('novo'))

@app.route('/api/criar', methods=['POST', ])
def criar_api():

    if request.json['cpf'].isdigit() and request.json['renda'].isdigit():
        score = regra_score.defini_score()
        nova_pessoa = Pessoa(request.json['cpf'], request.json['nome'], request.json['renda'], request.json['logradouro']
                         , request.json['numero_logradouro'], request.json['bairro'],score,
                         regra_score.gerar_credito(request.json['renda'], score))
        pessoa_dao.salvar(nova_pessoa)

        return jsonpickle.encode(nova_pessoa)
    else:
        response = app.response_class(
            response=json.dumps('Digite apenas número nos campos de CPF e Renda'),
            status=400,
            mimetype='application/json'
        )
        return response


@app.route('/deletar/<string:cpf>')
def deletar(cpf):
    pessoa_dao.deletar(cpf)
    flash('Cadastro removido com sucesso!')
    return redirect(url_for('consultacadastro'))


@app.route('/api/deletar/<string:cpf>', methods=['DELETE'])
def deletar_api(cpf):
    try:
        pessoa_dao.deletar(cpf)
        return jsonify({'Menssagem': 'Cadastro removido com sucesso'})
    except Exception as e:
        return jsonify({'Menssagem': str(e)})


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()