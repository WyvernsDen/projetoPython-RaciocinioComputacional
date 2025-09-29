# Daniel Tivirolli Mariotto
# ADS
import json
import sys

# defining basic strings and methods
error_unrecognized = "\nErro: comando não reconhecido."
error_undefined = "Erro: não definido."
error_dev = "\nErro: comando em desenvolvimento."
msg_exit = "\nSaindo..."
select_command = "\nInforme o comando desejado: "

str_main_menu = ("\n=============  Menu Principal  =============\n\n"
                 "1 - Estudantes\n"
                 "2 - Disciplinas\n"
                 "3 - Professores\n"
                 "4 - Turmas\n"
                 "5 - Matrículas\n"
                 "x - Sair")

def method_press_enter():
    input("\nPressione `Enter` para continuar.")

def method_main_menu():
    while True:
        main_choice = str.lower(input(select_command))
        if main_choice == '1':
            print(Estudante.str_op_menu)
            method_op_menu(main_choice)
        elif main_choice == '2':
            print(Disciplina.str_op_menu)
            method_op_menu(main_choice)
        elif main_choice == '3':
            print(Professor.str_op_menu)
            method_op_menu(main_choice)
        elif main_choice == '4':
            print(Turma.str_op_menu)
            method_op_menu(main_choice)
        elif main_choice == '5':
            print(Matricula.str_op_menu)
            method_op_menu(main_choice)
        elif main_choice == 'x':
            sys.exit(msg_exit)
        else:
            print(error_unrecognized)
            method_press_enter()
            continue

def method_op_menu(main_choice):
    while True:
        op_choice = str.lower(input(select_command))
        if main_choice == '1':
            if op_choice == 'c':
                estudante.incluir(Estudante.str_op_menu, main_choice)
                break
            elif op_choice == 'l':
                estudante.listar(Estudante.str_op_menu, main_choice)
                break
            elif op_choice == 'u':
                estudante.modificar(Estudante.str_op_menu, main_choice)
                break
            elif op_choice == 'd':
                estudante.excluir(Estudante.str_op_menu, main_choice)
                break
            elif op_choice == 'q':
                print(str_main_menu)
                method_main_menu()
                break
        elif main_choice == '2':
            if op_choice == 'c':
                disciplina.incluir(Disciplina.str_op_menu, main_choice)
                break
            elif op_choice == 'l':
                disciplina.listar(Disciplina.str_op_menu, main_choice)
                break
            elif op_choice == 'u':
                disciplina.modificar(Disciplina.str_op_menu, main_choice)
                break
            elif op_choice == 'd':
                disciplina.excluir(Disciplina.str_op_menu, main_choice)
                break
            elif op_choice == 'q':
                print(str_main_menu)
                method_main_menu()
                break
        elif main_choice == '3':
            if op_choice == 'c':
                professor.incluir(Professor.str_op_menu, main_choice)
                break
            elif op_choice == 'l':
                professor.listar(Professor.str_op_menu, main_choice)
                break
            elif op_choice == 'u':
                professor.modificar(Professor.str_op_menu, main_choice)
                break
            elif op_choice == 'd':
                professor.excluir(Professor.str_op_menu, main_choice)
                break
            elif op_choice == 'q':
                print(str_main_menu)
                method_main_menu()
                break
        elif main_choice == '4':
            if op_choice == 'c':
                turma.incluir(Turma.str_op_menu, main_choice)
                break
            elif op_choice == 'l':
                turma.listar(Turma.str_op_menu, main_choice)
                break
            elif op_choice == 'u':
                turma.modificar(Turma.str_op_menu, main_choice)
                break
            elif op_choice == 'd':
                turma.excluir(Turma.str_op_menu, main_choice)
                break
            elif op_choice == 'q':
                print(str_main_menu)
                method_main_menu()
                break
        elif main_choice == '5':
            if op_choice == 'c':
                matricula.incluir(Matricula.str_op_menu, main_choice)
                break
            elif op_choice == 'l':
                matricula.listar(Matricula.str_op_menu, main_choice)
                break
            elif op_choice == 'u':
                matricula.modificar(Matricula.str_op_menu, main_choice)
                break
            elif op_choice == 'd':
                matricula.excluir(Matricula.str_op_menu, main_choice)
                break
            elif op_choice == 'q':
                print(str_main_menu)
                method_main_menu()
                break

        else:
            print(error_unrecognized)
            method_press_enter()
            continue

