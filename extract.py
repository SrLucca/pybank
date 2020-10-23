import os

def extrato():
    while(True):
        os.system('cls')
        saldo_conta = open('saldo.txt','r')
        for saldonaconta in saldo_conta.readlines():
            print(f'SALDO ATUAL: {saldonaconta}')
        saldo_conta.close()
        os.system('pause')
        break
        
    return