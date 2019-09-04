from flask import Flask
from flask_cors import CORS
import os
import mysql.connector
from configparser import ConfigParser
from flask import render_template, request, redirect, flash, url_for, jsonify, json
from models import Pessoa
import json, jsonpickle
import regra_score
from dao import PessoaDao

#from dbaccess import dbconfig, connect

app = Flask(__name__)
app.secret_key = 'ConstroleCadastro'
cors = CORS(app, resource={r"/*":{"origins": "*"}})


config = ConfigParser()
config.read("db.config")


db = mysql.connector.connect(host="us-cdbr-iron-east-02.cleardb.net", user="b78e789bf5ed96",
                             password ="6da9c81f", database="heroku_93dc94d1abacf09")

#from views import *


pessoa_dao = PessoaDao(db)


@app.route('/')
def index():
    return render_template('menu_principal.html', titulo='Constrole de Cadastro')


@app.route('/cadastros',  methods=['GET',])
def consultacadastro():
    lista = pessoa_dao.listar()
    r = json.dumps(lista, default=lambda o: o.__dict__,sort_keys=True, indent=4)
    loaded_r = json.loads(r)
    if request.content_type not in ['application/json', 'application/json; charset=UTF-8']:
        return render_template('consulta_cadastro.html', titulo='Constrole de Cadastro', pessoas=loaded_r)
    else:
        return jsonpickle.encode(lista)


@app.route('/api/cadastros', methods=['GET', ])
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
        #if request.content_type not in ['application/json', 'application/json; charset=UTF-8']:
        #    pass

        #pessoa_json = request.get_json()
        """x = pessoa_json.get('cpf')
        nova_pessoa = Pessoa(pessoa_json['cpf'], pessoa_json['nome'], pessoa_json['renda'], pessoa_json['logradouro']
               , pessoa_json['numero_logradouro'], pessoa_json['bairro'], score,
               regra_score.gerar_credito(pessoa_json['renda'], score))
        """
        nova_pessoa = Pessoa(request.form['cpf'], request.form['nome'], request.form['renda'], request.form['logradouro']
                             , request.form['numero'], request.form['bairro'], score,
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
                             , request.json['numero_logradouro'], request.json['bairro'], score,
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