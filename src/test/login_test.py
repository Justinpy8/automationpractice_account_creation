from src.all_imports import *
# from src.conftest import driver

data = utils.load_yaml("C:/Dev/automationpractice_homework/data/parameter.yml")
logs = utils.create_logger()

url = data["url"]
username = data["username"]
password = data["password"]


@pytest.mark.login
@pytest.mark.positive_test
def test_login_case1(driver):
    logs.info("Starting the login case 1 test!")
    login_page = LoginPage(driver)
    driver.get(url)
    time.sleep(2)
    login_page.sign_in(username, password)
