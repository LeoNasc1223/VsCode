#Criamos uma função 
"""
#Essa função precisa receber um parametro: nome
def Hello(nome):
    print(f"Olá, {nome}!")

#Chamamos a função e dentro do parênteses colocamos o parametro que ela precisa para funcionar
Hello("Leo")
"""
#Bola de cristal mágica
"""
#Importamos a biblioteca random para gerar dados aleatórios
import random

#Criamos uma função que precisa receber um parametro para funcionar: answerNumber
def getAnswer(answerNumber):
    if answerNumber == 1:
        return "Sim."
    elif answerNumber == 2:
        return "Não."
    elif answerNumber == 3:
        return "Talvez."
    elif answerNumber == 4:
        return "Definitivamente sim."
    elif answerNumber == 5:
        return "Definitivamente não."
    elif answerNumber == 6:
        return "Pergunte novamente mais tarde."
    elif answerNumber == 7:
        return "Com certeza."
    elif answerNumber == 8:
        return "Não conte com isso."
    elif answerNumber == 9:
        return "É certo."
criamos uma variável para receber um valor aleatório, entre os numeros 1 a 9
r = random.randint(1, 9)
#Criamos uma variável que vai receber a resposta retornada da função
#Colocamos a variável com o numero aleatório como parametro da função
fortune = getAnswer(r)
#inprimimos a resposta na tela
print(fortune)
"""
#Teste de print com end e sep
"""
print("Hello")
print("World")

#Usamos o ent="" para colocar a linha de baixo na mesma linha
print("Hello ", end="")
print("World")

print("cat", "dog", "mouse", sep=", ")
"""
#O cara é genio demais
"""
def spam():
    eggs = 12
    return eggs

eggs = spam()
print(eggs)
"""

#Tratamento de erros com try e except
"""
def spam(divideBy):
    #Usamos o try: para caso ocorra algum erro ele nao pare o programa
    try:
        return 42 / divideBy
    except:
        print("Error: Você tentou dividir por zero.")


print(spam(2))
print(spam(0))
print(spam(12))
print(spam(1))
print(spam(0))
"""
#Jogo de adivinhação com funções
"""
import random

#Mesma pegada da outra vez, criamos a variável para receber um numero aleatório
r = random.randint(1, 20)

def verificar_chute(chute, r):
        if chute < r:
            return "Seu palpite é muito baixo."
        elif chute > r:
            return "Seu palpite é muito alto."
        else:
            return "Você acertou!"

while True:
    print("Adivinhe o número entre 1 e 20.")

    chute = int(input("Digite seu palpite: "))
         
    resultado = verificar_chute(chute, r)
    print(resultado)
    if chute == r:
        break
print("Obrigado por jogar!")
"""

#Exercicio pratico
def collatz(numero):
    if numero % 2 == 0:
        return numero // 2
    else:
        return 3 * numero + 1

while True:
    try:
        n = int(input("Digite um numero inteiro: "))

        while n != 1:
            n = collatz(n)
            print(collatz(n))
    except ValueError:
        print("digite um numero inteiro por favor!")
