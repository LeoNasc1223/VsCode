from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()

navegador = webdriver.Chrome(options=chrome_options)

try:
    navegador.get("https://www.mercadolivre.com.br")

    navegador.maximize_window()

    barra_de_busca = navegador.find_element(By.CLASS_NAME, "nav-search-input")
    barra_de_busca.send_keys("SSD 1TB")

    lupa_barra_de_busca = navegador.find_element(By.CLASS_NAME, "nav-icon-search")
    lupa_barra_de_busca.click()

    time.sleep(3)

    lista_produtos = navegador.find_elements(By.CLASS_NAME, "poly-card__content")

    for produto in lista_produtos[:5]:
        nome = produto.find_element(By.CLASS_NAME, "poly-component__title").text
        container_preco = produto.find_element(By.CLASS_NAME, "poly-price__current")
        elemento_preco = container_preco.find_element(By.CLASS_NAME, "andes-money-amount")
        texto_preco = elemento_preco.get_attribute("aria-label")

        preco_formatado = texto_preco.replace("Antes:", "").replace("Agora: ", "").replace(" reais com ", ".").replace(" centavos", "").replace(" reais", "").replace("", "").strip()

        print(f"Nome {nome} | Preço R${preco_formatado}") 

        float_do_preco = float(preco_formatado)

        if float_do_preco < 400.00:
            print(f"Esse produto esta com preço baixo!")

        print("--------------------------")   
    
    time.sleep(20)
    navegador.quit()

except ValueError as e:
    print(f"Ocorreu um erro:{e}")