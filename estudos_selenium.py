from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()

navegador.get("https://www.worten.pt/search?query=iphone")

navegador.maximize_window()

time.sleep(5)

aceitar_cookies = navegador.find_element(By.CLASS_NAME, "button--md button--primary button--black button")
aceitar_cookies.click()


lista_de_produtos = navegador.find_elements(By.CLASS_NAME, "listing-content__list-container")



for produto in lista_de_produtos:
    nome = navegador.find_element(By.CLASS_NAME, "product-card__details").text
    print(nome)

time.sleep(999)