from webdriver_functions import *

# data:

url = "http://automationpractice.com/"
email = "jj@sweet2.com"
title = "male"
firstname = "Justin"
lastname = "Rich"
password = "t56"
date = "13"
month = 'May'
year = "1984"
companyname = "Lucky Brand"
address_line1 = "123 Superman Ave"
address_line2 = "1st Floor"
city = "Brooklyn"
state = "New York"
zipcode = "12345"
country = "United States"
additionalinfo = "Not sure what to put in here"
homephone = "123-123-7899"
mobilephone = "258-369-8888"
aliasaddress = "123 sweet st"

# Executions:

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
closing_browser()
