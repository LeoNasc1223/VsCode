#Exercicio nivel 3
"""
produto = {"nome": "Arroz", "preço": 5.00, "estoque": 2}

print(f"Digite o novo preco do {produto['nome']}")
novo_preco = float(input(">>"))

produto["preço"] = novo_preco

print("-----------------------")

for info, valor in produto.items():
    print(f"{info}:{valor}")

preco_total = produto["preço"] * produto["estoque"]

print(f"Valor Total:{preco_total}")
"""

#Exercicio nivel 4
"""
escola = {
    "Turma_A": {"João": 8.5, "Maria": 9.0},
    "Turma_B": {"José": 5.5, "Ana": 10.0}
}

for turma, infos in  escola.items():
    for nome, nota in infos.items():
        if nota > 7.0:
            print(f"Nome:{nome} Nota:{nota}")
        else:
            continue
"""

"""
#Exercicio nivel boss
import pyperclip

inventario = {
    "espada": {"quantidade": 1, "valor": 50},
    "pocao": {"quantidade": 10, "valor": 5},
    "escudo": {"quantidade": 0, "valor": 30}
}

relatorio = []

for items, infos in inventario.items():
    if infos["quantidade"] > 0:
        texto = f"{items}:{infos["valor"]}"
        relatorio.append(texto)

texto_formatado = "\n".join(relatorio)

pyperclip.copy(texto_formatado)

print("Relatório copiado!")
"""

"""
#Exercicio de fixação
import pyperclip

mapa_estelar = {
    "Via Lactea": {
        "Sistema Solar": {
            "Terra": {"carga": "Medicamentos", "prioridade": 10},
            "Marte": {"carga": "Minerais", "prioridade": 5}
        },
        "Alpha Centauri": {
            "Proxima b": {"carga": "Medicamentos", "prioridade": 8}
        }
            },
        "Andromeda": {
        "Sistema Z9": {
            "Xylos": {"carga": "Agua", "prioridade": 9},
            "Zon-2": {"carga": "Medicamentos", "prioridade": 10}
        }
    }
}

planetas_com_medicamentos = []

def verificar_medicamentos(dados):
    for galaxia, sistema in dados.items():
        for sistema, dados_sistemas in sistema.items():
            for planeta, dados_planetas in dados_sistemas.items():
                if dados_planetas["carga"] == "Medicamentos":
                    frase = f"Medicamentos encontrados no planeta {planeta} (Galáxia {galaxia})"
                    planetas_com_medicamentos.append(frase)

verificar_medicamentos(mapa_estelar)

texto_formatado = "\n".join(planetas_com_medicamentos)

pyperclip.copy(texto_formatado)
print("Relatório copiado para a área de tranfêrencia")
"""

frota_espacial = {
    "Falcon-9": [
        {"missao": "Marte", "status": "Sucesso", "ganho": 5000},
        {"missao": "Lua", "status": "Falha", "ganho": 0},
    ],
    "Enterprise": [
        {"missao": "Saturno", "status": "Sucesso", "ganho": 12000},
        {"missao": "Plutão", "status": "Sucesso", "ganho": 8000},
    ],
    "Discovery": [
        {"missao": "Vênus", "status": "Falha", "ganho": 0},
    ]
}

relatorio_financeiro = []

lucro_total = 0

def analisar_lucros(dados):
    global lucro_total
    for frota, missoes in frota_espacial.items():
        for info_missoes in missoes:
            if info_missoes["status"] == "Sucesso":
                texto = f"Nave {frota} | Missão {info_missoes["missao"]} | Lucro: R${info_missoes["ganho"]}"
                lucro_total += info_missoes["ganho"]
                relatorio_financeiro.append(texto)
            

analisar_lucros(frota_espacial)

texto_formatado = "\n".join(relatorio_financeiro)

print(texto_formatado)
print(f"Lucro Total:{lucro_total}")