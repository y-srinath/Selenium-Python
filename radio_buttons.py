import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://practice.expandtesting.com/radio-buttons")
print(driver.title)
print(driver.current_url)

# Verify all radio buttons are visible on the page
assert driver.find_element(By.ID, "blue").is_displayed(), "Expected 'blue' radio button to be visible"
assert driver.find_element(By.ID, "red").is_displayed(), "Expected 'red' radio button to be visible"
assert driver.find_element(By.ID, "green").is_displayed(), "Expected 'green' radio button to be visible"
assert driver.find_element(By.ID, "tennis").is_displayed(), "Expected 'tennis' radio button to be visible"
assert driver.find_element(By.ID, "basketball").is_displayed(), "Expected 'basketball' radio button to be visible"

# Verify default selections: blue and tennis are pre-checked
assert driver.find_element(By.ID, "blue").is_selected(), "Expected 'blue' to be selected by default"
assert driver.find_element(By.ID, "tennis").is_selected(), "Expected 'tennis' to be selected by default"

# Verify green is disabled
assert not driver.find_element(By.ID, "green").is_enabled(), "Expected 'green' to be disabled"

# Select a different color
driver.find_element(By.ID, "red").click()
assert driver.find_element(By.ID, "red").is_selected(), "Expected 'red' to be selected"
assert not driver.find_element(By.ID, "blue").is_selected(), "Expected 'blue' to be deselected after selecting 'red'"

# Select a different sport
driver.find_element(By.ID, "basketball").click()
assert driver.find_element(By.ID, "basketball").is_selected(), "Expected 'basketball' to be selected"
assert not driver.find_element(By.ID, "tennis").is_selected(), "Expected 'tennis' to be deselected after selecting 'basketball'"

print("All assertions passed.")

time.sleep(3)
