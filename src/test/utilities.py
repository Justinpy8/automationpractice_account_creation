from src.test.all_imports import *

# to find the full location of your project in your system use this
ROOT_DIR = dirname(dirname(abspath(__file__)))

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