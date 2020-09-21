from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
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


def email_address_check(email):
    """Entering the account creation page"""
    sign_in_button = driver.find_element_by_xpath("//a[@class='login']")
    sign_in_button.click()
    time.sleep(2)
    """Entering the email address"""
    email_address = driver.find_element_by_xpath("//input[@id='email_create']")
    email_address.send_keys(email)
    driver.find_element_by_xpath("//button[@id='SubmitCreate']").click()
    time.sleep(2)
    """Email address not available error"""
    try:
        email_unavailable_error = driver.find_element_by_xpath("//div[@id='create_account_error']")
        if email_unavailable_error.is_displayed():
            print("This email address already has an account")
    except NoSuchElementException as error:
        print(f"This email address is available for new account creation")


def title_info(title):
    """Title"""
    male = driver.find_element_by_xpath("//input[@id='id_gender1']")
    female = driver.find_element_by_xpath("//input[@id='id_gender2']")
    if title == "male":
        male.click()
    if title == "female":
        female.click()
    print("Title has been selected")


def name_info(firstname, lastname):
    """first name info"""
    first_name = driver.find_element_by_xpath("//input[@id='customer_firstname']")
    first_name.send_keys(firstname)

    """last name info to the address section"""
    address_first_name = driver.find_element_by_xpath("//input[@id='firstname']")
    address_first_name.send_keys(firstname)
    print(f"Entering {firstname} as the first name.")

    """last name info"""
    last_name = driver.find_element_by_xpath("//input[@id='customer_lastname']")
    last_name.send_keys(lastname)

    """"last name info to the address section"""
    address_last_name = driver.find_element_by_xpath("//input[@id='lastname']")
    address_last_name.send_keys(lastname)
    print(f"Entering {lastname} as the first name.")


def password_info(password):
    """password info"""
    pass_word = driver.find_element_by_xpath("//input[@id='passwd']")
    pass_word.send_keys(password)
    print(f"Entering {password} as the first name.")


def date_of_birth(date, month, year, ):
    """date info"""
    date_dropdown = driver.find_element_by_xpath("//select[@id='days']")
    date_selection = Select(date_dropdown)
    date_selection.select_by_value(date)
    print(f"Selected {date} as the date")
    time.sleep(1)

    """month info"""
    month_dropdown = driver.find_element_by_xpath("//select[@id='months']")
    month_selection = Select(month_dropdown)
    month_selection.select_by_visible_text(f"{month} ")
    print(f"Selected {month} as the month")
    time.sleep(1)

    """year info"""
    year_dropdown = driver.find_element_by_xpath("//select[@id='years']")
    year_selection = Select(year_dropdown)
    year_selection.select_by_value(year)
    print(f"Selected {year} as the month")
    time.sleep(1)


def news_letter():
    newsletter = driver.find_element_by_xpath("//input[@id='newsletter']")
    newsletter.click()


def special_offers():
    offers = driver.find_element_by_xpath("//input[@id='optin']")
    offers.click()






