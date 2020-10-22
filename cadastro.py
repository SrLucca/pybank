from login import singin
import os

list = []


def register(cpf,user,senha):
    while(True):
        try:
            past_archivo = os.mkdir('{}'.format(cpf))
            directory = 'C:\\Users\\Lucia\\Desktop\\Lucca\\programação'
            os.chdir(r'C:\Users\Lucia\Desktop\Lucca\programação\{}'.format(cpf))
            archivo_db = open(f'nome.txt','w')
            archivo_db.writelines('{}'.format(user))
            archivo_db.close()
            archivo_db_senha = open(f'senha.txt','w')
            archivo_db_senha.writelines('{}'.format(senha))
            archivo_db_senha.close()
            print('USUARIO CADASTRADO')
            list.clear()
            os.chdir(r'C:\Users\Lucia\Desktop\Lucca\programação')
            os.system('pause')
            os.system('cls')
            continue
        except FileExistsError:
            print('Usuario ja CADASTRADO.')
            list.clear()
            os.system('pause')
            os.system('cls')
            singin()
            continue


def singup():
    while(True):
        os.system('cls')
        print('TELA DE CADASTRO')
        user = input('Insira seu nome COMPLETO: ')
        cpf = input('Insira seu CPF: ')
        senha = input('Insira sua SENHA: ')
        for num in cpf:
            list.append(num)
        count_numbers = len(list)
        if count_numbers > 11 or count_numbers < 11:
            print('CPF INVÁLIDO')
            list.clear()
            os.system('pause')
            os.system('cls')
            continue
        else:
            int(cpf)
            list.clear()
            register(cpf,user,senha)
            break
    return cpf,user,senha


    