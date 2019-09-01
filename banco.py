import mysql.connector



def teste_banco():
  mydb = mysql.connector.connect(
  host="us-cdbr-iron-east-02.cleardb.net",
  user="b78e789bf5ed96",
  passwd="6da9c81f"
  )

  mycursor = mydb.cursor()

  mycursor.execute("SELECT cpf FROM heroku_93dc94d1abacf09.cadastro_pessoa")

  myresult = mycursor.fetchall()

  for x in myresult:
    return x



print(teste_banco())