bugs = []

descricao = [
    "(1) Falha no login (Nome de usuário, endereço de e-mail ou número de telefone)",
    "(2) Falha no login - Senha"
]

prioridade = ["1 - Alta", "2 - Média", "3 - Baixa"]

status = ["(1) Pendente", "(2) Concluído"]


while True:

    menu = input("\nSelecione: 1-Reportar | 2-Listar | 3-Sair: ")
    opcaoinvalida = "Opção inválida!"

    if menu == "1":

        print("\nEscolha a descrição do bug:")
        for item in descricao:
            print(item)

        menudescricao = input("Número: ")

        while menudescricao not in ("1", "2"):
            print(opcaoinvalida)
            menudescricao = input("Número: ")

        indice_descricao = int(menudescricao) - 1
        descricao_escolhida = descricao[indice_descricao]

        print("\nEscolha a prioridade:")
        for item in prioridade:
            print(item)

        menuprioridade = input("Número: ")

        while menuprioridade not in ("1", "2", "3"):
            print(opcaoinvalida)
            menuprioridade = input("Número: ")

        indice_prioridade = int(menuprioridade) - 1
        prioridade_escolhida = prioridade[indice_prioridade]

        print("\nEscolha o status:")
        for item in status:
            print(item)

        menustatus = input("Número: ")

        while menustatus not in ("1", "2"):
            print(opcaoinvalida)
            menustatus = input("Número: ")

        indice_status = int(menustatus) - 1
        status_escolhido = status[indice_status]

        bug_criado = {
            "descricao": descricao_escolhida,
            "prioridade": prioridade_escolhida,
            "status": status_escolhido
        }

        bugs.append(bug_criado)

        print("\nBug cadastrado com sucesso!")

    elif menu == "2":

        if not bugs:
            print("\nSem bugs cadastrados")

        else:
            print("\nLISTA DE BUGS:\n")

            for i, bug in enumerate(bugs, start=1):
                print(f"BUG {i}")
                print("Descrição:", bug["descricao"])
                print("Prioridade:", bug["prioridade"])
                print("Status:", bug["status"])

            print("\nO que deseja fazer agora?")
            input("(ENTER para voltar ao menu)")

    elif menu == "3":
        print("Saindo...")
        break

    else:
        print(opcaoinvalida)
