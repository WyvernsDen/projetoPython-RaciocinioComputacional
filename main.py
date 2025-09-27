# Daniel Tivirolli Mariotto
# ADS
import json
import sys

# defining variables
class Menu:
    main = ("\n=============  Menu Principal  =============\n\n"
             "1 - Estudantes\n"
             "2 - Disciplinas\n"
             "3 - Professores\n"
             "4 - Turmas\n"
             "5 - Matrículas\n"
             "x - Sair")
    estudantes = ("\n=====  Menu Operacional  [Estudantes]  =====\n\n"
             "c - Incluir\n"
             "l - Listar\n"
             "u - Atualizar\n"
             "d - Excluir\n"
             "q - Menu Principal")
    disciplinas = ("\n=====  Menu Operacional  [Disciplinas]  =====\n\n"
             "c - Incluir\n"
             "l - Listar\n"
             "u - Atualizar\n"
             "d - Excluir\n"
             "q - Menu Principal")
    professores = ("\n=====  Menu Operacional  [Professores]  =====\n\n"
             "c - Incluir\n"
             "l - Listar\n"
             "u - Atualizar\n"
             "d - Excluir\n"
             "q - Menu Principal")
    turmas = ("\n=======  Menu Operacional  [Turmas]  =======\n\n"
             "c - Incluir\n"
             "l - Listar\n"
             "u - Atualizar\n"
             "d - Excluir\n"
             "q - Menu Principal")
    matriculas = ("\n=====  Menu Operacional  [Matrículas]  =====\n\n"
             "c - Incluir\n"
             "l - Listar\n"
             "u - Atualizar\n"
             "d - Excluir\n"
                        # FIX: change q to b
             "q - Menu Principal")
    estudantes_modificar = ("\n===========  Modificar Estudante  ===========\n\n"
                          "1 - Código\n"
                          "2 - Nome\n"
                          "3 - CPF\n"
                          "b - Voltar")
    disciplinas_modificar = ("\n===========  Modificar Disciplina  ===========\n\n"
                          "1 - Código\n"
                          "2 - Nome\n"
                          "b - Voltar")
    professores_modificar = ("\n===========  Modificar Professor  ===========\n\n"
                          "1 - Código\n"
                          "2 - Nome\n"
                          "3 - CPF\n"
                          "b - Voltar")
    turmas_modificar = ("\n=============  Modificar Turma  =============\n\n"
                          "1 - Código da turma\n"
                          "2 - Código do professor\n"
                          "3 - Código da disciplina\n"
                          "b - Voltar")
    matriculas_modificar = ("\n===========  Modificar Matrícula  ===========\n\n"
                          "1 - Código da turma\n"
                          "b - Voltar")

error_unrecognized = "\nErro: comando não reconhecido."
error_undefined = "Erro: não definido."
error_dev = "\nErro: comando em desenvolvimento."
msg_exit = "\nSaindo..."
select_command = "\nInforme o comando desejado: "

def method_press_enter():
    input("\nPressione `Enter` para continuar.")

def method_error_undefined():
    print(error_undefined)
    method_press_enter()

# we're going to either load jsons into lists or create lists if no jsons exist
try:
    with open("estudantes.json", "r", encoding="utf-8") as file_estudantes:
        lista_estudantes = json.load(file_estudantes)
except:
    lista_estudantes = []

try:
    with open("disciplinas.json", "r", encoding="utf-8") as file_disciplinas:
        lista_disciplinas = json.load(file_disciplinas)
except:
    lista_disciplinas = []

try:
    with open("professores.json", "r", encoding="utf-8") as file_professores:
        lista_professores = json.load(file_professores)
except:
    lista_professores = []

try:
    with open("turmas.json", "r", encoding="utf-8") as file_turmas:
        lista_turmas = json.load(file_turmas)
except:
    lista_turmas = []

try:
    with open("matriculas.json", "r", encoding="utf-8") as file_matriculas:
        lista_matriculas = json.load(file_matriculas)
except:
    lista_matriculas = []

# now we're actually getting started
def main_menu():
    while True:
        main_choice = str.lower(input(select_command))
        if main_choice == '1':
            print(Menu.estudantes)
            op_menu(main_choice)
        elif main_choice == '2':
            print(Menu.disciplinas)
            op_menu(main_choice)
        elif main_choice == '3':
            print(Menu.professores)
            op_menu(main_choice)
        elif main_choice == '4':
            print(Menu.turmas)
            op_menu(main_choice)
        elif main_choice == '5':
            print(Menu.matriculas)
            op_menu(main_choice)
        elif main_choice == 'x':
            sys.exit(msg_exit)
        else:
            print(error_unrecognized)
            method_press_enter()
            continue


def op_menu(main_choice):
    while True:
        op_choice = str.lower(input(select_command))
        if main_choice == '1':
            if op_choice == 'c':
                Estudantes.incluir(main_choice)
                break
            elif op_choice == 'l':
                Estudantes.listar(main_choice)
                break
            elif op_choice == 'u':
                Estudantes.modificar(main_choice)
                break
            elif op_choice == 'd':
                Estudantes.excluir(main_choice)
                break
            elif op_choice == 'q':
                print(Menu.main)
                main_menu()
                break
        elif main_choice == '2':
            if op_choice == 'c':
                Disciplinas.incluir(main_choice)
                break
            elif op_choice == 'l':
                Disciplinas.listar(main_choice)
                break
            elif op_choice == 'u':
                Disciplinas.modificar(main_choice)
                break
            elif op_choice == 'd':
                Disciplinas.excluir(main_choice)
                break
            elif op_choice == 'q':
                print(Menu.main)
                main_menu()
                break
        elif main_choice == '3':
            if op_choice == 'c':
                Professores.incluir(main_choice)
                break
            elif op_choice == 'l':
                Professores.listar(main_choice)
                break
            elif op_choice == 'u':
                Professores.modificar(main_choice)
                break
            elif op_choice == 'd':
                Professores.excluir(main_choice)
                break
            elif op_choice == 'q':
                print(Menu.main)
                main_menu()
                break
        elif main_choice == '4':
            if op_choice == 'c':
                Turmas.incluir(main_choice)
                break
            elif op_choice == 'l':
                Turmas.listar(main_choice)
                break
            elif op_choice == 'u':
                Turmas.modificar(main_choice)
                break
            elif op_choice == 'd':
                Turmas.excluir(main_choice)
                break
            elif op_choice == 'q':
                print(Menu.main)
                main_menu()
                break
        elif main_choice == '5':
            if op_choice == 'c':
                Matriculas.incluir(main_choice)
                break
            elif op_choice == 'l':
                Matriculas.listar(main_choice)
                break
            elif op_choice == 'u':
                Matriculas.modificar(main_choice)
                break
            elif op_choice == 'd':
                Matriculas.excluir(main_choice)
                break
            elif op_choice == 'q':
                print(Menu.main)
                main_menu()
                break

        else:
            print(error_unrecognized)
            method_press_enter()
            continue

