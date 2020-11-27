import os

def changep():
    while(True):
        print("================ PY BANK =================")
        print('|             ALTERAR SENHA              |')
        print('|para sair escreva "sair" na sua senha   |')

        current_password = input('|Digite sua SENHA ATUAL: ')
        
        if current_password == 'sair':
            break
        
        arquivo_senha = open('senha.txt','r')
        for senha in arquivo_senha.readlines():
            
            if current_password != senha:
                print('='*33)
                print('SENHA INCORRETA!')
                os.system('pause')
                os.system('cls')
                arquivo_senha.close()
                continue
            else:
                arquivo_senha.close()
                new_password = input('|Insira a NOVA SENHA: ')
                confirm_password = input('|Repita a NOVA SENHA: ')

                if confirm_password != new_password:
                    print('='*33)
                    print('SENHA INCORRETA!')
                    os.system('pause')
                    os.system('cls')
                    break
                else:
                    arquivo_senha = open('senha.txt','w')
                    arquivo_senha.writelines(new_password)
                    arquivo_senha.close()
                    print('='*33,'\nNOVA SENHA CRIADA')
                    os.system('pause')
                    os.system('cls')
                    break
            
    return