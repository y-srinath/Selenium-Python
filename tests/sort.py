import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
print(driver.title)
print(driver.current_url)

#driver.implicitly_wait(5) # Set an implicit wait to handle dynamic content loading

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click() # Click on the first column header to sort
time.sleep(2) # Wait for sorting to complete
product_elements = driver.find_elements(By.XPATH, "//tr/td[1]") # Get names of all products
product_names = [veg.text.strip() for veg in product_elements if veg.text.strip()] # Extract and clean product names, ignoring empty entries
print("Products from browser:", product_names)
sorted_product_names = product_names.copy()
sorted_product_names.sort()
print("Products sorted in Python:", sorted_product_names)

assert product_names == sorted_product_names, "Products are not sorted correctly on the webpage"

print("All assertions passed.")

time.sleep(3)