class Estudantes:
    @staticmethod
    def incluir(main_choice):
        def text_success():
            print(f"\nEstudante N.º{estudante_codigo} "
                  f"com o nome '{estudante_nome}' e o CPF '{estudante_cpf}' "
                  f"foi incluído(a) com êxito.")
        estudante_codigo = int(input("\nInforme o código do(a) estudante: "))
        estudante_nome = str(input("\nInforme o nome do(a) estudante: "))
        estudante_cpf = str(input("\nInforme o CPF do(a) estudante: "))
        if len(lista_estudantes) == 0:
        # first we're checking if the list is empty
            estudante_dict = {
                "codigo": estudante_codigo,
                "nome": estudante_nome,
                "cpf": estudante_cpf
            }
            lista_estudantes.append(estudante_dict)
            with open("estudantes.json", "w", encoding="utf-8") as file_estudantes:
                json.dump(lista_estudantes, file_estudantes, ensure_ascii=False)
            text_success()
        else:
        # if it's not empty we're checking if any dictionary within the list has any of the same info
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
            if nada_igual:
            # if none of the info is the same we're gonna go ahead and create a dictionary for that student
                estudante_dict = {
                    "codigo": estudante_codigo,
                    "nome": estudante_nome,
                    "cpf": estudante_cpf
                }
                lista_estudantes.append(estudante_dict)
                with open("estudantes.json", "w", encoding="utf-8") as file_estudantes:
                    json.dump(lista_estudantes, file_estudantes, ensure_ascii=False)
                text_success()
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
        # SOMEONE should probably fix this inconsistency with method_press_enter...
        method_press_enter()
        print(Menu.estudantes)
        op_menu(main_choice)

    @staticmethod
    def listar(main_choice):
        if len(lista_estudantes) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhum(a) estudante foi encontrado(a).")
        else:
        # if it's not empty we'll print the list
        # IMPLEMENT: order the list instead of just printing it
            print(f"\nTotal de {len(lista_estudantes)} estudante(s) encontrado(s): ")
            for dicionario_listar in lista_estudantes:
                print(f"N.º{dicionario_listar["codigo"]}   "
                      f"Nome: {dicionario_listar["nome"]}   "
                      f"CPF: {dicionario_listar["cpf"]}")
        method_press_enter()
        print(Menu.estudantes)
        op_menu(main_choice)

    @staticmethod
    # IMPLEMENT: quando modificar um estudante, mudar o codigo na lista de matriculas
    def modificar(main_choice):
        if len(lista_estudantes) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhum(a) estudante foi encontrado(a).")
            # here's the method_press_enter inconsistency...
            method_press_enter()
            print(Menu.estudantes)
        else:
        # if it's not empty we're asking student's #
            estudante_modificar = None
            codigo_estudante_modificar = input("\nInforme o código do(a) estudante á ser modificado(a): ")
            for dicionario_modificar in lista_estudantes:
            # then we're finding the right dictionary to modify
                if dicionario_modificar["codigo"] == int(codigo_estudante_modificar):
                    estudante_modificar = dicionario_modificar
                    print(f"\nVocê escolheu o(a) estudante: `N.º{codigo_estudante_modificar}  "
                          f" Nome: {dicionario_modificar["nome"]}   "
                          f"CPF: {dicionario_modificar["cpf"]}`")
                    break
            while True:
            # then we're implementing a menu for modifying the chosen dictionary
                if estudante_modificar is None:
                    print(f"\nEstudante N.º{codigo_estudante_modificar} não encontrado(a).")
                    method_press_enter()
                else:
                    print(Menu.estudantes_modificar)
                    opcao_modificar = str.lower(input(select_command))
                    if opcao_modificar == '1':
                        codigo_antigo = estudante_modificar["codigo"]
                        codigo_novo = int(input("\nInforme o código novo: "))
                        for check in lista_estudantes:
                            if codigo_novo == check["codigo"]:
                                print(f"\nNão foi possível modificar este(a) estudante, "
                                      f"já existe um(a) estudante cadastrado(a) com o N.º{codigo_novo}.")
                                break
                            else:
                                estudante_modificar["codigo"] = codigo_novo
                                print(f"\nCódigo modificado com êxito.\n"
                                      f"Código antigo: {codigo_antigo}\n"
                                      f"Código novo: {estudante_modificar["codigo"]}")
                                with open("estudantes.json", "w", encoding="utf-8") as file_estudantes:
                                    json.dump(lista_estudantes, file_estudantes, ensure_ascii=False)
                                method_press_enter()
                    elif opcao_modificar == '2':
                        nome_antigo = estudante_modificar["nome"]
                        nome_novo = input("\nInforme o nome novo: ")
                        for check in lista_estudantes:
                            if nome_novo == check["nome"]:
                                print(f"\nNão foi possível modificar este(a) estudante, "
                                      f"já existe um(a) estudante cadastrado(a) com o nome '{nome_novo}'.")
                                break
                            else:
                                estudante_modificar["nome"] = nome_novo
                                print(f"\nNome modificado com êxito.\n"
                                      f"Nome antigo: {nome_antigo}\n"
                                      f"Nome novo: {estudante_modificar["nome"]}")
                                with open("estudantes.json", "w", encoding="utf-8") as file_estudantes:
                                    json.dump(lista_estudantes, file_estudantes, ensure_ascii=False)
                                method_press_enter()
                    elif opcao_modificar == '3':
                        cpf_antigo = estudante_modificar["cpf"]
                        cpf_novo = input("\nInforme o CPF novo: ")
                        for check in lista_estudantes:
                            if cpf_novo == check["cpf"]:
                                print(f"\nNão foi possível modificar este(a) estudante, "
                                      f"já existe um(a) estudante cadastrado(a) com o CPF '{cpf_novo}'.")
                                break
                            else:
                                estudante_modificar["cpf"] = cpf_novo
                                print(f"\nCPF modificado com êxito.\n"
                                      f"CPF antigo: {cpf_antigo}\n"
                                      f"CPF novo: {estudante_modificar["cpf"]}")
                                with open("estudantes.json", "w", encoding="utf-8") as file_estudantes:
                                    json.dump(lista_estudantes, file_estudantes, ensure_ascii=False)
                                method_press_enter()
                    elif opcao_modificar == 'b':
                        print(Menu.estudantes)
                        op_menu(main_choice)
                        break
                    else:
                        print(error_unrecognized)
                        method_press_enter()

    # IMPLEMENT: quando excluir um estudante, deletar a matrícula
    @staticmethod
    def excluir(main_choice):
        # first we're checking if the list is empty
        if len(lista_estudantes) == 0:
            print("\nComando indisponível: Nenhum(a) estudante foi encontrado(a).")
        else:
        # if it's not empty we're asking the # to search for
            estudante_remover = None
            codigo_remover = int(input("\nInforme o código do(a) estudante á ser removido(a): "))
            for dicionario_remover in lista_estudantes:
            # then we're finding the right dictionary to modify
                if dicionario_remover["codigo"] == codigo_remover:
                    estudante_remover = dicionario_remover
                    estudante_remover_codigo = dicionario_remover["codigo"]
                    estudante_remover_nome = dicionario_remover["nome"]
                    estudante_remover_cpf = dicionario_remover["cpf"]
                    break
            if estudante_remover is None:
                print(f"\nEstudante com o código {codigo_remover} não encontrado(a).")
            else:
            # now we're going to make sure that the user chose the right student
                print(f"\nVocê escolheu o(a) estudante: `N.º{estudante_remover_codigo}  "
                          f" Nome: {estudante_remover_nome}   "
                          f"CPF: {estudante_remover_cpf}`")
                option_yn = str.lower(input("\nDigite 'sim' se realmente deseja excluir este(a) estudante: "))
                if option_yn == 'sim':
                    lista_estudantes.remove(estudante_remover)
                    with open("estudantes.json", "w", encoding="utf-8") as file_estudantes:
                        json.dump(lista_estudantes, file_estudantes, ensure_ascii=False)
                    print(f"\nEstudante N.º{estudante_remover_codigo} "
                          f"foi excluído(a) com êxito.")
                else:
                    print("\nEstudante não excluído(a).")
        method_press_enter()
        print(Menu.estudantes)
        op_menu(main_choice)

