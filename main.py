import os
from telainicial import telainicial
while(True):
    os.system('cls')
    os.chdir(r'C:\Users\Lucia\Desktop\Lucca\programação')
    print("============ PY BANK ============")
    print('| LOGIN - [01]                   |')
    print('| CADASTRO - [02]                |')
    print('| SAIR - [03]                    |')
    try:
        choice = int(input('==================================\nSELECIONE SUA OPÇÃO: '))
        if choice == 3:
            break
        else:
            telainicial(choice)
    except:
        print('OPÇÃO INVÁLIDA')
        os.system('pause')
        os.system('cls')
        continue