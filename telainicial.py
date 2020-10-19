from login import singin
from cadastro import singup

def telainicial(choice):
    if choice == 1:
        return singin()
    if choice == 2:
        return singup()