import os
import shutil

usuario_destino = os.getcwd()

def delete():
    while(True):
        print("============ PY BANK ============")
        print('|         ENCERRAR CONTA        |')
        cpf = input('|Digite seu CPF: ')
        current_password = input('|Digite sua SENHA: ')
            
        if current_password == 'sair':
            break
        
        arquivo_senha = open('senha.txt','r')
        
        for senha in arquivo_senha.readlines():

            if current_password != senha:
                print('='*33)
                print('SENHA INCORRETA!')
                os.system('pause')
                os.system('cls')
                continue
            else:
                arquivo_senha.close()
                usuario_destino += '\\usuarios'
                shutil.rmtree('{}'.format(cpf))
                print('='*33,'CONTA DELETADA')
                os.system('pause')
                os.system('cls')
                exit(0)

    return