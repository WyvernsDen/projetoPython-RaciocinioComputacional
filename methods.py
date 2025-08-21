# defining methods

from variables import Menu, Messages
import sys

def method_menu_principal():
    print(Menu.principal)
    def method_menu_operacional():
        selected_command_menu_operacional = str.lower(input(Messages.select_command))
        if selected_command_menu_operacional == 'c':
            print(Menu.incluir)
            sys.exit(Messages.exit)
        elif selected_command_menu_operacional == 'l':
            print(Menu.listar)
            sys.exit(Messages.exit)
        elif selected_command_menu_operacional == 'u':
            print(Menu.atualizar)
            sys.exit(Messages.exit)
        elif selected_command_menu_operacional == 'd':
            print(Menu.excluir)
            sys.exit(Messages.exit)
        elif selected_command_menu_operacional == 'q':
            print(method_menu_principal())
        else:
            print(Messages.error_unrecognized)
            print(method_menu_operacional())
    selected_command_menu_principal = str.lower(input(Messages.select_command))
    if selected_command_menu_principal == 'x':
        sys.exit(Messages.exit)
    elif selected_command_menu_principal == '1':
        print(Menu.estudantes)
        print(method_menu_operacional())
    elif selected_command_menu_principal == '2':
        print(Menu.disciplinas)
        print(method_menu_operacional())
    elif selected_command_menu_principal == '3':
        print(Menu.professores)
        print(method_menu_operacional())
    elif selected_command_menu_principal == '4':
        print(Menu.turmas)
        print(method_menu_operacional())
    elif selected_command_menu_principal == '5':
        print(Menu.matriculas)
        print(method_menu_operacional())
    else:
        print(Messages.error_unrecognized)
        print(method_menu_principal())
    return selected_command_menu_principal
