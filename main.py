from bugs import cadastrar_bug, listar_bugs, excluir_bugs, editar_bugs, bugs

opcaoinvalida = ("\nOpção inválida!\n")


while True:

    menu = input("\nSelecione: 1-Reportar | 2-Listar | 3-Sair:\n")

    while menu not in ("1", "2", "3"):
        print(opcaoinvalida)
        menu = input("Selecione novamente:\n")

    if menu == "1":

        cadastrar_bug()

    elif menu == "2":

        listar_bugs()

        if not bugs:
            continue

        escolha = input(
            "\n1 - Voltar\n"
            "2 - Excluir bug\n"
            "3 - Editar bug\n"
            "4 - Sair\n"
        )

        if escolha == "2":
            excluir_bugs()

        elif escolha == "3":
            editar_bugs()

        elif escolha == "4":
            break

    elif menu == "3":

        print("Saindo...")
        break
