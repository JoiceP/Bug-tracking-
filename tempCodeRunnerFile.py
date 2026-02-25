# listas
bugs = []
descricao = ["(1) Falha no login (Nome de usuário, endereço de e-mail ou número de telefone)",
             "(2) Falha no login - Senha"]
prioridade = [" 1 - Alta", " 2 - Média", " 3 - Baixa"]
status = ["(1) Pendente", "(2) Concluído"]

# dicionario
dado_bug1 = {"descrição": "Falha no login (Nome de usuário, endereço de e-mail ou número de telefone)",
             "prioridade": "Alta",
             "status": "Pendente"
             }
menu = input("Selecione a opção: 1 - Reportar | 2 - Listar bugs | 3 - Sair: ")
opcaoinvalida = ("Opção inválida! Escolha uma opção válida")
if menu == "1":
    print(descricao)
    menudescricao = input("Escolha o bug pelo número:")
    while menudescricao not in ("1", "2"):
        print(opcaoinvalida)
        print(descricao)
        menudescricao = input("Escolha o bug pelo número:")

    indice_descricao = int(menudescricao) - 1
    descricao_escolhida = descricao[indice_descricao]

    print(prioridade)

    menuprioridade = input("Qual a prioridade?")
    while menuprioridade not in ("1", "2", "3"):
        print(opcaoinvalida)
        print(prioridade)
        menuprioridade = input("Qual a prioridade?")

    indice_prioridade = int(menuprioridade) - 1
    prioridade_escolhida = prioridade[indice_prioridade]

    print(status)

    menustatus = input("Qual o status?")
    while menustatus not in ("1", "2"):
        print(opcaoinvalida)
        print(status)
        menustatus = input("Qual o status?")
    print("Finish por enquanto")

    indice_status = int(menustatus) - 1
    status_escolhido = status[indice_status]

    print("Voce registrou o bug", descricao_escolhida, ", com prioridade",
          prioridade_escolhida, ", e status", status_escolhido)

    bug_criado = {
        "descricao": descricao_escolhida,
        "prioridade": prioridade_escolhida,
        "status": status_escolhido
    }

    bugs.append(bug_criado)

if menu == "2":
    # ver o que imprimir se a lista ainda estiver vazia
    print(bugs)
    # o que deseja fazer ... (reportar novo bug, etc etc etc...)
if menu == "3":
    print("Saindo.. teste")
