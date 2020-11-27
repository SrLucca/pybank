import os
import shutil



def delete():
    while(True):
        os.system('cls')
        print("================= PY BANK ====================")
        print('|               ENCERRAR CONTA               |')
        print('|    para SAIR escreva "sair" na sua SENHA   |')
        cpf = input('|Digite seu CPF: ')
        current_password = input('|Digite sua SENHA: ')
        
        diretorio_raiz = os.path.dirname(__file__)

        if current_password == 'sair':
            break

        if cpf not in os.listdir('{}\\usuarios'.format(diretorio_raiz)):

            print('='*33,'\nSEU CPF ESTA INCORRETO')
            os.system('pause')
            os.system('cls')
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
                os.chdir('{}\\usuarios'.format(diretorio_raiz))
                shutil.rmtree('{}'.format(cpf))
                os.chdir('{}'.format(diretorio_raiz))
                print('='*33,'\nCONTA DELETADA')
                os.system('pause')
                os.system('cls')
                exit(0)

    return