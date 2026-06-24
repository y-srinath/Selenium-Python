from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

# Store parent window
parent_window = driver.current_window_handle

print("Parent Window:", parent_window)

# Open child window
driver.find_element(By.LINK_TEXT, "Click Here").click()

# Get all window handles
all_windows = driver.window_handles

print("All Windows:", all_windows)

# Switch to child window
for window in all_windows:
    if window != parent_window:
        driver.switch_to.window(window)
        break

print("Child Window Title:", driver.title)

# Validation
assert "New Window" in driver.page_source

# Close child window
driver.close()

# Switch back to parent window
driver.switch_to.window(parent_window)

print("Back to Parent:", driver.title)

driver.quit()