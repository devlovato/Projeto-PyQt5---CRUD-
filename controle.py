# Importando uic e o Qtwidgets do PyQt5
from ast import Return
from cmath import log
from turtle import st
from PyQt5 import uic, QtWidgets
import mysql.connector

conexao = mysql.connector.connect(host="localhost",user="root",password="",database="db_user")
    
cursor = conexao.cursor()

def Login(): 
    Email = login.lineEdit.text()
    Password = login.lineEdit_2.text()
    # label para mostrar no formulario
    # label = login.label.label_4.text()

    try:
        # USANDO A FORMATAÇAO .FORMAT PARA FOMATAR O DADO VINDO DA MANEIRA CORRETA
        cursor.execute("SELECT tb_user_pass, tb_user_email  FROM tb_user WHERE tb_user_email='{}'".format(Email))
        password_db = cursor.fetchall()
        # print(password_db[0][0])
        
        if Password == password_db[0][0]:
            login.label_4.text()
            login.label_4.setText("DADOS CORRETOS")
            # print("DADOS CORRETOS")
            dash.show()
            login.close()
        else:
            login.label_4.setText("DADOS INCORRETOS")
            # print("DADOS INCORRETOS")
    except:
        print("OCORREU UM ERRO NA VALIDAÇAO DO FORMULARIO")
def Cadastro():
    cadastro.show()
    Nome = cadastro.lineEdit_3.text()
    Email = cadastro.lineEdit.text()
    Password = cadastro.lineEdit_2.text()
    sexo = ""
    if(cadastro.radioButton.isChecked()):
        sexo = "M"
    elif(cadastro.radioButton_2.isChecked()):
        sexo = "F"
    try:
        Insert = f'INSERT INTO tb_user(tb_user.tb_user_nome,tb_user.tb_user_email,tb_user.tb_user_pass,tb_user_sexo) VALUES("{Nome}","{Email}","{Password}","{sexo}")'
        cursor.execute(Insert)
        conexao.commit()
        cadastro.label_6.text()
        cadastro.label_6.setText("DEU CERTO")
        cadastro.lineEdit.setText("")
        cadastro.lineEdit_2.setText("")
        cadastro.lineEdit_3.setText("")
        Chamalog()
    except:
        cadastro.label_6.setText("DEU ERRO")
        conexao.close()
def Listar():
    cursor.execute("SELECT*FROM tb_user")
    dados_lidos = cursor.fetchall()
    dash.tableWidget.setRowCount(len(dados_lidos))
    dash.tableWidget.setColumnCount(4)
    for i in range(0, len(dados_lidos)):
        for j in range(0,4):
            dash.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def Deletar():
    linha = dash.tableWidget.currentRow()
    dash.tableWidget.removeRow(linha)
    try:
        cursor.execute("SELECT tb_user_id FROM tb_user")
        dados_id = cursor.fetchall()
        dados_limpo = dados_id[linha][0]
        # # delete = f'DELETE FROM tb_user WHERE tb_user_id="{dados_limpo}"'
        cursor.execute("DELETE FROM tb_user WHERE tb_user_id="+str(dados_limpo))
        conexao.commit()
        print("FOI APAGADO COM SUCESSO",dados_limpo)
    except:
        print("DEU ERRO")   


# FUNÇOES DE CHAMADA E FECHAMENTO DE FORMULARIO
def ChamaCad():
    cadastro.show()
    login.close()
def ChamaDash():
    dash.show()
    login.close()
def Chamalog():
    login.show()
    cadastro.close()
def closeDash():
    dash.close()


app = QtWidgets.QApplication([])
cadastro = uic.loadUi("Ui/cadastro.ui")
login = uic.loadUi("Ui/login.ui")
listar = uic.loadUi("Ui/listar.ui")
dash  = uic.loadUi('Ui/dashboard.ui')


Listar()
dash.dell_btn.clicked.connect(Deletar)
dash.pushButton_2.clicked.connect(closeDash)
cadastro.pushButton.clicked.connect(Cadastro)
login.pushButton.clicked.connect(Login)
login.pushButton_2.clicked.connect(ChamaCad)


# TEST
# listar.pushButton.clicked.connect(Deletar)

login.show()
app.exec()