class Disciplinas:
    @staticmethod
    def incluir(main_choice):
        def text_success():
            print(f"\nDisciplina N.º{disciplina_codigo} de "
                  f"'{disciplina_nome}' foi incluída com êxito.")
        disciplina_codigo = int(input("\nInforme o código do(a) disciplina: "))
        disciplina_nome = str(input("\nInforme o nome do(a) disciplina: "))
        if len(lista_disciplinas) == 0:
        # first we're checking if the list is empty
            disciplina_dict = {
                "codigo": disciplina_codigo,
                "nome": disciplina_nome,
            }
            lista_disciplinas.append(disciplina_dict)
            with open("disciplinas.json", "w", encoding="utf-8") as file_disciplinas:
                json.dump(lista_disciplinas, file_disciplinas, ensure_ascii=False)
            text_success()
        else:
        # if it's not empty we're checking if any dictionary within the list has any of the same info
            codigo_igual = False
            nome_igual = False
            nada_igual = False
            for dicionario_criar in lista_disciplinas:
                if dicionario_criar["codigo"] == disciplina_codigo:
                    codigo_igual = True
                if dicionario_criar["nome"] == disciplina_nome:
                    nome_igual = True
                if not codigo_igual and not nome_igual:
                    nada_igual = True
            if nada_igual:
            # if none of the info is the same we're gonna go ahead and create a dictionary for that subject
                disciplina_dict = {
                    "codigo": disciplina_codigo,
                    "nome": disciplina_nome,
                }
                lista_disciplinas.append(disciplina_dict)
                with open("disciplinas.json", "w", encoding="utf-8") as file_disciplinas:
                    json.dump(lista_disciplinas, file_disciplinas, ensure_ascii=False)
                text_success()
            # if any info is repeated we'll tell the user what is
            else:
                if nome_igual and codigo_igual:
                    print("\nNão foi possível incluír este(a) disciplina, "
                          "já existe um cadastro com todos dados iguais.")
                elif nome_igual and not codigo_igual:
                    print("\nNão foi possível incluír este(a) disciplina, "
                          "já existe um cadastro com o mesmo nome.")
                elif codigo_igual and not nome_igual:
                    print("\nNão foi possível incluír este(a) disciplina, "
                          "já existe um cadastro com o mesmo código.")
        # SOMEONE should probably fix this inconsistency with method_press_enter...
        method_press_enter()
        print(Menu.disciplinas)
        op_menu(main_choice)
    @staticmethod
    def listar(main_choice):
        if len(lista_disciplinas) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhuma disciplina foi encontrado(a).")
        else:
        # if it's not empty we'll print the list
        # IMPLEMENT: order the list instead of just printing it
            print(f"\nTotal de {len(lista_disciplinas)} disciplina(s) encontrada(s): ")
            for dicionario_listar in lista_disciplinas:
                print(f"N.º{dicionario_listar["codigo"]}   "
                      f"Nome: {dicionario_listar["nome"]}")
        method_press_enter()
        print(Menu.disciplinas)
        op_menu(main_choice)

    # IMPLEMENT: quando modificar uma disciplina, mudar o codigo na lista de turmas
    @staticmethod
    def modificar(main_choice):
        if len(lista_disciplinas) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhuma disciplina foi encontrada.")
            # here's the method_press_enter inconsistency...
            method_press_enter()
            print(Menu.disciplinas)
        else:
        # if it's not empty we're asking student's #
            disciplina_modificar = None
            codigo_disciplina_modificar = input("\nInforme o código da disciplina a ser modificada: ")
            for dicionario_modificar in lista_disciplinas:
            # then we're finding the right dictionary to modify
                if dicionario_modificar["codigo"] == int(codigo_disciplina_modificar):
                    disciplina_modificar = dicionario_modificar
                    print(f"\nVocê escolheu a disciplina: `N.º{codigo_disciplina_modificar}  "
                          f" Nome: {dicionario_modificar["nome"]}`")
                    break
            while True:
            # then we're implementing a menu for modifying the chosen dictionary
                if disciplina_modificar is None:
                    print(f"\nDisciplina N.º{codigo_disciplina_modificar} não encontrada.")
                    method_press_enter()
                else:
                    print(Menu.disciplinas_modificar)
                    opcao_modificar = str.lower(input(select_command))
                    if opcao_modificar == '1':
                        codigo_antigo = disciplina_modificar["codigo"]
                        codigo_novo = int(input("\nInforme o código novo: "))
                        for check in lista_disciplinas:
                            if codigo_novo == check["codigo"]:
                                print(f"\nNão foi possível modificar esta disciplina, "
                                      f"já existe uma disciplina cadastrada com o N.º{codigo_novo}.")
                                break
                            else:
                                disciplina_modificar["codigo"] = codigo_novo
                                print(f"\nCódigo modificado com êxito.\n"
                                      f"Código antigo: {codigo_antigo}\n"
                                      f"Código novo: {disciplina_modificar["codigo"]}")
                                with open("disciplinas.json", "w", encoding="utf-8") as file_disciplinas:
                                    json.dump(lista_disciplinas, file_disciplinas, ensure_ascii=False)
                                method_press_enter()
                    elif opcao_modificar == '2':
                        nome_antigo = disciplina_modificar["nome"]
                        nome_novo = input("\nInforme o nome novo: ")
                        for check in lista_disciplinas:
                            if nome_novo == check["nome"]:
                                print(f"\nNão foi possível modificar esta disciplina, "
                                      f"já existe uma disciplina cadastrada com o nome '{nome_novo}'.")
                                break
                            else:
                                disciplina_modificar["nome"] = nome_novo
                                print(f"\nNome modificado com êxito.\n"
                                      f"Nome antigo: {nome_antigo}\n"
                                      f"Nome novo: {disciplina_modificar["nome"]}")
                                with open("disciplinas.json", "w", encoding="utf-8") as file_disciplinas:
                                    json.dump(lista_disciplinas, file_disciplinas, ensure_ascii=False)
                                method_press_enter()
                    elif opcao_modificar == 'b':
                        print(Menu.disciplinas)
                        op_menu(main_choice)
                        break
                    else:
                        print(error_unrecognized)
                        method_press_enter()

    @staticmethod
    def excluir(main_choice):
        # first we're checking if the list is empty
        if len(lista_disciplinas) == 0:
            print("\nComando indisponível: Nenhuma disciplina foi encontrada.")
        else:
        # if it's not empty we're asking the # to search for
            disciplina_remover = None
            codigo_remover = int(input("\nInforme o código da disciplina a ser removida: "))
            for dicionario_remover in lista_disciplinas:
            # then we're finding the right dictionary to modify
                if dicionario_remover["codigo"] == codigo_remover:
                    disciplina_remover = dicionario_remover
                    disciplina_remover_codigo = dicionario_remover["codigo"]
                    disciplina_remover_nome = dicionario_remover["nome"]
                    break
            if disciplina_remover is None:
                print(f"\nDisciplina com o código {codigo_remover} não encontrada.")
            else:
            # now we're going to make sure that the user chose the right student
                print(f"\nVocê escolheu o(a) disciplina: `N.º{disciplina_remover_codigo}  "
                          f" Nome: {disciplina_remover_nome}`")
                option_yn = str.lower(input("\nDigite 'sim' se realmente deseja excluir esta disciplina: "))
                if option_yn == 'sim':
                    lista_disciplinas.remove(disciplina_remover)
                    with open("disciplinas.json", "w", encoding="utf-8") as file_disciplinas:
                        json.dump(lista_disciplinas, file_disciplinas, ensure_ascii=False)
                    print(f"\nDisciplina N.º{disciplina_remover_codigo} "
                          f"foi excluída com êxito.")
                else:
                    print("\nDisciplina não excluída.")
        method_press_enter()
        print(Menu.disciplinas)
        op_menu(main_choice)

