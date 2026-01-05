import os
"""
#Utilizar \ para escrever caracteres especiais
print("Mesmo assim eu nao \"Matei ele\" ")
#Utilizar \n para quebrar a linha
print("Não entendo o por que disso \nmas sei que tem algum motivo")
#Utilizar \t para tabulação (Não sei oq é tabulação)
print("Eu nao sei oq é \tabulação")
#Utilizar r antes das primeiras aspas duplas para transformar em string pura
print(r"Isso é a string pu\"\"ra")
#Utilizar tres aspas duplas para uma string de multiplas linhas
"""
os.system("cls" if os.name == "nt" else "clear")
"""
spam = "Hello"



print(spam[4])

for i in spam:
    print(i)


pelo = spam[:2]

print(pelo)
"""
"""
while True:
    age = input("Digite sua idade:")
    if age.isdecimal():
        break
    else:
        print("Tente novamente!")

while True:
    senha = input("Digite sua senha ")
    if senha.isalnum():
        if senha == "1223":
            print("Acesso liberado")
        else:
            print("Tente novamente")
    else:
        print("Tente novamente")
"""
#Acredito que isso sera bastante importante no futuro
"""
lista = ['carro', 'moto', 'avião', 'navio']

lista = " ".join(lista)

print(lista)

print("Hello Meu Nome é Leonardo".split())
"""
"""
dados = input("Digite os itens que desejas salvar no banco de dados:")

dados = dados.split()
input()

print(dados)
"""
"""
import pyperclip, os

senhas = {"email": "08101626Leo*",
          "instagram": "122312",
          "tiktok": "08101626"}

def verificar_senha(dados, conta_escolhida):
        #Lembre que quando só temos uma chave e um valor simples nao precisa do for, so usamos o for quando temos dicionarios aninhados
        if conta_escolhida in dados:
            senha = dados[conta_escolhida]
            pyperclip.copy(senha)
            print(f"Senha de {conta_escolhida} copiada com sucesso para a área de tranferencia")
        else:
            print(f"Senha para {conta_escolhida} não encontrada!")
            print(f"Digite a senha para {conta_escolhida}")
            nova_senha = input(">>")
            dados[conta_escolhida] = nova_senha
            print("Senha salva com sucesso!")

while True:
    print("Selecione a conta para copiar a senha:")
    for c in senhas:
        print(c)
    conta_escolhida = input(">>")   
    verificar_senha(senhas, conta_escolhida)
"""
"""
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
"""

import pyperclip

texto_final = ""

lista_de_linhas = []

texto_copiado = pyperclip.paste()

for linha in texto_copiado.split("\n"):
    lista_com_bullet = f"* {linha}"
    lista_de_linhas.append(lista_com_bullet)

texto_final = "\n".join(lista_de_linhas)

print(texto_final)