from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import select
import time

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()


def launching_website(url):
    driver.get(url)
    print(f"{url} is loading")


def sign_in(username, password):
    """Entering the sign in page"""
    sign_in_button = driver.find_element_by_xpath("//a[@class='login']")
    sign_in_button.click()
    time.sleep(2)
    """Enter username"""
    email_address = driver.find_element_by_xpath("//input[@id='email']")
    email_address.send_keys(username)
    """Enter password"""
    pw = driver.find_element_by_xpath("//input[@id='passwd']")
    pw.send_keys(password)
    """Click to sign in"""
    driver.find_element_by_xpath("//button[@id='SubmitLogin']").click()
