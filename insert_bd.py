import os
import mysql.connector
from mysql.connector import Error
from bd import connect

#insere os dados no banco de dados ja conectado
def insert(nome,cpf,email,idade,numero):

    conn = connect()
    try:
        if conn.is_connected():
            insert_data = f"""INSERT INTO clientes
                                (nome, CPF, email, idade, telefone) 
                                VALUE 
                                ({nome},{cpf},{email},{idade},{numero})
                                """
            cursor = conn.cursor()
            cursor.execute(insert_data)
            conn.commit()
            printn(cursor.rowcount, "Cliente Cadastrado!")
            cursor.close()
            os.system('pause')
            exit(0)
    except Error as erro:
        print(f"Erro ao conectar ao DATABASE: {erro}")
        os.system('pause')
        exit(0)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Conexao finalizada.")
            os.system('pause')
            exit(0)
    return
    '''
    `id` int NOT NULL AUTO_INCREMENT,
    `nome` varchar(200) NOT NULL,
    `CPF` int NOT NULL,
    `email` varchar(200) NOT NULL,
    `idade` varchar(3) NOT NULL,
    `telefone` varchar(9) NOT NULL,
    '''