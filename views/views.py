import json, jsonpickle, sys
from flask import render_template, request, redirect, flash, url_for, jsonify, json
from models.models import Pessoa
from controllers.regra_score import gerar_credito, defini_score,formataValor, formataCpf, formataDecimal
from models.dao import PessoaDao
from server import app
from commons.grava_log import log_info

pessoa_dao = PessoaDao()


@app.route('/')
def index():
    return render_template('menu_principal.html', titulo='Constrole de Cadastro')


@app.route('/cadastros',  methods=['GET',])
def consultacadastro():
    log_info(request.method +' '+ request.path )
    lista = pessoa_dao.listar()
    lista_json = json.dumps(lista,default=lambda o: o.__dict__,sort_keys=True, indent=2)
    return render_template('consulta_cadastro.html', titulo='Constrole de Cadastro', pessoas=json.loads(lista_json))


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Cadastro')


@app.route('/criar', methods=['POST', ])
def criar():

    if not pessoa_dao.buscaCpf(formataCpf(request.form['cpf'])):
        score = defini_score()
        pessoa_dao.salvar(Pessoa(formataCpf(request.form['cpf']),
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

@app.route('/v1/cadastros/', methods=['GET', ])
def consultacadastro_api():

    cpf = request.args.get('cpf')

    if not cpf:
        return json.dumps(pessoa_dao.listar(),default=lambda o: o.__dict__,sort_keys=True, indent=2)
    else:
        return json.dumps(pessoa_dao.buscaCpf(formataCpf(cpf)),default=lambda o: o.__dict__,sort_keys=True, indent=2)


@app.route('/v1/deletar/<string:cpf>', methods=['DELETE',])
def deletar_api(cpf):
    try:
        pessoa_dao.deletar(cpf)

        return app.response_class(
            response=json.dumps('Cadastro removido com sucesso'),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return app.response_class(
            response=json.dumps(str(e)),
            status=400,
            mimetype='application/json'
        )



@app.route('/v1/criar', methods=['POST', ])
def criar_api():

    if (pessoa_dao.buscaCpf(formataCpf(request.json['cpf'], True))):
        score = defini_score()
        nova_pessoa = Pessoa(formataCpf(request.json['cpf'], True),
                            request.json['nome'],
                            formataValor(formataDecimal(request.json['renda'])),
                            request.json['logradouro'],
                            request.json['numero'],
                            request.json['bairro'],
                            score,
                            gerar_credito(request.json['renda'],
                            score))
        pessoa_dao.salvar(nova_pessoa)

        return app.response_class(
            response=json.dumps(nova_pessoa,default=lambda o: o.__dict__,sort_keys=True, indent=2),
            status=201,
            mimetype='application/json'
        )
    else:
        return app.response_class(
            response=json.dumps('CPF já cadastrado!'),
            status=400,
            mimetype='application/json'
        )