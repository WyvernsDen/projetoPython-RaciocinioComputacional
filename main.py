# Daniel Tivirolli Mariotto
# ADS

import sys

# defining the strings beforehand to make the code easier to read
class Menu:
    main = ("\n=============  Menu Principal  =============\n\n"
             "1 - Estudantes\n"
             "2 - Disciplinas\n"
             "3 - Professores\n"
             "4 - Turmas\n"
             "5 - Matrículas\n"
             "x - Sair\n")
    estudantes = ("\n=====  Menu Operacional  [Estudantes]  =====\n\n"
             "c - Incluir\n"
             "l - Listar\n"
             "u - Atualizar\n"
             "d - Excluir\n"
             "q - Menu Principal\n")
    disciplinas = ("\n=====  Menu Operacional  [Disciplinas]  =====\n\n"
             "c - Incluir\n"
             "l - Listar\n"
             "u - Atualizar\n"
             "d - Excluir\n"
             "q - Menu Principal\n")
    professores = ("\n=====  Menu Operacional  [Professores]  =====\n\n"
             "c - Incluir\n"
             "l - Listar\n"
             "u - Atualizar\n"
             "d - Excluir\n"
             "q - Menu Principal\n")
    turmas = ("\n=======  Menu Operacional  [Turmas]  =======\n\n"
             "c - Incluir\n"
             "l - Listar\n"
             "u - Atualizar\n"
             "d - Excluir\n"
             "q - Menu Principal\n")
    matriculas = ("\n=====  Menu Operacional  [Matrículas]  =====\n\n"
             "c - Incluir\n"
             "l - Listar\n"
             "u - Atualizar\n"
             "d - Excluir\n"
             "q - Menu Principal\n")

class CRUD:
    incluir = ("\n---------  Incluir  ---------\n\n"
              "Ainda em desenvolvimento.")
    listar = ("\n----------  Lista  ----------\n\n"
              "Ainda em desenvolvimento.")
    atualizar = ("\n--------  Atualizar  --------\n\n"
              "Ainda em desenvolvimento.")
    excluir = ("\n---------  Excluir  ---------\n\n"
              "Ainda em desenvolvimento.")

error_unrecognized = "Erro: comando não reconhecido."
error_dev = "Erro: comando em desenvolvimento."
exit_msg = "\nSaindo...\n"
select_command = "Selecione um comando: "

# defining methods for the menu loop and the CRUD system
def main_menu():
    while True:
        choice = str.lower(input(select_command))
        if choice == '1':
            print(Menu.estudantes)
            crud()
        elif choice == '2':
            print(Menu.disciplinas)
            crud()
        elif choice == '3':
            print(Menu.professores)
            crud()
        elif choice == '4':
            print(Menu.turmas)
            crud()
        elif choice == '5':
            print(Menu.matriculas)
            crud()
        elif choice == 'x':
            sys.exit(exit_msg)
        else:
            print(error_unrecognized)
            continue

def crud():
    while True:
        choice = str.lower(input(select_command))
        if choice == 'c':
            print(error_dev)
            continue
        elif choice == 'l':
            print(error_dev)
            continue
        elif choice == 'u':
            print(error_dev)
            continue
        elif choice == 'd':
            print(error_dev)
            continue
        elif choice == 'q':
            print(Menu.main)
            main_menu()
            break
        else:
            print(error_unrecognized)
            continue

# prints menu and starts method
print(Menu.main)
main_menu()
