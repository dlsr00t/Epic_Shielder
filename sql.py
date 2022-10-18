import sqlite3
from sqlite3 import Error


def conexaoBanco(caminho):
    try:
        con = sqlite3.connect(caminho)
    except Error as er:
        print(er)
    else:
        print("\033[32mConectado ao banco!\033[m")
        return con

def createTable(conexao):
    try:
        tsql = """
        CREATE TABLE log (
        NUSUARIO INTEGER PRIMARY KEY AUTOINCREMENT,
        USUARIO VARCHAR(200), 
        SENHA VARCHAR(200)
        );
        """
        conexao.cursor()
        conexao.execute(tsql)
    except Error as er:
        print(f'\033[1;31m{str(er)}\033[m')
    else:
        print("\033[32mTabela criada!\033[m")


def userCreator(conexao, usuario, senha):
    try:
        query = f"""INSERT INTO log(USUARIO, SENHA)
                    VALUES('{usuario}', '{senha}'); 
        """
        conexao.cursor()
        conexao.execute(query)
        conexao.commit()
    except Error as er:
        print(f'\033[1;31m{str(er)}\033[m')
    else:
        print("\033[32mValores inseridos com sucesso!\033[m")

def userDelete(conexao, usuario):
    try:
        query = f"""
        DELETE FROM log WHERE USUARIO={usuario};

        """
        conexao.cursor()
        conexao.execute(query)
        conexao.commit()
    except Error as er:
        print(er)
    else:
        print("\033[32mValores deletados com sucesso!\033[m")

def viewAllUser(conexao):
    try:
        query = f"""
        SELECT * FROM log;
        """
        conexao.cursor()
        variavel = conexao.execute(query)
        variavel = variavel.fetchall()
        print(variavel)
        #conexao.commit()

    except Error as er:
        print(er)

con = conexaoBanco("cash_bank.db")

#createTable(con)
#userCreator(con, "clecio", "87654321")
#userDelete(con, "clecio")
viewAllUser(con)
userDelete(con, 1)