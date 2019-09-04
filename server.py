from flask import Flask
from flask_cors import CORS
import os
from configparser import ConfigParser
import mysql.connector
from configparser import ConfigParser

#from dbaccess import dbconfig, connect

app = Flask(__name__)
app.secret_key = 'ConstroleCadastro'
cors = CORS(app, resource={r"/*":{"origins": "*"}})


config = ConfigParser()
config.read("db.config")



db = mysql.connector.connect(host="us-cdbr-iron-east-02.cleardb.net", user="b78e789bf5ed96",
                             password ="6da9c81f", database="heroku_93dc94d1abacf09")
#        config.get('DB','host'),
#                            config.get('DB','user'),
#                            config.get('DB','passwd'))



#connect(dbconfig(filename, section))


from views import *


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()