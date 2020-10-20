import os

list = []


def register(cpf,user):
    while(True):
        try:
            past_archivo = os.mkdir('{}'.format(cpf))
            directory = 'C:\\Users\\Lucia\\Desktop\\Lucca\\programação'
            os.chdir(r'C:\Users\Lucia\Desktop\Lucca\programação\{}'.format(cpf))
            archivo_db = open(f'{user}.txt','w')
            archivo_db.writelines('Nome: {}\nCPF: {}'.format(user,cpf))
            archivo_db.close()
            print('USUARIO CADASTRADO')
            list.clear()
            os.chdir(r'C:\Users\Lucia\Desktop\Lucca\programação')
            os.system('pause')
            os.system('cls')
            break
        except FileExistsError:
            print('Usuario ja CADASTRADO.')
            list.clear()
            os.system('pause')
            os.system('cls')
            break


def singup():
    while(True):
        user = input('Insira seu nome COMPLETO: ')
        cpf = input('Insira seu CPF: ')
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
            register(cpf,user)
            break
    return cpf,user


    