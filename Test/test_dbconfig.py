from unittest import TestCase, mock
from models.dbaccess import dbconfig



class TestDbconfig(TestCase):

    def setUp(self):
        self.configdb = dbconfig("config.ini", "db")

    @mock.patch('src.dbaccess')
    def test_ler_arquivo_config_para_obter_info_de_acesso_ao_db(self, mock_config_parser):
        mock_config_parser = mock_config_parser.return_value
        self.configdb("config.ini", "db")

        mock_config_parser.assert_called_once_with()

        mock_config_parser.read.assert_called_once_with("config.ini", "DB")


