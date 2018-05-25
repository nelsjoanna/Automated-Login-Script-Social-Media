import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass

usr = input('Enter your username or email: ')
pwd = getpass('Enter your password : ')

def logintwitter():
    browser = selenium.webdriver.Chrome('/Users/Joanna/Exec/chromedriver')
    browser.get('https://www.twitter.com/login')
    fillusr = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
    fillusr.send_keys(usr)
    fillpass = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')))
    fillpass.send_keys(pwd)
    login = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
    login.click()
    return browser

browser = logintwitter()

def PoshmarkLogin():
	browser.get('https://www.poshmark.com/login')
	poshmarkuser = browser.find_element_by_xpath('//*[@id="login_form_username_email"]')
	poshmarkuser.send_keys(usr)
	fillpass = browser.find_element_by_xpath('//input[@id="login_form_password"]')
	fillpass.send_keys(pwd)
	loginbutton = browser.find_element_by_xpath('//button[.="Log In"]')
	loginbutton.click()
	return browser

browser = PoshmarkLogin()
