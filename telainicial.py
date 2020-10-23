from login import singin
from cadastro import singup
import os

def telainicial():
    '''
    CAPTURA A OPÇÃO DO USUARIO E O REDIRECIONA
    '''
    while(True):
        os.system('cls')
        
        #ENTRA NO DIRETÓRIO CORRETO PARA EVITAR ERROS
        os.chdir(r'C:\Users\Lucia\Desktop\Lucca\programação\usuarios')


        print("============ PY BANK ============")
        print('| LOGIN - [01]                   |')
        print('| CADASTRO - [02]                |')
        print('| SAIR - [03]                    |')
        
        #ESCOLHA DO USUARIO
        choice = int(input('==================================\nSELECIONE SUA OPÇÃO: '))
        
        #ESCOLHA 1 = CHAMA A FUNÇÃO DE LOGIN
        if choice == 1:
            return singin()

        #ESCOLHA 2 = CHAMA A FUNÇÃO DE CADASTRO
        if choice == 2:
            return singup()

        #ESCOLHA 3 = SAI DO PROGRAMA
        if choice == 3:
            break