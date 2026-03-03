bugs = []

descricoes = {
    "1": "Falha no login (Usuário/E-mail/Telefone)",
    "2": "Falha no login - Senha"
}

prioridades = {
    "1": "Baixa",
    "2": "Média",
    "3": "Alta"
}

statuss = {
    "1": "Pendente",
    "2": "Concluído"
}

opcaoinvalida = ("\n    Opção inválida!\n")


# Criar funções: cadastrar_bug() / listar_bugs() / excluir_bugs()


def cadastrar_bug():

    print("\nTipos de bug disponíveis: ")
    for i, texto in descricoes.items():
        print(f"{i} - {texto}")
    escolha_descricao = input("\nEscolha qual seria a descrição do bug: \n")
    while escolha_descricao not in descricoes:
        print(opcaoinvalida)
        escolha_descricao = input(
            "Escolha qual seria o bug pelo número: \n")

    for i, texto in prioridades.items():
        print(f"{i} - {texto}")

    escolha_prioridade = input("\nEscolha a prioridade: \n")
    while escolha_prioridade not in prioridades:
        print(opcaoinvalida)
        escolha_prioridade = input("\nEscolha a prioridade: \n")

    for i, texto in statuss.items():
        print(f"{i} - {texto}")

    escolha_status = input("\nEscolha o status: \n")
    while escolha_status not in statuss:
        print(opcaoinvalida)
        escolha_status = input("\nEscolha o status: \n")

    print("\nBug cadastrado com sucesso!")

    texto_descricao, texto_prioridade, texto_status = indice(
        escolha_descricao, escolha_prioridade, escolha_status
    )

    bug_criado = {
        "descricao": texto_descricao,
        "prioridade": texto_prioridade,
        "status": texto_status
    }

    bugs.append(bug_criado)


def listar_bugs():
    if not bugs:
        print("Nenhum bug cadastrado")
    else:
        print("\nLista de bugs:\n")
        for i, bug in enumerate(bugs, start=1):
            print(f" Bug {i}")
            print(f"   Descrição : {bug['descricao']}")
            print(f"   Prioridade: {bug['prioridade']}")
            print(f"   Status    : {bug['status']}")


def excluir_bugs():

    listar_bugs()
    excluir_bug = int(input("Selecione o número do bug que deseja excluir:"))
    excluir_bug = excluir_bug - 1

    if 0 <= excluir_bug < len(bugs):
        bug_removido = bugs[excluir_bug]
        del bugs[excluir_bug]
        print(f"Bug {excluir_bug + 1} excluído com sucesso!")
    else:
        print("Número inválido! Não existe bug com esse número.")
        # opcao de cancelar


def editar_bugs():
    if not bugs:
        print("Nenhum bug cadastrado.")
        return
    listar_bugs()

    editar_bug = int(input("Selecione o número do bug que deseja editar:"))
    indice = editar_bug - 1
    if not (0 <= indice < len(bugs)):
        print("Número inválido.")
        return

    menu_editar_bug = input(
        "O que voce deseja editar? \n (1) Descrição \n (2) Prioridade \n (3) Status \n (4) Editar tudo \n (5) Cancelar")

    while menu_editar_bug not in ("1", "2", "3", "4", "5"):
        print(opcaoinvalida)
        menu_editar_bug = input(
            "O que voce deseja editar? \n (1) Descrição \n (2) Prioridade \n (3) Status \n (4) Editar tudo \n (5) Cancelar")

    if menu_editar_bug == "1":
        print(descricoes)
        nova_descricao = input(
            "\nEscolha qual seria a nova descrição do bug: \n")

        while nova_descricao not in descricoes:
            print(opcaoinvalida)
            nova_descricao = input(
                "Escolha qual seria o bug pelo número: \n")

        bugs[indice]["descricao"] = descricoes[nova_descricao]
        print("Bug atualizado com sucesso!")
    elif menu_editar_bug == "2":
        print(prioridades)
        nova_prioridade = input("\n Escolha a nova prioridade: \n")
        while nova_prioridade not in prioridades:
            print(opcaoinvalida)
            nova_prioridade = input("\n Escolha a nova prioridade: \n")

        bugs[indice]["prioridade"] = prioridades[nova_prioridade]
        print("Bug atualizado com sucesso!")
    elif menu_editar_bug == "3":
        print(statuss)
        novo_status = input("\n Escolha o novo status: \n")
        while novo_status not in statuss:
            print(opcaoinvalida)
            novo_status = input("\n Escolha o novo status: \n")

        bugs[indice]["status"] = statuss[novo_status]
        print("Bug atualizado com sucesso!")
    # elif menu_editar_bug == "4":

    elif menu_editar_bug == "5":
        print("Saindo...")
        return


def indice(descricao, prioridade, status):
    texto_descricao = descricoes[descricao]
    texto_prioridade = prioridades[prioridade]
    texto_status = statuss[status]

    return texto_descricao, texto_prioridade, texto_status


while True:

    menu = input("\nSelecione: 1-Reportar | 2-Listar | 3-Sair: \n")
    while menu not in ("1", "2", "3"):
        print(opcaoinvalida)
        menu = input("Selecione: 1-Reportar | 2-Listar | 3-Sair: \n")

    if menu == "1":

        cadastrar_bug()

    elif menu == "2":
        listar_bugs()

        print("O que gostaria de fazer agora?")
        menuexcluireditar = input(
            " (1) - Voltar ao Menu Principal \n (2) - Excluir/Editar bug \n (3) - Sair\n")

        while menuexcluireditar not in ("1", "2", "3"):
            print(opcaoinvalida)
            menuexcluireditar = input(
                " (1) - Voltar ao Menu Principal \n (2) - Excluir/Editar bug \n (3) - Sair\n")
        if menuexcluireditar == "1":
            continue

        elif menuexcluireditar == "2":
            escolha_excluir_editar = input(
                "O que voce deseja? \n (1) Excluir bug cadastrado \n (2) Editar bug cadastrado")
            while escolha_excluir_editar not in ("1", "2"):
                print(opcaoinvalida)
                escolha_excluir_editar = input(
                    "O que voce deseja? \n (1) Excluir bug cadastrado \n (2) Editar bug cadastrado")
            if escolha_excluir_editar == "1":
                excluir_bugs()
            elif escolha_excluir_editar == "2":
                editar_bugs()
        elif menuexcluireditar == "3":
            print("Saindo...")
            break

    elif menu == "3":
        print("Saindo...")
        break
