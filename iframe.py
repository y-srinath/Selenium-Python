import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
print(driver.title)
print(driver.current_url)

# Verify the page heading is visible in the main document
heading = driver.find_element(By.TAG_NAME, "h3")
assert "An iFrame containing the TinyMCE" in heading.text, f"Unexpected heading: {heading.text}"

# Switch into the TinyMCE iframe
driver.switch_to.frame("mce_0_ifr")

# Read and verify default content inside the iframe
body = driver.find_element(By.ID, "tinymce")
default_text = body.text
print("Default iframe content:", default_text)
assert "Your content goes here." in default_text, f"Unexpected default content: {default_text}"

# Clear and set content via JS (contenteditable — .clear() and send_keys unreliable on TinyMCE)
driver.execute_script("arguments[0].innerHTML = '<p>Hello from Selenium!</p>';", body)
typed_text = body.text
print("Typed iframe content:", typed_text)
assert "Hello from Selenium!" in typed_text, f"Text not entered correctly: {typed_text}"

# Switch back to the main document
driver.switch_to.default_content()

# Verify we are back — heading should still be accessible
print("Main document heading:", heading.text)
assert heading.is_displayed(), "Expected heading to be visible after switching back to main content"

print("All assertions passed.")

time.sleep(5)
