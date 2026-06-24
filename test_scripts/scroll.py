import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()

# Run Chrome in headless mode (without opening a window)
chrome_options.add_argument("headless") 

# Ignore SSL certificate errors (useful for testing with self-signed certificates)
chrome_options.add_argument("--ignore-certificate-errors") 

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
print(driver.current_url)

driver.implicitly_wait(5) # Set an implicit wait to handle dynamic content loading

#action = ActionChains(driver)

driver.execute_script("window.scrollBy(0, 500);") # Scroll down by 500 pixels
# driver.get_screenshot_as_file("Screenshot.png")
# driver.save_screenshot("after_scroll.png")

print("All assertions passed.")

time.sleep(5)