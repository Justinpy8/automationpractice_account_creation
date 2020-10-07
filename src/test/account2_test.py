from src.utilities import load_yaml, create_logger
from src.all_imports import *

# from src.steps.account_creation_steps import *

data = utils.load_yaml("C:/Dev/automationpractice_homework/data/parameter.yml")
logs = utils.create_logger()

# Parameters:

url = data["dataset2"]["url"]
email = data["dataset2"]["email"]
title = data["dataset2"]["title"]
firstname = data["dataset2"]["firstname"]
lastname = data["dataset2"]["lastname"]
password = data["dataset2"]["password"]
date = data["dataset2"]["date"]
month = data["dataset2"]["month"]
year = data["dataset2"]["year"]
companyname = data["dataset2"]["companyname"]
address_line1 = data["dataset2"]["address_line1"]
address_line2 = data["dataset2"]["address_line2"]
city = data["dataset2"]["city"]
state = data["dataset2"]["state"]
zipcode = data["dataset2"]["zipcode"]
country = data["dataset2"]["country"]
additionalinfo = data["dataset2"]["additionalinfo"]
homephone = data["dataset2"]["homephone"]
mobilephone = data["dataset2"]["mobilephone"]
aliasaddress = data["dataset2"]["aliasaddress"]


@pytest.mark.positive
@pytest.mark.account_creation
@pytest.mark.account_creation_positive
def test_account_creation_case2(driver):
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
