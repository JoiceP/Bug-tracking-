import json

with open("classificacoes.json", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

descricoes = dados["descricoes"]
prioridades = dados["prioridades"]
statuss = dados["statuss"]