class Estudante:

    str_op_menu = ("\n=====  Menu Operacional  [Estudantes]  =====\n\n"
                    "c - Incluir\n"
                    "l - Listar\n"
                    "u - Atualizar\n"
                    "d - Excluir\n"
                    "q - Menu Principal")

    def __init__(self):
        try:
            with open("estudantes.json", "r", encoding="utf-8") as file:
                self.lista = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.lista = []

    def incluir(self, str_op_menu, main_choice):
        codigo_valido = True
        cpf_valido = False
        input_codigo = input("\nInforme o código do(a) estudante: ")
        nome = str(input("\nInforme o nome do(a) estudante: "))
        input_cpf = str(input("\nInforme o CPF do(a) estudante: "))
        cpf = (f"{input_cpf[:3]}"
               f".{input_cpf[3:6]}"
               f".{input_cpf[6:9]}"
               f"-{input_cpf[9:]}")
        try:
            codigo = int(input_codigo)
        except ValueError:
            codigo = input_codigo
            codigo_valido = False
        if len(input_cpf.strip(".-")) == 11:
            cpf_valido = True
        str_success = (f"\nEstudante N.º{codigo} "
                  f"com o nome '{nome}' e o CPF '{cpf}' "
                  f"foi incluído(a) com êxito.")
        if codigo_valido and cpf_valido:
            if len(self.lista) == 0:
                # first we're checking if the list is empty
                dictionary = {
                    "codigo": codigo,
                    "nome": nome,
                    "cpf": cpf
                }
                self.lista.append(dictionary)
                with open("estudantes.json", "w", encoding="utf-8") as file:
                    json.dump(self.lista, file, ensure_ascii=False)
                print(str_success)
            else:
                # if it's not empty we're checking if any dictionary within the list has any of the same info
                codigo_igual = False
                nome_igual = False
                cpf_igual = False
                nada_igual = False
                for dicionario_criar in self.lista:
                    if dicionario_criar["codigo"] == codigo:
                        codigo_igual = True
                    if dicionario_criar["nome"] == nome:
                        nome_igual = True
                    if dicionario_criar["cpf"] == cpf:
                        cpf_igual = True
                    if not codigo_igual and not nome_igual and not cpf_igual:
                        nada_igual = True
                if nada_igual:
                    # if none of the info is the same we're gonna go ahead and create a dictionary for that student
                    dictionary = {
                        "codigo": codigo,
                        "nome": nome,
                        "cpf": cpf
                    }
                    self.lista.append(dictionary)
                    with open("estudantes.json", "w", encoding="utf-8") as file:
                        json.dump(self.lista, file, ensure_ascii=False)
                    print(str_success)
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
            if codigo_valido and not cpf_valido:
                print("\nCPF inválido, tente novamente com um CPF válido.")
            elif not codigo_valido and cpf_valido:
                print("\nCódigo inválido, tente novamente com um código válido.")
            elif not codigo_valido and not cpf_valido:
                print("\nCódigo e CPF inválidos, tente novamente com dados válidos.")
        # SOMEONE should probably fix this inconsistency with method_press_enter...
        method_press_enter()
        print(str_op_menu)
        method_op_menu(main_choice)

    def listar(self, str_op_menu, main_choice):
        if len(self.lista) == 0:
            # first we're checking if the list is empty
            print("\nComando indisponível: Nenhum(a) estudante foi encontrado(a).")
        else:
            # if it's not empty we'll print the list
            # IMPLEMENT: order the list instead of just printing it
            print(f"\nTotal de {len(self.lista)} estudante(s) encontrado(s): ")
            for dicionario_listar in self.lista:
                print(f"N.º{dicionario_listar["codigo"]}   "
                      f"Nome: {dicionario_listar["nome"]}   "
                      f"CPF: {dicionario_listar["cpf"]}")
        method_press_enter()
        print(str_op_menu)
        method_op_menu(main_choice)

    # IMPLEMENT: quando modificar um estudante, mudar o codigo na lista de matriculas
    def modificar(self, str_op_menu, main_choice):
        str_mod_menu = ("\n===========  Modificar Estudante  ===========\n\n"
                        "1 - Código\n"
                        "2 - Nome\n"
                        "3 - CPF\n"
                        "b - Voltar")
        if len(self.lista) == 0:
            # first we're checking if the list is empty
            print("\nComando indisponível: Nenhum(a) estudante foi encontrado(a).")
            # here's the method_press_enter inconsistency...
            method_press_enter()
            print(str_op_menu)
        else:
            # if it's not empty we're asking student's #
            estudante_modificar = None
            codigo_estudante_modificar = input("\nInforme o código do(a) estudante á ser modificado(a): ")
            for dicionario_modificar in self.lista:
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
                    print(str_mod_menu)
                    opcao_modificar = str.lower(input(select_command))
                    if opcao_modificar == '1':
                        codigo_antigo = estudante_modificar["codigo"]
                        codigo_novo = int(input("\nInforme o código novo: "))
                        for check in self.lista:
                            if codigo_novo == check["codigo"]:
                                print(f"\nNão foi possível modificar este(a) estudante, "
                                      f"já existe um(a) estudante cadastrado(a) com o N.º{codigo_novo}.")
                                break
                            else:
                                estudante_modificar["codigo"] = codigo_novo
                                print(f"\nCódigo modificado com êxito.\n"
                                      f"Código antigo: {codigo_antigo}\n"
                                      f"Código novo: {estudante_modificar["codigo"]}")
                                with open("estudantes.json", "w", encoding="utf-8") as file:
                                    json.dump(self.lista, file, ensure_ascii=False)
                                method_press_enter()
                    elif opcao_modificar == '2':
                        nome_antigo = estudante_modificar["nome"]
                        nome_novo = input("\nInforme o nome novo: ")
                        for check in self.lista:
                            if nome_novo == check["nome"]:
                                print(f"\nNão foi possível modificar este(a) estudante, "
                                      f"já existe um(a) estudante cadastrado(a) com o nome '{nome_novo}'.")
                                break
                            else:
                                estudante_modificar["nome"] = nome_novo
                                print(f"\nNome modificado com êxito.\n"
                                      f"Nome antigo: {nome_antigo}\n"
                                      f"Nome novo: {estudante_modificar["nome"]}")
                                with open("estudantes.json", "w", encoding="utf-8") as file:
                                    json.dump(self.lista, file, ensure_ascii=False)
                                method_press_enter()
                    elif opcao_modificar == '3':
                        cpf_antigo = estudante_modificar["cpf"]
                        cpf_novo = input("\nInforme o CPF novo: ")
                        for check in self.lista:
                            if cpf_novo == check["cpf"]:
                                print(f"\nNão foi possível modificar este(a) estudante, "
                                      f"já existe um(a) estudante cadastrado(a) com o CPF '{cpf_novo}'.")
                                break
                            else:
                                estudante_modificar["cpf"] = cpf_novo
                                print(f"\nCPF modificado com êxito.\n"
                                      f"CPF antigo: {cpf_antigo}\n"
                                      f"CPF novo: {estudante_modificar["cpf"]}")
                                with open("estudantes.json", "w", encoding="utf-8") as file:
                                    json.dump(self.lista, file, ensure_ascii=False)
                                method_press_enter()
                    elif opcao_modificar == 'b':
                        print(self.str_op_menu)
                        method_op_menu(main_choice)
                        break
                    else:
                        print(error_unrecognized)
                        method_press_enter()

    # IMPLEMENT: quando excluir um estudante, deletar a matrícula
    def excluir(self, str_op_menu, main_choice):
        # first we're checking if the list is empty
        if len(self.lista) == 0:
            print("\nComando indisponível: Nenhum(a) estudante foi encontrado(a).")
        else:
            # if it's not empty we're asking the # to search for
            estudante_remover = None
            codigo_remover = int(input("\nInforme o código do(a) estudante á ser removido(a): "))
            for dicionario_remover in self.lista:
                # then we're finding the right dictionary to modify
                if dicionario_remover["codigo"] == codigo_remover:
                    estudante_remover = dicionario_remover
                    estudante_remover_codigo = dicionario_remover["codigo"]
                    estudante_remover_nome = dicionario_remover["nome"]
                    estudante_remover_cpf = dicionario_remover["cpf"]
                    break
            if estudante_remover is None:
                print(f"\nEstudante N.º{codigo_remover} não encontrado(a).")
            else:
                # now we're going to make sure that the user chose the right student
                print(f"\nVocê escolheu o(a) estudante: `N.º{estudante_remover_codigo}  "
                      f" Nome: {estudante_remover_nome}   "
                      f"CPF: {estudante_remover_cpf}`")
                option_yn = str.lower(input("\nDigite 'sim' se realmente deseja excluir este(a) estudante: "))
                if option_yn == 'sim':
                    self.lista.remove(estudante_remover)
                    with open("estudantes.json", "w", encoding="utf-8") as file:
                        json.dump(self.lista, file, ensure_ascii=False)
                    print(f"\nEstudante N.º{estudante_remover_codigo} "
                          f"foi excluído(a) com êxito.")
                else:
                    print("\nEstudante não excluído(a).")
        method_press_enter()
        print(str_op_menu)
        method_op_menu(main_choice)

