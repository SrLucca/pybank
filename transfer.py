import os
from exittouserscreen import exit_user

def transferto():

    while(True):

        print("========================= PY BANK =========================")
        print('|                      TRANSFERÊNCIA                      |')
        print('|                 para SAIR escreva "sair"                |')

        user = input('|Insira SEU CPF: ')
        to_user = input('|Insira o CPF do USUARIO a quem você irá transferir: ')
        qtd = input('|Insira o VALOR a ser transferido - R$: ')

        
        os.chdir(r'C:\Users\Lucia\Documents\GitHub\pybank\usuarios')

        if user not in os.listdir():
            print('='*33,'\nSEU CPF ESTA INCORRETO')
            os.system('pause')
            os.system('cls')
            break

        if to_user not in os.listdir():
            print('='*33,'\nUSUARIO NÃO CADASTRADO')
            os.system('pause')
            os.chdir(r'C:\Users\Lucia\Documents\GitHub\pybank\usuarios\{}'.format(user))
            os.system('cls')
            exit_user()

        else:
            os.chdir(r'C:\Users\Lucia\Documents\GitHub\pybank\usuarios{}'.format(user))
            saldo_exist = ''
            confer_saldo = open('saldo.txt','r')
            for saldo in confer_saldo.readlines():
                saldo_exist += saldo
                confer_saldo.close()


                if int(saldo_exist) - int(qtd) < 0:
                    print('='*33,'\nSALDO INSUFICIENTE PARA COMPLETAR A OPERAÇÃO')
                    os.system('pause')
                    os.system('cls')
                    exit_user()

                    #SE EXISTIR...
                else:
                    os.chdir(r'C:\Users\Lucia\Documents\GitHub\pybank\usuarios\{}'.format(user))
                    
                    update_saldo = open('saldo.txt','w')
                    new_saldo = int(saldo_exist) - int(qtd)
                    update_saldo.writelines(f'{new_saldo}')
                    update_saldo.close()

                    os.chdir(r'C:\Users\Lucia\Documents\GitHub\pybank\usuarios')
                    os.chdir(r'C:\Users\Lucia\Documents\GitHub\pybank\usuarios\{}'.format(to_user))
                    
                    saldo_existente = ''

                    saldo_conta = open('saldo.txt','r')
                    for saldonaconta in saldo_conta.readlines():
                        saldo_existente += saldonaconta
                    
                        saldo_user = open('saldo.txt','w')
                        novo_saldo = int(saldo_existente) + int(qtd)
                        saldo_conta = open('saldo.txt','w')
                        saldo_conta.writelines('{}'.format(novo_saldo))
                        saldo_conta.close()
                    print('='*33,'\nQUANTIA DEPOSITADA!')
                    os.system('pause')
                    os.chdir(r'C:\Users\Lucia\Documents\GitHub\pybank\usuarios\{}'.format(user))
                    os.system('cls')
                    exit_user()
    
    return