from ast import Return
from cmath import log
from msilib.schema import Error
from PyQt5 import uic, QtWidgets
import mysql.connector
import pyfiglet

result = pyfiglet.figlet_format("PyQt5 e MYSQL")
print(result)


conexao = mysql.connector.connect(host="localhost",user="root",password="",database="db_user")


# METODO DE LOGIN 
def Login(): 
    global Email, Password
    Email = login.lineEdit.text()
    Password = login.lineEdit_2.text()
    
    if Email =="" and Password =="":
       login.label_4.setText("Digite um Email e Senha!")
    else:
        try:    
            cursor = conexao.cursor()
            # USANDO A FORMATAÇAO .FORMAT PARA FOMATAR O DADO VINDO DA MANEIRA CORRETA
            cursor.execute("SELECT tb_user_pass, tb_user_email FROM tb_user WHERE tb_user_email='{}'".format(Email))
            password_db = cursor.fetchall()

            cursor.execute("SELECT tb_user_permission tb_user_pass, tb_user_email FROM tb_user WHERE tb_user_email='{}'".format(Email))
            permissao_db = cursor.fetchall()

            if Password == password_db[0][0] and permissao_db[0][0] == 1:
                ListarAdm()
                # print("Dados Corretos ADM")

            elif Password == password_db[0][0]:
                login.lineEdit.text()
                login.lineEdit.setText("")  
                login.lineEdit_2.text()
                login.lineEdit_2.setText("")
                Listar()
            else:
                login.label_4.setText("E-mail ou senha Incorretos")
        except ValueError:
            login.label_4.setText("Digite um Email e Senha!", ValueError)
            # print("OCORREU UM ERRO NA VALIDAÇAO DO FORMULARIO",ValueError)
    return conexao
# METODO CADASTRAR 
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
    
    if  Nome=="" or Email =="" or Password =="" or sexo=="":
        cadastro.label_6.setText("PREENCHA TODOS OS CAMPOS!")
        # print("PREENCHA OS CAMPOS PARA PODER PROSEGUIR")
    else:
        try:
            cursor = conexao.cursor()
            Insert = f'INSERT INTO tb_user(tb_user.tb_user_nome,tb_user.tb_user_email,tb_user_pass,tb_user_sexo) VALUES("{Nome}","{Email}", "{Password}","{sexo}")'
            cursor.execute(Insert)
            conexao.commit()
            cadastro.label_6.text()
            cadastro.label_6.setText("CADASTRADO COM SUCESSO!")
            cadastro.lineEdit.setText("")
            cadastro.lineEdit_2.setText("")
            cadastro.lineEdit_3.setText("")
            Chamalog()
        except ValueError:
            cadastro.label_6.setText("OCORREU UM ERRO ",ValueError)
    return conexao
# METODO LISTAR, PARA USUARIO COMUM 
def Listar():
    try:
        dash.tableWidget.hide()   
        dash.cad_btn.hide()
        dash.dell_btn.hide()
        login.close()
        dash.show()
    except ValueError:
        print("OCORREU UM ERRO ",ValueError)
    return conexao

# METODO DELETAR
def Deletar():

    if (dash.tableWidget.cellClicked):
        linha = dash.tableWidget.currentRow()
        dash.tableWidget.removeRow(linha)
        # print('SELECIONADO')

        if (linha>0):
            try:
                cursor = conexao.cursor()
                cursor.execute("SELECT tb_user_id FROM tb_user")
                dados_id = cursor.fetchall()
                dados_limpo = dados_id[linha][0]
                # print(dados_limpo)
                cursor.execute("DELETE FROM tb_user WHERE tb_user_id="+str(dados_limpo))
                conexao.commit()
                # print("FOI APAGADO COM SUCESSO",dados_limpo)
                dash.label_2.text()
                dash.label_2.setText("ID '"+str(dados_limpo)+"' DELETADO!")
            except ValueError:
                print("OCORREU UM ERRO",ValueError)
        else:
            dash.label_2.setText("NAO HÁ MAIS REGISTROS")
        return conexao
    else:
        print('LINHA NAO FOI CLICADA')
# METODO LISTAR, APENAS PARA USUARIOS ADM 
def ListarAdm():
    dash.show()
    login.close()
    dash.tableWidget.show()   
    dash.cad_btn.show()
    dash.dell_btn.show()
    try:
        cursor = conexao.cursor()
        dash.label.text()
        dash.label.setText("Gerenciamento de Usuario")
        cursor.execute("SELECT*FROM tb_user")
        dados_lidos = cursor.fetchall()
        dash.tableWidget.setRowCount(len(dados_lidos))
        dash.tableWidget.setColumnCount(6)
        for i in range(0, len(dados_lidos)):
            for j in range(0,6):
                dash.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    except ValueError:
        print('ERRO',ValueError)
    return conexao



def PegaDados():
        linha = dash.tableWidget.currentRow()
        cursor = conexao.cursor()
        cursor.execute("SELECT tb_user_id FROM tb_user")
        dados_id = cursor.fetchall()
        id = dados_id[linha][0]
        cursor.execute("SELECT*FROM tb_user WHERE tb_user_id="+str(id))       
        usuario = cursor.fetchall()

        global valor_do_id
        valor_do_id = id

        # print(usuario[0][0])
        # print(usuario[0][1])
        dash.id.setText(str(usuario[0][0]))
        dash.nome.setText(str(usuario[0][1]))
        dash.email.setText(str(usuario[0][2]))
        dash.senha.setText(str(usuario[0][3]))

def AlteraDados():
    nome =  dash.nome.text()
    email=  dash.email.text()
    senha=  dash.senha.text()
    try:
        cursor = conexao.cursor()
        cursor.execute("UPDATE tb_user SET tb_user_nome = '{}', tb_user_email ='{}',tb_user_pass='{}' WHERE tb_user_id = {}".format(nome,email,senha,valor_do_id))     
        conexao.commit()
    except ValueError:
        print('ERRO',ValueError)
    return conexao


#  FUNÇOES DE CHAMADA E FECHAMENTO DE FORMULARIO
def ChamaCad():
    cadastro.show()
    login.close()
def Chamalog():
    login.show()
    cadastro.close()
def closeDash():
    login.lineEdit.text()
    login.lineEdit.setText("")  
    login.lineEdit_2.text()
    login.lineEdit_2.setText("")
    dash.close()
    login.show()

  
app = QtWidgets.QApplication([])

cadastro = uic.loadUi('Projeto-PyQt5---CRUD-/Ui/cadastro.ui')
login = uic.loadUi("Projeto-PyQt5---CRUD-/Ui/login.ui")
listar = uic.loadUi("Projeto-PyQt5---CRUD-/Ui/listar.ui")
dash  = uic.loadUi('Projeto-PyQt5---CRUD-/Ui/dashboard.ui')


dash.dell_btn.clicked.connect(Deletar)

dash.tableWidget.doubleClicked.connect(PegaDados)
dash.upt_btn.clicked.connect(AlteraDados)

dash.pushButton_2.clicked.connect(closeDash)
cadastro.pushButton.clicked.connect(Cadastro)
cadastro.pushButton_2.clicked.connect(Chamalog)
login.pushButton.clicked.connect(Login)
login.pushButton_2.clicked.connect(ChamaCad)

# teste 


login.show()
app.exec()