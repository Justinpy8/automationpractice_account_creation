import logging
import time
import datetime
from selenium import webdriver
from os.path import abspath, dirname

driver = webdriver.Chrome()
# to find the full location of your project in your system use this
ROOT_DIR = dirname(dirname(abspath(__file__)))


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


def get_str_day():
    return time.strftime("%Y%m%d")  # 20200927


def get_str_seconds():
    return time.strftime("%Y%m%d_%H%M%S", time.localtime())


def create_logger(filename=""):
    logging.basicConfig(filename=f"{ROOT_DIR}/logs/{filename}{get_str_day()}.log",
                        level=logging.INFO,
                        format="%(asctime)-15s [%(levelname)s] %(funcName)s: %(message)s",
                        filemode='a')  # 'w' - to overwrite in each run, 'a' - append
    return logging.getLogger()


def closing_browser():
    driver.close()
