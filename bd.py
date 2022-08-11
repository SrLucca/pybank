import os
import mysql.connector

#conecta ao banco de dados 'banco'
def connect():

    con = mysql.connector.connect(host='localhost',database='banco',user='root',password='@Lucca123_')
    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão ",db_info)
        cursor = con.cursor()
        cursor.execute("select database();")
        linha = cursor.fetchone()
        print("Conectado ao banco de dados ",linha)
        os.system('pause')
    '''
    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada")
    '''
    
    return con