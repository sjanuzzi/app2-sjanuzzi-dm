
schema = 'heroku_2f4f5627753b053'
def SQL_EXCLUI_POR_CPF():
    return 'delete from '+ schema +'.cadastro_pessoa where cpf = %s'

def SQL_BUSCA_CADASTRO():
    return 'select cpf, nome, CONVERT(renda, char(100)) as renda, logradouro, numero,bairro, socre, valor_credito ' \
           'from '+ schema +'.cadastro_pessoa'

def SQL_CRIA_CADASTRO():
    return 'insert into '+ schema +'.cadastro_pessoa (cpf,nome,renda,logradouro,numero,bairro,socre,' \
                    'valor_credito) values (%s, %s, %s,%s, %s, %s,%s, %s)'

def SQL_BUSCA_CPF():
    return 'select cpf, nome, CONVERT(renda, char(100)) as renda, logradouro, numero,bairro, socre, valor_credito from '+ schema +'.cadastro_pessoa where cpf = %s'



"""
SQL_EXCLUI_POR_CPF = 'delete from heroku_2f4f5627753b053.cadastro_pessoa where cpf = %s'
SQL_BUSCA_CADASTRO = 'select cpf, nome, CONVERT(renda, char(100)) as renda, logradouro, numero,bairro, socre, valor_credito from heroku_2f4f5627753b053.cadastro_pessoa'
SQL_CRIA_CADASTRO= 'insert into heroku_2f4f5627753b053.cadastro_pessoa (cpf,nome,renda,logradouro,numero,bairro,socre,' \
                    'valor_credito) values (%s, %s, %s,%s, %s, %s,%s, %s)'
SQL_BUSCA_CPF = 'SELECT cpf, nome, renda, logradouro, numero,bairro, socre, valor_credito from heroku_2f4f5627753b053.cadastro_pessoa where cpf = %s'

#db = connect(dbconfig(filename, section))

"""