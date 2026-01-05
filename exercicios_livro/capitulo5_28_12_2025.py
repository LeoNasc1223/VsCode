"""
#Criamos um dicionario, do lado ESQUERDO fica a CHAVE(key) e do lado DIREITO fica o VALOR(value)
informacoes = {"nome": "Leonardo", "idade": "16", "altura": "1,73"}

#Podemos usar as chaves como variáveis
print(f"Meu nome é {informacoes["nome"]}, tenho {informacoes['idade']} anos e {informacoes['altura']} de altura")
"""
"""
aniversarios = {"carlos": "Março 26", "ana": "Julho 15", "beatriz": "Dezembro 5"}

while True:
    print("Digite o nome da pessoa que você quer checar o aniversário:")
    nome = input("> ")

    #Para cada nome(CHAVE(key)) no dicionário aniversário
    if nome in aniversarios:
        #Imprimimos o nome e o aniversario[nome] (da mesma forma que as listas, colocamos o que nos queremos que apareça entre [])
        print(f"O aniversário de {nome} é {aniversarios[nome]}")
    else:
        print("Não tenho informação sobre o aniversário de {nome}")
        #Caso nao tenhamos a informação no dicionário, criamos a variavel (caso nao tenha), para armazenar o qual vai ser o VALOR(value) para a CHAVE(key) que nao existe
        bday = input("Qual é a data?:")
        #Colocamos o nome do dicionario[CHAVA(key)] recebe = o VALOR(value) que acabamos de criar em cima
        aniversarios[nome] = bday
        print("Aniversários atualizados")
"""

"""
spam = {'color': 'red', 'age': 42}

#Para cada VALOR(values) in spam.values():
for v in spam.values():
    print(v)

#Para cada CHAVE(key) (com tudo dentro) in spam.items()
for i in spam.items():
    print(i)

#Para cada CHAVE(key) (apenas as chaves) in spam.keys()
for k in spam.keys():
    print(k)

#Para cada CHAVE(key), vamos armazenar o VALOR(values) na variável v in spam.items()
for k, v in spam.items():
    print(f"Key: {k}, Values: {str(v)}")
"""

"""
picnic_items = {"apple": 5, "cups": 2}

#Usamos o nome_do_dicionario.get("Procura a CHAVE(key) e recebe o valor dela, se nao encontrar a CHAVE(key) retorna 0")
print(f"eu estou levando {str(picnic_items.get("cups", 0))} copos")

print(f"eu estou levandno {str(picnic_items.get("eggs", 0))} ovos")
"""

"""
spam = {'name': 'Pooka', 'age': 5}

#Usamos o nome_do_dicionario.setdefault("Nome da variavel que queremos procurar", se nao encontrar define o valor "aqui", se encontrar nao faz nada)
spam.setdefault("color", "black")

print(spam)

spam.setdefault("color", "white")

print(spam)
"""
"""
import pprint

mensagem = "And i was trapped, I'm alone, has no body, no senses, no fellings, I was in the hell looking at the heaven."

contagem = {}

for caractere in mensagem:
    contagem.setdefault(caractere, 0)
    contagem[caractere] = contagem[caractere] + 1

pprint.pprint(contagem)
"""
"""
tabuleiro = {"topo-E": "", "topo-M": "", "topo-D": "",
             "meio-E": "", "meio-M": "", "meio-D": "",
             "baixo-E": "", "baixo-M": "", "baixo-D": ""}

def imprimir_tabuleiro(tabuleiro):
    print(f"{tabuleiro["topo-E"]} | {tabuleiro['topo-M']} | {tabuleiro['topo-D']}")
    print("-+-+-")
    print(f"{tabuleiro['meio-E']} | {tabuleiro['meio-M']} | {tabuleiro['meio-D']}")
    print("-+-+-")
    print(f"{tabuleiro['baixo-E']} | {tabuleiro['baixo-M']} | {tabuleiro['baixo-D']}")

turn = "X"

for i in range(9):
    imprimir_tabuleiro(tabuleiro)
    print(f"Mova para {turn}")

    movimento = input()

    tabuleiro[movimento] = turn

    if turn == "X":
        turn = "O"
    else:
        turn = "X"

imprimir_tabuleiro(tabuleiro)
"""
"""
esta_trazendo = {"Alice": {"Maça": 5, "Sucos": 2},
                 "Carlos": {"Balas": 10, "Sucos": 4},
                 "Maria": {"Copos": 5, "Maça": 3},
                 "Marcela": {"Balas": 12, "Pratos": 5},
                 "Roberto": {"Faca": 1, "Pistola": 1}}

#Função para somar mesmos itens dentre de um dicionario
def total_de_itens(quem, item):
    numero_de_itens = 0
    for k, v in quem.items():
        numero_de_itens += v.get(item, 0)
    return numero_de_itens 

print("O que cada um está trazendo?:")
print(f"-Maças {str(total_de_itens(esta_trazendo, "Maça"))}")
print(f"-Sucos {str(total_de_itens(esta_trazendo, "Sucos"))}")
print(f"-Copos {str(total_de_itens(esta_trazendo, "Copos"))}")
print(f"-Balas {str(total_de_itens(esta_trazendo, "Balas"))}")
print(f"-Pratos {str(total_de_itens(esta_trazendo, "Pratos"))}")
print(f"-Faca {str(total_de_itens(esta_trazendo, "Faca"))}")
print(f"-Pistola {str(total_de_itens(esta_trazendo, "Pistola"))}")
"""
"""
produtos = {"caneta": 4.00, "lápis": 2.00, "estojo": 5.00}

for nomes, valores in produtos.items():
    print(f"{nomes} valor:{valores}")
"""

