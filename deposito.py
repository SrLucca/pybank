import os
from exittouserscreen import exit_user


def deposit():
    
    while(True):
        
        '''
        ACESSA O SALDO DO USUARIO E O ATUALIZA COM A QUANTIDADE RETIRADA
        '''
        saldo_existente = ''

        saldo_conta = open('saldo.txt','r')
        for saldonaconta in saldo_conta.readlines():
            saldo_existente += saldonaconta

        os.system('cls')
        print("========================= PY BANK =========================")
        print('|                         DEPÓSITO                        |')
        print('|                 para SAIR escreva "sair"                |')
        
        qtd_deposito = int(input('| Insira a quantia a ser DEPOSITADA - R$: '))
        
        user_senha = input('Insira sua senha: ')
        
        arquivo_senha = open('senha.txt','r')
        for senha in arquivo_senha.readlines():
            
            if user_senha != senha:
                print('SENHA INCORRETA!')
                os.system('pause')
                os.system('cls')
                continue
            else:

                novo_saldo = int(saldo_existente) + int(qtd_deposito)
                saldo_conta = open('saldo.txt','w')
                saldo_conta.writelines('{}'.format(f'{novo_saldo}'))
                saldo_conta.close()
                
                
                saldo_conta = open('saldo.txt','r')
                for saldonaconta in saldo_conta.readlines():
                    print('='*33,'\nQUANTIA DEPOSITADA!')
                    print(f'SALDO ATUAL: {saldonaconta}')
                    os.system('pause')
                    os.system('cls')
                    saldo_conta.close()
                    exit_user()
        arquivo_senha.close()
    return