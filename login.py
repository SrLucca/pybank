import os
from telausuario import screenuser

def singin():
    while(True):
        os.chdir(r'C:\Users\Lucia\Desktop\Lucca\programação')
        user_login = input('Insira seu CPF COMPLETO: ')
        if user_login not in os.listdir():
            print('USUARIO NÃO CADASTRADO')
            break
        else:
            os.chdir(r'C:\Users\Lucia\Desktop\Lucca\programação\{}'.format(user_login))
            print(f'Olá,{os.listdir()}')
            screenuser()
            break
    return user_login