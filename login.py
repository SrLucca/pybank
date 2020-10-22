import os
from telausuario import screenuser

def singin():
    while(True):
        os.chdir(r'C:\Users\Lucia\Desktop\Lucca\programação')
        user_login = input('Insira seu CPF COMPLETO: ')
        user_senha = input('Insira sua SENHA: ')
        
        if user_login not in os.listdir():
            print('USUARIO NÃO CADASTRADO')
            os.system('pause')
            os.system('cls')
            continue

        else:
            os.chdir(r'C:\Users\Lucia\Desktop\Lucca\programação\{}'.format(user_login))
            arquivo_senha = open('senha.txt','r')
            for senha in arquivo_senha.readlines():
                if user_senha != senha:
                    print('SENHA INCORRETA!')
                    os.system('pause')
                    os.system('cls')
                    continue
                else:
                    arquivo_name = open('nome.txt','r')
                    for name in arquivo_name.readlines():
                        print(f'Olá, {name}')
                    arquivo_name.close()
                    os.system('pause')
                    screenuser()
                    break
    return user_login, user_senha