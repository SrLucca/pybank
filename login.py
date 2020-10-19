import os

def singin():
    while(True):
        user_login = input('Isira seu NOME COMPLETO: ')
        try:
            past_archivo = os.mkdir('{}'.format(user_login))
            print('USUARIO NÃO CADASTRADO')
            os.removedirs((r'C:\Users\Lucia\Desktop\Lucca\programação\{}'.format(user_login)))
            break
        except FileExistsError:
            print(f'Olá, {user_login}!')
            break
    return user_login