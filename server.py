from flask import Flask
from flask_cors import CORS
import os
from models.dbaccess import dbconfig, connect
from configparser import ConfigParser
from flask import render_template, request, redirect, flash, url_for, jsonify, json
from models.models import Pessoa
import json, jsonpickle
from controllers import regra_score
from models.dao import PessoaDao


app = Flask(__name__)
app.secret_key = 'ConstroleCadastro'
cors = CORS(app, resource={r"/*":{"origins": "*"}})


#config = ConfigParser()
#config.read("db.config")

filename = 'db.config'
section = 'DB'
db = connect(dbconfig(filename, section))

#db = mysql.connector.connect(host="us-cdbr-iron-east-02.cleardb.net", user="b9915482ede514",password ="61427871", database="heroku_2f4f5627753b053")

from views.views import *




#pessoa_dao = PessoaDao(db)




def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()