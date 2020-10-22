from login import singin
from cadastro import singup
import os

def telainicial():
    while(True):
        os.system('cls')
        os.chdir(r'C:\Users\Lucia\Desktop\Lucca\programação')
        print("============ PY BANK ============")
        print('| LOGIN - [01]                   |')
        print('| CADASTRO - [02]                |')
        print('| SAIR - [03]                    |')
        
        choice = int(input('==================================\nSELECIONE SUA OPÇÃO: '))
        if choice == 1:
            return singin()
        if choice == 2:
            return singup()
        if choice == 3:
            break