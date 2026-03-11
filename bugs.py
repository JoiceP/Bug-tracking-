from utils import cadastro_aux, indice
from classificacoes import descricoes, prioridades, statuss

bugs = []

opcaoinvalida = ("\nOpção inválida!\n")


def cadastrar_bug():

    escolha_descricao = cadastro_aux(descricoes, "\nEscolha a descrição: ")
    escolha_prioridade = cadastro_aux(prioridades, "\nEscolha a prioridade: ")
    escolha_status = cadastro_aux(statuss, "\nEscolha o status: ")

    texto_descricao, texto_prioridade, texto_status = indice(
        escolha_descricao,
        escolha_prioridade,
        escolha_status
    )

    bug_criado = {
        "descricao": texto_descricao,
        "prioridade": texto_prioridade,
        "status": texto_status
    }

    bugs.append(bug_criado)

    print("\nBug cadastrado com sucesso!")


def listar_bugs():

    if not bugs:
        print("Nenhum bug cadastrado")
        return

    print("\nLista de bugs:\n")

    for i, bug in enumerate(bugs, start=1):
        print(f"Bug {i}")
        print(f"  Descrição : {bug['descricao']}")
        print(f"  Prioridade: {bug['prioridade']}")
        print(f"  Status    : {bug['status']}")


def excluir_bugs():

    if not bugs:
        print("Nenhum bug cadastrado")
        return

    listar_bugs()

    excluir_bug = int(
        input("Selecione o número do bug que deseja excluir:\n")
    ) - 1

    if 0 <= excluir_bug < len(bugs):

        del bugs[excluir_bug]

        print("Bug excluído com sucesso!")

    else:

        print("Número inválido!")


def editar_bugs():

    if not bugs:
        print("Nenhum bug cadastrado.")
        return

    listar_bugs()

    indice_edit = int(
        input("Selecione o número do bug que deseja editar: ")
    ) - 1

    if not (0 <= indice_edit < len(bugs)):
        print("Número inválido.")
        return

    menu = input(
        "O que voce deseja editar?\n"
        "1 - Descrição\n"
        "2 - Prioridade\n"
        "3 - Status\n"
        "4 - Cancelar\n"
    )

    while menu not in ("1", "2", "3", "4"):
        print(opcaoinvalida)
        menu = input("Escolha novamente: ")

    if menu == "1":

        nova_descricao = cadastro_aux(
            descricoes,
            "\nEscolha a nova descrição: "
        )

        bugs[indice_edit]["descricao"] = descricoes[nova_descricao]

    elif menu == "2":

        nova_prioridade = cadastro_aux(
            prioridades,
            "\nEscolha a nova prioridade: "
        )

        bugs[indice_edit]["prioridade"] = prioridades[nova_prioridade]

    elif menu == "3":

        novo_status = cadastro_aux(
            statuss,
            "\nEscolha o novo status: "
        )

        bugs[indice_edit]["status"] = statuss[novo_status]

    elif menu == "4":
        return

    print("Bug atualizado com sucesso!")
