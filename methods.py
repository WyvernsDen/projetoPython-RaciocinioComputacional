# what the hell am i doing

from variables import menu1, menu2
import sys

def method_menu1():
    print(menu1)
    def method_menu2():
        print(menu2)
        selected_command_menu2 = str.lower(input("Command: "))
        if selected_command_menu2 == 'c':
            print(f"Selected: {selected_command_menu2}\nStill in development.\nExiting...")
            sys.exit()
        elif selected_command_menu2 == 'p':
            print(f"Selected: {selected_command_menu2}\nStill in development.\nExiting...")
            sys.exit()
        elif selected_command_menu2 == 'd':
            print(f"Selected: {selected_command_menu2}\nStill in development.\nExiting...")
            sys.exit()
        elif selected_command_menu2 == 'x':
            print(f"Selected: {selected_command_menu2}")
            print(method_menu1())
        else:
            print("Error: not a command")
    selected_command_menu1 = str.lower(input("Command: "))
    if selected_command_menu1 == 'q':
        sys.exit(f"Selected: {selected_command_menu1}\nExiting...")
    elif selected_command_menu1 == 'a':
        print(f"Selected: {selected_command_menu1}")
        print(method_menu2())
    elif selected_command_menu1 == 'b':
        print(f"Selected: {selected_command_menu1}")
        print(method_menu2())
    elif selected_command_menu1 == 'c':
        print(f"Selected: {selected_command_menu1}")
        print(method_menu2())
    elif selected_command_menu1 == 'd':
        print(f"Selected: {selected_command_menu1}")
        print(method_menu2())
    else:
        print("Error: not a command")
    return selected_command_menu1