class Disciplina:

    str_op_menu = ("\n=====  Menu Operacional  [Disciplinas]  =====\n\n"
                   "c - Incluir\n"
                   "l - Listar\n"
                   "u - Atualizar\n"
                   "d - Excluir\n"
                   "q - Menu Principal")

    def __init__(self):
        nome = None
        codigo = None
        try:
            with open("disciplinas.json", "r", encoding="utf-8") as file:
                self.lista = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.lista = []

    def incluir(self, str_op_menu, main_choice):
        def text_success():
            print(f"\nDisciplina N.º{codigo} de "
                  f"'{nome}' foi incluída com êxito.")
        codigo = int(input("\nInforme o código do(a) disciplina: "))
        nome = str(input("\nInforme o nome do(a) disciplina: "))
        if len(self.lista) == 0:
        # first we're checking if the list is empty
            disciplina_dict = {
                "codigo": codigo,
                "nome": nome,
            }
            self.lista.append(disciplina_dict)
            with open("disciplinas.json", "w", encoding="utf-8") as file_disciplinas:
                json.dump(self.lista, file_disciplinas, ensure_ascii=False)
            text_success()
        else:
        # if it's not empty we're checking if any dictionary within the list has any of the same info
            codigo_igual = False
            nome_igual = False
            nada_igual = False
            for dicionario_criar in self.lista:
                if dicionario_criar["codigo"] == codigo:
                    codigo_igual = True
                if dicionario_criar["nome"] == nome:
                    nome_igual = True
                if not codigo_igual and not nome_igual:
                    nada_igual = True
            if nada_igual:
            # if none of the info is the same we're gonna go ahead and create a dictionary for that subject
                disciplina_dict = {
                    "codigo": codigo,
                    "nome": nome,
                }
                self.lista.append(disciplina_dict)
                with open("disciplinas.json", "w", encoding="utf-8") as file_disciplinas:
                    json.dump(self.lista, file_disciplinas, ensure_ascii=False)
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
        print(str_op_menu)
        method_op_menu(main_choice)

    def listar(self, str_op_menu, main_choice):
        if len(self.lista) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhuma disciplina foi encontrado(a).")
        else:
        # if it's not empty we'll print the list
        # IMPLEMENT: order the list instead of just printing it
            print(f"\nTotal de {len(self.lista)} disciplina(s) encontrada(s): ")
            for dicionario_listar in self.lista:
                print(f"N.º{dicionario_listar["codigo"]}   "
                      f"Nome: {dicionario_listar["nome"]}")
        method_press_enter()
        print(str_op_menu)
        method_op_menu(main_choice)

    # IMPLEMENT: quando modificar uma disciplina, mudar o codigo na lista de turmas
    def modificar(self, str_op_menu, main_choice):

        str_mod_menu = ("\n===========  Modificar Disciplina  ===========\n\n"
                        "1 - Código\n"
                        "2 - Nome\n"
                        "b - Voltar")

        if len(self.lista) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhuma disciplina foi encontrada.")
            # here's the method_press_enter inconsistency...
            method_press_enter()
            print(str_op_menu)
        else:
        # if it's not empty we're asking student's #
            disciplina_modificar = None
            codigo_disciplina_modificar = input("\nInforme o código da disciplina a ser modificada: ")
            for dicionario_modificar in self.lista:
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
                    print(str_mod_menu)
                    opcao_modificar = str.lower(input(select_command))
                    if opcao_modificar == '1':
                        codigo_antigo = disciplina_modificar["codigo"]
                        codigo_novo = int(input("\nInforme o código novo: "))
                        for check in self.lista:
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
                                    json.dump(self.lista, file_disciplinas, ensure_ascii=False)
                                method_press_enter()
                    elif opcao_modificar == '2':
                        nome_antigo = disciplina_modificar["nome"]
                        nome_novo = input("\nInforme o nome novo: ")
                        for check in self.lista:
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
                                    json.dump(self.lista, file_disciplinas, ensure_ascii=False)
                                method_press_enter()
                    elif opcao_modificar == 'b':
                        print(str_op_menu)
                        method_op_menu(main_choice)
                        break
                    else:
                        print(error_unrecognized)
                        method_press_enter()

    def excluir(self, str_op_menu, main_choice):
        # first we're checking if the list is empty
        if len(self.lista) == 0:
            print("\nComando indisponível: Nenhuma disciplina foi encontrada.")
        else:
        # if it's not empty we're asking the # to search for
            disciplina_remover = None
            codigo_remover = int(input("\nInforme o código da disciplina a ser removida: "))
            for dicionario_remover in self.lista:
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
                    self.lista.remove(disciplina_remover)
                    with open("disciplinas.json", "w", encoding="utf-8") as file_disciplinas:
                        json.dump(self.lista, file_disciplinas, ensure_ascii=False)
                    print(f"\nDisciplina N.º{disciplina_remover_codigo} "
                          f"foi excluída com êxito.")
                else:
                    print("\nDisciplina não excluída.")
        method_press_enter()
        print(str_op_menu)
        method_op_menu(main_choice)

