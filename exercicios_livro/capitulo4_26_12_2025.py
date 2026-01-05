"""
#nome_da_lista[numero_do_item]

spam = ["cat", "dog", 12, True, False, 0,1]

print(f"Hello {spam[1]}")
"""

"""
#nome_da_lista[numero_da_lista][numero_do_item_da_lista_escolhida]

spam = [["cat", "dog"], [12, 2, 41], [True, False]]

print(spam[0][1])
"""

"""
nome_da_lista[-numero_do_item_ao_contrario]

spam = ["cat", "dog", 12, True, False, 0,1]

print(spam[-6])
"""

"""
spam = ["cat", "dog", "mouse"]

print(spam[:])

del spam[1]

print(spam[:])
"""

"""
#Fiz sozinhoooo!!!
import os

minha_lista = []

while True:
    try:
        quantidade = input("Digite o numero de itens que voce quer adicionar na lista:")
        quantidade = int(quantidade)

        for i in range(quantidade):
            item = input("Digite o item:")
            minha_lista = minha_lista + [item]

        os.system('clear')
        
        for itens in minha_lista:
            print("Itens na lista:", end="")
            print(itens)
        break

    except ValueError:
        os.system('clear')
        print("Digite um numero inteiro")
"""

"""
minha_lista = ["batata", "cenoura", "tomate"]

#Usamos o nome_da_lista.append() para adicionar o que estiver dentro dos parenteses na lista (sempre será no final da lista)
minha_lista.append("teste")
print(minha_lista)

#Usamos o nome_da_lista.insert() para adicionar o que estiver dentro dos parenteses na posição que definirmos 
#(sempre leva dois argumentos, a posição que o item ficará e o item que sera inserido)
minha_lista.insert(1, "teste2")
print(minha_lista)
"""

"""
import os

def adicionar(escolha):
    if escolha.lower() == "adicionar":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Digite o item que quer adicionar:", end="")
        item_a_adicionar = str(input())
        carrinho_de_compras.append(item_a_adicionar)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Novo carrinho de compras")
        
        for i in carrinho_de_compras:
            print(i)

def remover(escolha):
    print("Escolha o item que deseja remover:")
        
    for posicao, item in enumerate(carrinho_de_compras):
        print(f"{posicao} -> {item}")
        
    item_a_remover = input()
        
    os.system('cls' if os.name == 'nt' else 'clear')

    if item_a_remover in carrinho_de_compras:
        carrinho_de_compras.remove(item_a_remover)
        print(f"item {item_a_remover} removido com sucesso!")
    else:
        print("Digite um item valido")
        
    for i in carrinho_de_compras:
        print(i)

carrinho_de_compras = ["banana", "maçã", "pêra", "uva"]

while True:
    print("Deseja adicionar ou remover itens?")
    escolha = str(input(">"))

    if escolha.lower() == "adicionar":
        adicionar(escolha)

    if escolha.lower() == "remover":
        remover(escolha)
"""
"""
import random

#Criamos uma lista para armazenar as respostas
mensagem = ["Sim", "Não", "Talvez", "Com certeza", "De jeito nenhum", "Provavelmente", "Duvido"]

#O item da lista que vamos imprimir será definido pelo random.randint(entre 0 e o tamanho(da lista)) - 1
print(mensagem[random.randint(0, len(mensagem)) - 1])
"""
"""
nome = "Leonardo"

#Para cada LETRA na strinf Leonardo imprima a LETRA
for i in nome:
    print(f"*** {i} ***")
"""
"""
spam = [2, 4, 6, 8, 10]

spam[2] = "hello"
print(spam)
"""

"""
spam = ["a", "b", "c", "d"]


print(spam[int(int("3" * 2) / 11)])
print(spam[-1])
print(spam[:2])
print(spam[2:])
print(spam[1:2])

print("---------------------------")

bacon = [3.14, 'cat', 11, 'cat', True]

print(bacon.index("cat"))

bacon.remove("cat")

print(bacon)

bacon.insert(1, "mijo")

print(bacon)

bacon.append("mijo")

print(bacon)
"""
