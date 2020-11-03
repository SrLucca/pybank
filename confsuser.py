import os
from exitoperations import exitoperation
from changename import changen
from changeold import changeo
from changepassword import changep
from delaccount import delete


def choiceconf():
    os.system('cls')
    while(True):
        print("============ PY BANK ============")
        print('|    CONFIGURAÇÕES DA CONTA     |')
        print('|[1] - Alterar NOME             |')
        print('|[2] - Alterar SENHA            |')
        print('|[3] - Alterar IDADE            |')
        print('|[4] - Encerrar CONTA           |')
        print('|[5] - SAIR                     |')

        try:
            choice = int(input('=================================\nSELECIONE SUA OPÇÃO: '))
            changes(choice)

        except ValueError:
            print('OPÇÃO INVÁLIDA')
            os.system('pause')
            os.system('cls')
            continue
        
        if choice == 5:
            exitoperation()
            os.system('cls')

    return

def changes(choice):
    
    if choice == 1:
        changen()

    if choice == 2:
        changep()

    if choice == 3:
        changeo()

    if choice == 4:
        delete()
        
    return