class Professor:

    str_op_menu = ("\n=====  Menu Operacional  [Professores]  =====\n\n"
                    "c - Incluir\n"
                    "l - Listar\n"
                    "u - Atualizar\n"
                    "d - Excluir\n"
                    "q - Menu Principal")

    def __init__(self):
        try:
            with open("professores.json", "r", encoding="utf-8") as file:
                self.lista = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.lista = []

    def incluir(self, str_op_menu, main_choice):
        codigo_valido = True
        cpf_valido = False
        input_codigo = input("\nInforme o código do(a) professor(a): ")
        nome = str(input("\nInforme o nome do(a) professor(a): "))
        input_cpf = str(input("\nInforme o CPF do(a) professor(a): "))
        cpf = (f"{input_cpf[:3]}"
               f".{input_cpf[3:6]}"
               f".{input_cpf[6:9]}"
               f"-{input_cpf[9:]}")
        try:
            codigo = int(input_codigo)
        except ValueError:
            codigo = input_codigo
            codigo_valido = False
        if len(input_cpf.strip(".-")) == 11:
            cpf_valido = True
        str_success = (f"\nProfessor(a) N.º{codigo} "
                       f"com o nome '{nome}' e o CPF '{cpf}' "
                       f"foi incluído(a) com êxito.")
        if cpf_valido and codigo_valido:
            if len(self.lista) == 0:
            # first we're checking if the list is empty
                dictionary = {
                    "codigo": codigo,
                    "nome": nome,
                    "cpf": cpf
                }
                self.lista.append(dictionary)
                with open("professores.json", "w", encoding="utf-8") as file:
                    json.dump(self.lista, file, ensure_ascii=False)
                print(str_success)
            else:
            # if it's not empty we're checking if any dictionary within the list has any of the same info
                codigo_igual = False
                nome_igual = False
                cpf_igual = False
                nada_igual = False
                for dicionario_criar in self.lista:
                    if dicionario_criar["codigo"] == codigo:
                        codigo_igual = True
                    if dicionario_criar["nome"] == nome:
                        nome_igual = True
                    if dicionario_criar["cpf"] == cpf:
                        cpf_igual = True
                    if not codigo_igual and not nome_igual and not cpf_igual:
                        nada_igual = True
                if nada_igual:
                # if none of the info is the same we're gonna go ahead and create a dictionary for that student
                    dictionary = {
                        "codigo": codigo,
                        "nome": nome,
                        "cpf": cpf
                    }
                    self.lista.append(dictionary)
                    with open("professores.json", "w", encoding="utf-8") as file:
                        json.dump(self.lista, file, ensure_ascii=False)
                    print(str_success)
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
        else:
            if codigo_valido and not cpf_valido:
                print("\nCPF inválido, tente novamente com um CPF válido.")
            elif not codigo_valido and cpf_valido:
                print("\nCódigo inválido, tente novamente com um código válido.")
            elif not codigo_valido and not cpf_valido:
                print("\nCódigo e CPF inválidos, tente novamente com dados válidos.")
        # SOMEONE should probably fix this inconsistency with method_press_enter...
        method_press_enter()
        print(str_op_menu)
        method_op_menu(main_choice)

    def listar(self, str_op_menu, main_choice):
        if len(self.lista) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhum(a) professor(a) foi encontrado(a).")
        else:
        # if it's not empty we'll print the list
        # IMPLEMENT: order the list instead of just printing it
            print(f"\nTotal de {len(self.lista)} professor(as) encontrado(as): ")
            for dicionario_listar in self.lista:
                print(f"N.º{dicionario_listar["codigo"]}   "
                      f"Nome: {dicionario_listar["nome"]}   "
                      f"CPF: {dicionario_listar["cpf"]}")
        method_press_enter()
        print(str_op_menu)
        method_op_menu(main_choice)

    # IMPLEMENT: quando modificar um professor, mudar o codigo na lista de turmas
    def modificar(self, str_op_menu, main_choice):

        str_mod_menu = ("\n===========  Modificar Professor  ===========\n\n"
                        "1 - Código\n"
                        "2 - Nome\n"
                        "3 - CPF\n"
                        "b - Voltar")

        if len(self.lista) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhum(a) professor(a) foi encontrado(a).")
            # here's the method_press_enter inconsistency...
            method_press_enter()
            print(str_op_menu)
        else:
        # if it's not empty we're asking student's #
            professor_modificar = None
            codigo_professor_modificar = input("\nInforme o código do(a) professor(a) a ser modificado(a): ")
            for dicionario_modificar in self.lista:
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
                    print(str_mod_menu)
                    opcao_modificar = str.lower(input(select_command))
                    if opcao_modificar == '1':
                        codigo_antigo = professor_modificar["codigo"]
                        codigo_novo = int(input("\nInforme o código novo: "))
                        for check in self.lista:
                            if codigo_novo == check["codigo"]:
                                print(f"\nNão foi possível modificar este(a) professor(a), "
                                      f"já existe um(a) professor(a) cadastrado(a) com o N.º{codigo_novo}.")
                                break
                            else:
                                professor_modificar["codigo"] = codigo_novo
                                print(f"\nCódigo modificado com êxito.\n"
                                      f"Código antigo: {codigo_antigo}\n"
                                      f"Código novo: {professor_modificar["codigo"]}")
                                with open("professores.json", "w", encoding="utf-8") as file:
                                    json.dump(self.lista, file, ensure_ascii=False)
                                method_press_enter()
                    elif opcao_modificar == '2':
                        nome_antigo = professor_modificar["nome"]
                        nome_novo = input("\nInforme o nome novo: ")
                        for check in self.lista:
                            if nome_novo == check["nome"]:
                                print(f"\nNão foi possível modificar este(a) professor(a), "
                                      f"já existe um(a) professor(a) cadastrado(a) com o nome '{nome_novo}'.")
                                break
                            else:
                                professor_modificar["nome"] = nome_novo
                                print(f"\nNome modificado com êxito.\n"
                                      f"Nome antigo: {nome_antigo}\n"
                                      f"Nome novo: {professor_modificar["nome"]}")
                                with open("professores.json", "w", encoding="utf-8") as file:
                                    json.dump(self.lista, file, ensure_ascii=False)
                                method_press_enter()
                    elif opcao_modificar == '3':
                        cpf_antigo = professor_modificar["cpf"]
                        cpf_novo = input("\nInforme o CPF novo: ")
                        for check in self.lista:
                            if cpf_novo == check["cpf"]:
                                print(f"\nNão foi possível modificar este(a) professor(a), "
                                      f"já existe um(a) professor(a) cadastrado(a) com o CPF '{cpf_novo}'.")
                                break
                            else:
                                professor_modificar["cpf"] = cpf_novo
                                print(f"\nCPF modificado com êxito.\n"
                                      f"CPF antigo: {cpf_antigo}\n"
                                      f"CPF novo: {professor_modificar["cpf"]}")
                                with open("professores.json", "w", encoding="utf-8") as file:
                                    json.dump(self.lista, file, ensure_ascii=False)
                                method_press_enter()
                    elif opcao_modificar == 'b':
                        print(str_op_menu)
                        method_op_menu(main_choice)
                        break
                    else:
                        print(error_unrecognized)
                        method_press_enter()

    def excluir(self, str_op_menu, main_choice):
        # first we're checking if the list is empty
        if len(self.lista) == 0:
            print("\nComando indisponível: Nenhum(a) professor(a) foi encontrado(a).")
        else:
        # if it's not empty we're asking the # to search for
            professor_remover = None
            codigo_remover = int(input("\nInforme o código do(a) professor(a) a ser removido(a): "))
            for dicionario_remover in self.lista:
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
                    self.lista.remove(professor_remover)
                    with open("professores.json", "w", encoding="utf-8") as file:
                        json.dump(self.lista, file, ensure_ascii=False)
                    print(f"\nProfessor(a) N.º{professor_remover_codigo} "
                          f"foi excluído(a) com êxito.")
                else:
                    print("\nProfessor(a) não excluído(a).")
        method_press_enter()
        print(str_op_menu)
        method_op_menu(main_choice)

