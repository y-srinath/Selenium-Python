import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Replace with the appropriate WebDriver for your browser (e.g., Chrome, Firefox)
driver.get("https://practice.expandtesting.com/login")
print(driver.title)
print(driver.current_url)

# Username
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("practice")

# Password
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("SuperSecretPassword!")

# Login button
#driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Login']").click()

message = driver.find_element(By.CLASS_NAME, "alert-success").text
#message = driver.find_element(By.XPATH, "//div[contains(@class,'alert-info')]/p").text
print(message)

assert "You logged into a secure area!" in message, "Expected 'You logged into a secure area!' in the message, but got: " + message

time.sleep(3)
