import mysql.connector
conexao = mysql.connector.connect(host="localhost",user="root",password="",database="db_user")
cursor = conexao.cursor()