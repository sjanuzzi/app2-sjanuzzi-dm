from models.models import Pessoa
#TODO  https://pt.stackoverflow.com/questions/365490/verificar-se-registros-existem-com-python
SQL_EXCLUI_POR_CPF = 'delete from heroku_2f4f5627753b053.cadastro_pessoa where cpf = %s'
SQL_BUSCA_CADASTRO = 'select cpf, nome, renda, logradouro, numero,bairro, socre, valor_credito from heroku_2f4f5627753b053.cadastro_pessoa'
SQL_CRIA_CADASTRO= 'insert into heroku_2f4f5627753b053.cadastro_pessoa (cpf,nome,renda,logradouro,numero,bairro,socre,' \
                   'valor_credito) values (%s, %s, %s,%s, %s, %s,%s, %s)'
SQL_BUSCA_CPF = 'SELECT cpf, nome, renda, logradouro, numero,bairro, socre, valor_credito from heroku_2f4f5627753b053.cadastro_pessoa where cpf = %s'

class PessoaDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, pessoa):
        cursor = self.__db.cursor()
        cursor.execute(SQL_CRIA_CADASTRO, (pessoa.cpf, pessoa.nome, pessoa.renda, pessoa.logradouro,
                                           pessoa.numero_logradouro, pessoa.bairro, pessoa.score_pessoa,
                                           pessoa.valor_credito))
        self.__db.commit()
        return pessoa

    def listar(self):
        return traduz_pessoas(self.__db.cursor().execute(SQL_BUSCA_CADASTRO).fetchall())

    def buscaCpf(self, cpf):
        return self.__db.cursor().execute(SQL_BUSCA_CPF, (cpf,))


    def deletar(self, cpf):
        self.__db.cursor().execute(SQL_EXCLUI_POR_CPF, (cpf, ))
        self.__db.commit()


def traduz_pessoas(pessoa):
    def cria_pessoa_com_tupla(tupla):
        return Pessoa(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7])
    return list(map(cria_pessoa_com_tupla, pessoa))


