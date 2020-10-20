import os
from telausuario import screenuser

def singin():
    while(True):
        user_login = input('Insira seu CPF COMPLETO: ')
        try:
            past_archivo = os.mkdir('{}'.format(user_login))
            print('USUARIO NÃO CADASTRADO')
            os.removedirs((r'C:\Users\Lucia\Desktop\Lucca\programação\{}'.format(user_login)))
            break
        except FileExistsError:
            os.chdir(r'C:\Users\Lucia\Desktop\Lucca\programação\{}'.format(user_login))
            print(f'Olá,{os.listdir()}')
            screenuser()
            break
    return user_login