#Dicionarios aninhados
"""
rede = {"Brasil": {"São Paulo": {"Centro": {"Funcionarios": {"Joao": 150, "Maria": 50}}},
"Rio de Janeiro": {"Copacabana": {"Funcionario": {"Carlos": 200, "Joana": 30}}}}}

#Passo 1
#crio uma variavel para o nome contendo o item mais alto da hierarquia
#coloco uma virgula e crio a variavel para o nome dentro da variavel anterior
#coloco in para o nome do dicionario.items():

#Passo 2
#dentro da segunda variavel que eu havia criado eu copio o nome dela depois do for e no final.items():
#depois da virgula eu crio a variavel para o nome dentro da variavel anterior

#Passo 3 (repetivel)
#pego o nome dessa variavel que eu acabei de criar  e coloco no final.items()
#no comeco eu crio uma variavel para armazenar as chaves dentro desse nivel
#depois da virgula eu crio outra variavel para armazenar alguma coisa

#Passo 4
#por fim eu pego essa variavel que eu criei pra armazenar nao sei oq
#depois da virgual crio uma variavel sujestiva chamada valor, para armazenar o valor
#coloco a variavel que eu nao sei oq arqmazena direito no final.items()

####################################################

for pais, estado in rede.items():
    for estado, cidade in estado.items():
        for unidade, funcionarios in cidade.items():
            for funcionarios, alguma_coisa in funcionarios.items():
                for alguma_coisa, valor in alguma_coisa.items():
                    print(valor)

#####################################################

for nome1, nome2 in nome_biblioteca
    for nome2, nome3 in nome2
        for nome4, nome5 in nome3
            for nome5, nome6 in nome5
                for nome6, nome7, nome6
                    for nome7, nome8 in nome7

#####################################################
"""

"""
import os

inventario = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
loot_dragao = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def mostrar_inventario(dados):
    total_de_itens = 0

    for i, v in dados.items():
        print(f"{i} -> {v}")
        total_de_itens += v
    print(f"Total: {total_de_itens}")

def adicionar_itens(dados, itens):
        for iten in itens:
            if iten in dados:
                  dados[iten] + 1
            else:
                 dados[iten] = 1

print(mostrar_inventario(inventario))
input()

os.system("cls" if os.name == "nt" else "clear")

input(f"Voce matou o dragão, pressione 'Enter' para coletar os  itens.")
os.system("cls" if os.name == "nt" else "clear")

print(f"Itens dropados: {loot_dragao}")
input()

print("Novo inventario:")
print(adicionar_itens(inventario, loot_dragao))
print(mostrar_inventario(inventario))
"""