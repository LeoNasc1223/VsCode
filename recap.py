precos_brutos = ["R$ 1.250,00", "R$ 890,50", "Preço sob consulta", "R$ 2.100,00", "Indisponível"]

precos_limpos = []

for preco in precos_brutos:
    try:
        texto_limpo = preco.replace("R$", "").replace(".", "").replace(",", ".")
        valor_final = float(texto_limpo)
        precos_limpos.append(valor_final)
    except ValueError as e:
        print(f"Item inválido pulado: {preco}")


for tudo in precos_limpos:
    print(tudo)