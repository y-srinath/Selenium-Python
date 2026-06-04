import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Replace with the appropriate WebDriver for your browser (e.g., Chrome, Firefox)
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
#driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.ID, "name").send_keys("Test")
driver.find_element(By.ID, "email").send_keys("test1234@email.com")
driver.find_element(By.XPATH, "//label[text()='Male']/preceding-sibling::input").click()
driver.find_element(By.NAME, "mobile").send_keys("1234567890")
driver.find_element(By.NAME, "dob").send_keys("01011991")
driver.find_element(By.NAME, "subjects").send_keys("Testing")
driver.find_element(By.XPATH, "//label[normalize-space()='Sports']/preceding-sibling::input").click()
driver.find_element(By.XPATH, "//label[normalize-space()='Music']/preceding-sibling::input").click()

driver.find_element(By.XPATH, "//input[@type='submit']").click()

time.sleep(3)