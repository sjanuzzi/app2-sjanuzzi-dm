
## GYPZ- Tech Challenge 

  
Aplicação utiliza a infraestrutura na plataforma em nuvem Heroku. 

* Tecnologia utilizadas: 
	* - Python version 3.7.3 
	* - Flask version 1.0.3 
	* - Flask-Cors version 3.0.7 
	* - MySql Connector Python version 8.0.11
	* - Banco de dados ClearDB MySQL 
	* - Html com Fornt-end com bootstrap
    
## Estrutura de diretório do projeto

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
Test/
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
	
 **Metodos:**
**[GET]** - retorna todas as solicitações cadastradas
  
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

**Link para as rotas.**      [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/7e29256f1ea954ed625e)


**Logs:**

Aplicação com estrutura de log Trace (logging função built-in do python)
Heroku disponibiliza um view que fornece todos os logs que a aplicação gerou

   - **Exemplo:** 
  ````
2019-09-06T15:41:31.505479+00:00 app[web.1]:     request.json['numero'],
2019-09-06T15:41:31.505487+00:00 app[web.1]: KeyError: 'numero'
2019-09-06T15:41:31.506166+00:00 app[web.1]: 2019-09-06 15:41:31,506 - werkzeug - INFO - 10.97.208.49 - - [06/Sep/2019 15:41:31] "POST /api/solicitacoes HTTP/1.1" 500 -
2019-09-06T15:41:31.504866+00:00 heroku[router]: at=info method=POST path="/api/solicitacoes" host=app-sjanuzzi.herokuapp.com request_id=86836d1d-b2ba-48cd-913e-2189fcb06caf fwd="177.58.165.125" dyno=web.1 connect=1ms service=117ms status=500 bytes=481 protocol=http
2019-09-06T15:42:35.479562+00:00 heroku[router]: at=info method=POST path="/api/solicitacoes" host=app-sjanuzzi.herokuapp.com request_id=44dd2e9f-7d52-42f7-ac96-38f5ee373c85 fwd="177.58.165.125" dyno=web.1 connect=1ms service=229ms status=201 bytes=409 protocol=http
2019-09-06T15:42:35.478615+00:00 app[web.1]: 2019-09-06 15:42:35,478 - werkzeug - INFO - 10.16.205.17 - - [06/Sep/2019 15:42:35] "POST /api/solicitacoes HTTP/1.1" 201 -
2019-09-06T16:00:46.422168+00:00 heroku[router]: at=info method=GET path="/api/solicitacoes" host=app-sjanuzzi.herokuapp.com request_id=b1a09458-033f-4fb8-9d7e-06936886eb83 fwd="177.58.165.125" dyno=web.1 connect=1ms service=138ms status=200 bytes=1145 protocol=https
2019-09-06T16:00:46.420417+00:00 app[web.1]: 2019-09-06 16:00:46,420 - werkzeug - INFO - 10.63.157.85 - - [06/Sep/2019 16:00:46] "GET /api/solicitacoes HTTP/1.1" 200 -
2019-09-06T16:01:03.619598+00:00 app[web.1]: 2019-09-06 16:01:03,619 - werkzeug - INFO - 10.63.157.85 - - [06/Sep/2019 16:01:03] "DELETE /api/solicitacoes/10120929122 HTTP/1.1" 200 -
2019-09-06T16:01:03.621743+00:00 heroku[router]: at=info method=DELETE path="/api/solicitacoes/10120929122" host=app-sjanuzzi.herokuapp.com request_id=d440d936-f435-4e16-8d63-d8781213fd8a fwd="177.58.165.125" dyno=web.1 connect=1ms service=110ms status=200 bytes=209 protocol=https
````
