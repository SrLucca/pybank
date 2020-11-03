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
        os.chdir(r'C:\Users\Lucia\Documents\GitHub\pybank\usuarios')


        print("============ PY BANK ============")
        print('| LOGIN - [01]                   |')
        print('| CADASTRO - [02]                |')
        print('| SAIR - [03]                    |')
        
        #ESCOLHA DO USUARIO
        try:
            choice = int(input('==================================\nSELECIONE SUA OPÇÃO: '))
            if choice == 3:
                break
            firstchoice(choice)
        except ValueError:
            print('OPÇÃO INVÁLIDA')
            os.system('pause')
            os.system('cls')
            continue


def firstchoice(choice):

    while(True):
        #ESCOLHA 1 = CHAMA A FUNÇÃO DE LOGIN
        if choice == 1:
            return singin()

        #ESCOLHA 2 = CHAMA A FUNÇÃO DE CADASTRO
        if choice == 2:
            return singup()
    return