class Professores:
    @staticmethod
    def incluir(main_choice):
        def text_success():
            print(f"\nProfessor(a) N.º{professor_codigo} "
                  f"com o nome '{professor_nome}' e o CPF '{professor_cpf}' "
                  f"foi incluído(a) com êxito.")
        professor_codigo = int(input("\nInforme o código do(a) professor(a): "))
        professor_nome = str(input("\nInforme o nome do(a) professor(a): "))
        professor_cpf = str(input("\nInforme o CPF do(a) professor(a): "))
        if len(lista_professores) == 0:
        # first we're checking if the list is empty
            professor_dict = {
                "codigo": professor_codigo,
                "nome": professor_nome,
                "cpf": professor_cpf
            }
            lista_professores.append(professor_dict)
            with open("professores.json", "w", encoding="utf-8") as file_professores:
                json.dump(lista_professores, file_professores, ensure_ascii=False)
            text_success()
        else:
        # if it's not empty we're checking if any dictionary within the list has any of the same info
            codigo_igual = False
            nome_igual = False
            cpf_igual = False
            nada_igual = False
            for dicionario_criar in lista_professores:
                if dicionario_criar["codigo"] == professor_codigo:
                    codigo_igual = True
                if dicionario_criar["nome"] == professor_nome:
                    nome_igual = True
                if dicionario_criar["cpf"] == professor_cpf:
                    cpf_igual = True
                if not codigo_igual and not nome_igual and not cpf_igual:
                    nada_igual = True
            if nada_igual:
            # if none of the info is the same we're gonna go ahead and create a dictionary for that student
                professor_dict = {
                    "codigo": professor_codigo,
                    "nome": professor_nome,
                    "cpf": professor_cpf
                }
                lista_professores.append(professor_dict)
                with open("professores.json", "w", encoding="utf-8") as file_professores:
                    json.dump(lista_professores, file_professores, ensure_ascii=False)
                text_success()
            # if any info is repeated we'll tell the user what is
            else:
                if cpf_igual and nome_igual and codigo_igual:
                    print("\nNão foi possível incluír este(a) professor(a), "
                          "já existe um cadastro com todos dados iguais.")
                elif nome_igual and codigo_igual and not cpf_igual:
                    print("\nNão foi possível incluír este(a) professor(a), "
                          "já existe um cadastro com o mesmo nome e código.")
                elif cpf_igual and codigo_igual and not nome_igual:
                    print("\nNão foi possível incluír este(a) professor(a), "
                          "já existe um cadastro com o mesmo código e CPF.")
                elif cpf_igual and nome_igual and not codigo_igual:
                    print("\nNão foi possível incluír este(a) professor(a), "
                          "já existe um cadastro com o mesmo nome e CPF.")
                elif cpf_igual and not nome_igual and not codigo_igual:
                    print("\nNão foi possível incluír este(a) professor(a), "
                          "já existe um cadastro com o mesmo CPF.")
                elif nome_igual and not codigo_igual and not cpf_igual:
                    print("\nNão foi possível incluír este(a) professor(a), "
                          "já existe um cadastro com o mesmo nome.")
                elif codigo_igual and not nome_igual and not cpf_igual:
                    print("\nNão foi possível incluír este(a) professor(a), "
                          "já existe um cadastro com o mesmo código.")
        # SOMEONE should probably fix this inconsistency with method_press_enter...
        method_press_enter()
        print(Menu.professores)
        op_menu(main_choice)

    @staticmethod
    def listar(main_choice):
        if len(lista_professores) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhum(a) professor(a) foi encontrado(a).")
        else:
        # if it's not empty we'll print the list
        # IMPLEMENT: order the list instead of just printing it
            print(f"\nTotal de {len(lista_professores)} professor(as) encontrado(as): ")
            for dicionario_listar in lista_professores:
                print(f"N.º{dicionario_listar["codigo"]}   "
                      f"Nome: {dicionario_listar["nome"]}   "
                      f"CPF: {dicionario_listar["cpf"]}")
        method_press_enter()
        print(Menu.professores)
        op_menu(main_choice)

    # IMPLEMENT: quando modificar um professor, mudar o codigo na lista de turmas

    @staticmethod
    def modificar(main_choice):
        if len(lista_professores) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhum(a) professor(a) foi encontrado(a).")
            # here's the method_press_enter inconsistency...
            method_press_enter()
            print(Menu.professores)
        else:
        # if it's not empty we're asking student's #
            professor_modificar = None
            codigo_professor_modificar = input("\nInforme o código do(a) professor(a) a ser modificado(a): ")
            for dicionario_modificar in lista_professores:
            # then we're finding the right dictionary to modify
                if dicionario_modificar["codigo"] == int(codigo_professor_modificar):
                    professor_modificar = dicionario_modificar
                    print(f"\nVocê escolheu o(a) professor(a): `N.º{codigo_professor_modificar}  "
                          f" Nome: {dicionario_modificar["nome"]}   "
                          f"CPF: {dicionario_modificar["cpf"]}`")
                    break
            while True:
            # then we're implementing a menu for modifying the chosen dictionary
                if professor_modificar is None:
                    print(f"\nProfessor(a) N.º{codigo_professor_modificar} não encontrado(a).")
                    method_press_enter()
                else:
                    print(Menu.professores_modificar)
                    opcao_modificar = str.lower(input(select_command))
                    if opcao_modificar == '1':
                        codigo_antigo = professor_modificar["codigo"]
                        codigo_novo = int(input("\nInforme o código novo: "))
                        for check in lista_professores:
                            if codigo_novo == check["codigo"]:
                                print(f"\nNão foi possível modificar este(a) professor(a), "
                                      f"já existe um(a) professor(a) cadastrado(a) com o N.º{codigo_novo}.")
                                break
                            else:
                                professor_modificar["codigo"] = codigo_novo
                                print(f"\nCódigo modificado com êxito.\n"
                                      f"Código antigo: {codigo_antigo}\n"
                                      f"Código novo: {professor_modificar["codigo"]}")
                                with open("professores.json", "w", encoding="utf-8") as file_professores:
                                    json.dump(lista_professores, file_professores, ensure_ascii=False)
                                method_press_enter()
                    elif opcao_modificar == '2':
                        nome_antigo = professor_modificar["nome"]
                        nome_novo = input("\nInforme o nome novo: ")
                        for check in lista_professores:
                            if nome_novo == check["nome"]:
                                print(f"\nNão foi possível modificar este(a) professor(a), "
                                      f"já existe um(a) professor(a) cadastrado(a) com o nome '{nome_novo}'.")
                                break
                            else:
                                professor_modificar["nome"] = nome_novo
                                print(f"\nNome modificado com êxito.\n"
                                      f"Nome antigo: {nome_antigo}\n"
                                      f"Nome novo: {professor_modificar["nome"]}")
                                with open("professores.json", "w", encoding="utf-8") as file_professores:
                                    json.dump(lista_professores, file_professores, ensure_ascii=False)
                                method_press_enter()
                    elif opcao_modificar == '3':
                        cpf_antigo = professor_modificar["cpf"]
                        cpf_novo = input("\nInforme o CPF novo: ")
                        for check in lista_professores:
                            if cpf_novo == check["cpf"]:
                                print(f"\nNão foi possível modificar este(a) professor(a), "
                                      f"já existe um(a) professor(a) cadastrado(a) com o CPF '{cpf_novo}'.")
                                break
                            else:
                                professor_modificar["cpf"] = cpf_novo
                                print(f"\nCPF modificado com êxito.\n"
                                      f"CPF antigo: {cpf_antigo}\n"
                                      f"CPF novo: {professor_modificar["cpf"]}")
                                with open("professores.json", "w", encoding="utf-8") as file_professores:
                                    json.dump(lista_professores, file_professores, ensure_ascii=False)
                                method_press_enter()
                    elif opcao_modificar == 'b':
                        print(Menu.professores)
                        op_menu(main_choice)
                        break
                    else:
                        print(error_unrecognized)
                        method_press_enter()

    @staticmethod
    def excluir(main_choice):
        # first we're checking if the list is empty
        if len(lista_professores) == 0:
            print("\nComando indisponível: Nenhum(a) professor(a) foi encontrado(a).")
        else:
        # if it's not empty we're asking the # to search for
            professor_remover = None
            codigo_remover = int(input("\nInforme o código do(a) professor(a) a ser removido(a): "))
            for dicionario_remover in lista_professores:
            # then we're finding the right dictionary to modify
                if dicionario_remover["codigo"] == codigo_remover:
                    professor_remover = dicionario_remover
                    professor_remover_codigo = dicionario_remover["codigo"]
                    professor_remover_nome = dicionario_remover["nome"]
                    professor_remover_cpf = dicionario_remover["cpf"]
                    break
            if professor_remover is None:
                print(f"\nProfessor(a) com o código {codigo_remover} não encontrado(a).")
            else:
            # now we're going to make sure that the user chose the right student
                print(f"\nVocê escolheu o(a) professor(a): `N.º{professor_remover_codigo}  "
                          f" Nome: {professor_remover_nome}   "
                          f"CPF: {professor_remover_cpf}`")
                option_yn = str.lower(input("\nDigite 'sim' se realmente deseja excluir este(a) professor(a): "))
                if option_yn == 'sim':
                    lista_professores.remove(professor_remover)
                    with open("professores.json", "w", encoding="utf-8") as file_professores:
                        json.dump(lista_professores, file_professores, ensure_ascii=False)
                    print(f"\nProfessor(a) N.º{professor_remover_codigo} "
                          f"foi excluído(a) com êxito.")
                else:
                    print("\nProfessor(a) não excluído(a).")
        method_press_enter()
        print(Menu.professores)
        op_menu(main_choice)

