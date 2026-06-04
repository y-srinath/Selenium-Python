import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
print(driver.current_url)

driver.implicitly_wait(5) # Set an implicit wait to handle dynamic content loading

action = ActionChains(driver)

# Verify Hoverable Dropdown
assert driver.find_element(By.ID, "mousehover").is_displayed(), "Expected hoverable dropdown to be visible"

hover_element = driver.find_element(By.ID, "mousehover")
driver.execute_script("arguments[0].scrollIntoView(true);", hover_element)
action.move_to_element(hover_element).perform()
#driver.find_element(By.LINK_TEXT, "Top").click()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click()
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()

top_option = driver.find_element(By.LINK_TEXT, "Top")

assert top_option.is_displayed(), "Top option is not visible after hover"
#assert not top_option.is_displayed(), "Top option should NOT be visible"

print("All assertions passed.")

time.sleep(5)