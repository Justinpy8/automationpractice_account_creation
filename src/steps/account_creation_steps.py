# from src.utilities import *


from src.all_imports import *
from selenium import webdriver



logs = utils.create_logger()



data = utils.load_yaml("C:/Dev/automationpractice_homework/data/parameter.yml")

url = data["url"]
email = data["email"]
title = data["title"]
firstname = data["firstname"]
lastname = data["lastname"]
password = data["password"]
date = data["date"]
month = data["month"]
year = data["year"]
companyname = data["companyname"]
address_line1 = data["address_line1"]
address_line2 = data["address_line2"]
city = data["city"]
state = data["state"]
zipcode = data["zipcode"]
country = data["country"]
additionalinfo = data["additionalinfo"]
homephone = data["homephone"]
mobilephone = data["mobilephone"]
aliasaddress = data["aliasaddress"]


def screen_shots(message=""):
    """Define time format for the file name"""
    system_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')

    """Set the file location for the screenshot files"""
    file_path = 'C:/Dev/automationpractice_homework/screenshots/'

    """Create the file name for the screen shot file."""
    file_name = f"{message}_error_{system_time}.png"

    """Create the variable contains the file location and file name formatting"""
    full_file_path = f"{file_path}{file_name}"

    """Take the screen shot and save it to the predefined location"""
    driver.save_screenshot(full_file_path)


def launching_website(url):
    driver.get(url)
    logs.info(f"{url} is loading")


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
    try:
        sign_in_button = driver.find_element_by_xpath("//a[@class='login']")
        sign_in_button.click()
        time.sleep(2)
        """Entering the email address"""
        email_address = driver.find_element_by_xpath("//input[@id='email_create']")
        email_address.send_keys(email)
        driver.find_element_by_xpath("//button[@id='SubmitCreate']").click()
        time.sleep(2)
        """Email address not available error"""
        email_unavailable_error = driver.find_element_by_xpath("//div[@id='create_account_error']")
        if email_unavailable_error.is_displayed():
            logs.error("This email address already has an account")
            screen_shots("unavailable email address")
            logs.info("Screen shot of the error message has been saved")
    except NoSuchElementException as err:
        logs.error(err)


def title_info(title):
    """Title"""
    male = driver.find_element_by_xpath("//input[@id='id_gender1']")
    female = driver.find_element_by_xpath("//input[@id='id_gender2']")
    if title == "male":
        male.click()
    if title == "female":
        female.click()
    logs.info("Title has been selected")


def name_info(firstname, lastname):
    """first name info"""
    first_name = driver.find_element_by_xpath("//input[@id='customer_firstname']")
    first_name.send_keys(firstname)
    logs.info(f"Entering {firstname} as the first name.")

    """last name info"""
    last_name = driver.find_element_by_xpath("//input[@id='customer_lastname']")
    last_name.send_keys(lastname)
    logs.info(f"Entering {lastname} as the first name.")


def password_info(password):
    """password info"""
    pass_word = driver.find_element_by_xpath("//input[@id='passwd']")
    pass_word.send_keys(password)
    logs.info(f"Entering {password} as the password.")


def date_of_birth(date, month, year, ):
    """date info"""
    date_dropdown = driver.find_element_by_xpath("//select[@id='days']")
    date_selection = Select(date_dropdown)
    date_selection.select_by_value(date)
    logs.info(f"Date selected: {date}")
    time.sleep(1)

    """month info"""
    month_dropdown = driver.find_element_by_xpath("//select[@id='months']")
    month_selection = Select(month_dropdown)
    month_selection.select_by_visible_text(f"{month} ")
    logs.info(f"Month Selected: {month}")
    time.sleep(1)

    """year info"""
    year_dropdown = driver.find_element_by_xpath("//select[@id='years']")
    year_selection = Select(year_dropdown)
    year_selection.select_by_value(year)
    logs.info(f"Year selected: {year}")
    time.sleep(1)


def news_letter():
    newsletter = driver.find_element_by_xpath("//input[@id='newsletter']")
    newsletter.click()
    logs.info(f"Sign up for our newsletter box is checked")


def special_offers():
    offers = driver.find_element_by_xpath("//input[@id='optin']")
    offers.click()
    logs.info(f"Receive special offers from our partners box is checked")


def company_name(companyname):
    company = driver.find_element_by_xpath("//input[@id='company']")
    company.send_keys(companyname)
    logs.info(f"Company name is: {companyname}")


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

    logs.info("The following address info have been entered: ")
    logs.info(f"{address_line1}\n{address_line2}\n{city}\n{state}\n{zipcode}\n{country}")


def additional_info(additionalinfo):
    additional = driver.find_element_by_xpath("//textarea[@id='other']")
    additional.send_keys(additionalinfo)
    logs.info(f"The following additional info has been appended:\n{additionalinfo}")


def home_phone(homephone):
    homenum = driver.find_element_by_xpath("//input[@id='phone']")
    homenum.send_keys(homephone)
    logs.info(f"Home phone number is: {homephone} ")


def mobile_phone(mobilephone):
    mobilenum = driver.find_element_by_xpath("//input[@id='phone_mobile']")
    mobilenum.send_keys(mobilephone)
    logs.info(f"Mobile phone number is: {mobilephone}")


def address_alias(aliasaddress):
    alias = driver.find_element_by_xpath("//input[@id='alias']")
    alias.send_keys(aliasaddress)
    logs.info(f"{aliasaddress} is being entered as the alias address")


def register_button():
    reg_button = driver.find_element_by_xpath("//button[@id='submitAccount']")
    reg_button.click()
    time.sleep(10)

    """Checking for error message after clicking on the register button """
    error_msg = driver.find_element_by_xpath("//div[@class='alert alert-danger']")
    if error_msg.is_displayed():
        screen_shots('Registration')
        logs.warning("Registration error message screen shot has been captured")
    else:
        """Testing to see if the account creation is a success by finding the sign out button"""
        logout_botton = driver.find_element_by_xpath("//a[@class='logout']")
        assert logout_botton.is_displayed(), logs.error("Account creation failed")
        logs.info("Account creation is successful - the sign out button is displayed.")


# def closing_browser():
#     driver.close()
