from email import message
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Replace with the appropriate WebDriver for your browser (e.g., Chrome, Firefox)
driver.get("https://practice.expandtesting.com/autocomplete")
print(driver.title)
print(driver.current_url)

driver.find_element(By.ID, "country").send_keys("I")

countries = driver.find_elements(By.CSS_SELECTOR, "#countryautocomplete-list div")
for country in countries:
    print(country.text)

print(f"There are {len(countries)} countries available.")

for country in countries:
    if country.text == "Italy":
        country.click()
        break
driver.find_element(By.XPATH, "//button[text()='Submit']").click()

#driver.find_element(By.XPATH, "//div[@id='countryautocomplete-list']//div[text()='India']").click()

message = driver.find_element(By.ID, "result").text
print(driver.find_element(By.ID, "result").get_attribute("innerText"))
country_name = message.split(": ")[1]
assert country_name == "India", \
f"Expected 'India', but got '{country_name}'"

time.sleep(5)