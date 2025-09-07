import time
from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# IMPORTANT: For web elements, we use Selenium's 'By', not AppiumBy
from selenium.webdriver.common.by import By

# This script demonstrates how to automate a mobile web browser, in this case, Safari on iOS.

# --- 1. Setup Phase ---
print("Defining iOS capabilities for Safari automation...")
capabilities = {
    'platformName': 'iOS',
    'appium:automationName': 'XCUITest',
    'appium:platformVersion': '18.6',
    'appium:deviceName': 'iPhone 16e',
    # This capability tells Appium to launch and automate the Safari browser
    # instead of a native app.
    'appium:browserName': 'Safari',
    # This is a helpful capability that tells Appium to automatically switch
    # into the webview context as soon as the session starts.
    'appium:autoWebview': True
}
appium_options = XCUITestOptions().load_capabilities(capabilities)

driver = None
try:
    # --- 2. Action Phase ---
    print("Connecting to Appium server...")
    driver = webdriver.Remote('http://127.0.0.1:4723', options=appium_options)
    wait = WebDriverWait(driver, 20)
    print("Driver session started successfully. Safari should be running.\n")

    # --- 3. Interact with the Web Page ---
    # Because we are in a web context, we use standard Selenium commands.
    print("Navigating to the target URL...")
    driver.get("http://www.dummypoint.com/seleniumtemplate.html")
    print("Navigation complete.\n")

    # --- 4. Find Web Elements and Perform Actions ---
    # CRITICAL: Inside a webview, you use Selenium's locators (By.ID, By.XPATH, etc.),
    # NOT Appium's native locators (AppiumBy.ID, AppiumBy.ACCESSIBILITY_ID).

    print("Finding the input field by its web ID...")
    # The locator is a simple string, just like in web automation.
    input_field_locator = (By.ID, "user_input")
    input_field = wait.until(EC.visibility_of_element_located(input_field_locator))

    input_field.click()
    input_field.send_keys("Hello from Appium Web Test!")
    print("Successfully typed into the input field.\n")

    print("Finding and clicking the submit button...")
    submit_button_locator = (By.ID, "submitbutton")
    submit_button = wait.until(EC.element_to_be_clickable(submit_button_locator))
    submit_button.click()
    print("Submit button clicked.")

    print("\n✅ Test Passed: Successfully automated the web page in Safari.")
    input("\nScript finished. Press Enter to quit...")

except TimeoutException:
    print("\n❌ Test Failed: A timeout occurred while waiting for a web element.")
except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")

finally:
    # --- 5. Teardown Phase ---
    if driver:
        print("Closing session...")
        driver.quit()
        print("Driver session closed.")
