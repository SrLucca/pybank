import os

def screenuser():
    '''
    CAPTURA A OPÇÃO DO USUARIO E O REDIRECIONA PARA A OPERAÇÃO BANCÁRIA ESCOLHIDA
    '''
    while(True):
        os.system('cls')
        print("============ PY BANK ============")
        print('| DEPÓSITOS - [01]              |')
        print('| SAQUES - [02]                 |')
        print('| TRANSFERÊNCIAS - [03]         |')
        print('| EXTRATO - [04]                |')
        print('| SAIR - [05]                   |')
        choice = int(input('==================================\nSELECIONE SUA OPÇÃO: '))
        if choice == 5:
            exit(0)
    return choice