# what the hell am i doing

from variables import menu_1, menu_2, menu_a, menu_l, menu_u, menu_d, error_unrecognized
import sys

def method_menu_1():
    print(menu_1)
    def method_menu_2():
        print(menu_2)
        selected_command_menu_2 = str.lower(input("Comando: "))
        if selected_command_menu_2 == 'a':
            print(menu_a)
            sys.exit()
        elif selected_command_menu_2 == 'l':
            print(menu_l)
            sys.exit()
        elif selected_command_menu_2 == 'u':
            print(menu_u)
            sys.exit()
        elif selected_command_menu_2 == 'd':
            print(menu_d)
            sys.exit()
        elif selected_command_menu_2 == 'q':
            print(method_menu_1())
        else:
            print(error_unrecognized)
            print(method_menu_2())
    selected_command_menu_1 = str.lower(input("Comando: "))
    if selected_command_menu_1 == 'x':
        sys.exit(f"Saindo...")
    elif selected_command_menu_1 == '1':
        print(method_menu_2())
    elif selected_command_menu_1 == '2':
        print(method_menu_2())
    elif selected_command_menu_1 == '3':
        print(method_menu_2())
    elif selected_command_menu_1 == '4':
        print(method_menu_2())
    elif selected_command_menu_1 == '5':
        print(method_menu_2())
    else:
        print(error_unrecognized)
        print(method_menu_1())
    return selected_command_menu_1