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
    print(f"Entering {firstname} as the first name.")

    """last name info"""
    last_name = driver.find_element_by_xpath("//input[@id='customer_lastname']")
    last_name.send_keys(lastname)
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
    print(f"Sign up for our newsletter box is checked")


def special_offers():
    offers = driver.find_element_by_xpath("//input[@id='optin']")
    offers.click()
    print(f"Receive special offers from our partners box is checked")


def company_name(companyname):
    company = driver.find_element_by_xpath("//input[@id='company']")
    company.send_keys(companyname)
    print(f"Company name is: {companyname}")


def address(address_line1, address_line2, city, state, zipcode, country):
    """Entering the address info into the 1st address box:
    ******Street address, P.O. Box, Company name, etc.******
    """
    address_box1 = driver.find_element_by_xpath("//input[@id='address1']")
    address_box1.send_keys(address_line1)

    """Entering the address info into the 2nd address box:
    ******Apartment, suite, unit, building, floor, etc...******
    """
    address_box2 = driver.find_element_by_xpath("//input[@id='address2']")
    address_box2.send_keys(address_line2)

    """Entering the City info"""
    city_name = driver.find_element_by_xpath("//input[@id='city']")
    city_name.send_keys(city)

    """Choosing the states from the dropdown list"""
    states_list = driver.find_element_by_xpath("//select[@id='id_state']")
    select_list = Select(states_list)
    select_list.select_by_visible_text(state)
    time.sleep(1)

    """Entering the zip code"""
    postalcode = driver.find_element_by_xpath("//input[@id='postcode']")
    postalcode.send_keys(zipcode)

    """Choose country from the dropdown list"""
    country_list = driver.find_element_by_xpath("//select[@id='id_country']")
    country_select = Select(country_list)
    country_select.select_by_visible_text(country)

    print("The following address info have been entered: ")
    print(f"{address_line1}\n{address_line2}\n{city}\n{state}\n{zipcode}\n{country}")


def additional_info(additionalinfo):
    additional = driver.find_element_by_xpath("//textarea[@id='other']")
    additional.send_keys(additionalinfo)
    print(f"Entering {additionalinfo} into the Additional Information box")


def home_phone(homephone):
    homenum = driver.find_element_by_xpath("//input[@id='phone']")
    homenum.send_keys(homephone)
    print(f"{homephone} is being entered as home phone number")


def mobile_phone(mobilephone):
    mobilenum = driver.find_element_by_xpath("//input[@id='phone_mobile']")
    mobilenum.send_keys(mobilephone)
    print(f"{mobilephone} is being entered as home phone number")


def address_alias(aliasaddress):
    alias = driver.find_element_by_xpath("//input[@id='alias']")
    alias.send_keys(aliasaddress)
    print(f"{aliasaddress} is being entered as the alias address")


def register_button():
    reg_button = driver.find_element_by_xpath("//button[@id='submitAccount']")
    reg_button.click()


def closing_browser():
    driver.close()
