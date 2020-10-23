from login import singin
import os
from exittomenu import exit_

list = []


def register(cpf,user,senha,idade):
    '''
    PARTE LOGICA DO CADASTRO
    '''
    while(True):
        #ENTRA NO DIRETÓRIO CORRETO PARA CRIAÇÃO DA PASTA DO USUARIO QUE LEVA SEU CPF
        os.chdir(r'C:\Users\Lucia\Desktop\Lucca\programação\usuarios')

        #VERIFICA SE O USUARIO JA EXISTE
        if cpf in os.listdir():
            print('='*33,'\nUsuario ja CADASTRADO.')
            list.clear()
            os.system('pause')
            os.system('cls')
            break

        else:
            #CRIAÇÃO DA PASTA DO USUARIO QUE LEVA SEU CPF
            past_archivo = os.mkdir('{}'.format(cpf))

            #ENTRA NA PASTA DO USUARIO
            os.chdir(r'C:\Users\Lucia\Desktop\Lucca\programação\usuarios\{}'.format(cpf))
            
            #CRIAÇÃO DO NOME.TXT QUE CONTEM O NOME DO USUARIO
            archivo_db = open(f'nome.txt','w')
            archivo_db.writelines('{}'.format(user))
            archivo_db.close()

            #CRIAÇÃO DO SENHA.TXT QUE CONTEM A SENHA DO USUARIO
            archivo_db_senha = open(f'senha.txt','w')
            archivo_db_senha.writelines('{}'.format(senha))
            archivo_db_senha.close()

            #CRIAÇÃO DA IDADE.TXT QUE CONTEM A IDADE DO USUARIO
            archivo_db_senha = open(f'idade.txt','w')
            archivo_db_senha.writelines('{}'.format(idade))
            archivo_db_senha.close()

            #CONFIRMAÇÃO DO REGISTO
            print('='*33,'\nUSUARIO CADASTRADO')
            list.clear()

            #VOLTA PARA PASTA QUE CONTEM TODOS OS USUARIOS
            os.chdir(r'C:\Users\Lucia\Desktop\Lucca\programação\usuarios')
            os.system('pause')
            os.system('cls')
            continue



def singup():
    '''
    CAPTURA AS INFORMAÇÕES DO USUARIO E AS VALIDA PARA PODER FAZER O REGISTRO(REGISTER)
    '''
    while(True):
        os.system('cls')
        print("============ PY BANK ============")
        print('|        TELA DE CADASTRO       |')
        print('|    para SAIR escreva "sair"   |')
        
        user = input('| Insira seu nome COMPLETO: ')
        #SAIR PARA A TELA INICIAL
        if user == 'sair':
            exit_()
        else:
            pass

        cpf = input('| Insira seu CPF: ')
        #SAIR PARA A TELA INICIAL
        if cpf == 'sair':
            exit_()
        else:
            pass

        senha = input('| Insira sua SENHA: ')
        #SAIR PARA A TELA INICIAL
        if senha == 'sair':
            exit_()
        else:
            pass

        idade = int(input('| Insira sua IDADE: '))
        #SAIR PARA A TELA INICIAL
        if idade == 'sair':
            exit_()
        else:
            pass

        #VALIDAR SE CPF TEM 11 CARACTERES
        for num in cpf:
            list.append(num)
        count_numbers = len(list)
        if count_numbers > 11 or count_numbers < 11:
            print('='*33,'\nCPF INVÁLIDO')
            list.clear()
            os.system('pause')
            os.system('cls')
            break

        #VALIDAR SE O USUARIO TEM MAIS DE 18 ANOS
        elif idade < 18:
            os.system('cls')
            print("================ PY BANK ================")
            print('APENAS MAIORES DE IDADE PODEM CRIAR CONTA')
            os.system('pause')
            break

        #ENVIAR AS INFORMAÇÕES VALIDAS PARA O REGISTRO(REGISTER)
        else:
            int(cpf)
            list.clear()
            register(cpf,user,senha,idade)
            break
    return cpf,user,senha,idade


    