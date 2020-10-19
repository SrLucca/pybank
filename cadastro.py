import os

def singup():
    while(True):
        user = input('Insira seu nome COMPLETO: ')
        cpf = int(input('Insira seu CPF: '))
        try:
            past_archivo = os.mkdir('{}'.format(user))
            directory = 'C:\\Users\\Lucia\\Desktop\\Lucca\\programação'
            os.chdir(r'C:\Users\Lucia\Desktop\Lucca\programação\{}'.format(user))
            archivo_db = open(f'{user}-INFO.txt','w')
            archivo_db.writelines('{}\n{}'.format(user,cpf))
            archivo_db.close()
            print('USUARIO CADASTRADO')
            break
        except FileExistsError:
            print('Usuario ja CADASTRADO.')
            break
    return user, cpf
