from src.utilities import load_yaml, create_logger
from src.all_imports import *

# from src.steps.account_creation_steps import *

data = utils.load_yaml("C:/Dev/automationpractice_homework/data/parameter.yml")
logs = utils.create_logger()

# Parameters:

url = data["dataset3"]["url"]
email = data["dataset3"]["email"]
title = data["dataset3"]["title"]
firstname = data["dataset3"]["firstname"]
lastname = data["dataset3"]["lastname"]
password = data["dataset3"]["password"]
date = data["dataset3"]["date"]
month = data["dataset3"]["month"]
year = data["dataset3"]["year"]
companyname = data["dataset3"]["companyname"]
address_line1 = data["dataset3"]["address_line1"]
address_line2 = data["dataset3"]["address_line2"]
city = data["dataset3"]["city"]
state = data["dataset3"]["state"]
zipcode = data["dataset3"]["zipcode"]
country = data["dataset3"]["country"]
additionalinfo = data["dataset3"]["additionalinfo"]
homephone = data["dataset3"]["homephone"]
mobilephone = data["dataset3"]["mobilephone"]
aliasaddress = data["dataset3"]["aliasaddress"]


@pytest.mark.positive
@pytest.mark.account_creation
@pytest.mark.account_creation_positive
def test_account_creation_case3(driver):
    logs.info("Starting account creation positive case #1 test!")
    account_creation = AccountCreationPage(driver)
    account_creation.launching_website(url)
    account_creation.email_address_check(email)
    account_creation.title_info(title)
    account_creation.name_info(firstname, lastname)
    account_creation.password_info(password)
    account_creation.date_of_birth(date, month, year)
    account_creation.special_offers()
    account_creation.news_letter()
    account_creation.company_name(companyname)
    account_creation.address(address_line1, address_line2, city, state, zipcode, country)
    account_creation.additional_info(additionalinfo)
    account_creation.home_phone(homephone)
    account_creation.mobile_phone(mobilephone)
    account_creation.address_alias(aliasaddress)
    account_creation.register_button()
    account_creation.account_confirmation()
    account_creation.signout()
