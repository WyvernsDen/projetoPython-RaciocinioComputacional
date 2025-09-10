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
    estudantes_modificar = ("\n===========  Modificar Estudante  ===========\n\n"
                          "1 - Código\n"
                          "2 - Nome\n"
                          "3 - CPF\n"
                          "b - Voltar\n")

error_unrecognized = "\nErro: comando não reconhecido.\n"
error_dev = "\nErro: comando em desenvolvimento."
msg_exit = "\nSaindo..."
select_command = "Informe o comando desejado: "

def press_enter():
    input("\nPressione `Enter` para continuar.")

lista_estudantes = []

# defining methods for the menu loops and CRUD
def main_menu():
    while True:
        choice = str.lower(input(select_command))
        if choice == '1':
            print(Menu.estudantes)
            crud_estudantes()
            break
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
            press_enter()
            continue

def crud_estudantes():
    while True:
        choice = str.lower(input(select_command))
        if choice == 'c':
            if len(lista_estudantes) == 0:
                estudante_codigo = 1
            else:
                estudante_codigo = len(lista_estudantes) + 1
            estudante_nome = input("\nInforme o nome do(a) estudante: ")
            estudante_cpf = input("\nInforme o CPF do(a) estudante: ")
            estudante_dict = {
                "codigo": estudante_codigo,
                "nome": estudante_nome,
                "cpf": estudante_cpf
            }
            lista_estudantes.append(estudante_dict)
            print(f"\nEstudante `N.º{estudante_codigo}; Nome:{estudante_nome}; CPF:{estudante_cpf}` foi incluído(a) com êxito.")
            print(lista_estudantes)
            press_enter()
            print(Menu.estudantes)
        elif choice == 'l':
            if len(lista_estudantes) == 0:
                print("\nNenhum estudante foi encontrado.")
            else:
                print(f"\nTotal de {len(lista_estudantes)} estudante(s) encontrado(s): ")
                for dicionario_listar in lista_estudantes:
                    print(f"N.º{dicionario_listar["codigo"]}; "
                          f"Nome: {dicionario_listar["nome"]}; "
                          f"CPF: {dicionario_listar["cpf"]}")
            press_enter()
            print(Menu.estudantes)
            continue
        elif choice == 'u':
            if len(lista_estudantes) == 0:
                print("\nNenhum estudante foi encontrado.")
            else:
                estudante_modificar = None
                codigo_estudante_modificar = input("\nInforme o código do estudante á ser modificado: ")
                for dicionario_modificar in lista_estudantes:
                    if dicionario_modificar["codigo"] == int(codigo_estudante_modificar):
                        estudante_modificar = dicionario_modificar
                        print(f"\nVocê escolheu o(a) estudante N.º{codigo_estudante_modificar};"
                              f" Nome: {dicionario_modificar["nome"]}; "
                              f"CPF: {dicionario_modificar["cpf"]}.")
                        break
                while True:
                    if estudante_modificar is None:
                        print(f"\nEstudante com código {codigo_estudante_modificar} não encontrado.")
                        press_enter()
                    else:
                        print(Menu.estudantes_modificar)
                        opcao_modificar = str.lower(input(select_command))
                        if opcao_modificar == '1':
                            codigo_antigo = estudante_modificar["codigo"]
                            estudante_modificar["codigo"] = int(input("\nInforme o código novo: "))
                            print(f"\nCódigo modificado com êxito:\n"
                                  f"Código antigo: {codigo_antigo}\n"
                                  f"Código novo: {estudante_modificar["codigo"]}")
                            press_enter()
                        elif opcao_modificar == '2':
                            nome_antigo = estudante_modificar["nome"]
                            estudante_modificar["nome"] = input("\nInforme o nome novo: ")
                            print(f"\nNome modificado com êxito:\n"
                                  f"Nome antigo: {nome_antigo}\n"
                                  f"Nome novo: {estudante_modificar["nome"]}")
                            press_enter()
                        elif opcao_modificar == '3':
                            cpf_antigo = estudante_modificar["cpf"]
                            estudante_modificar["cpf"] = input("\nInforme o CPF novo: ")
                            print(f"\nCPF modificado com êxito:\n"
                                  f"CPF antigo: {cpf_antigo}\n"
                                  f"CPF novo: {estudante_modificar["cpf"]}")
                            press_enter()
                        elif opcao_modificar == 'b':
                            print(Menu.estudantes)
                            break
                        else:
                            print(error_unrecognized)
                            press_enter()
        elif choice == 'd':
            if len(lista_estudantes) == 0:
                print("\nNenhum estudante foi encontrado.")
            else:
                estudante_remover = None
                codigo_remover = int(input("\nInforme o código do estudante á ser removido: "))
                for dicionario_remover in lista_estudantes:
                    if dicionario_remover["codigo"] == codigo_remover:
                        estudante_remover = dicionario_remover
                        break
                if estudante_remover is None:
                    print(f"\nEstudante com código {codigo_remover} não encontrado.")
                else:
                    lista_estudantes.remove(estudante_remover)
                    # CHECK IF CODE IS EMPTY AND MOVE DOWN
            press_enter()
            print(Menu.estudantes)
            continue
        elif choice == 'q':
            print(Menu.main)
            main_menu()
            break
        else:
            print(error_unrecognized)
            press_enter()
            continue


# prints menu and starts method
print(Menu.main)
main_menu()
# print(Dictionaries.estudantes)