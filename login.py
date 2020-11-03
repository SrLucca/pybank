import os
from telausuario import screenuser
from choicesuser import ways
from exittomenu import exit_


def singin():
    '''
    CAPTURA AS INFORMAÇÃO DO USUARIO E AS VERIFICA PARA FAZER O LOGIN
    '''
    while(True):
        os.system('cls')
        print("============ PY BANK ============")
        print('|         TELA DE LOGIN         |')
        print('|    para SAIR escreva "sair"   |')

        #ENTRA NO DIRETÓRIO CERTO PARA EVITAR ERROS
        os.chdir(r'C:\Users\Lucia\Documents\GitHub\pybank\usuarios')

        #CPF DO USUARIO
        user_login = input('| Insira seu CPF COMPLETO: ')
        
        #SAIR PARA A TELA INICIAL
        if user_login == 'sair':
            exit_()
        else:
            pass
        
        #SENHA DO USUARIO
        user_senha = input('| Insira sua SENHA: ')
        
        #SAIR PARA A TELA INICIAL
        if user_senha == 'sair':
            exit_()
        else:
            pass
        
        #VALIDAR SE O USUARIO REALMENTE EXISTE APARTIR DO CPF
        if user_login not in os.listdir():
            print('='*33,'\nUSUARIO NÃO CADASTRADO')
            os.system('pause')
            os.system('cls')
            continue
        
        #SE EXISTIR...
        else:
            #ENTRA NA PASTA ONDE CONTEM AS INFORMAÇÕES DO USUARIO, QUE LEVA SEU CPF
            os.chdir(r'C:\Users\Lucia\Documents\GitHub\pybank\usuarios\{}'.format(user_login))
            
            #VALIDAÇÃO DA SENHA ANTES PEDIDA
            arquivo_senha = open('senha.txt','r')
            for senha in arquivo_senha.readlines():
                if user_senha != senha:
                    print('SENHA INCORRETA!')
                    os.system('pause')
                    os.system('cls')
                    continue

                #SE TUDO ESTIVER CORRETO, ENTRA NO ARQUIVO NOME.TXT E CAPTURA O NOME DO USUARIO PARA DAR OLÁ
                else:
                    arquivo_name = open('nome.txt','r')
                    os.system('cls')
                    for name in arquivo_name.readlines():
                        print(f'Olá, {name}')
                    arquivo_name.close()
                    os.system('pause')
                    
                    #MANDAR O USUARIO PARA AS OPÇÕES - OPERAÇÕES OU CONFIGURAÇÕES
                    ways()
                    break
    return user_login, user_senha


