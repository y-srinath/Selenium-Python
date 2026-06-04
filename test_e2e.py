import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_e2e(browserInstance):
    driver = browserInstance
    driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card h-100']")))
    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    for product in products:
        productName = product.find_element(By.XPATH, "div/h4/a").text
        if productName == "Nokia Edge":
            product.find_element(By.XPATH, "div/button").click()

    driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    driver.find_element(By.ID, "country").send_keys("ind")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element(By.LINK_TEXT, "India").click()
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
    success_message = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert "Success! Thank you!" in success_message, "Purchase was not successful"  

    time.sleep(4)