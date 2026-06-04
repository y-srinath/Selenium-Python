import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
print(driver.title)
print(driver.current_url)

# --- Simple alert ---
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert = driver.switch_to.alert
alert_text = alert.text
print("Simple alert text:", alert_text)
assert "I am a JS Alert" in alert_text, f"Unexpected simple alert text: {alert_text}"
alert.accept()
result_text = driver.find_element(By.ID, "result").text
assert "You successfully clicked an alert" in result_text, f"Unexpected result: {result_text}"

# --- Confirm alert: accept ---
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
confirm = driver.switch_to.alert
confirm_text = confirm.text
print("Confirm alert text:", confirm_text)
assert "I am a JS Confirm" in confirm_text, f"Unexpected confirm alert text: {confirm_text}"
confirm.accept()
result_text = driver.find_element(By.ID, "result").text
assert "You clicked: Ok" in result_text, f"Expected Ok result, got: {result_text}"

# --- Confirm alert: dismiss ---
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
driver.switch_to.alert.dismiss()
result_text = driver.find_element(By.ID, "result").text
assert "You clicked: Cancel" in result_text, f"Expected Cancel result, got: {result_text}"

# --- Prompt alert: enter text and accept ---
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
prompt = driver.switch_to.alert
prompt_text = prompt.text
print("Prompt alert text:", prompt_text)
assert "I am a JS prompt" in prompt_text, f"Unexpected prompt text: {prompt_text}"
prompt.send_keys("Selenium Tester")
prompt.accept()
result_text = driver.find_element(By.ID, "result").text
assert "Selenium Tester" in result_text, f"Expected name in prompt result, got: {result_text}"

# --- Prompt alert: dismiss ---
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
driver.switch_to.alert.dismiss()
result_text = driver.find_element(By.ID, "result").text
assert "You entered: null" in result_text, f"Expected null result, got: {result_text}"

print("All assertions passed.")

time.sleep(5)
