from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
import os

CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', 'C:/Users/faruc/Downloads/chromedriver_win32 (1)/chromedriver.exe')
GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', 'C:/Program Files (x86)/Google/Chrome\Application/chrome.exe')

options = Options()
options.binary_location = GOOGLE_CHROME_BIN
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.headless = True

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH , chrome_options=options)


url = 'https://www.exito.com/celular-samsung-galaxy-a50-128gb-negro-24415/p'

driver.get(url)

el = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[4]/div/section/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[1]')
print('***********************222222222222*******')
print(el.text)
print('************22****************33333333**')