class Turma:

    str_op_menu = ("\n=======  Menu Operacional  [Turmas]  =======\n\n"
                    "c - Incluir\n"
                    "l - Listar\n"
                    "u - Atualizar\n"
                    "d - Excluir\n"
                    "q - Menu Principal")

    def __init__(self):
        try:
            with open("turmas.json", "r", encoding="utf-8") as file:
                self.lista = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.lista = []
        try:
            with open("disciplinas.json", "r", encoding="utf-8") as file:
                self.disciplina_lista = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.disciplina_lista = []
        try:
            with open("professores.json", "r", encoding="utf-8") as file:
                self.professor_lista = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.professor_lista = []

    def incluir(self, str_op_menu, main_choice):
        def text_success():
            print(f"\nTurma N.º{turma_codigo} "
                  f"com o(a) professor(a) '{professor_nome}' e a disciplina '{disciplina_nome}' "
                  f"foi incluída com êxito.")
        turma_codigo = int(input("\nInforme o código da turma: "))
        professor_codigo = int(input("\nInforme o código do(a) professor(a): "))
        disciplina_codigo = int(input("\nInforme o código da disciplina: "))
        professor_existe = False
        disciplina_existe = False
        for check_professor in self.professor_lista:
            if check_professor["codigo"] == professor_codigo:
                professor_existe = True
                professor_nome = check_professor["nome"]
        for check_disciplina in self.disciplina_lista:
            if check_disciplina["codigo"] == disciplina_codigo:
                disciplina_existe = True
                disciplina_nome = check_disciplina["nome"]
        if professor_existe and disciplina_existe:
        # first we're checking if the list is empty
            if len(self.lista) == 0:
                dictionary = {
                    "turma_codigo": int(turma_codigo),
                    "professor_codigo": int(professor_codigo),
                    "disciplina_codigo": int(disciplina_codigo)
                }
                self.lista.append(dictionary)
                with open("turmas.json", "w", encoding="utf-8") as file:
                    json.dump(self.lista, file, ensure_ascii=False)
                text_success()
        # if it's not empty we're checking if any dictionary within the list has the same #
            else:
                codigo_igual_turma = False
                for dicionario_criar in self.lista:
                    if dicionario_criar["turma_codigo"] == turma_codigo:
                        codigo_igual_turma = True
                if not codigo_igual_turma:
                    # if none of them have the same # we'll create a dictionary for that class
                    dictionary = {
                        "turma_codigo": int(turma_codigo),
                        "professor_codigo": int(professor_codigo),
                        "disciplina_codigo": int(disciplina_codigo)
                    }
                    self.lista.append(dictionary)
                    with open("turmas.json", "w", encoding="utf-8") as file:
                        json.dump(self.lista, file, ensure_ascii=False)
                    text_success()
                # if the # is repeated we'll tell the user
                else:
                    if codigo_igual_turma:
                        print("\nErro: Não foi possível cadastrar esta turma, "
                              "já existe uma turma com o mesmo código.")
        # if any of the checks fail we'll tell the user what did
        elif not professor_existe and not disciplina_existe:
            print(f"\nProfessor(a) e disciplina não encontrados, "
                  f"tente novamente com cadastros existentes, ou crie cadastros novos.")
        elif not professor_existe and disciplina_existe:
            print(f"\nProfessor(a) não encontrado(a), "
                  f"tente novamente com um cadastro existente, ou crie um novo.")
        elif professor_existe and not disciplina_existe:
            print(f"\nDisciplina não encontrada, "
                  f"tente novamente com um cadastro existente, ou crie um novo.")
        else:
            print(error_undefined)
            method_press_enter()
        # SOMEONE should probably fix this inconsistency with method_press_enter...
        method_press_enter()
        print(str_op_menu)
        method_op_menu(main_choice)

    def listar(self, str_op_menu, main_choice):
        if len(self.lista) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhuma turma foi encontrada.")
        else:
        # if it's not empty we'll print the list
        # IMPLEMENT: order the list instead of just printing it
            print(f"\nTotal de {len(self.lista)} turma(s) encontrada(s): ")
            for dicionario_listar in self.lista:
                professor_nome = None
                disciplina_nome = None
                for dicionario_professor in self.professor_lista:
                    professor_nome = dicionario_professor["nome"]
                    break
                for dicionario_disciplina in self.disciplina_lista:
                    disciplina_nome = dicionario_disciplina["nome"]
                    break
                print(f"Turma N.º{dicionario_listar["turma_codigo"]}    "
                      f"Disciplina: {disciplina_nome}    "
                      f"Professor(a): {professor_nome}")
        method_press_enter()
        print(str_op_menu)
        method_op_menu(main_choice)

    # IMPLEMENT: quando modificar uma turma, mudar o codigo na lista de matriculas
    def modificar(self, str_op_menu, main_choice):

        str_mod_menu = ("\n=============  Modificar Turma  =============\n\n"
                        "1 - Código da turma\n"
                        "2 - Código do professor\n"
                        "3 - Código da disciplina\n"
                        "b - Voltar")

        if len(self.lista) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhuma turma foi encontrada.")
            # here's the method_press_enter inconsistency...
            method_press_enter()
            print(str_op_menu)
        else:
        # if it's not empty we're asking student's #
            turma_modificar = None
            codigo_turma_modificar = input("\nInforme o código da turma a ser modificada: ")
            for dicionario_modificar in self.lista:
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
                    print(str_mod_menu)
                    opcao_modificar = str.lower(input(select_command))
                    if opcao_modificar == '1':
                        codigo_antigo_turma = turma_modificar["turma_codigo"]
                        codigo_novo_turma = int(input("\nInforme o código novo da turma: "))
                        for check in self.lista:
                            if codigo_novo_turma == check["turma_codigo"]:
                                print(f"\nNão foi possível modificar esta turma, "
                                      f"já existe uma turma cadastrada com o N.º{codigo_novo_turma}.")
                                break
                            else:
                                turma_modificar["turma_codigo"] = codigo_novo_turma
                                print(f"\nCódigo modificado com êxito.\n"
                                      f"Código antigo: {codigo_antigo_turma}\n"
                                      f"Código novo: {turma_modificar["turma_codigo"]}")
                                with open("turmas.json", "w", encoding="utf-8") as file:
                                    json.dump(self.lista, file, ensure_ascii=False)
                                method_press_enter()
                    elif opcao_modificar == '2':
                        codigo_antigo_professor = turma_modificar["professor_codigo"]
                        codigo_novo_professor = int(input("\nInforme o código do(a) professor(a) novo(a): "))
                        for check_professor in self.professor_lista:
                            if codigo_novo_professor == check_professor["codigo"]:
                                turma_modificar["professor_codigo"] = codigo_novo_professor
                                print(f"\nCódigo modificado com êxito.\n"
                                      f"Código antigo: {codigo_antigo_professor}\n" 
                                      f"Código novo: {turma_modificar["professor_codigo"]}")
                                with open("turmas.json", "w", encoding="utf-8") as file:
                                    json.dump(self.lista, file, ensure_ascii=False)
                                method_press_enter()
                            else:
                                print(f"Erro: Professor(a) não encontrado(a), "
                                      f"tente novamente com um(a) professor(a) existente, "
                                      f"ou crie um novo cadastro.")
                                method_press_enter()
                    elif opcao_modificar == '3':
                        codigo_antigo_disciplina = turma_modificar["disciplina_codigo"]
                        codigo_novo_disciplina = int(input("\nInforme o código da disciplina nova: "))
                        for check_disciplina in self.disciplina_lista:
                            if codigo_novo_disciplina == check_disciplina["codigo"]:
                                turma_modificar["disciplina_codigo"] = codigo_novo_disciplina
                                print(f"\nCódigo modificado com êxito.\n"
                                      f"Código antigo: {codigo_antigo_disciplina}\n"
                                      f"Código novo: {turma_modificar["disciplina_codigo"]}")
                                with open("turmas.json", "w", encoding="utf-8") as file:
                                    json.dump(self.lista, file, ensure_ascii=False)
                                method_press_enter()
                            else:
                                print(f"Erro: Disciplina não encontrada, "
                                      f"tente novamente com uma disciplina existente, "
                                      f"ou crie um novo cadastro.")
                                method_press_enter()
                    elif opcao_modificar == 'b':
                        print(str_op_menu)
                        method_op_menu(main_choice)
                        break
                    else:
                        print(error_unrecognized)
                        method_press_enter()

    def excluir(self, str_op_menu, main_choice):
        # first we're checking if the list is empty
        if len(self.lista) == 0:
            print("\nComando indisponível: Nenhuma turma foi encontrada.")
        else:
        # if it's not empty we're asking the # to search for
            turma_remover = None
            codigo_remover = int(input("\nInforme o código da turma a ser removida: "))
            for dicionario_remover in self.lista:
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
                    self.lista.remove(turma_remover)
                    with open("turmas.json", "w", encoding="utf-8") as file:
                        json.dump(self.lista, file, ensure_ascii=False)
                    print(f"\nTurma N.º{turma_remover_codigo} "
                          f"foi excluída com êxito.")
                else:
                    print("\nTurma não excluída.")
            method_press_enter()
            print(str_op_menu)
            method_op_menu(main_choice)

