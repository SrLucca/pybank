import os
from changepassword import changep
from delaccount import delete


def choiceconf():
    
    while(True):
        os.system('cls')
        print("============ PY BANK ============")
        print('|    CONFIGURAÇÕES DA CONTA     |')
        print('|[1] - Alterar SENHA            |')
        print('|[2] - Encerrar CONTA           |')
        print('|[3] - SAIR                     |')

        try:
            choice = int(input('=================================\nSELECIONE SUA OPÇÃO: '))
            changes(choice)

        except ValueError:
            print('OPÇÃO INVÁLIDA')
            os.system('pause')
            os.system('cls')
            continue
        
        if choice == 3:
            break
            os.system('cls')

    return

def changes(choice):
    
    if choice == 1:
        changep()
    
    if choice == 2:
        delete()

        
    return