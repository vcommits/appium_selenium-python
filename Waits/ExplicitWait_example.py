from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# This script demonstrates the modern, best-practice use of Explicit Waits.

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
    print("Driver session started.")

    # Create a WebDriverWait instance. We will reuse this object for all our waits.
    # It will wait a maximum of 10 seconds for conditions to be met.
    wait = WebDriverWait(driver, 10)

    # --- Find and click the first element ---
    # We wait for the element to be clickable before we interact with it.
    # The locator is a tuple: (strategy, value)
    print("Waiting for 'Enter Value' button to be clickable...")
    enter_value_locator = (AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
    enter_value_button = wait.until(EC.element_to_be_clickable(enter_value_locator))
    enter_value_button.click()
    print("Button clicked.")

    # --- Find and type into the second element ---
    # On the new screen, we wait for the EditText field to be visible.
    print("Waiting for the EditText field to be visible...")
    edit_text_locator = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    text_field = wait.until(EC.visibility_of_element_located(edit_text_locator))

    text_to_send = "Skill2Lead"
    print(f"Typing '{text_to_send}' into the field...")
    text_field.send_keys(text_to_send)
    print("Text sent successfully.")

    input("\nScript finished. Press Enter to quit...")

except TimeoutException:
    print("\n❌ Test Failed: A timeout occurred while waiting for an element.")
except NoSuchElementException:
    print("\n❌ Test Failed: Could not find an element with the specified locator.")
finally:
    # --- 3. Teardown Phase ---
    if driver:
        driver.quit()
        print("Driver session closed.")
