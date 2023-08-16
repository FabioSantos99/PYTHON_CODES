from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = Options()
options.add_argument('profile-directory=Default')
options.add_argument('user-data-dir=/tmp/browser')
options.add_argument("--start-maximized")

webdriver_service = Service('C:\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=webdriver_service)
wait = WebDriverWait(driver, 10)

url = "https://wolf.bet/login"
url2 = "https://windice.io"

driver.get(url)
sleep(2)
#driver.execute_script("window.open('http://windice.io', '_blank')")
#sleep(3)

import pandas as pd

tabela = pd.read_excel("Msg.xlsx")
print(tabela)

for i, wolfbet in enumerate(tabela["WOLFBET"]):
    windice = tabela.loc[i, "WINDICE"]

    # driver.switch_to.window(driver.window_handles[0])

    wf = wait.until(EC.element_to_be_clickable((By.ID, 'chat-input')))
    wf.clear()
    wf.send_keys(wolfbet)
    sleep(2)
    wf.send_keys(Keys.RETURN)
    sleep(304)
    driver.get(url2)

    elem = wait.until(EC.element_to_be_clickable((By.ID, 'chatMsg')))
    elem.clear()
    elem.send_keys(windice)
    sleep(2)
    elem.send_keys(Keys.RETURN)
    sleep(294)
    driver.get(url)