class Matricula:

    str_op_menu = ("\n=====  Menu Operacional  [Matrículas]  =====\n\n"
                    "c - Incluir\n"
                    "l - Listar\n"
                    "u - Atualizar\n"
                    "d - Excluir\n"
                    # FIX: change q to b
                    "q - Menu Principal")

    def __init__(self):
        try:
            with open("matriculas.json", "r", encoding="utf-8") as file:
                self.lista = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.lista = []
        try:
            with open("estudantes.json", "r", encoding="utf-8") as file:
                self.estudante_lista = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.estudante_lista = []
        try:
            with open("turmas.json", "r", encoding="utf-8") as file:
                self.turma_lista = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.turma_lista = []

    def incluir(self, str_op_menu, main_choice):
        def text_success():
            print(f"\nEstudante N.º{estudante_codigo} "
                  f"foi matrículado(a) na turma N.º{turma_codigo} com êxito.")
        estudante_codigo = int(input("\nInforme o código do(a) estudante: "))
        turma_codigo = int(input("\nInforme o código da turma: "))
        turma_existe = False
        estudante_existe = False
        for check_estudante in self.estudante_lista:
            if check_estudante["codigo"] == estudante_codigo:
                estudante_existe = True
                estudante_nome = check_estudante["nome"]
        for check_turma in self.turma_lista:
            if check_turma["turma_codigo"] == turma_codigo:
                turma_existe = True
        if turma_existe and estudante_existe:
            if len(self.lista) == 0:
            # first we're checking if the list is empty
                dictionary = {
                    "estudante_codigo": int(estudante_codigo),
                    "turma_codigo": int(turma_codigo),
                }
                self.lista.append(dictionary)
                with open("matriculas.json", "w", encoding="utf-8") as file:
                    json.dump(self.lista, file, ensure_ascii=False)
                text_success()
            else:
            # if it's not empty we're checking if any dictionary within the list has any of the same info

                # if none of the info is the same we're gonna go ahead and create a dictionary for that student
                if turma_existe and estudante_existe:
                    dictionary = {
                        "estudante_codigo": int(estudante_codigo),
                        "turma_codigo": int(turma_codigo),
                    }
                    self.lista.append(dictionary)
                    with open("matriculas.json", "w", encoding="utf-8") as file:
                        json.dump(self.lista, file, ensure_ascii=False)
                    text_success()
                # if any info is repeated we'll tell the user what is
        elif not turma_existe and not estudante_existe:
            print(f"\nTurma e estudante não encontrados, "
                  f"tente novamente com cadastros existentes, ou crie cadastros novos.")
        elif not turma_existe and estudante_existe:
            print(f"\nTurma não encontrada, "
                  f"tente novamente com um cadastro existente, ou crie um novo.")
        elif turma_existe and not estudante_existe:
            print(f"\nEstudante não encontrado(a), "
                  f"tente novamente com um cadastro existente, ou crie um novo.")
        # SOMEONE should probably fix this inconsistency with method_press_enter...
        method_press_enter()
        print(str_op_menu)
        method_op_menu(main_choice)

    def listar(self, str_op_menu, main_choice):
        if len(self.lista) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhuma matrícula foi encontrada.")
        else:
        # if it's not empty we'll print the list
        # IMPLEMENT: order the list instead of just printing it
            print(f"\nTotal de {len(self.lista)} matrícula(s) encontrada(s): ")
            for dicionario_listar in self.lista:
                estudante_nome = None
                for dicionario_estudante in self.estudante_lista:
                    estudante_nome = dicionario_estudante["nome"]
                print(f"Estudante N.º{dicionario_listar["estudante_codigo"]} - {estudante_nome}"
                      f"    Turma N.º{dicionario_listar["turma_codigo"]}")
        method_press_enter()
        print(str_op_menu)
        method_op_menu(main_choice)

    def modificar(self, str_op_menu, main_choice):

        str_mod_menu = ("\n===========  Modificar Matrícula  ===========\n\n"
                        "1 - Código da turma\n"
                        "b - Voltar")

        if len(self.lista) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhuma matrícula foi encontrada.")
            # here's the method_press_enter inconsistency...
            method_press_enter()
            print(str_op_menu)
        else:
        # if it's not empty we're asking student's #
            estudante_existe = False
            matricula_modificar = None
            codigo_estudante_modificar = int(input("\nInforme o código do(a) estudante cuja matrícula deseja modificar: "))
            for check_estudante in self.estudante_lista:
                if check_estudante["codigo"] == codigo_estudante_modificar:
                    estudante_existe = True
                    estudante_nome = check_estudante["nome"]
                    break
            for dicionario_modificar in self.lista:
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
                    print(str_mod_menu)
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
                        for check_turma in self.turma_lista:
                            if codigo_novo_turma == check_turma["turma_codigo"]:
                                matricula_modificar["turma_codigo"] = codigo_novo_turma
                                print(f"\nCódigo modificado com êxito.\n"
                                      f"Código antigo: {codigo_antigo_turma}\n"
                                      f"Código novo: {matricula_modificar["turma_codigo"]}")
                                with open("matriculas.json", "w", encoding="utf-8") as file:
                                    json.dump(self.lista, file, ensure_ascii=False)
                                method_press_enter()
                            else:
                                print(f"\nTurma não encontrada, "
                                      f"tente novamente com uma turma existente, "
                                      f"ou crie um novo cadastro.")
                                method_press_enter()
                    elif opcao_modificar == 'b':
                        print(str_op_menu)
                        method_op_menu(main_choice)
                        break
                    else:
                        print(error_unrecognized)
                        method_press_enter()

    def excluir(self, str_op_menu, main_choice):
        # first we're checking if the list is empty
        if len(self.lista) == 0:
            print("\nComando indisponível: Nenhuma matrícula foi encontrada.")
        else:
        # if it's not empty we're asking the # to search for
            estudante_existe = False
            matricula_remover = None
            codigo_remover = int(input("\nInforme o código do(a) estudante cuja matrícula deseja remover: "))
            for check_estudante in self.estudante_lista:
                if check_estudante["codigo"] == codigo_remover:
                    estudante_existe = True
                    break
            for dicionario_remover in self.lista:
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
                        self.lista.remove(matricula_remover)
                        with open("matriculas.json", "w", encoding="utf-8") as file:
                            json.dump(self.lista, file, ensure_ascii=False)
                        print(f"\nMatricula N.º{estudante_remover_codigo} "
                              f"foi excluído(a) com êxito.")
                    else:
                        print("\nMatricula não excluído(a).")
        method_press_enter()
        print(str_op_menu)
        method_op_menu(main_choice)

# instancing
estudante = Estudante()
disciplina = Disciplina()
professor = Professor()
turma = Turma()
matricula = Matricula()

# start application
print(str_main_menu)
method_main_menu()