class Turmas:
    @staticmethod
    def incluir(main_choice):
        def text_success():
            print(f"\nTurma N.º{turma_codigo} "
                  f"com o(a) professor(a) '{professor_nome}' e a disciplina '{disciplina_nome}' "
                  f"foi incluída com êxito.")
        turma_codigo = int(input("\nInforme o código da turma: "))
        professor_codigo = int(input("\nInforme o código do(a) professor(a): "))
        disciplina_codigo = int(input("\nInforme o código da disciplina: "))
        professor_existe = False
        disciplina_existe = False
        for check_professor in lista_professores:
            if check_professor["codigo"] == professor_codigo:
                professor_existe = True
                professor_nome = check_professor["nome"]
        for check_disciplina in lista_disciplinas:
            if check_disciplina["codigo"] == disciplina_codigo:
                disciplina_existe = True
                disciplina_nome = check_disciplina["nome"]
        if professor_existe and disciplina_existe:
        # first we're checking if the list is empty
            if len(lista_turmas) == 0:
                turma_dict = {
                    "turma_codigo": turma_codigo,
                    "professor_codigo": professor_codigo,
                    "disciplina_codigo": disciplina_codigo
                }
                lista_turmas.append(turma_dict)
                with open("turmas.json", "w", encoding="utf-8") as file_turmas:
                    json.dump(lista_turmas, file_turmas, ensure_ascii=False)
                text_success()
        # if it's not empty we're checking if any dictionary within the list has the same #
            else:
                codigo_igual_turma = False
                for dicionario_criar in lista_turmas:
                    if dicionario_criar["turma_codigo"] == turma_codigo:
                        codigo_igual_turma = True
                if not codigo_igual_turma:
                    # if none of them have the same # we'll create a dictionary for that class
                    turma_dict = {
                        "turma_codigo": turma_codigo,
                        "professor_codigo": professor_codigo,
                        "disciplina_codigo": disciplina_codigo
                    }
                    lista_turmas.append(turma_dict)
                    with open("turmas.json", "w", encoding="utf-8") as file_turmas:
                        json.dump(lista_turmas, file_turmas, ensure_ascii=False)
                    text_success()
                # if the # is repeated we'll tell the user
                else:
                    if codigo_igual_turma:
                        print("\nErro: Não foi possível cadastrar esta turma, "
                              "já existe uma turma com o mesmo código.")
        # if any of the checks fail we'll tell the user what did
        elif not professor_existe and not disciplina_existe:
            print(f"Erro: Professor(a) e disciplina não encontrados, "
                  f"tente novamente com cadastros existentes, ou crie cadastros novos.")
        elif not professor_existe and disciplina_existe:
            print(f"Erro: Professor(a) não encontrado(a), "
                  f"tente novamente com um cadastro existente, ou crie um novo.")
        elif professor_existe and not disciplina_existe:
            print(f"Erro: Disciplina não encontrada, "
                  f"tente novamente com um cadastro existente, ou crie um novo.")
        else:
            method_error_undefined()
        # SOMEONE should probably fix this inconsistency with method_press_enter...
        method_press_enter()
        print(Menu.turmas)
        op_menu(main_choice)

    @staticmethod
    def listar(main_choice):
        if len(lista_turmas) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhuma turma foi encontrada.")
        else:
        # if it's not empty we'll print the list
        # IMPLEMENT: order the list instead of just printing it
            print(f"\nTotal de {len(lista_turmas)} turma(s) encontrada(s): ")
            for dicionario_listar in lista_turmas:
                print(f"Turma N.º{dicionario_listar["turma_codigo"]}   "
                      f"Professor(a) N.º{dicionario_listar["professor_codigo"]}   "
                      f"Disciplina N.º{dicionario_listar["disciplina_codigo"]}")
        method_press_enter()
        print(Menu.turmas)
        op_menu(main_choice)

    # IMPLEMENT: quando modificar uma turma, mudar o codigo na lista de matriculas
    @staticmethod
    def modificar(main_choice):
        if len(lista_turmas) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhuma turma foi encontrada.")
            # here's the method_press_enter inconsistency...
            method_press_enter()
            print(Menu.turmas)
        else:
        # if it's not empty we're asking student's #
            turma_modificar = None
            codigo_turma_modificar = input("\nInforme o código da turma a ser modificada: ")
            for dicionario_modificar in lista_turmas:
            # then we're finding the right dictionary to modify
                if dicionario_modificar["turma_codigo"] == int(codigo_turma_modificar):
                    turma_modificar = dicionario_modificar
                    print(f"\nVocê escolheu a turma N.º{codigo_turma_modificar} com o(a) "
                          f"professor(a) N.º{dicionario_modificar["professor_codigo"]} e a "
                          f"disciplina N.º{dicionario_modificar["disciplina_codigo"]}`")
                    break
            while True:
            # then we're implementing a menu for modifying the chosen dictionary
                if turma_modificar is None:
                    print(f"\nTurma N.º{codigo_turma_modificar} não encontrada.")
                    method_press_enter()
                else:
                    print(Menu.turmas_modificar)
                    opcao_modificar = str.lower(input(select_command))
                    if opcao_modificar == '1':
                        codigo_antigo_turma = turma_modificar["turma_codigo"]
                        codigo_novo_turma = int(input("\nInforme o código novo da turma: "))
                        for check in lista_turmas:
                            if codigo_novo_turma == check["turma_codigo"]:
                                print(f"\nNão foi possível modificar esta turma, "
                                      f"já existe uma turma cadastrada com o N.º{codigo_novo_turma}.")
                                break
                            else:
                                turma_modificar["turma_codigo"] = codigo_novo_turma
                                print(f"\nCódigo modificado com êxito.\n"
                                      f"Código antigo: {codigo_antigo_turma}\n"
                                      f"Código novo: {turma_modificar["turma_codigo"]}")
                                with open("turmas.json", "w", encoding="utf-8") as file_turmas:
                                    json.dump(lista_turmas, file_turmas, ensure_ascii=False)
                                method_press_enter()
                    elif opcao_modificar == '2':
                        codigo_antigo_professor = turma_modificar["professor_codigo"]
                        codigo_novo_professor = int(input("\nInforme o código do(a) professor(a) novo(a): "))
                        for check_professor in lista_professores:
                            if codigo_novo_professor == check_professor["codigo"]:
                                turma_modificar["professor_codigo"] = codigo_novo_professor
                                print(f"\nCódigo modificado com êxito.\n"
                                      f"Código antigo: {codigo_antigo_professor}\n" 
                                      f"Código novo: {turma_modificar["professor_codigo"]}")
                                with open("turmas.json", "w", encoding="utf-8") as file_turmas:
                                    json.dump(lista_turmas, file_turmas, ensure_ascii=False)
                                method_press_enter()
                            else:
                                print(f"Erro: Professor(a) não encontrado(a), "
                                      f"tente novamente com um(a) professor(a) existente, "
                                      f"ou crie um novo cadastro.")
                                method_press_enter()
                    elif opcao_modificar == '3':
                        codigo_antigo_disciplina = turma_modificar["disciplina_codigo"]
                        codigo_novo_disciplina = int(input("\nInforme o código da disciplina nova: "))
                        for check_disciplina in lista_disciplinas:
                            if codigo_novo_disciplina == check_disciplina["codigo"]:
                                turma_modificar["disciplina_codigo"] = codigo_novo_disciplina
                                print(f"\nCódigo modificado com êxito.\n"
                                      f"Código antigo: {codigo_antigo_disciplina}\n"
                                      f"Código novo: {turma_modificar["disciplina_codigo"]}")
                                with open("turmas.json", "w", encoding="utf-8") as file_turmas:
                                    json.dump(lista_turmas, file_turmas, ensure_ascii=False)
                                method_press_enter()
                            else:
                                print(f"Erro: Disciplina não encontrada, "
                                      f"tente novamente com uma disciplina existente, "
                                      f"ou crie um novo cadastro.")
                                method_press_enter()
                    elif opcao_modificar == 'b':
                        print(Menu.turmas)
                        op_menu(main_choice)
                        break
                    else:
                        print(error_unrecognized)
                        method_press_enter()

    @staticmethod
    def excluir(main_choice):
        # first we're checking if the list is empty
        if len(lista_turmas) == 0:
            print("\nComando indisponível: Nenhuma turma foi encontrada.")
        else:
        # if it's not empty we're asking the # to search for
            turma_remover = None
            codigo_remover = int(input("\nInforme o código da turma a ser removida: "))
            for dicionario_remover in lista_turmas:
            # then we're finding the right dictionary to modify
                if dicionario_remover["turma_codigo"] == codigo_remover:
                    turma_remover = dicionario_remover
                    turma_remover_codigo = dicionario_remover["turma_codigo"]
                    professor_remover_codigo = dicionario_remover["professor_codigo"]
                    disciplina_remover_codigo = dicionario_remover["disciplina_codigo"]
                    break
            if turma_remover is None:
                print(f"\nTurma com o código {codigo_remover} não encontrada.")
            else:
            # now we're going to make sure that the user chose the right student
                print(f"\nVocê escolheu a turma N.º{turma_remover_codigo} com o(a) "
                      f"professor(a) N.º{professor_remover_codigo} e a "
                      f"disciplina N.º{disciplina_remover_codigo}`")
                option_yn = str.lower(input("\nDigite 'sim' se realmente deseja excluir esta turma: "))
                if option_yn == 'sim':
                    lista_turmas.remove(turma_remover)
                    with open("turmas.json", "w", encoding="utf-8") as file_turmas:
                        json.dump(lista_turmas, file_turmas, ensure_ascii=False)
                    print(f"\nTurma N.º{turma_remover_codigo} "
                          f"foi excluída com êxito.")
                else:
                    print("\nTurma não excluída.")
            method_press_enter()
            print(Menu.turmas)
            op_menu(main_choice)

