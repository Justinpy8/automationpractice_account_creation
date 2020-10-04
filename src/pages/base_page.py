from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import datetime

import src.utilities as utils


# from src.steps.account_creation_steps import driver


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def screen_shots(self, message=""):
        """Define time format for the file name"""
        system_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
        """Set the file location for the screenshot files"""
        file_path = 'C:/Dev/automationpractice_homework/screenshots/'
        """Create the file name for the screen shot file."""
        file_name = f"{message}_error_{system_time}.png"
        """Create the variable contains the file location and file name formatting"""
        full_file_path = f"{file_path}{file_name}"
        """Take the screen shot and save it to the predefined location"""
        self.driver.save_screenshot(full_file_path)
