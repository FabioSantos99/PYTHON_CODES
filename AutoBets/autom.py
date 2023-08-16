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

wolf = ["good afternoon and good luck",
"green more for all ",
"the profitable is save coins an low bets",
"have a luck day",
"run to the hills run for your coins",
"have a nice fun",
"go to the usd now",
"keep on earning",
"more think positive about rolls",
"keep on hunt",
 " let's to earn",
"crypto train has arrived don't be late",
"go to bet",
"go to the hunt",
"good night",
"Everyone have fun",
"Gl to everyone",
"patiently waiting ... and earning",
"Next round now",
"Go to the next rround coins",
"Good morning"]

windice = ["boa tarde",
"boa sorte a todos",
"Sigamos nessa batalha",
"avante com cabeça erguida ",
"Sigamos com a sorte sempre",
"proxima lucrada chegando",
"Vamo simbora",
"Vamo guardando e ganhando as moedinhas",
"Boremos amigos",
"Vamo tentar um pouco de ltc aqui",
"sorte pra quem tá on",
"avante positivo nas apostas",
" tá osso aqui hoje viu",
" vamo de contests",
"Vamo pra mais uma chance que hoje tá efe",
"Oia ai as apostas dando certo",
"boremos na fé",
"Agora é hora de subir nas contests",
" como vão ai as apostas de vcs ai galera?",
"e vamo subindo",
" depois volto galera, inté"
]

secs = [600, 465, 510, 890, 490, 569, 794, 984, 564, 715, 659,400, 444, 598, 701, 930, 532, 693, 793, 1000, 5]

driver.get(url)
sleep(2)
driver.execute_script("window.open('http://windice.io', '_blank')")
sleep(3)

if len(wolf) == len(windice) and len(wolf) == len(secs):
    for i in range(len(wolf)):
        wolf_name = wolf[i]
        windice_name = windice[i]
        secs_name = secs[i]

        driver.switch_to.window(driver.window_handles[0])
        wait.until(EC.element_to_be_clickable((By.ID, 'chat-input'))).send_keys(wolf_name)
        sleep(2)
        wait.until(EC.element_to_be_clickable((By.NAME, 'chat_message_submit'))).click()
        sleep(5)

        driver.switch_to.window(driver.window_handles[1])
        elem = wait.until(EC.element_to_be_clickable((By.ID, 'chatMsg')))
        elem.clear()
        elem.send_keys(windice_name)
        sleep(2)
        elem.send_keys(Keys.RETURN)
        sleep(secs_name)
        sleep(3)

        driver.switch_to.window(driver.window_handles[0])
else:
    print("Dados não conferem")

input()
