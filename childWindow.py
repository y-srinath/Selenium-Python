import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.espncricinfo.com/")

print("Main title:", driver.title)
print("Main URL:", driver.current_url)
time.sleep(2)

wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

parent_window = driver.current_window_handle

# Dismiss cookie/consent overlay if present
try:
    accept_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH,
            "//button[contains(translate(normalize-space(.), 'ACCEPT', 'accept'), 'accept')"
            " or contains(translate(normalize-space(.), 'AGREE', 'agree'), 'agree')]"
        ))
    )
    accept_btn.click()
    print("Dismissed consent overlay")
    time.sleep(2)
except Exception:
    print("No consent overlay found")

# Locate the IPL 2026 nav tab (sponsor prefix like 'Tata' may appear)
ipl_tab = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//nav//a[contains(., 'IPL 2026')] | //a[contains(., 'IPL 2026')]")
))
print("Found IPL 2026 tab:", ipl_tab.text.strip())
time.sleep(2)

# Hover to reveal the dropdown
actions.move_to_element(ipl_tab).perform()
print("Hovered over IPL 2026 tab")
time.sleep(2)

# Get the Points Table href from the dropdown — exclude the current tab itself
points_table = wait.until(EC.visibility_of_element_located(
    (By.XPATH,
     "//a[contains(normalize-space(.), 'Points Table') and not(contains(., 'IPL 2026'))]")
))
points_table_url = points_table.get_attribute("href")
print("Found Points Table URL:", points_table_url)

# Open Points Table explicitly in a new window
driver.execute_script("window.open(arguments[0], '_blank');", points_table_url)
print("Opened Points Table in new window")
time.sleep(3)

# Switch to the new window
all_windows = driver.window_handles
for window in all_windows:
    if window != parent_window:
        driver.switch_to.window(window)
        break
print("Switched to new window")

wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

print("Points Table URL:", driver.current_url)
print("Points Table title:", driver.title)

assert "points-table" in driver.current_url.lower() or "points" in driver.title.lower(), \
    f"Expected Points Table page but got: {driver.current_url}"
print("Assertion passed: Points Table page loaded successfully")

time.sleep(10)