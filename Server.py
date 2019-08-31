from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_cors import CORS
import os
import uuid
import regra_score


app = Flask(__name__)
app.secret_key = 'SauloJanuzzi'
cors = CORS(app, resource={r"/*":{"origins": "*"}})


class pessoa:
    def __init__(self, nome, cpf, renda, logradouro, numero_logradouro, bairro, score_pessoa, valor_credito, id):
        self.nome = nome
        self.cpf = cpf
        self.renda = renda
        self.logradouro = logradouro
        self.numero_logradouro = numero_logradouro
        self.bairro = bairro
        self.score_pessoa = score_pessoa
        self.valor_credito = valor_credito
        self.id = id



pessoa1 = pessoa('Saulo Januzzi', '12345678990', 28456, 'Rua das Piabas', '133', 'jardim',301,1000, uuid.uuid1())
pessoa2 = pessoa('Pedro Januzzi', '32112332112', 13456, 'Rua das Piabas', '133', 'jardim',660, 500,uuid.uuid1())

lista = [pessoa1, pessoa2]

@app.route('/teste')
def teste():
    return "<h1>Hello World!</h1>"


@app.route('/')
def index():
    return render_template('lista.html', titulo='Constrole de Cadastro', pessoas=lista)

@app.route('/consultacadastros')
def consultacadastro():
    return render_template('lista.html', titulo='Constrole de Cadastro', pessoas    =lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Cadastro')

@app.route('/criar', methods=['POST',])
def criar():
    score = regra_score.defini_score()

    nova_pessoa = pessoa(request.form['nome'], request.form['cpf'], request.form['renda'], request.form['logradouro']
                         , request.form['numero'], request.form['bairro'],score ,
                         regra_score.gerar_credito(request.form['renda'], score), uuid.uuid1())

    lista.append(nova_pessoa)
    flash('Cadastro realizado com sucesso!')
    return redirect(url_for('consultacadastro'))


@app.route('/deletar')
def deletar():
    return redirect(url_for('novo'))



@app.route('/menu')
def menu():
    return render_template('menu.html', titulo='Controle de Cartão de Crédito')


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()