from flask import render_template, request, redirect, flash, url_for, jsonify, json
from models.models import Pessoa
import json, jsonpickle
from controllers.regra_score import gerar_credito, defini_score,formataValor, formataCpf, formataDecimal
from models.dao import PessoaDao
from server import app

filename = 'db.config'
section = 'DB'
pessoa_dao = PessoaDao(filename, section )


@app.route('/')
def index():
    return render_template('menu_principal.html', titulo='Constrole de Cadastro')


@app.route('/cadastros',  methods=['GET',])
def consultacadastro():
    lista = pessoa_dao.listar()
    lista_json = json.dumps(lista,default=lambda o: o.__dict__,sort_keys=True, indent=2)
    if request.content_type not in ['application/json', 'application/json; charset=UTF-8']:
        return render_template('consulta_cadastro.html', titulo='Constrole de Cadastro', pessoas=json.loads(lista_json))
    else:
        return lista_json


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Cadastro')


@app.route('/criar', methods=['POST', ])
def criar():

    if (pessoa_dao.buscaCpf(formataCpf(request.form['cpf'], True))):
        score = defini_score()
        pessoa_dao.salvar(Pessoa(formataCpf(request.form['cpf'], True),
                            request.form['nome'],
                            formataValor(formataDecimal(request.form['renda'])),
                            request.form['logradouro'],
                            request.form['numero'],
                            request.form['bairro'],
                            score,
                            gerar_credito(request.form['renda'],
                            score)))
        flash('Cadastro realizado com sucesso!')
        return redirect(url_for('consultacadastro'))
    else:
        flash('CPF já cadastrado!')
        return redirect(url_for('consultacadastro'))


@app.route('/deletar/<string:cpf>')
def deletar(cpf):
    pessoa_dao.deletar(cpf)
    flash('Cadastro removido com sucesso!')
    return redirect(url_for('consultacadastro'))


#======================== rotas API =============================================

@app.route('/api/deletar/<string:cpf>', methods=['DELETE'])
def deletar_api(cpf):
    try:
        pessoa_dao.deletar(cpf)
        return jsonify({'Menssagem': 'Cadastro removido com sucesso'})
    except Exception as e:
        return jsonify({'Menssagem': str(e)})

@app.route('/api/cadastros', methods=['GET', ])
def consultacadastro_api():
    return jsonpickle.encode(pessoa_dao.listar())

@app.route('/api/criar', methods=['POST', ])
def criar_api():

    if request.json['cpf'].isdigit() and request.json['renda'].isdigit():
        score = defini_score()
        nova_pessoa = Pessoa(request.json['cpf'], request.json['nome'], request.json['renda'], request.json['logradouro']
                             , request.json['numero_logradouro'], request.json['bairro'], score,
                             gerar_credito(request.json['renda'], score))
        pessoa_dao.salvar(nova_pessoa)

        return jsonpickle.encode(nova_pessoa)
    else:
        response = app.response_class(
            response=json.dumps('Digite apenas número nos campos de CPF e Renda'),
            status=400,
            mimetype='application/json'
        )
        return response


