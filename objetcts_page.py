
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.google.com")

elementos = driver.find_element(By.CLASS_NAME,'gLFyf')

dados = []

for elemento in elementos:
     dados.append(elemento.text)
     print(dados)


driver.quit()