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
            estudante_codigo = int(input("\nInforme o código do(a) estudante: "))
            estudante_nome = str(input("\nInforme o nome do(a) estudante: "))
            estudante_cpf = str(input("\nInforme o CPF do(a) estudante: "))
        # first we're checking if the list is empty
            if len(lista_estudantes) == 0:
                estudante_dict = {
                    "codigo": estudante_codigo,
                    "nome": estudante_nome,
                    "cpf": estudante_cpf
                }
                lista_estudantes.append(estudante_dict)
                print(f"\nEstudante `N.º{estudante_codigo}   "
                      f"Nome: {estudante_nome}   CPF: {estudante_cpf}` "
                      f"foi incluído(a) com êxito.")
        # if it's not empty we're checking if any dictionary within the list has any of the same info
            else:
                codigo_igual = False
                nome_igual = False
                cpf_igual = False
                nada_igual = False
                for dicionario_criar in lista_estudantes:
                    if dicionario_criar["codigo"] == estudante_codigo:
                        codigo_igual = True
                    if dicionario_criar["nome"] == estudante_nome:
                        nome_igual = True
                    if dicionario_criar["cpf"] == estudante_cpf:
                        cpf_igual = True
                    if not codigo_igual and not nome_igual and not cpf_igual:
                        nada_igual = True
            # if none of the info is the same we're gonna go ahead and create a dictionary for that student
                if nada_igual:
                    estudante_dict = {
                        "codigo": estudante_codigo,
                        "nome": estudante_nome,
                        "cpf": estudante_cpf
                    }
                    lista_estudantes.append(estudante_dict)
                    print(f"\nEstudante `N.º{estudante_codigo}   "
                          f"Nome: {estudante_nome}   CPF: {estudante_cpf}` "
                          f"foi incluído(a) com êxito.")
                    break
            # if any info is repeated we'll tell the user what is
                else:
                    if cpf_igual and nome_igual and codigo_igual:
                        print("\nNão foi possível incluír este(a) estudante, "
                              "já existe um cadastro com todos dados iguais.")
                    elif nome_igual and codigo_igual and not cpf_igual:
                        print("\nNão foi possível incluír este(a) estudante, "
                              "já existe um cadastro com o mesmo nome e código.")
                    elif cpf_igual and codigo_igual and not nome_igual:
                        print("\nNão foi possível incluír este(a) estudante, "
                              "já existe um cadastro com o mesmo código e CPF.")
                    elif cpf_igual and nome_igual and not codigo_igual:
                        print("\nNão foi possível incluír este(a) estudante, "
                              "já existe um cadastro com o mesmo nome e CPF.")
                    elif cpf_igual and not nome_igual and not codigo_igual:
                        print("\nNão foi possível incluír este(a) estudante, "
                              "já existe um cadastro com o mesmo CPF.")
                    elif nome_igual and not codigo_igual and not cpf_igual:
                        print("\nNão foi possível incluír este(a) estudante, "
                              "já existe um cadastro com o mesmo nome.")
                    elif codigo_igual and not nome_igual and not cpf_igual:
                        print("\nNão foi possível incluír este(a) estudante, "
                              "já existe um cadastro com o mesmo código.")
                    else:
                        break
        # someone should probably fix this inconsistency...
            press_enter()
            print(Menu.estudantes)
        elif choice == 'l':
            if len(lista_estudantes) == 0:
                print("\nComando indisponível: Nenhum(a) estudante foi encontrado(a).")
            else:
                print(f"\nTotal de {len(lista_estudantes)} estudante(s) encontrado(s): ")
                for dicionario_listar in lista_estudantes:
                    print(f"N.º{dicionario_listar["codigo"]}   "
                          f"Nome: {dicionario_listar["nome"]}   "
                          f"CPF: {dicionario_listar["cpf"]}")
            press_enter()
            print(Menu.estudantes)
            continue
        elif choice == 'u':
            if len(lista_estudantes) == 0:
                print("\nComando indisponível: Nenhum(a) estudante foi encontrado(a).")
            # here's the inconsistency...
                press_enter()
                print(Menu.estudantes)
            else:
                estudante_modificar = None
                codigo_estudante_modificar = input("\nInforme o código do(a) estudante á ser modificado(a): ")
            # first we're choosing a dictionary to modify
                for dicionario_modificar in lista_estudantes:
                    if dicionario_modificar["codigo"] == int(codigo_estudante_modificar):
                        estudante_modificar = dicionario_modificar
                        print(f"\nVocê escolheu o(a) estudante: `N.º{codigo_estudante_modificar}  "
                              f" Nome: {dicionario_modificar["nome"]}   "
                              f"CPF: {dicionario_modificar["cpf"]}`")
                        break
            # then we're implementing a menu for modifying the chosen dictionary
                while True:
                    if estudante_modificar is None:
                        print(f"\nEstudante N.º{codigo_estudante_modificar} não encontrado(a).")
                        press_enter()
                    else:
                        print(Menu.estudantes_modificar)
                        opcao_modificar = str.lower(input(select_command))
                        if opcao_modificar == '1':
                            codigo_antigo = estudante_modificar["codigo"]
                            estudante_modificar["codigo"] = int(input("\nInforme o código novo: "))
                            print(f"\nCódigo modificado com êxito.\n"
                                  f"Código antigo: {codigo_antigo}\n"
                                  f"Código novo: {estudante_modificar["codigo"]}")
                            press_enter()
                        elif opcao_modificar == '2':
                            nome_antigo = estudante_modificar["nome"]
                            estudante_modificar["nome"] = input("\nInforme o nome novo: ")
                            print(f"\nNome modificado com êxito.\n"
                                  f"Nome antigo: {nome_antigo}\n"
                                  f"Nome novo: {estudante_modificar["nome"]}")
                            press_enter()
                        elif opcao_modificar == '3':
                            cpf_antigo = estudante_modificar["cpf"]
                            estudante_modificar["cpf"] = input("\nInforme o CPF novo: ")
                            print(f"\nCPF modificado com êxito.\n"
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
                print("\nComando indisponível: Nenhum(a) estudante foi encontrado(a).")
            else:
                estudante_remover = None
                codigo_remover = int(input("\nInforme o código do(a) estudante á ser removido(a): "))
                for dicionario_remover in lista_estudantes:
                    if dicionario_remover["codigo"] == codigo_remover:
                        estudante_remover = dicionario_remover
                        break
                if estudante_remover is None:
                    print(f"\nEstudante com o código {codigo_remover} não encontrado(a).")
                else:
                    lista_estudantes.remove(estudante_remover)
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