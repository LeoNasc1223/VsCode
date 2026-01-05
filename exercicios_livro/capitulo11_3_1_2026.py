import webbrowser, pyperclip, requests, bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
"""
pesquisa = "youtube"

webbrowser.open(f"https://www.{pesquisa}.com")
"""
"""
local = pyperclip.paste()

if local:
    webbrowser.open(f"https://www.google.com/maps/place/{local}")
else:
    print("O clipboard esta vasio, copie algum endereço e tente novamente!")
"""
"""
re = requests.get("https://automatetheboringstuff.com/files/rj.txt")

re.raise_for_status()

print(f"Tipo do  objeto: {type(re)}")
print("-" *20)
print(re.text[:250])
"""
"""
re = requests.get("https://automatetheboringstuff.com/files/rj.txt")
re.raise_for_status()

with open("Romeu e Julieta.txt", "wb") as arquivo:
    for pedaco in re.iter_content(100000):
        arquivo.write(pedaco)

print("Arquivo baixado com sucesso!")
"""
"""
re = requests.get("https://www.logo.wine/a/logo/Python_(programming_language)/Python_(programming_language)-Logo.wine.svg")
re.raise_for_status()

with open("logo python.png", "wb") as imagem:
    for pedaco in re.iter_content(100000):
        imagem.write(pedaco)
"""
"""
re = requests.get("https://www.google.com/")
re.raise_for_status()

with open("html_do_google", "wb") as arquivo:
    for pedaco in re.iter_content(100000):
        arquivo.write(pedaco)
"""
#----------------------------------------------------------------------------------------------------------
"""
html_exemplo = '''
<html>
  <body>
    <h1 id="titulo-principal">Loja do Python</h1>
    <p class="produto">Mouse Gamer - R$ 150,00</p>
    <p class="produto">Teclado Mecânico - R$ 300,00</p>
    <a href="https://google.com" id="link-externo">Sair do site</a>
  </body>
</html>
'''

soup = bs4.BeautifulSoup(html_exemplo, "html.parser")

titulos = soup.select("#titulo-principal")
produtos = soup.select(".produto")

print(f"Titulo:{titulos[0].getText()}")

for p in produtos:
    print(f"Produtos encontrados: {p.getText()}")
"""
"""
arquivo_html = open("index.html", encoding="utf=8")

soup = bs4.BeautifulSoup(arquivo_html, "html.parser")

titulo = soup.select("#titulo-pagina")
produto = soup.select(".produto")

for item in produto:
    nome = item.select(".nome-livro")[0].getText()
    preco = item.select(".preco")[0].getText()
    link = item.select(".link-detalhes")[0].get("href")
    print(f"Livro:{nome} | {preco} | {link}")

arquivo_html.close()
"""
#---------------------------------------------------------------------------------------------------------------------

brave_options = Options()
brave_options.binary_location = '/usr/bin/brave-browser'

driver = webdriver.Chrome(options=brave_options)

driver.get("http://books.toscrape.com/")

nome_primeiro_livro = driver.find_element(By.CSS_SELECTOR, "h3 a")


print(nome_primeiro_livro.get_attribute("title"))