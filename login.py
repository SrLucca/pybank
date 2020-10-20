import os
from telausuario import screenuser

def singin():
    while(True):
        try:
            user_login = input('Insira seu CPF COMPLETO: ')
            name_user = input('Insira seu NOME: ')
            try:
                past_archivo = os.mkdir('{}'.format(user_login))
                print('USUARIO NÃO CADASTRADO')
                os.removedirs((r'C:\Users\Lucia\Desktop\Lucca\programação\{}'.format(user_login)))
                break
            except FileExistsError:
                print(f'Olá, {name_user}!')
                screenuser()
                break
        except:
            continue
    return user_login