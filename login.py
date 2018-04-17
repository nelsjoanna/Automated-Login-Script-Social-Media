import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass

usr = raw_input('Enter your username or email: ')
pwd = getpass('Enter your password : ')
url = 'https://www.twitter.com/login'


def logintwitter():
    browser = selenium.webdriver.Chrome('/Users/Joanna/Exec/chromedriver')
    browser.get(url)
    fillusr = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
    fillusr.send_keys(usr)
    fillpass = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')))
    fillpass.send_keys(pwd)
    login = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
    login.click()


logintwitter()
