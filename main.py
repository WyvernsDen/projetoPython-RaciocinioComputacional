# Daniel Tivirolli Mariotto
# ADS

import sys

# defining strings and simple methods
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

error_unrecognized = "\nErro: comando não reconhecido.\n"
error_dev = "\nErro: comando em desenvolvimento."
msg_exit = "\nSaindo..."
select_command = "Informe o comando desejado: "

def press_enter():
    input("\nPressione `Enter` para continuar.")

class Lists:
    estudantes_nomes = []

# defining methods for the menu loops and CRUD
def main_menu():
    while True:
        choice = str.lower(input(select_command))
        if choice == '1':
            print(Menu.estudantes)
            crud_estudantes()
        elif choice == '2':
            print(error_dev)
            press_enter()
            print(Menu.main)
            continue
        elif choice == '3':
            print(error_dev)
            press_enter()
            print(Menu.main)
            continue
        elif choice == '4':
            print(error_dev)
            press_enter()
            print(Menu.main)
            continue
        elif choice == '5':
            print(error_dev)
            press_enter()
            print(Menu.main)
            continue
        elif choice == 'x':
            sys.exit(msg_exit)
        else:
            print(error_unrecognized)
            continue

def crud_estudantes():
    while True:
        choice = str.lower(input(select_command))
        if choice == 'c':
            estudante = input("\nInforme o nome do(a) estudante: ")
            Lists.estudantes_nomes.append(estudante)
            print(f"\nEstudante `{estudante}` foi incluído(a) com êxito.")
            press_enter()
            print(Menu.estudantes)
            continue
        elif choice == 'l':
            if len(Lists.estudantes_nomes) == 0:
                print("\nNenhum estudante foi encontrado.")
            else:
                print(f"\nTotal de {len(Lists.estudantes_nomes)} estudante(s) encontrado(s): ")
                for estudante in Lists.estudantes_nomes:
                    print(estudante)
            press_enter()
            print(Menu.estudantes)
            continue
        elif choice == 'u':
            print(error_dev)
            press_enter()
            print(Menu.estudantes)
            continue
        elif choice == 'd':
            print(error_dev)
            press_enter()
            print(Menu.estudantes)
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
