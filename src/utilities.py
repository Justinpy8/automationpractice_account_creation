import logging
import time
import datetime
import yaml
from os.path import abspath, dirname

# to find the full location of your project in your system use this
ROOT_DIR = dirname(dirname(abspath(__file__)))


# ******************************System tools*********************************
def get_str_day():
    return time.strftime("%Y%m%d")  # 20200927


def get_str_seconds():
    return time.strftime("%Y%m%d_%H%M%S", time.localtime())


def create_logger(filename=""):
    logging.basicConfig(filename=f"C:/Dev/automationpractice_homework/logs/{filename}{get_str_day()}.log",
                        level=logging.INFO,
                        format="%(asctime)-15s [%(levelname)s] %(funcName)s: %(message)s",
                        filemode='a')  # 'w' - to overwrite in each run, 'a' - append
    return logging.getLogger()


def load_yaml(filepath):
    """Initiating safe loading the yaml file from dir path"""
    with open(filepath, 'r') as info:
        document = yaml.safe_load(info)
    return document
