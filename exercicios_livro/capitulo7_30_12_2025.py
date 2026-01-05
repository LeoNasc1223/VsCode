import re, pyperclip

"""
regex_heroi = re.compile(r"Bat(wo)*man")

mo = regex_heroi.findall(f"O meu super heroi favorito é o Batwoman e o Batman")
"""

"""
mensagem = "O Agente ABC e o Agente XYZ verificaram o Nível 10, mas o Agente MOT não possui acesso ao Nível 99."

regex_agentes = re.compile(r"Agente [A-Z]{3}")

regex_nivel = re.compile(r"Nível \d\d")

moA = regex_agentes.findall(mensagem)

moN = regex_nivel.findall(mensagem)

print("Nomes dos Agentes:")
for a in moA:
    print(a)
print("Nível dos Agentes:")
for n in moN:
    print(n)
"""

"""
codigos = "Senha1: AB1234@, Senha2: xy9999!, Senha3: 12abcd#"

regex_senha = re.compile(r"[aA-zZ]{2}\d\d\d\d[!@#$]")

mo = regex_senha.findall(codigos)

for s in mo:
    print(s)
"""
"""
sujeira = "ID-8821-Valor-500-Status-OK"

regex_limpeza = re.compile(r"[^0-9]")

resultado = regex_limpeza.sub("", sujeira)

print(f"Dados Limpos: {resultado}")
"""