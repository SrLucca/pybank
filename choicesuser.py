from telausuario import screenuser
from confsuser import choiceconf
from exittooptions import exittouseroptions
import os


def ways():
    while(True):
        os.system('cls')
        '''
        CAPTURA A OPÇÃO QUE O USUARIO DESEJA E O REDIRECIONA
        '''
        print("==================== PY BANK ===================")
        print('| OPERAÇÕES BANCÁRIAS - [01]                   |')
        print('| CONFIGURAÇÕES DO USUÁRIO - [02]              |')
        print('| SAIR - [03]                                  |')
        
        try:
            choice = int(input('==================================\nSELECIONE SUA OPÇÃO: '))

        except ValueError:
                print('OPÇÃO INVÁLIDA')
                os.system('pause')
                os.system('cls')
                continue

        if choice == 1:
            screenuser()
        if choice == 2:
            choiceconf()
        if choice == 3:
            exit(0)
        if choice < 1.0 or choice > 3.0:
            print('OPÇÃO INVÁLIDA')
            os.system('pause')
            os.system('cls')
            continue
        
