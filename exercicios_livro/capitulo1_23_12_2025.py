#Uso print para imprimir algo na tela
print("Qual é o seu nome?")

#Uso input() para receber uma  informação do usuário
meu_nome = input()

#Uso f no começo para colocar a variável dentro das {}
print(f"É bom te conhecer, {meu_nome}")

print("O tamanho do seu nome é:")

#Uso o len para mostrar quantos caracterez na palavra
print(len(meu_nome))

print("Qual é a sua idade?")

minha__idade = input()

#Converto a idade informada para numero inteiro com int() para fazer a soma e depois transformo tudo em string com o str()
print("Você terá " + str(int(minha__idade) + 1) + " no próximo ano.")
