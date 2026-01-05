#Que idiota kaskakska, precisa nem de explicação
"""
nome = ""

while nome != "seu nome":
    nome = input("Digite seu nome: ")

print("Obrigado por digitar seu nome corretamente!")
"""

#Uso while True para manter o programa funcionando até segunda ordem
"""
while True:
    nome = input("Digite seu nome: ")
    #Verifico se o nome inserido pelo usuário é diferente de "Leo", se for, ele executa de novo o loop usando o continue
    if nome != "Leo":
        continue
    senha = input("Digite sua senha: ")
    #Verifico se a senha inserida pelo usuário é diferente de "1234", se for, ele executa de novo o loop usando o continue
    if senha != "1234":
        continue
    #se o nome for igual a "Leo" e a senha for igual a "1223"
    break
print("Acesso concedido!")
"""

#Exemplo com for
"""
vezes = input("Ate qual numero devemos contar?:")

#Convertemos o numero que o usuário digitou para inteiro com int()
vezes = int(vezes)

#Para cada numero no numero de vezes digitado pelo usuário
for i in range(vezes):
    #imprime o numero e soma + 1
    print(i + 1)
"""

#Exemplo somando numeros de 0 a 100
"""
total = 0

for num in range(101):
    #Usamos o += para somar a variável a ela mesma mais o num do for
    total += num
print(total)
"""

import random, os, sys, math

"""
#Imprime na tela 5 numeros aleatorios
for i in range(5):
    print(random.randint(1, 10))
"""

"""
while True:
    print("Digite 'sair' para sair")
    resposta = input()
    if resposta == "sair":
        sys.exit()
    print("Você digitou: " + resposta)
"""
#Exercicio 13

for i in range(1, 11):
    print(i)

print("----------------------------")

numero = 1
while numero != 11:
    print(numero)
    numero +=1

print("----------------------------")
#Teste bonus

absoluto = -42

print(abs(absoluto))