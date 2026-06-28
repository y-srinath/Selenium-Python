import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox OR edge")
    parser.addoption("--headless", action="store_true", default=False, help="Run tests in headless mode")


@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser")
    headless = request.config.getoption("headless")

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    elif browser_name == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Edge(options=options)

    driver.set_window_size(1920, 1080)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    print(driver.title)
    print(driver.current_url)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()  # post condition to close the browser after test execution