class Matriculas:
    @staticmethod
    def incluir(main_choice):
        def text_success():
            print(f"\nEstudante N.º{estudante_codigo} "
                  f"foi matrículado(a) na turma N.º{turma_codigo} com êxito.")
        estudante_codigo = int(input("\nInforme o código do(a) estudante: "))
        turma_codigo = int(input("\nInforme o código da turma: "))
        turma_existe = False
        estudante_existe = False
        for check_estudante in lista_estudantes:
            if check_estudante["codigo"] == estudante_codigo:
                estudante_existe = True
        for check_turma in lista_turmas:
            if check_turma["turma_codigo"] == turma_codigo:
                turma_existe = True
        if turma_existe and estudante_existe:
            if len(lista_matriculas) == 0:
            # first we're checking if the list is empty
                matricula_dict = {
                    "estudante_codigo": estudante_codigo,
                    "turma_codigo": turma_codigo,
                }
                lista_matriculas.append(matricula_dict)
                with open("matriculas.json", "w", encoding="utf-8") as file_matriculas:
                    json.dump(lista_matriculas, file_matriculas, ensure_ascii=False)
                text_success()
            else:
            # if it's not empty we're checking if any dictionary within the list has any of the same info

                # if none of the info is the same we're gonna go ahead and create a dictionary for that student
                if turma_existe and estudante_existe:
                    matricula_dict = {
                        "estudante_codigo": estudante_codigo,
                        "turma_codigo": turma_codigo,
                    }
                    lista_matriculas.append(matricula_dict)
                    with open("matriculas.json", "w", encoding="utf-8") as file_matriculas:
                        json.dump(lista_matriculas, file_matriculas, ensure_ascii=False)
                    text_success()
                # if any info is repeated we'll tell the user what is
        elif not turma_existe and not estudante_existe:
            print(f"Erro: Turma e estudante não encontrados, "
                  f"tente novamente com cadastros existentes, ou crie cadastros novos.")
        elif not turma_existe and estudante_existe:
            print(f"Erro: Turma não encontrada, "
                  f"tente novamente com um cadastro existente, ou crie um novo.")
        elif turma_existe and not estudante_existe:
            print(f"Erro: Estudante não encontrado(a), "
                  f"tente novamente com um cadastro existente, ou crie um novo.")
        # SOMEONE should probably fix this inconsistency with method_press_enter...
        method_press_enter()
        print(Menu.matriculas)
        op_menu(main_choice)

    @staticmethod
    def listar(main_choice):
        if len(lista_matriculas) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhuma matrícula foi encontrada.")
        else:
        # if it's not empty we'll print the list
        # IMPLEMENT: order the list instead of just printing it
            print(f"\nTotal de {len(lista_matriculas)} matrícula(s) encontrada(s): ")
            for dicionario_listar in lista_matriculas:
                print(f"Estudante N.º{dicionario_listar["estudante_codigo"]}   "
                      f"Turma N.º{dicionario_listar["turma_codigo"]}")
        method_press_enter()
        print(Menu.matriculas)
        op_menu(main_choice)

    @staticmethod
    def modificar(main_choice):
        if len(lista_matriculas) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhuma matrícula foi encontrada.")
            # here's the method_press_enter inconsistency...
            method_press_enter()
            print(Menu.matriculas)
        else:
        # if it's not empty we're asking student's #
            estudante_existe = False
            matricula_modificar = None
            codigo_estudante_modificar = int(input("\nInforme o código do(a) estudante cuja matrícula deseja modificar: "))
            for check_estudante in lista_estudantes:
                if check_estudante["codigo"] == codigo_estudante_modificar:
                    estudante_existe = True
                    estudante_nome = check_estudante["nome"]
                    break
            for dicionario_modificar in lista_matriculas:
            # then we're finding the right dictionary to modify
                if dicionario_modificar["estudante_codigo"] == codigo_estudante_modificar:
                    matricula_modificar = dicionario_modificar
                    print(f"\nVocê escolheu o(a) estudante N.º{codigo_estudante_modificar}, '{estudante_nome}', "
                          f"matrículado(a) na turma N.º{dicionario_modificar["turma_codigo"]}.")
                    break
            while True:
            # then we're implementing a menu for modifying the chosen dictionary
                if matricula_modificar is None and estudante_existe:
                    print(f"\n\nErro: Estudante N.º{codigo_estudante_modificar} não está matrículado(a), "
                          f"tente novamente com um(a) estudante matrículado(a).")
                    method_press_enter()
                elif not estudante_existe:
                    print(f"\n\nErro: Estudante N.º{codigo_estudante_modificar} não encontrado(a), "
                          f"tente novamente com um(a) estudante cadastrado(a) e matrículado(a).")
                    method_press_enter()
                else:
                    print(Menu.matriculas_modificar)
                    opcao_modificar = str.lower(input(select_command))
                    # if opcao_modificar == '1':
                    #     codigo_antigo_estudante = matricula_modificar["estudante_codigo"]
                    #     codigo_novo_estudante = int(input("\nInforme o código novo do(a) estudante: "))
                    #     for check_estudante in lista_estudantes:
                    #         if codigo_novo_estudante == check_estudante["codigo"]:
                    #             matricula_modificar["estudante_codigo"] = codigo_novo_estudante
                    #             print(f"\nCódigo modificado com êxito.\n"
                    #                   f"Código antigo: {codigo_antigo_estudante}\n"
                    #                   f"Código novo: {matricula_modificar["professor_codigo"]}")
                    #             with open("matriculas.json", "w", encoding="utf-8") as file_matriculas:
                    #                 json.dump(lista_matriculas, file_matriculas, ensure_ascii=False)
                    #             method_press_enter()
                    #         else:
                    #             print(f"Erro: Estudante não encontrado(a), "
                    #                   f"tente novamente com um(a) estudante existente, "
                    #                   f"ou crie um novo cadastro.")
                    #             method_press_enter()
                    if opcao_modificar == '1':
                        codigo_antigo_turma = matricula_modificar["turma_codigo"]
                        codigo_novo_turma = int(input("\nInforme o código da turma nova: "))
                        for check_turma in lista_turmas:
                            if codigo_novo_turma == check_turma["turma_codigo"]:
                                matricula_modificar["turma_codigo"] = codigo_novo_turma
                                print(f"\nCódigo modificado com êxito.\n"
                                      f"Código antigo: {codigo_antigo_turma}\n"
                                      f"Código novo: {matricula_modificar["turma_codigo"]}")
                                with open("matriculas.json", "w", encoding="utf-8") as file_matriculas:
                                    json.dump(lista_matriculas, file_matriculas, ensure_ascii=False)
                                method_press_enter()
                            else:
                                print(f"\nErro: Turma não encontrada, "
                                      f"tente novamente com uma turma existente, "
                                      f"ou crie um novo cadastro.")
                                method_press_enter()
                    elif opcao_modificar == 'b':
                        print(Menu.matriculas)
                        op_menu(main_choice)
                        break
                    else:
                        print(error_unrecognized)
                        method_press_enter()

    @staticmethod
    def excluir(main_choice):
        # first we're checking if the list is empty
        if len(lista_matriculas) == 0:
            print("\nComando indisponível: Nenhuma matrícula foi encontrada.")
        else:
        # if it's not empty we're asking the # to search for
            estudante_existe = False
            matricula_remover = None
            codigo_remover = int(input("\nInforme o código do(a) estudante cuja matrícula deseja remover: "))
            for check_estudante in lista_estudantes:
                if check_estudante["codigo"] == codigo_remover:
                    estudante_existe = True
                    break
            for dicionario_remover in lista_matriculas:
            # then we're finding the right dictionary to modify
                if dicionario_remover["estudante_codigo"] == codigo_remover:
                    matricula_remover = dicionario_remover
                    estudante_remover_codigo = dicionario_remover["estudante_codigo"]
                    turma_remover_codigo = dicionario_remover["turma_codigo"]
                    break
            if matricula_remover is None and estudante_existe:
                print(f"\nErro: Estudante N.º{codigo_remover} não está matrículado(a), "
                      f"tente novamente com um(a) estudante matrículado(a).")
                method_press_enter()
            elif not estudante_existe:
                print(f"\nErro: Estudante N.º{codigo_remover} não encontrado(a), "
                      f"tente novamente com um(a) estudante cadastrado(a) e matrículado(a).")
                method_press_enter()
            else:
                # now we're going to make sure that the user chose the right student
                    print(f"\nVocê escolheu o(a) estudante N.º{estudante_remover_codigo}, "
                          f"matrículado na turma N.º{turma_remover_codigo}.")
                    option_yn = str.lower(input("\nDigite 'sim' se realmente deseja remover a matrícula deste(a) estudante: "))
                    if option_yn == 'sim':
                        lista_matriculas.remove(matricula_remover)
                        with open("matriculas.json", "w", encoding="utf-8") as file_matriculas:
                            json.dump(lista_matriculas, file_matriculas, ensure_ascii=False)
                        print(f"\nMatricula N.º{estudante_remover_codigo} "
                              f"foi excluído(a) com êxito.")
                    else:
                        print("\nMatricula não excluído(a).")
        method_press_enter()
        print(Menu.matriculas)
        op_menu(main_choice)

# prints menu and starts method
print(Menu.main)
main_menu()