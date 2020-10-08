from src.all_imports import *
from selenium.webdriver.support.select import Select
from src.pages.base_page import *

logs = utils.create_logger()


class LoginPage(BasePage):

    def sign_in(self, username, password):
        """Entering the sign in page"""
        sign_in_button = self.driver.find_element_by_xpath("//a[@class='login']")
        sign_in_button.click()
        time.sleep(2)

        """Enter username"""
        email_address = self.driver.find_element_by_xpath("//input[@id='email']")
        email_address.send_keys(username)
        logs.info(f"Entering User Name: {username}")
        """Enter password"""
        pw = self.driver.find_element_by_xpath("//input[@id='passwd']")
        pw.send_keys(password)
        logs.info(f"Entering User Name: {password}")
        """Click to sign in"""
        self.driver.find_element_by_xpath("//button[@id='SubmitLogin']").click()
        print("Click to sign in.......")


class AccountCreationPage(BasePage):

    def launching_website(self, url):
        self.driver.get(url)
        logs.info(f"{url} is loading")

    def email_address_check(self, email):
        """Entering the account creation page"""
        sign_in_button = self.driver.find_element_by_xpath("//a[@class='login']")
        sign_in_button.click()
        time.sleep(2)
        """Entering the email address"""
        email_address = self.driver.find_element_by_xpath("//input[@id='email_create']")
        email_address.send_keys(email)
        self.driver.find_element_by_xpath("//button[@id='SubmitCreate']").click()
        time.sleep(2)
        logs.info(f"{email} is being entered as User Name")

        try:
            """Email address not available error"""
            email_unavailable_error = self.driver.find_element_by_xpath("//div[@id='create_account_error']")
            if email_unavailable_error.is_displayed():
                logs.error("This email address already exist")
                self.screen_shots("unavailable email address")
                logs.info("Screen shot of the error message has been saved")
        except NoSuchElementException as err:
            pass

    def title_info(self, title):
        """Title"""
        male = self.driver.find_element_by_xpath("//input[@id='id_gender1']")
        female = self.driver.find_element_by_xpath("//input[@id='id_gender2']")
        if title == "male":
            male.click()
        elif title == "female":
            female.click()
        logs.info("Title has been selected")

    def name_info(self, firstname, lastname):
        """first name info"""
        first_name = self.driver.find_element_by_xpath("//input[@id='customer_firstname']")
        first_name.send_keys(firstname)
        logs.info(f"Entering {firstname} as the first name.")

        """last name info"""
        last_name = self.driver.find_element_by_xpath("//input[@id='customer_lastname']")
        last_name.send_keys(lastname)
        logs.info(f"Entering {lastname} as the first name.")

    def password_info(self, password):
        """password info"""
        pass_word = self.driver.find_element_by_xpath("//input[@id='passwd']")
        pass_word.send_keys(password)
        logs.info(f"Entering {password} as the password.")

    def date_of_birth(self, date, month, year):
        """date info"""
        selecting = Select
        date_dropdown = self.driver.find_element_by_xpath("//select[@id='days']")
        date_selection = selecting(date_dropdown)
        date_selection.select_by_value(date)
        logs.info(f"Date selected: {date}")
        time.sleep(1)

        """month info"""
        month_dropdown = self.driver.find_element_by_xpath("//select[@id='months']")
        month_selection = selecting(month_dropdown)
        month_selection.select_by_visible_text(f"{month} ")
        logs.info(f"Month Selected: {month}")
        time.sleep(1)

        """year info"""
        year_dropdown = self.driver.find_element_by_xpath("//select[@id='years']")
        year_selection = selecting(year_dropdown)
        year_selection.select_by_value(year)
        logs.info(f"Year selected: {year}")
        time.sleep(1)

    def news_letter(self):
        newsletter = self.driver.find_element_by_xpath("//input[@id='newsletter']")
        newsletter.click()
        logs.info(f"Sign up for our newsletter box is checked")

    def special_offers(self):
        offers = self.driver.find_element_by_xpath("//input[@id='optin']")
        offers.click()
        logs.info(f"Receive special offers from our partners box is checked")

    def company_name(self, companyname):
        company = self.driver.find_element_by_xpath("//input[@id='company']")
        company.send_keys(companyname)
        logs.info(f"Company name is: {companyname}")

    def address(self, address_line1, address_line2, city, state, zipcode, country):
        """Entering the address info into the 1st address box:
        ******Street address, P.O. Box, Company name, etc.******
        """
        address_box1 = self.driver.find_element_by_xpath("//input[@id='address1']")
        address_box1.send_keys(address_line1)

        """Entering the address info into the 2nd address box:
        ******Apartment, suite, unit, building, floor, etc...******
        """
        address_box2 = self.driver.find_element_by_xpath("//input[@id='address2']")
        address_box2.send_keys(address_line2)

        """Entering the City info"""
        city_name = self.driver.find_element_by_xpath("//input[@id='city']")
        city_name.send_keys(city)

        """Choosing the states from the dropdown list"""
        states_list = self.driver.find_element_by_xpath("//select[@id='id_state']")
        select_list = Select(states_list)
        select_list.select_by_visible_text(state)
        time.sleep(1)

        """Entering the zip code"""
        postalcode = self.driver.find_element_by_xpath("//input[@id='postcode']")
        postalcode.send_keys(zipcode)

        """Choose country from the dropdown list"""
        country_list = self.driver.find_element_by_xpath("//select[@id='id_country']")
        country_select = Select(country_list)
        country_select.select_by_visible_text(country)

        logs.info("The following address info have been entered: ")
        logs.info(f"\n{address_line1}\n{address_line2}\n{city}\n{state}\n{zipcode}\n{country}")

    def additional_info(self, additionalinfo):
        additional = self.driver.find_element_by_xpath("//textarea[@id='other']")
        additional.send_keys(additionalinfo)
        logs.info(f"The following additional info has been appended:\n{additionalinfo}")

    def home_phone(self, homephone):
        homenum = self.driver.find_element_by_xpath("//input[@id='phone']")
        homenum.send_keys(homephone)
        logs.info(f"Home phone number is: {homephone} ")

    def mobile_phone(self, mobilephone):
        mobilenum = self.driver.find_element_by_xpath("//input[@id='phone_mobile']")
        mobilenum.send_keys(mobilephone)
        logs.info(f"Mobile phone number is: {mobilephone}")

    def address_alias(self, aliasaddress):
        alias = self.driver.find_element_by_xpath("//input[@id='alias']")
        alias.send_keys(aliasaddress)
        logs.info(f"{aliasaddress} is being entered as the alias address")

    def register_button(self):
        reg_button = self.driver.find_element_by_xpath("//button[@id='submitAccount']")
        reg_button.click()
        time.sleep(5)
        logs.info("Registering the account.........")

    def account_confirmation(self):
        """Checking for error message after clicking on the register button """
        try:
            """Testing to see if the account creation is a success by finding the sign out button"""
            logout_button = self.driver.find_element_by_xpath("//a[@class='logout']")
            if logout_button.is_displayed():
                logs.info("Account creation is successful - the sign out button is displayed.")
            else:
                error_msg = self.driver.find_element_by_xpath("//div[@class='alert alert-danger']")
                error_msg.is_displayed()
                self.screen_shots('Registration')
                logs.error("Registration error message screen shot has been captured")

        except NoSuchElementException as err:
            logs.warning(err)

    def signout(self):
        logout = self.driver.find_element_by_xpath("//a[@class='logout']")
        logout.click()
        print("Signing out now........")
        time.sleep(2)

