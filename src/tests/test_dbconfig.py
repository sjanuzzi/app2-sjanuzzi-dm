from unittest import TestCase
from src.dbaccess import dbconfig

class TestDbconfig(TestCase):

    def test_ler_arquivo_config_para_obter_info_de_acesso_ao_db(self):
        filename = 'src/config.ini'
        section = 'DB'

        config = dbconfig(filename, section)
        set.assertTrue(
            "{'host': 'us-cdbr-iron-east-02.cleardb.net', 'user': 'b78e789bf5ed96', 'password': '6da9c81f', 'database': 'heroku_93dc94d1abacf09'}", config)