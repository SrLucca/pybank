import os
from deposito import deposit
from extract import extrato
from withdrawals import saque
from transfer import transferto
from exitoperations import exitoperation

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
        try:
            choice = int(input('==================================\nSELECIONE SUA OPÇÃO: '))
        except ValueError:
            print('OPÇÃO INVÁLIDA')
            os.system('pause')
            os.system('cls')
            continue

        if choice == 5:
            os.system('cls')
            exitoperation()

        if choice == 1:
            deposit()
        
        if choice == 2:
            saque()
        
        if choice == 3:
            transferto()

        if choice == 4:
            extrato()

    return choice