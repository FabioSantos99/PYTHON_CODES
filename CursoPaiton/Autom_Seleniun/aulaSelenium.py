from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = Options()
options.add_argument('profile-directory=Default')
options.add_argument('user-data-dir=/tmp/browser')
options.add_argument("--mute-audio")

webdriver_service = Service('C:\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=webdriver_service)
wait = WebDriverWait(driver, 10)

url = "https://wolf.bet/login"
url2 = "https://windice.io/pt"

driver.get(url)

