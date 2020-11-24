import os
from exittouserscreen import exit_user


def saque():
    
    saldo_existente = ''

    saldo_conta = open('saldo.txt','r')
    for saldonaconta in saldo_conta.readlines():
        saldo_existente += saldonaconta

    os.system('cls')
    print("========================= PY BANK =========================")
    print('|                         SAQUE                           |')
    print('|                 para SAIR escreva "sair"                |')
    
    qtd_saque = int(input('| Insira a quantia a ser RETIRADA - R$: '))
    
    user_senha = input('Insira sua senha: ')
    
    arquivo_senha = open('senha.txt','r')
    for senha in arquivo_senha.readlines():
        
        if user_senha != senha:
            print('SENHA INCORRETA!')
            os.system('pause')
            os.system('cls')
            break
        else:
            novo_saldo = int(saldo_existente) - int(qtd_saque)
            if novo_saldo < 0:
                print("SALDO INSUFICIENTE")
                os.system('pause')
                os.system('cls')
                break
            else:
                saldo_conta = open('saldo.txt','w')
                saldo_conta.writelines('{}'.format(novo_saldo))
                saldo_conta.close()

            saldo_conta = open('saldo.txt','r')
            for saldonaconta in saldo_conta.readlines():
                print('='*33,'\nQUANTIA RETIRADA!')
                print(f'SALDO ATUAL: {saldonaconta}')
                os.system('pause')
                os.system('cls')
            saldo_conta.close()
            exit_user()
        arquivo_senha.close()
            
        
    return