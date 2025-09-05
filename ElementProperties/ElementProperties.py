from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This script demonstrates how to get various properties from a UI element.

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

    # --- 3. Find an Element and Get its Properties ---
    # We'll use the 'ENTER SOME VALUE' button as our example element.
    print("Finding the target element...")
    enter_value_locator = (AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
    target_element = wait.until(EC.visibility_of_element_located(enter_value_locator))
    print("Element found.\n")

    # --- 4. Print the Element's Properties ---
    print("--- Element Property Information ---")
    # .is_displayed() returns True if the element is visible on the screen.
    print(f"Is Displayed? : {target_element.is_displayed()}")

    # .is_enabled() returns True if the element is interactive (not greyed out).
    print(f"Is Enabled?   : {target_element.is_enabled()}")

    # .is_selected() returns True if an element (like a checkbox) is selected.
    print(f"Is Selected?  : {target_element.is_selected()}")

    # .size returns a dictionary with the element's height and width in pixels.
    print(f"Size          : {target_element.size}")

    # .location returns a dictionary with the element's x and y coordinates on the screen.
    print(f"Location      : {target_element.location}")

    input("\nScript finished. Press Enter to quit...")

finally:
    # --- 5. Teardown Phase ---
    if driver:
        driver.quit()
        print("Driver session closed.")
