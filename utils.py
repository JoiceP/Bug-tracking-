from classificacoes import descricoes, prioridades, statuss


def indice(descricao, prioridade, status):

    texto_descricao = descricoes[descricao]
    texto_prioridade = prioridades[prioridade]
    texto_status = statuss[status]

    return texto_descricao, texto_prioridade, texto_status


def cadastro_aux(opcoes, mensagem):

    print()

    for i, texto in opcoes.items():
        print(f"{i} - {texto}")

    escolha = input(mensagem)

    while escolha not in opcoes:
        print("\nOpção inválida!\n")
        escolha = input(mensagem)

    return escolha
