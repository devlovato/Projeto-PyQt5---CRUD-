import mysql.connector
from pyfiglet import figlet_format
from termcolor import colored
from mysql.connector import errorcode
texto = figlet_format("DATA",width=200)
texto = colored(texto,"blue")
print(texto)
conexao = mysql.connector.connect(host="localhost",user="root",password="")

cursor = conexao.cursor()
try:
    cursor.execute("CREATE DATABASE db_user;")
    # UTILIZA O BANCO DE DADOS
    cursor.execute("USE db_user;")
    # CRIA A A TABELA USUARIO
    cursor.execute("CREATE TABLE tb_user(\ntb_user_id integer not null auto_increment primary key,\ntb_user_nome varchar(100) not null,\n tb_user_email varchar(100) not null,\ntb_user_pass varchar(100)not null,\ntb_user_sexo char(1)not null,\ntb_user_permission BOOLEAN\n);")

    cursor.execute("INSERT INTO `db_user`.`tb_user` (`tb_user_nome`, `tb_user_email`, `tb_user_pass`, `tb_user_sexo`, `tb_user_permission`) VALUES ('Eduardo', 'lovato.py@gmail.com', '12345678', 'M', '1');")
    cursor.execute("INSERT INTO `db_user`.`tb_user` (`tb_user_nome`, `tb_user_email`, `tb_user_pass`, `tb_user_sexo`, `tb_user_permission`) VALUES ('Fernando', 'fernando@yahoo.com', '123456', 'M', '0');")
    cursor.execute("INSERT INTO `db_user`.`tb_user` (`tb_user_nome`, `tb_user_email`, `tb_user_pass`, `tb_user_sexo`, `tb_user_permission`) VALUES ('Allan', 'allan@outlook.com', '419256', 'M', '0');")
    cursor.execute("INSERT INTO `db_user`.`tb_user` (`tb_user_nome`, `tb_user_email`, `tb_user_pass`, `tb_user_sexo`, `tb_user_permission`) VALUES ('Ester', 'ester@aws.com', '400289', 'F', '0');")
    cursor.execute("INSERT INTO `db_user`.`tb_user` (`tb_user_nome`, `tb_user_email`, `tb_user_pass`, `tb_user_sexo`, `tb_user_permission`) VALUES ('Pedro', 'pedro@azure.com', '456548', 'M', '0');")
    cursor.execute("INSERT INTO `db_user`.`tb_user` (`tb_user_nome`, `tb_user_email`, `tb_user_pass`, `tb_user_sexo`, `tb_user_permission`) VALUES ('Marcelo', 'marcelo@gmail.com', '511878', 'M', '0');")
    cursor.execute("INSERT INTO `db_user`.`tb_user` (`tb_user_nome`, `tb_user_email`, `tb_user_pass`, `tb_user_sexo`, `tb_user_permission`) VALUES ('Alvaro', 'alvaro@gmail.com', '465454', 'M', '0');")
    cursor.execute("INSERT INTO `db_user`.`tb_user` (`tb_user_nome`, `tb_user_email`, `tb_user_pass`, `tb_user_sexo`, `tb_user_permission`) VALUES ('Marcela', 'marcela@youtube.com', '456565', 'F', '0');")
    cursor.execute("INSERT INTO `db_user`.`tb_user` (`tb_user_nome`, `tb_user_email`, `tb_user_pass`, `tb_user_sexo`, `tb_user_permission`) VALUES ('Gabriela', 'gabi@globo.com', '456546', 'F', '0');")
    cursor.execute("INSERT INTO `db_user`.`tb_user` (`tb_user_nome`, `tb_user_email`, `tb_user_pass`, `tb_user_sexo`, `tb_user_permission`) VALUES ('Estela', 'estela@accenture.com', '465646', 'F', '0');")
    cursor.execute("INSERT INTO `db_user`.`tb_user` (`tb_user_nome`, `tb_user_email`, `tb_user_pass`, `tb_user_sexo`, `tb_user_permission`) VALUES ('Maria', 'maria@zoom.com', '545545', 'F', '0');")
    conexao.commit()
except mysql.connector.Error as erro:
    print('ERRO',erro)