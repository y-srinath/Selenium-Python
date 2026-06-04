import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()  # Replace with the appropriate WebDriver for your browser (e.g., Chrome, Firefox)
driver.get("https://practice.expandtesting.com/form-validation")
print(driver.title)
print(driver.current_url)


Contact_Name = driver.find_element(By.ID, "validationCustom01")  # use your actual id
Contact_Name.clear()
Contact_Name.send_keys("Test")

driver.find_element(By.NAME, "contactnumber").send_keys("123-4567890")
driver.find_element(By.NAME, "pickupdate").send_keys("01011991")

payment_dropdown = Select(driver.find_element(By.ID, "validationCustom04"))
payment_dropdown.select_by_value("cashondelivery")


driver.find_element(By.XPATH, "//button[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME, "alert-info").text
#message = driver.find_element(By.XPATH, "//div[contains(@class,'alert-info')]/p").text
print(message)

assert "Thank you" in message, "Expected 'Thank you' in the message, but got: " + message

time.sleep(3)
