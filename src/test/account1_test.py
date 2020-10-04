from src.utilities import load_yaml, create_logger
from src.all_imports import *
from src.steps.account_creation_steps import *


@pytest.mark.account_creation
@pytest.mark.account_creation_positive
def test_account_creation_case1(driver):
    logs.info("Starting account creation positive case #1 test!")
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
    create_logger('test_scenario1')
