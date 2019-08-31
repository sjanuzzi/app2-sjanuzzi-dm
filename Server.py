from flask import Flask, render_template, request, redirect, session, flash, url_for
import os
from flask_cors import CORS


app = Flask(__name__)
app.secret_key = 'SauloJanuzzi'
cors = CORS(app, resource={r"/*":{"origins": "*"}})


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
lista = [jogo1, jogo2]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Constrole de Cadastro', jogos=lista)

@app.route('/consultacadastros')
def consultaCadastro():
    return render_template('lista.html', titulo='Constrole de Cadastro', jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Cadastro')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request. form['nome']
    categoria = request. form['categoria']
    console = request. form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    flash('Cadastro realizado com sucesso!')
    return redirect(url_for('novo'))


@app.route('/deletar')
def deletar():
    return redirect(url_for('novo'))



@app.route('/menu', methods=['GET'])
def menu():
    return render_template('menu.html', titulo='Constrole de Cadastro', jogos=lista)


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    app.run()