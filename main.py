# I am at my wit's end, if you find this message tell nietzche he was right about python
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
            print(str_main_menu)
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
            else:
                print(error_unrecognized)
                method_press_enter()
                print(Estudante.str_op_menu)
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
            else:
                print(error_unrecognized)
                method_press_enter()
                print(Disciplina.str_op_menu)
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
            else:
                print(error_unrecognized)
                method_press_enter()
                print(Professor.str_op_menu)
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
            else:
                print(error_unrecognized)
                method_press_enter()
                print(Turma.str_op_menu)
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
                print(Matricula.str_op_menu)

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
        try:
            with open("matriculas.json", "r", encoding="utf-8") as file:
                self.matricula_lista = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.matricula_lista = []

    def incluir(self, str_op_menu, main_choice):
        codigo_valido = True
        cpf_valido = False
        codigo = input("\nInforme o código do(a) estudante: ")
        nome = input("\nInforme o nome do(a) estudante: ")
        cpf = input("\nInforme o CPF do(a) estudante: ")
        try:
            codigo = int(codigo)
        except ValueError:
            codigo_valido = False
        if len(cpf.strip(".-")) == 11:
            cpf_valido = True
            cpf = (f"{cpf[:3]}"
                   f".{cpf[3:6]}"
                   f".{cpf[6:9]}"
                   f"-{cpf[9:]}")
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
                print("\nCódigo inválido, tente novamente com um código numérico válido.")
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
            codigo_estudante_valido = True
            codigo_estudante_modificar = input("\nInforme o código do(a) estudante á ser modificado(a): ")
            try:
                codigo_estudante_modificar = int(codigo_estudante_modificar)
            except ValueError:
                codigo_estudante_valido = False
            if codigo_estudante_valido:
                for dicionario_modificar in self.lista:
                    # then we're finding the right dictionary to modify
                    if dicionario_modificar["codigo"] == codigo_estudante_modificar:
                        estudante_modificar = dicionario_modificar
                        print(f"\nVocê escolheu o(a) estudante: `N.º{codigo_estudante_modificar}  "
                              f" Nome: {dicionario_modificar["nome"]}   "
                              f"CPF: {dicionario_modificar["cpf"]}`")
                        break
                if estudante_modificar is None:
                    print(f"\nEstudante N.º{codigo_estudante_modificar} não encontrado(a).")
                    method_press_enter()
                    print(str_op_menu)
                    method_op_menu(main_choice)
                else:
                    while True:
                        # then we're implementing a menu for modifying the chosen dictionary
                            print(str_mod_menu)
                            opcao_modificar = str.lower(input(select_command))
                            if opcao_modificar == '1':
                                codigo_antigo = estudante_modificar["codigo"]
                                codigo_novo = input("\nInforme o código novo: ")
                                codigo_novo_valido = True
                                try:
                                    codigo_novo = int(codigo_novo)
                                except ValueError:
                                    codigo_novo_valido = False
                                if codigo_novo_valido:
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
                                else:
                                    print("\nCódigo do(a) estudante inválido, tente novamente com um código numérico válido.")
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
                                cpf_valido = False
                                if len(cpf_novo.strip(".-")) == 11:
                                    cpf_valido = True
                                    cpf = (f"{cpf[:3]}"
                                           f".{cpf[3:6]}"
                                           f".{cpf[6:9]}"
                                           f"-{cpf[9:]}")
                                if cpf_valido:
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
                                else:
                                    print("\nCPF inválido, tente novamente com um CPF válido.")
                            elif opcao_modificar == 'b':
                                print(self.str_op_menu)
                                method_op_menu(main_choice)
                                break
                            else:
                                print(error_unrecognized)
                                method_press_enter()
            else:
                print("\nCódigo do(a) estudante inválido, tente novamente com um código numérico válido.")

    def excluir(self, str_op_menu, main_choice):
        # first we're checking if the list is empty
        if len(self.lista) == 0:
            print("\nComando indisponível: Nenhum(a) estudante foi encontrado(a).")
        else:
            # if it's not empty we're asking the # to search for
            estudante_remover = None
            estudante_matriculado = False
            codigo_remover_valido = True
            codigo_remover = input("\nInforme o código do(a) estudante á ser removido(a): ")
            try:
                codigo_remover = int(codigo_remover)
            except ValueError:
                codigo_remover_valido = False
            if codigo_remover_valido:
                for dicionario_remover in self.lista:
                    # then we're finding the right dictionary to modify
                    if dicionario_remover["codigo"] == codigo_remover:
                        estudante_remover = dicionario_remover
                        estudante_remover_codigo = dicionario_remover["codigo"]
                        estudante_remover_nome = dicionario_remover["nome"]
                        estudante_remover_cpf = dicionario_remover["cpf"]
                        break
                for dicionario_remover in self.matricula_lista:
                    if dicionario_remover["estudante_codigo"] == codigo_remover:
                        estudante_matriculado = True
                if not estudante_matriculado:
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
                else:
                    print(f"\nNão foi possível excluír estudante N.º{estudante_remover_codigo}, "
                          "este(a) estudante está matriculado. "
                          "Tente novamente após remover a matrícula.")
            else:
                print("\nCódigo do(a) estudante inválido, tente novamente com um código numérico válido.")

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
        try:
            with open("disciplinas.json", "r", encoding="utf-8") as file:
                self.lista = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.lista = []
        try:
            with open("turmas.json", "r", encoding="utf-8") as file:
                self.turma_lista = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.turma_lista = []

    def incluir(self, str_op_menu, main_choice):
        def text_success():
            print(f"\nDisciplina N.º{codigo} de "
                  f"'{nome}' foi incluída com êxito.")
        codigo = input("\nInforme o código do(a) disciplina: ")
        nome = input("\nInforme o nome do(a) disciplina: ")
        codigo_valido = True
        try:
            codigo = int(codigo)
        except ValueError:
            codigo_valido = False
        if codigo_valido:
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
        else:
            print("\nCódigo da disciplina inválido, tente novamente com um código numérico válido.")
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
            disciplina_em_turma = False
            turma_modificar = None
            codigo_disciplina_valido = True
            codigo_disciplina_modificar = input("\nInforme o código da disciplina a ser modificada: ")
            try:
                codigo_disciplina_modificar = int(codigo_disciplina_modificar)
            except ValueError:
                codigo_disciplina_valido = False
            for dicionario_modificar in self.lista:
            # then we're finding the right dictionary to modify
                if dicionario_modificar["codigo"] == codigo_disciplina_modificar:
                    disciplina_modificar = dicionario_modificar
                    print(f"\nVocê escolheu a disciplina: `N.º{codigo_disciplina_modificar}  "
                          f" Nome: {dicionario_modificar["nome"]}`")
                    break
            for dicionario_modificar in self.turma_lista:
                if dicionario_modificar["disciplina_codigo"] == codigo_disciplina_modificar:
                    turma_modificar = dicionario_modificar
                    disciplina_em_turma = True
            if disciplina_modificar is None:
                print(f"\nDisciplina N.º{codigo_disciplina_modificar} não encontrada.")
                method_press_enter()
                print(str_op_menu)
                method_op_menu(main_choice)
            else:
                if codigo_disciplina_valido:
                    while True:
                    # then we're implementing a menu for modifying the chosen dictionary
                            print(str_mod_menu)
                            opcao_modificar = str.lower(input(select_command))
                            if opcao_modificar == '1':
                                if not disciplina_em_turma:
                                    codigo_antigo = disciplina_modificar["codigo"]
                                    codigo_novo = input("\nInforme o código novo: ")
                                    codigo_novo_valido = True
                                    try:
                                        codigo_novo = int(codigo_novo)
                                    except ValueError:
                                        codigo_novo_valido = False
                                    if codigo_novo_valido:
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
                                    else:
                                        print("\nCódigo da disciplina inválido, tente novamente com um código numérico válido.")
                                else:
                                    codigo_antigo = disciplina_modificar["codigo"]
                                    codigo_novo = input("\nInforme o código novo: ")
                                    codigo_novo_valido = True
                                    try:
                                        codigo_novo = int(codigo_novo)
                                    except ValueError:
                                        codigo_novo_valido = False
                                    if codigo_novo_valido:
                                        for check in self.lista:
                                            if codigo_novo == check["codigo"]:
                                                print(f"\nNão foi possível modificar esta disciplina, "
                                                      f"já existe uma disciplina cadastrada com o N.º{codigo_novo}.")
                                                break
                                            else:
                                                disciplina_modificar["codigo"] = codigo_novo
                                                turma_modificar["disciplina_codigo"] = codigo_novo
                                                print(f"\nCódigo modificado com êxito.\n"
                                                      f"Código antigo: {codigo_antigo}\n"
                                                      f"Código novo: {disciplina_modificar["codigo"]}")
                                                with open("disciplinas.json", "w", encoding="utf-8") as file_disciplinas:
                                                    json.dump(self.lista, file_disciplinas, ensure_ascii=False)
                                                with open("turmas.json", "w", encoding="utf-8") as file_turmas:
                                                    json.dump(self.lista, file_turmas, ensure_ascii=False)
                                                method_press_enter()
                                    else:
                                        print("\nCódigo da disciplina inválido, tente novamente com um código numérico válido.")

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
                elif not codigo_disciplina_valido:
                    print("\nCódigo da disciplina invalido, tente novamente com um código numérico válido.")

    def excluir(self, str_op_menu, main_choice):
        # first we're checking if the list is empty
        if len(self.lista) == 0:
            print("\nComando indisponível: Nenhuma disciplina foi encontrada.")
        else:
        # if it's not empty we're asking the # to search for
            disciplina_remover = None
            disciplina_em_turma = False
            codigo_remover_valido = True
            codigo_remover = input("\nInforme o código da disciplina a ser removida: ")
            try:
                codigo_remover = int(codigo_remover)
            except ValueError:
                codigo_remover_valido = False
            if codigo_remover_valido:
                for dicionario_remover in self.lista:
                # then we're finding the right dictionary to modify
                    if dicionario_remover["codigo"] == codigo_remover:
                        disciplina_remover = dicionario_remover
                        disciplina_remover_codigo = dicionario_remover["codigo"]
                        disciplina_remover_nome = dicionario_remover["nome"]
                        break
                for dicionario_remover in self.turma_lista:
                    if dicionario_remover["disciplina_codigo"] == codigo_remover:
                        disciplina_em_turma = True
                if not disciplina_em_turma:
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
                else:
                    print(f"\nNão foi possível excluír a disciplina N.º{disciplina_remover_codigo}, "
                          "esta disciplina está associada a uma turma. "
                          "Tente novamente após excluir a turma.")
            else:
                print("\nCódigo da disciplina inválido, tente novamente com um código numérico válido.")

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
        try:
            with open("turmas.json", "r", encoding="utf-8") as file:
                self.turma_lista = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.turma_lista = []

    def incluir(self, str_op_menu, main_choice):
        codigo_valido = True
        cpf_valido = False
        input_codigo = input("\nInforme o código do(a) professor(a): ")
        nome = str(input("\nInforme o nome do(a) professor(a): "))
        cpf = str(input("\nInforme o CPF do(a) professor(a): "))
        try:
            codigo = int(input_codigo)
        except ValueError:
            codigo = input_codigo
            codigo_valido = False
        if len(cpf.strip(".-")) == 11:
            cpf_valido = True
            cpf = (f"{cpf[:3]}"
                   f".{cpf[3:6]}"
                   f".{cpf[6:9]}"
                   f"-{cpf[9:]}")
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
            codigo_professor_valido = True
            codigo_professor_modificar = input("\nInforme o código do(a) professor(a) a ser modificado(a): ")
            try:
                codigo_professor_modificar = int(codigo_professor_modificar)
            except ValueError:
                codigo_professor_valido = False
            if codigo_professor_valido:
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
                            codigo_novo = input("\nInforme o código novo: ")
                            codigo_novo_valido = True
                            try:
                                codigo_novo = int(codigo_novo)
                            except ValueError:
                                codigo_novo_valido = False
                            if codigo_novo_valido:
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
                            else:
                                print("\nCódigo do(a) professor(a) inválido, tente novamente com um código numérico válido.")
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
                            cpf_valido = False
                            if len(cpf_novo.strip(".-")) == 11:
                                cpf_valido = True
                                cpf = (f"{cpf[:3]}"
                                       f".{cpf[3:6]}"
                                       f".{cpf[6:9]}"
                                       f"-{cpf[9:]}")
                            if cpf_valido:
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
                            else:
                                print("\nCPF inválido, tente novamente com um CPF válido.")
                        elif opcao_modificar == 'b':
                            print(str_op_menu)
                            method_op_menu(main_choice)
                            break
                        else:
                            print(error_unrecognized)
                            method_press_enter()
            else:
               print("\nCódigo do(a) professor(a) inválido, tente novamente com um código numérico válido.")

    def excluir(self, str_op_menu, main_choice):
        # first we're checking if the list is empty
        if len(self.lista) == 0:
            print("\nComando indisponível: Nenhum(a) professor(a) foi encontrado(a).")
        else:
        # if it's not empty we're asking the # to search for
            professor_remover = None
            professor_em_turma = False
            codigo_remover_valido = True
            codigo_remover = int(input("\nInforme o código do(a) professor(a) a ser removido(a): "))
            try:
                codigo_remover = int(codigo_remover)
            except ValueError:
                codigo_remover_valido = False
            if codigo_remover_valido:
                for dicionario_remover in self.lista:
                # then we're finding the right dictionary to modify
                    if dicionario_remover["codigo"] == codigo_remover:
                        professor_remover = dicionario_remover
                        professor_remover_codigo = dicionario_remover["codigo"]
                        professor_remover_nome = dicionario_remover["nome"]
                        professor_remover_cpf = dicionario_remover["cpf"]
                        break
                for dicionario_remover in self.turma_lista:
                    if dicionario_remover["professor_codigo"] == codigo_remover:
                        professor_em_turma = True
                if not professor_em_turma:
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
                else:
                    print(f"\nNão foi possível excluír professor(a) N.º{professor_remover_codigo},"
                          f"este(a) professor(a) está associado(a) a uma turma. "
                          f"Tente novamente após excluir a turma.  ")
            else:
                print("\nCódigo do(a) professor(a) inválido, tente novamente com um código numérico válido.")

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
        turma_codigo = input("\nInforme o código da turma: ")
        professor_codigo = input("\nInforme o código do(a) professor(a): ")
        disciplina_codigo = input("\nInforme o código da disciplina: ")
        turma_codigo_valido = True
        professor_codigo_valido = True
        disciplina_codigo_valido = True
        try:
            turma_codigo = int(turma_codigo)
        except ValueError:
            turma_codigo_valido = False
        try:
            professor_codigo = int(professor_codigo)
        except ValueError:
            professor_codigo_valido = False
        try:
            disciplina_codigo = int(disciplina_codigo)
        except ValueError:
            disciplina_codigo_valido = False
        professor_existe = False
        disciplina_existe = False
        if turma_codigo_valido and professor_codigo_valido and disciplina_codigo_valido:
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
        elif turma_codigo_valido and professor_codigo_valido and not disciplina_codigo_valido:
            print("\nCódigo da disciplina inválido, tente novamente com um código válido.")
        elif turma_codigo_valido and not professor_codigo_valido and disciplina_codigo_valido:
            print("\nCódigo do(a) professor(a) inválido, tente novamente com um código válido.")
        elif not turma_codigo_valido and professor_codigo_valido and disciplina_codigo_valido:
            print("\nCódigo da turma inválido, tente novamente com um código válido.")
        elif not turma_codigo_valido and professor_codigo_valido and not disciplina_codigo_valido:
            print("\nCódigos da turma e disciplina inválidos, tente novamente com códigos válidos.")
        elif not turma_codigo_valido and not professor_codigo_valido and disciplina_codigo_valido:
            print("\nCódigos do(a) professor(a) e turma inválidos, tente novamente com códigos válidos.")
        elif turma_codigo_valido and not professor_codigo_valido and not disciplina_codigo_valido:
            print("\nCódigos do(a) professor(a) e disciplina inválidos, tente novamente com códigos válidos.")
        elif not turma_codigo_valido and not professor_codigo_valido and not disciplina_codigo_valido:
            print("\nTodos os códigos são inválidos, tente novamente com códigos válidos.")
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
            professor_nome = None
            disciplina_nome = None
            print(f"\nTotal de {len(self.lista)} turma(s) encontrada(s): ")
            for turma_listar in self.lista:
                for professor_listar in self.professor_lista:
                    if professor_listar["codigo"] == turma_listar["professor_codigo"]:
                        professor_nome = professor_listar["nome"]
                for disciplina_listar in self.disciplina_lista:
                    if disciplina_listar["codigo"] == turma_listar["disciplina_codigo"]:
                        disciplina_nome = disciplina_listar["nome"]
                print(f"Turma N.º{turma_listar["turma_codigo"]}    "
                                  f"Professor(a): {professor_nome}    "
                                  f"Disciplina: {disciplina_nome}")
        method_press_enter()
        print(str_op_menu)
        method_op_menu(main_choice)

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
            codigo_turma_valido = True
            codigo_turma_modificar = input("\nInforme o código da turma a ser modificada: ")
            try:
                codigo_turma_modificar = int(codigo_turma_modificar)
            except ValueError:
                codigo_turma_valido = False
            for dicionario_modificar in self.lista:
                # then we're finding the right dictionary to modify
                if dicionario_modificar["turma_codigo"] == codigo_turma_modificar:
                    turma_modificar = dicionario_modificar
                    print(f"\nVocê escolheu a turma N.º{codigo_turma_modificar} com o(a) professor(a) N.º{dicionario_modificar["professor_codigo"]}, "
                        f" e a disciplina N.º{dicionario_modificar["disciplina_codigo"]}.")
                    break
            if turma_modificar is None:
                print(f"\nTurma N.º{codigo_turma_modificar} não encontrada.")
                method_press_enter()
                print(str_op_menu)
                method_op_menu(main_choice)
            else:
                if codigo_turma_valido:
                    while True:
                        # then we're implementing a menu for modifying the chosen dictionary
                        print(str_mod_menu)
                        opcao_modificar = str.lower(input(select_command))
                        if opcao_modificar == '1':
                            codigo_antigo_turma = turma_modificar["turma_codigo"]
                            codigo_novo_turma = input("\nInforme o código novo da turma: ")
                            codigo_valido_turma = True
                            try:
                                codigo_novo_turma = int(codigo_novo_turma)
                            except ValueError:
                                codigo_valido_turma = False
                            if codigo_valido_turma:
                                for check_turma in self.lista:
                                    if codigo_novo_turma == check_turma["turma_codigo"]:
                                        print(f"\nNão foi possível modificar esta turma, "
                                              f"já existe uma turma cadastrada com o N.º{codigo_novo_turma}")
                                        break
                                    else:
                                        turma_modificar["turma_codigo"] = codigo_novo_turma
                                        print(f"\nCódigo modificado com êxito.\n"
                                              f"Código antigo: {codigo_antigo_turma}\n"
                                              f"Código novo: {turma_modificar["turma_codigo"]}")
                                        with open("turmas.json", "w", encoding="utf-8") as file:
                                            json.dump(self.lista, file, ensure_ascii=False)
                                        method_press_enter()
                                        break
                            else:
                                print("\nCódigo da turma inválido, tente novamente com um código válido.")
                        elif opcao_modificar == '2':
                            codigo_antigo_professor = turma_modificar["professor_codigo"]
                            codigo_novo_professor = input("\nInforme o código do(a) professor(a) novo: ")
                            codigo_valido_professor = True
                            try:
                                codigo_novo_professor = int(codigo_novo_professor)
                            except ValueError:
                                codigo_valido_professor = False
                            if codigo_valido_professor:
                                for check_professor in self.professor_lista:
                                    if codigo_novo_professor == check_professor["codigo"]:
                                        turma_modificar["professor_codigo"] = codigo_novo_professor
                                        print(f"\nCódigo modificado com êxito.\n"
                                              f"Código antigo: {codigo_antigo_professor}\n"
                                              f"Código novo: {turma_modificar["professor_codigo"]}")
                                        with open("turmas.json", "w", encoding="utf-8") as file_turmas:
                                            json.dump(self.lista, file_turmas, ensure_ascii=False)
                                        method_press_enter()
                                        break
                                    else:
                                        print(f"\nProfessor não encontrado(a), "
                                              f"tente novamente com um(a) professor(a) existente, "
                                              f"ou crie um novo cadastro.")
                                        break
                            else:
                                print("\nCódigo do(a) professor(a) inválido, tente novamente com um código válido.")
                        elif opcao_modificar == '3':
                            codigo_antigo_disciplina = turma_modificar["disciplina_codigo"]
                            codigo_novo_disciplina = input("\nInforme o código da disciplina nova: ")
                            codigo_valido_disciplina = True
                            try:
                                codigo_valido_disciplina = int(codigo_novo_disciplina)
                            except ValueError:
                                codigo_valido_disciplina = False
                            if codigo_valido_disciplina:
                                for check_disciplina in self.disciplina_lista:
                                    if codigo_novo_disciplina == check_disciplina["disciplina_codigo"]:
                                        turma_modificar["disciplina_codigo"] = codigo_novo_disciplina
                                        print(f"\nCódigo modificado com êxito.\n"
                                              f"Código antigo: {codigo_antigo_disciplina}\n"
                                              f"Código novo: {turma_modificar["disciplina_codigo"]}")
                                        with open("turmas.json", "w", encoding="utf-8") as file:
                                            json.dump(self.lista, file, ensure_ascii=False)
                                        method_press_enter()
                                        break
                                    else:
                                        print(f"\nDisciplina não encontrada, "
                                              f"tente novamente com uma disciplina existente, "
                                              f"ou crie um novo cadastro.")
                                        break
                            else:
                                print("\nCódigo da disciplina inválido, tente novamente com um código válido.")
                        elif opcao_modificar == 'b':
                            print(str_op_menu)
                            method_op_menu(main_choice)
                            break
                        else:
                            print(error_unrecognized)
                            method_press_enter()
                elif not codigo_turma_valido:
                    print("\nCódigo da turma inválido, tente novamente com um código numérico válido.")

    def excluir(self, str_op_menu, main_choice):
        # first we're checking if the list is empty
        if len(self.lista) == 0:
            print("\nComando indisponível: Nenhuma turma foi encontrada.")
        else:
        # if it's not empty we're asking the # to search for
            turma_remover = None
            codigo_remover = int(input("\nInforme o código da turma a ser removida: "))
            codigo_remover_valido = True
            try:
                codigo_remover = int(codigo_remover)
            except ValueError:
                codigo_remover_valido = False
            if codigo_remover_valido:
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
            else:
                print("\nCódigo da turma inválido, tente novamente com um código válido.")
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
            print(f"\nEstudante {estudante_nome} "
                  f"foi matrículado(a) na turma N.º{turma_codigo} com êxito.")
        estudante_codigo = input("\nInforme o código do(a) estudante: ")
        turma_codigo = input("\nInforme o código da turma: ")
        turma_existe = False
        estudante_existe = False
        matricula_existe = False
        estudante_matriculado = None
        turma_com_matricula = False
        codigo_turma_valido = True
        codigo_estudante_valido = True
        try:
            estudante_codigo = int(estudante_codigo)
        except ValueError:
            codigo_estudante_valido = False
        try:
            turma_codigo = int(turma_codigo)
        except ValueError:
            codigo_turma_valido = False
        if codigo_estudante_valido and codigo_turma_valido:
            for check_estudante in self.estudante_lista:
                if check_estudante["codigo"] == estudante_codigo:
                    estudante_existe = True
                    estudante_nome = check_estudante["nome"]
            for check_turma in self.turma_lista:
                if check_turma["turma_codigo"] == turma_codigo:
                    turma_existe = True
            for check_matricula in self.lista:
                if (check_matricula["estudante_codigo"] == estudante_codigo
                        and check_matricula["turma_codigo"]  == turma_codigo):
                    matricula_existe = True
                    break
            if turma_existe and estudante_existe and not matricula_existe:
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
            elif not matricula_existe:
                if not turma_existe and not estudante_existe:
                    print(f"\nTurma e estudante não encontrados, "
                          f"tente novamente com cadastros existentes, ou crie cadastros novos.")
                elif not turma_existe and estudante_existe:
                    print(f"\nTurma não encontrada, "
                          f"tente novamente com um cadastro existente, ou crie um novo.")
                elif turma_existe and not estudante_existe:
                    print(f"\nEstudante não encontrado(a), "
                          f"tente novamente com um cadastro existente, ou crie um novo.")
            elif matricula_existe:
                print("\nEstudante já matriculado(a) nesta turma, "
                      "tente novamente com outro cadastro, ou crie um novo.")
        elif not codigo_estudante_valido and codigo_turma_valido:
            print("\nCódigo do(a) estudante inválido, tente novamente com um código válido.")
        elif codigo_estudante_valido and not codigo_turma_valido:
            print("\nCódigo da turma inválido, tente novamente com um código válido.")
        elif not codigo_estudante_valido and not codigo_turma_valido:
            print("\nTodos os códigos são inválidos, tente novamente com códigos válidos.")
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
            for matricula_listar in self.lista:
                estudante_nome = None
                for estudante_listar in self.estudante_lista:
                    if estudante_listar["codigo"] == matricula_listar["estudante_codigo"]:
                        estudante_nome = estudante_listar["nome"]
                print(f"Estudante N.º{matricula_listar["estudante_codigo"]} - {estudante_nome}"
                      f"    Turma N.º{matricula_listar["turma_codigo"]}")
        method_press_enter()
        print(str_op_menu)
        method_op_menu(main_choice)

    def modificar(self, str_op_menu, main_choice):

        str_mod_menu = ("\n===========  Modificar Matrícula  ===========\n\n"
                        "1 - Código do(a) estudante\n"
                        "2 - Código da turma\n"
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
            turma_existe = False
            matricula_modificar = None
            codigo_estudante_valido = True
            codigo_turma_valido = True
            codigo_estudante_modificar = input("\nInforme o código do(a) estudante cuja matrícula deseja modificar: ")
            codigo_turma_modificar = input("\nInforme o código da turma desta matrícula: ")
            try:
                codigo_estudante_modificar = int(codigo_estudante_modificar)
            except ValueError:
                codigo_estudante_valido = False
            try:
                codigo_turma_modificar = int(codigo_turma_modificar)
            except ValueError:
                codigo_turma_valido = False
            if codigo_estudante_valido and codigo_turma_valido:
                while True:
                    for check_estudante in self.estudante_lista:
                        if check_estudante["codigo"] == codigo_estudante_modificar:
                            estudante_existe = True
                            estudante_nome = check_estudante["nome"]
                            break
                    for check_turma in self.turma_lista:
                        if check_turma["turma_codigo"] == codigo_turma_modificar:
                            turma_existe = True
                            break
                    for dicionario_modificar in self.lista:
                        # then we're finding the right dictionary to modify
                        if dicionario_modificar["estudante_codigo"] == codigo_estudante_modificar:
                            if dicionario_modificar["turma_codigo"] == codigo_turma_modificar:
                                matricula_modificar = dicionario_modificar
                                print(
                                    f"\nVocê escolheu o(a) estudante N.º{codigo_estudante_modificar}, '{estudante_nome}', "
                                    f"matrículado(a) na turma N.º{dicionario_modificar["turma_codigo"]}.")
                                break
                    if matricula_modificar is None and estudante_existe and turma_existe:
                        print(f"\nEstudante N.º{codigo_estudante_modificar} não está matrículado(a) "
                              f"na turma {codigo_turma_modificar} tente novamente com "
                              f"um(a) estudante matrículado(a) nesta turma.")
                        method_press_enter()
                        break
                    elif not estudante_existe and turma_existe:
                        print(f"\nEstudante não encontrado(a), "
                              f"tente novamente com um cadastro existente, "
                              f"ou crie um cadastro novo..")
                        method_press_enter()
                        break
                    elif estudante_existe and not turma_existe:
                        print(f"\nTurma não encontrada, "
                              f"tente novamente com um cadastro existente, "
                              f"ou crie uma turma nova.")
                        method_press_enter()
                        break
                    elif not estudante_existe and not turma_existe:
                        print(f"\nTurma e estudante não encontrados, "
                              f"tente novamente com cadastros existentes, "
                              f"ou crie cadastros novos.")
                        method_press_enter()
                        break
                    else:
                        # then we're implementing a menu for modifying the chosen dictionary
                        print(str_mod_menu)
                        opcao_modificar = str.lower(input(select_command))
                        if opcao_modificar == '1':
                            codigo_aceito = False
                            codigo_antigo_estudante = matricula_modificar["estudante_codigo"]
                            codigo_novo_estudante = int(input("\nInforme o código novo do(a) estudante: "))
                            for check_estudante in self.estudante_lista:
                                if codigo_novo_estudante == check_estudante["codigo"]:
                                    matricula_modificar["estudante_codigo"] = codigo_novo_estudante
                                    codigo_aceito = True
                            if codigo_aceito:
                                print(f"\nCódigo modificado com êxito.\n"
                                      f"Código antigo: {codigo_antigo_estudante}\n"
                                      f"Código novo: {matricula_modificar["estudante_codigo"]}")
                                with open("matriculas.json", "w", encoding="utf-8") as file_matriculas:
                                    json.dump(self.lista, file_matriculas, ensure_ascii=False)
                                method_press_enter()
                            else:
                                print(f"\nEstudante não encontrado(a), "
                                      f"tente novamente com um(a) estudante existente, "
                                      f"ou crie um novo cadastro.")
                        if opcao_modificar == '2':
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
                        elif opcao_modificar == 'b':
                            print(str_op_menu)
                            method_op_menu(main_choice)
                            break
                        else:
                            print(error_unrecognized)
                            method_press_enter()
            elif not codigo_estudante_valido and codigo_turma_valido:
                print("\nCódigo do(a) estudante inválido, tente novamente com um código válido.")
            elif codigo_estudante_valido and not codigo_turma_valido:
                print("\nCódigo da turma inválido, tente novamente com um código válido.")
            elif not codigo_estudante_valido and not codigo_turma_valido:
                print("\nCódigos inválidos, tente novamente com códigos válidos.")

    def excluir(self, str_op_menu, main_choice):
        # first we're checking if the list is empty
        if len(self.lista) == 0:
            print("\nComando indisponível: Nenhuma matrícula foi encontrada.")
        else:
        # if it's not empty we're asking the # to search for
            estudante_existe = False
            turma_existe = False
            matricula_remover = None
            codigo_estudante_valido = True
            codigo_turma_valido = True
            codigo_remover_estudante = input("\nInforme o código do(a) estudante cuja matrícula deseja remover: ")
            codigo_remover_turma = input("\nInforme o código da turma desta matrícula: ")
            try:
                codigo_remover_estudante = int(codigo_remover_estudante)
            except ValueError:
                codigo_estudante_valido = False
            try:
                codigo_remover_turma = int(codigo_remover_turma)
            except ValueError:
                codigo_turma_valido = False
            if codigo_estudante_valido and codigo_turma_valido:
                for check_estudante in self.estudante_lista:
                    if check_estudante["codigo"] == codigo_remover_estudante:
                        estudante_existe = True
                        break
                for check_turma in self.turma_lista:
                    if check_turma["turma_codigo"] == codigo_remover_turma:
                        turma_existe = True
                        break
                for dicionario_remover in self.lista:
                # then we're finding the right dictionary to modify
                    if (dicionario_remover["estudante_codigo"] == codigo_remover_estudante
                            and dicionario_remover["turma_codigo"] == codigo_remover_turma):
                        matricula_remover = dicionario_remover
                        estudante_remover_codigo = dicionario_remover["estudante_codigo"]
                        turma_remover_codigo = dicionario_remover["turma_codigo"]
                        break
                if matricula_remover is None and estudante_existe and turma_existe:
                    print(f"\nEstudante N.º{codigo_remover_estudante} não está matrículado(a), "
                          f"tente novamente com um(a) estudante matrículado(a).")
                    method_press_enter()
                elif not estudante_existe and turma_existe:
                    print(f"\nEstudante N.º{codigo_remover_estudante} não encontrado(a), "
                          f"tente novamente com um(a) estudante cadastrado(a) e matrículado(a).")
                    method_press_enter()
                elif estudante_existe and not turma_existe:
                    print(f"\nTurma N.º{codigo_remover_estudante} não encontrada, "
                          f"tente novamente com uma turma existente.")
                    method_press_enter()
                elif not estudante_existe and not turma_existe:
                    print(f"\nEstudante N.º{codigo_remover_estudante} e turma N.º{codigo_remover_turma} "
                          f"não encontrados, tente novamente com cadastros existentes.")
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
                            print(f"\nMatricula do(a) estudante N.º{estudante_remover_codigo} "
                                  f"na turma N.º{turma_remover_codigo} foi excluída com êxito.")
                        else:
                            print("\nMatricula não excluído(a).")
            else:
                print("\nCódigos inválidos, tente novamente com códigos válidos.")
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