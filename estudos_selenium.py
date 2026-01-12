from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()

navegador.get("https://www.pcdiga.com/")

navegador.maximize_window()

time.sleep(3)

permitir_cookies = navegador.find_element(By.XPATH, "//*[contains(text(), 'Permitir')]")
permitir_cookies.click()

time.sleep(3)

botao_armazenamento = navegador.find_element(By.XPATH, "//a[contains(., 'Armazenamento')]")
botao_armazenamento.click()

time.sleep(3)

lista_produtos = navegador.find_elements(By.CLASS_NAME, "product-list")

for produtos in lista_produtos:
    print(produtos.get_attribute("href").text)

time.sleep(999)