import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://practice.expandtesting.com/checkboxes")
print(driver.title)
print(driver.current_url)

# Verify default states: checkbox1 unchecked, checkbox2 checked
assert not driver.find_element(By.ID, "checkbox1").is_selected(), "Expected 'checkbox1' to be unchecked by default"
assert driver.find_element(By.ID, "checkbox2").is_selected(), "Expected 'checkbox2' to be checked by default"

# Check checkbox1 and verify it's now checked
driver.find_element(By.ID, "checkbox1").click()
assert driver.find_element(By.ID, "checkbox1").is_selected(), "Expected 'checkbox1' to be checked after clicking"

# Uncheck checkbox2 and verify it's now unchecked
driver.find_element(By.ID, "checkbox2").click()
assert not driver.find_element(By.ID, "checkbox2").is_selected(), "Expected 'checkbox2' to be unchecked after clicking"

# Both can be toggled independently — verify checkbox1 is still checked
assert driver.find_element(By.ID, "checkbox1").is_selected(), "Expected 'checkbox1' to remain checked"

print("All assertions passed.")

time.sleep(3)
