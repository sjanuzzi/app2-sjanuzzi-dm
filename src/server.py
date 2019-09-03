from flask import Flask
from flask_cors import CORS
import os, configparser, mysql.connector


app = Flask(__name__,template_folder='templates')
app.secret_key = 'ConstroleCadastro'
cors = CORS(app, resource={r"/*":{"origins": "*"}})


config = configparser.ConfigParser()
config.read("src/db.config")

db = mysql.connector.connect(
  host=config.get("DB", "host"),
  user=config.get("DB", "user"),
  passwd=config.get("DB", "passwd")
)

from src.views import *

def main():

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()