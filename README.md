

## GYPZ- Tech Challenge 

  
Aplicação utiliza a infraestrutur na plataforma em nuvem Heroku. 

* Tecnologia utilizadas: 
	* - Python version 3.7.3 
	* - Flask version 1.0.3 
	* - Flask-Cors version 3.0.7 
	* - MySql Connector Python version 8.0.11 -
	*  Banco de dados ClearDB MySQL 
    
## Estrutura de Diretório

```
commons/
    log.config
    grava_log.py
controllers/
    regra_score.py
models/
    sqlcomand.py
    models.py
    dbaccess.py
    dao.py
static/
    bootstrap.css
templates/
    template_erro.html
    template.html
    novo.html
    menu_principal.html
    consulta_cadastro_unitario.html
    consulta_cadastro.html
views/
    views.py
Test
    test_views.py
    test_defini_score.py
    test_dbconfig.py  
    templates/  
    config.ini
db.config  
Procfile
requirements.txt  
server.py 
```
## Rotas criadas nesse projeto

 * **Web** Rota principal para aplicação web
       `https://app-sjanuzzi.herokuapp.com/`
       
 * **Restful** - Rotas para as apis

  *  **Metodos:**
   - **[GET]** - retorna todas as solicitações cadastradas
  
		-   Rota: `http://app-sjanuzzi.herokuapp.com/v1/cadastros`
		      Return code 200
		    * Retorno será dos dados informado no momento do cadastro e mais o 		score e valor do crédito aprovado
  ````
				       [ 
				         { 
				            "bairro":"Satelite",
				            "cpf":"11223212331",
				            "logradouro":"Rua dos Planetas",
				            "nome":" Teste Json postman",
				            "numero_logradouro":"1",
				            "renda":"1039.00",
				            "score_pessoa":"777",
				            "valor_credito":"1000.00"
				         }
				      ]
  ````



   - **[POST]** - Para o cadastro de nova solicitação
		-  Rota: `app-sjanuzzi.herokuapp.com/v1/criar`
 ````   
     - return code: 201
      { 
        "bairro":"Satelite",
        "cpf":"22478547327",
        "logradouro":"Rua dos Planetas",
        "nome":" Teste Json postman",
        "numero":"1",
        "renda":"1039.00"
      }
  ````      
   **Retorno** será um json com o dados informados no cadastro de solicitação, mais o campo de score e valor do credito aprovado.
   ````
    {
       "bairro": "Satelite",
       "cpf": "22478547327",
       "logradouro": "Rua dos Planetas",
       "nome": " Teste Json postman",
       "numero_logradouro": "1",
       "renda": "1039.00",
       "score_pessoa": 642,
       "valor_credito": "1000.00"
    }
  ````

  
   - **[DELETE]** - Para o excluir um cadastro de solicitação

	 **Rota:** `app-sjanuzzi.herokuapp.com/v1/solicitacoes/{cpf}`
	   - return code: 200 
  
