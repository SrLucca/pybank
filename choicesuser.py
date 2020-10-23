from telausuario import screenuser
from confsuser import choiceconf


def ways():
    '''
    CAPTURA A OPÇÃO QUE O USUARIO DESEJA E O REDIRECIONA
    '''
    print("==================== PY BANK ===================")
    print('| OPERAÇÕES BANCÁRIAS - [01]                   |')
    print('| CONFIGURAÇÕES DO USUÁRIO - [02]              |')
    print('| SAIR - [03]                                  |')
    
    choice = int(input('==================================\nSELECIONE SUA OPÇÃO: '))
    if choice == 1:
        screenuser()
    if choice == 2:
        choiceconf()
    if choice == 3:
        exit(0)
