# defining methods

from variables import Menu, Messages
import sys

def main_menu():
    while True:
        choice = str.lower(input(Messages.select_command))
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
            sys.exit(f"Saindo...")
        else:
            print(Messages.error_unrecognized)
            continue

def crud():
    while True:
        choice = str.lower(input(Messages.select_command))
        if choice == 'c':
            print(Messages.error_dev)
            continue
        elif choice == 'l':
            print(Messages.error_dev)
            continue
        elif choice == 'u':
            print(Messages.error_dev)
            continue
        elif choice == 'd':
            print(Messages.error_dev)
            continue
        elif choice == 'q':
            print(Menu.main)
            main_menu()
            break
        else:
            print(Messages.error_unrecognized)
            continue