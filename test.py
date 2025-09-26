class Matriculas:
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
        # SOMEONE should probably fix this inconsistency with press_enter...
        press_enter()
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
        press_enter()
        print(Menu.estudantes)
        op_menu(main_choice)

    @staticmethod
    def modificar(main_choice):
        if len(lista_estudantes) == 0:
        # first we're checking if the list is empty
            print("\nComando indisponível: Nenhum(a) estudante foi encontrado(a).")
            # here's the press_enter inconsistency...
            press_enter()
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
                        with open("estudantes.json", "w", encoding="utf-8") as file_estudantes:
                            json.dump(lista_estudantes, file_estudantes, ensure_ascii=False)
                        print(Menu.estudantes)
                        op_menu(main_choice)
                        break
                    else:
                        print(error_unrecognized)
                        press_enter()

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
        press_enter()
        print(Menu.estudantes)
        op_menu(main_choice)