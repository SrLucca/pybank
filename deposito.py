import os
from exittouserscreen import exit_user


def deposit():
    
    while(True):
        os.system('cls')
        
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
        print('|             para SAIR escreva "sair" na SENHA           |')
        
        try:
            qtd_deposito = float(input('| Insira a quantia a ser DEPOSITADA - R$: '))


        except ValueError:
            print('OPÇÃO INVÁLIDA')
            os.system('pause')
            os.system('cls')
            break
        
        user_senha = input('Insira sua senha: ')

        if user_senha == 'sair':
            exit_user()
        
        arquivo_senha = open('senha.txt','r')
        for senha in arquivo_senha.readlines():
            
            if user_senha != senha:
                print('SENHA INCORRETA!')
                os.system('pause')
                os.system('cls')
                arquivo_senha.close()
                continue
            else:

                arquivo_senha.close()
                novo_saldo = float(saldo_existente) + float(qtd_deposito)
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
        
    return