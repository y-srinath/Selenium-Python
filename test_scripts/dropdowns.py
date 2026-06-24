import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://practice.expandtesting.com/dropdown")
print(driver.title)
print(driver.current_url)

# --- Simple dropdown ---
simple = Select(driver.find_element(By.ID, "dropdown"))
assert simple.first_selected_option.text == "Please select an option", \
    "Expected placeholder to be selected by default"

simple.select_by_value("1")
assert simple.first_selected_option.text == "Option 1", \
    "Expected 'Option 1' to be selected"

simple.select_by_value("2")
assert simple.first_selected_option.text == "Option 2", \
    "Expected 'Option 2' to be selected"

# --- Elements per page dropdown ---
per_page = Select(driver.find_element(By.ID, "elementsPerPageSelect"))
assert per_page.first_selected_option.get_attribute("value") == "10", \
    "Expected default elements per page to be 10"

per_page.select_by_value("50")
assert per_page.first_selected_option.get_attribute("value") == "50", \
    "Expected elements per page to be 50 after selection"

# --- Country dropdown ---
country = Select(driver.find_element(By.ID, "country"))
assert country.first_selected_option.text == "Select country", \
    "Expected country placeholder to be selected by default"

country.select_by_value("US")
assert country.first_selected_option.text == "United States", \
    "Expected 'United States' to be selected"

country.select_by_visible_text("Canada")
assert country.first_selected_option.get_attribute("value") == "CA", \
    "Expected country value to be 'CA' after selecting Canada"

print("All assertions passed.")

time.sleep(3)
