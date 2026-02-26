bugs = []

descricoes = {
    "1": "Falha no login (Usuário/E-mail/Telefone)",
    "2": "Falha no login - Senha"
}

prioridades = {
    "1": "Alta",
    "2": "Média",
    "3": "Baixa"
}

statuss = {
    "1": "Pendente",
    "2": "Concluído"
}


def indice(descricao, prioridade, status):
    texto_descricao = descricoes[descricao]
    texto_prioridade = prioridades[prioridade]
    texto_status = statuss[status]

    return texto_descricao, texto_prioridade, texto_status


while True:

    menu = input("\nSelecione: 1-Reportar | 2-Listar | 3-Sair: ")
    opcaoinvalida = "Opção inválida!"

    if menu == "1":

        print(descricoes)
        escolha_descricao = input("\nEscolha qual seria o bug pelo número:")
        while escolha_descricao not in ("1", "2"):
            print(opcaoinvalida)
            escolha_descricao = input(
                "Escolha qual seria o bug pelo número:\n")

        print(prioridades)
        escolha_prioridade = input("\nEscolha a prioridade:")
        while escolha_prioridade not in ("1", "2", "3"):
            print(opcaoinvalida)
            escolha_prioridade = input("\nEscolha a prioridade:")
            prioridade_txt = escolha_prioridade
        print(statuss)
        escolha_status = input("\nEscolha o status:")
        while escolha_status not in ("1", "2"):
            print(opcaoinvalida)
            escolha_status = input("\nEscolha o status:")

        print("Bug cadastrado com sucesso!")

        texto_descricao, texto_prioridade, texto_status = indice(
            escolha_descricao, escolha_prioridade, escolha_status
        )

        bug_criado = {
            "Descrição": texto_descricao,
            "Prioridade": texto_prioridade,
            "Status": texto_status
        }

        bugs.append(bug_criado)

    elif menu == "2":
        if not bugs:
            print("Nenhum bug cadastrado!")  # dar mais opções
        else:
            print("Esses são os seus bugs cadastrados:")
            print(bugs)
            print("O que gostaria de fazer agora?")
        menuexcluireditar = input(
            " (1) - Menu Principal \n (2) - Excluir/Editar Bug \n (3) - Sair\n")

        while menuexcluireditar not in ("1", "2", "3"):
            print(opcaoinvalida)
            menuexcluireditar = input(
                " (1) - Menu Principal \n (2) - Excluir/Editar Bug \n (3) - Sair\n")
        if menuexcluireditar == "1":
            print(menu)

        elif menuexcluireditar == "2":
            escolha_excluir_editar = input(
                "O que voce deseja? \n (1) Excluir bug cadastrado \n (2) Editar bug cadastrado")
            while escolha_excluir_editar not in ("1", "2"):
                print(opcaoinvalida)
                escolha_excluir_editar = input(
                    "O que voce deseja? \n (1) Excluir bug cadastrado \n (2) Editar bug cadastrado")
            if escolha_excluir_editar == "1":

                excluir_bug = print(bugs), input(
                    "Selecione o número do bug que deseja excluir:")

        elif menuexcluireditar == "3":
            print("Saindo....")
            break

    elif menu == "3":
        print("Saindo...")
        break

# Mostrar bugs numerados
# Realmente excluir pelo índice
# Criar funções: cadastrar_bug() / listar_bugs() /excluir_bug()
# Não repetir inputs (reutilizar função de validação)
# Fluxo do menu 2 está quebrado
# Exclusão ainda não existe de verdade
# Opção 1 (menu principal) não volta pro menu
# Mistura responsabilidades no mesmo bloco
# Menu principla (opção 2, corrigir)
