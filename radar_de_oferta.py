import requests, os, bs4, time

for i in range(1, 51):

    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    print(f"-------------------Paginá {i}---------------------")

    re = requests.get(url)
    re.raise_for_status()

    soup = bs4.BeautifulSoup(re.text, "html.parser")

    livros = soup.select(".product_pod")

    for item in livros:
        preco_texto = item.select(".price_color")[0].getText()

        preco_limpo = preco_texto[2:]

        preco_num = float(preco_limpo)

        if preco_num < 20.00:
            elemento = item.select("h3 a")[0]
            nome_completo = elemento.get("title")
            print(f"Nome do livro:{nome_completo}")
            print(f"Preço do livro: {preco_num}")
    
    time.sleep(1)