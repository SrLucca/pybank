import os

def deposit():
    '''
    ACESSA O SALDO DO USUARIO E O ATUALIZA COM A QUANTIDADE DEPOSITADA
    '''
    saldo_existente = ''

    saldo_conta = open('saldo.txt','r')
    for saldonaconta in saldo_conta.readlines():
        saldo_existente += saldonaconta

    os.system('cls')
    print("========================= PY BANK =========================")
    print('|                      TELA DE LOGIN                      |')
    print('|                 para SAIR escreva "sair"                |')
    
    qtd_deposito = int(input('| Insira a quantia a ser depositada - R$: '))
    
    user_senha = input('Insira sua senha: ')
    
    arquivo_senha = open('senha.txt','r')
    for senha in arquivo_senha.readlines():
        
        if user_senha != senha:
            print('SENHA INCORRETA!')
            os.system('pause')
            os.system('cls')
            exit(0)
        else:

            novo_saldo = int(saldo_existente) + int(qtd_deposito)
            saldo_conta = open('saldo.txt','w')
            saldo_conta.writelines('{}'.format(novo_saldo))
            saldo_conta.close()
            
            
            saldo_conta = open('saldo.txt','r')
            for saldonaconta in saldo_conta.readlines():
                print('='*33,'\nSALDO DEPOSITADO!')
                print(f'SALDO ATUAL: {saldonaconta}')
            saldo_conta.close()
            exit()
    return