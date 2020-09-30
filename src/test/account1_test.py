from src.utilities import load_yaml, create_logger
from src.all_imports import *
from src.steps.account_creation_steps import *
import pytest

data = load_yaml("C:/Dev/automationpractice_homework/data/parameter.yml")

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

@pytest.mark.regression
def test_scenario1():
    try:
        launching_website(url)
        email_address_check(email)
        title_info(title)
        name_info(firstname, lastname)
        password_info(password)
        date_of_birth(date, month, year)
        special_offers()
        news_letter()
        company_name(companyname)
        address(address_line1, address_line2, city, state, zipcode, country)
        additional_info(additionalinfo)
        home_phone(homephone)
        mobile_phone(mobilephone)
        address_alias(aliasaddress)
        register_button()
        create_logger('interesting')
        closing_browser()
    except WebDriverException as err:
        print(err)
