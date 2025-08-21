# what the hell am i doing
# ez dubs just like java (i still dont know wtf doing a week later)

from variables import menu, erro
import sys

def method_menu_principal():
    print(menu.principal)
    def method_menu_operacional():
        selected_command_menu_operacional = str.lower(input("Comando: "))
        if selected_command_menu_operacional == 'c':
            print(menu.incluir)
            sys.exit()
        elif selected_command_menu_operacional == 'l':
            print(menu.listar)
            sys.exit()
        elif selected_command_menu_operacional == 'u':
            print(menu.atualizar)
            sys.exit()
        elif selected_command_menu_operacional == 'd':
            print(menu.excluir)
            sys.exit()
        elif selected_command_menu_operacional == 'q':
            print(method_menu_principal())
        else:
            print(erro.nao_reconhecido)
            print(method_menu_operacional())
    selected_command_menu_principal = str.lower(input("Comando: "))
    if selected_command_menu_principal == 'x':
        sys.exit(f"Saindo...")
    elif selected_command_menu_principal == '1':
        print(menu.estudantes)
        print(method_menu_operacional())
    elif selected_command_menu_principal == '2':
        print(menu.disciplinas)
        print(method_menu_operacional())
    elif selected_command_menu_principal == '3':
        print(menu.professores)
        print(method_menu_operacional())
    elif selected_command_menu_principal == '4':
        print(menu.turmas)
        print(method_menu_operacional())
    elif selected_command_menu_principal == '5':
        print(menu.matriculas)
        print(method_menu_operacional())
    else:
        print(erro.nao_reconhecido)
        print(method_menu_principal())
    return selected_command_menu_principal