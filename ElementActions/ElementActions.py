from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# This script demonstrates the most common actions performed on a UI element.

# --- 1. Setup Phase ---
print("Defining capabilities...")
capabilities = {
    'platformName': 'Android',
    'appium:automationName': 'UiAutomator2',
    'appium:platformVersion': '16',
    'appium:deviceName': 'Pixel 9 Pro API 36',
    'appium:app': 'C:/Users/vmoor/OneDrive/Desktop/Android_Demo_App.apk'
}
appium_options = UiAutomator2Options().load_capabilities(capabilities)

driver = None
try:
    # --- 2. Action Phase ---
    print("Connecting to Appium server...")
    driver = webdriver.Remote('http://127.0.0.1:4723', options=appium_options)
    wait = WebDriverWait(driver, 10)
    print("Driver session started successfully.\n")

    # --- 3. Find an Element and Perform Actions ---
    # Action 1: .click()
    # We find a button and click it to navigate to the next screen.
    print("Finding the 'ENTER SOME VALUE' button...")
    enter_value_locator = (AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
    enter_value_button = wait.until(EC.element_to_be_clickable(enter_value_locator))

    enter_value_button.click()
    print("Action '.click()' executed successfully.\n")

    # Action 2: .send_keys()
    # We find a text input field and type into it.
    print("Finding the text input field...")
    edit_text_locator = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    text_field = wait.until(EC.visibility_of_element_located(edit_text_locator))

    text_to_send = "Hello World!"
    text_field.send_keys(text_to_send)
    print(f"Action '.send_keys(\"{text_to_send}\")' executed successfully.\n")
    time.sleep(2)  # Pause to see the text

    # Action 3: .clear()
    # We clear the text we just entered from the input field.
    text_field.clear()
    print("Action '.clear()' executed successfully.")

    input("\nScript finished. Press Enter to quit...")

finally:
    # --- 4. Teardown Phase ---
    if driver:
        driver.quit()
        print("Driver session closed.")
