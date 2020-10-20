import os

def screenuser():
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
            if choice == 5:
                break
        except:
            print('OPÇÃO INVÁLIDA')
            os.system('pause')
            os.system('cls')
            continue
    return choice