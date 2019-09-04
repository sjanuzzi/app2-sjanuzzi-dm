from flask import Flask
from flask_cors import CORS
import os
from dbaccess import dbconfig, connect

app = Flask(__name__)
app.secret_key = 'ConstroleCadastro'
cors = CORS(app, resource={r"/*":{"origins": "*"}})

filename = 'config.ini'
section = 'DB'
db = connect(dbconfig(filename, section))


from views import *


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()