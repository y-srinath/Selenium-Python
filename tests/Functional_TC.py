import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  # Replace with the appropriate WebDriver for your browser (e.g., Chrome, Firefox)
#driver.delete_all_cookies()
#driver.refresh()
driver.implicitly_wait(5) # Set an implicit wait to handle dynamic content loading 
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ca")
expected_products = ["Cauliflower - 1 Kg", "Carrot - 1 Kg", "Capsicum", "Cashews - 1 Kg"]
actual_products = []
time.sleep(2) # Wait for search results to update after typing in the search box
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(f"There are {len(results)} results matching your search criteria.")
assert len(results) > 0, "Expected at least one product to be displayed after search, but found none."

for result in results:
    product_name = result.find_element(By.TAG_NAME, "h4").text
    actual_products.append(product_name)
    #product_name = result.find_element(By.XPATH, "div/button").click()
    result.find_element(By.XPATH, ".//button[text()='ADD TO CART']").click()
assert set(expected_products).issubset(set(actual_products)), \
    f"Expected products {expected_products} not all found in actual products {actual_products}"

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#Total Value of Cart
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for i in prices:
    sum = sum + int(i.text)
print("Total price:", sum)
total_amount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == total_amount, \
    f"Total price mismatch: calculated sum is {sum}, but displayed total is {total_amount}"

#Applying Promo Code
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 5)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "promoInfo")))
promo_message = driver.find_element(By.CLASS_NAME, "promoInfo").text
print("Promo message:", promo_message)

# Validate discounted total
discounted_amount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert discounted_amount < total_amount, \
    f"Discounted total should be less than total amount, but got {discounted_amount} >= {total_amount}"

driver.quit()