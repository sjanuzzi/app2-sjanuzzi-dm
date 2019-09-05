from models.models import Pessoa
from models.dbaccess import dbconfig, connect
from models.sqlcomand import SQL_BUSCA_CPF, SQL_BUSCA_CADASTRO ,SQL_CRIA_CADASTRO,SQL_EXCLUI_POR_CPF
import sys


class PessoaDao:
    def __init__(self, filename, section):
        self.__filename = filename
        self._section = section

    def salvar(self, pessoa):
        try:
            db = PessoaDao.conexaodb()
            cursor = db.cursor()
            cursor.execute(SQL_CRIA_CADASTRO(), (pessoa.cpf, pessoa.nome, pessoa.renda, pessoa.logradouro,
                                           pessoa.numero_logradouro, pessoa.bairro, pessoa.score_pessoa,
                                           pessoa.valor_credito))
            db.commit()
            return pessoa
        except Exception as e:
            sys.stdout.write("salvar  erro ->> : {}".format(e))

    def listar(self):
        try:
            db = PessoaDao.conexaodb()
            cursor = db.cursor()
            cursor.execute(SQL_BUSCA_CADASTRO())
            retorno_pessoas = traduz_pessoas(cursor.fetchall())

            return retorno_pessoas
        except Exception as e:
            sys.stdout.write("listar  erro ->> : {}".format(e))

    def buscaCpf(self, cpf):
        try:
            db = PessoaDao.conexaodb()
            cursor = db.cursor()
            cursor.execute(SQL_BUSCA_CPF(),( cpf,))
            retorno_pessoas = traduz_pessoas(cursor.fetchall())
            db.close()
            if len(retorno_pessoas) != 0:
                return False
            else:
                return True
        except Exception as e:
            sys.stdout.write("buscaCpf erro ->>: {}".format(str(e)))


    def deletar(self, cpf):
        try:
            sys.stdout.write("cfp > : {}".format(cpf))
            sys.stdout.write(SQL_EXCLUI_POR_CPF())
            db = PessoaDao.conexaodb()
            db.cursor().execute(SQL_EXCLUI_POR_CPF(), (cpf, ))
            db.commit()
        except Exception as e:
            sys.stdout.write("deletar erro ->>: {}".format(str(e)))

    @staticmethod
    def conexaodb():
        filename = 'db.config'
        section = 'DB'
        return connect(dbconfig(filename, section))


def traduz_pessoas(pessoa):
    def cria_pessoa_com_tupla(tupla):
        return Pessoa(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7])
    return list(map(cria_pessoa_com_tupla, pessoa))

