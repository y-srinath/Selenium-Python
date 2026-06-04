import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox OR edge")

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
    elif browser_name == "edge":
        driver = webdriver.Edge()
        driver.set_window_size(1920, 1080)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    print(driver.title)
    print(driver.current_url)
    driver.implicitly_wait(5)
    yield driver
    driver.quit() #post condition to close the browser after test execution