import json
bugs = []

with open("classificacoes.json", encoding="utf-8") as classificacoes:
    dados = json.load(classificacoes)
    descricoes = dados["descricoes"]
    prioridades = dados["prioridades"]
    statuss = dados["statuss"]


opcaoinvalida = ("\n    Opção inválida!\n")


def cadastro_aux(opcoes, mensagem):
    print()
    for i, texto in opcoes.items():
        print(f"{i} - {texto}")

    escolha = input(mensagem)

    while escolha not in opcoes:
        print(opcaoinvalida)
        escolha = input(mensagem)
    return escolha


def cadastrar_bug():

    escolha_descricao = cadastro_aux(descricoes, "\nEscolha a descrição: ")

    escolha_prioridade = cadastro_aux(prioridades, "\nEscolha a prioridade: ")

    escolha_status = cadastro_aux(statuss, "\nEscolha o status: ")

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
    if not bugs:
        print("Nenhum bug cadastrado")
        return
    listar_bugs()
    excluir_bug = int(input("Selecione o número do bug que deseja excluir:\n"))
    excluir_bug = excluir_bug - 1

    if 0 <= excluir_bug < len(bugs):
        bug_removido = bugs[excluir_bug]
        del bugs[excluir_bug]
        print(f"Bug {excluir_bug + 1} excluído com sucesso!")
    else:
        print("\nNúmero inválido! Não existe bug com esse número.\n")
        # opcao de cancelar


def editar_bugs():

    if not bugs:
        print("Nenhum bug cadastrado.")
        return
    listar_bugs()

    editar_bug = int(input("Selecione o número do bug que deseja editar:"))
    indice_edit = editar_bug - 1
    if not (0 <= indice_edit < len(bugs)):
        print("Número inválido.")
        return

    menu_editar_bug = input(
        "O que voce deseja editar? \n (1) Descrição \n (2) Prioridade \n (3) Status \n (4) Editar tudo \n (5) Cancelar")

    while menu_editar_bug not in ("1", "2", "3", "4", "5"):
        print(opcaoinvalida)
        menu_editar_bug = input(
            "O que voce deseja editar? \n (1) Descrição \n (2) Prioridade \n (3) Status \n (4) Editar tudo \n (5) Cancelar")

    if menu_editar_bug == "1":

        nova_descricao = cadastro_aux(
            descricoes, "\nEscolha a nova descrição: ")

        bugs[indice_edit]["descricao"] = descricoes[nova_descricao]
        print("Bug atualizado com sucesso!")
    elif menu_editar_bug == "2":

        nova_prioridade = cadastro_aux(
            prioridades, "\nEscolha a nova prioridade: ")

        bugs[indice_edit]["prioridade"] = prioridades[
            nova_prioridade]
        print("Bug atualizado com sucesso!")
    elif menu_editar_bug == "3":

        novo_status = cadastro_aux(statuss, "\nEscolha o novo status: ")

        bugs[indice_edit]["status"] = statuss[novo_status]
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

        if not bugs:
            continue

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
            if not bugs:
                print("Voce não tem nenhum bug cadastrado")
                continue

            escolha_excluir_editar = input(
                "O que voce deseja? \n (1) Excluir bug cadastrado \n (2) Editar bug cadastrado\n")
            while escolha_excluir_editar not in ("1", "2"):
                print(opcaoinvalida)
                escolha_excluir_editar = input(
                    "O que voce deseja? \n (1) Excluir bug cadastrado \n (2) Editar bug cadastrado\n \n")
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
