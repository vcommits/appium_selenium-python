import time
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# This script is a modern version for finding iOS elements using various locator strategies.

# --- 1. Setup Phase ---
print("Defining iOS capabilities...")
capabilities = {
    'platformName': 'iOS',
    'appium:automationName': 'XCUITest',
    'appium:platformVersion': '18.6',
    'appium:deviceName': 'iPhone 16e',
    'appium:app': '/Users/Shawn/Library/Developer/Xcode/DerivedData/UICatalog-ghtojoxoetvchgdtznkfuvyhhopt/Build/Products/Debug-iphonesimulator/UICatalog.app'
}
appium_options = XCUITestOptions().load_capabilities(capabilities)

driver = None
try:
    # --- 2. Action Phase ---
    print("Connecting to Appium server...")
    driver = webdriver.Remote('http://127.0.0.1:4723', options=appium_options)
    wait = WebDriverWait(driver, 10)
    print("Driver session started successfully.\n")

    # --- 3. Find and Click an Element ---
    # The best practice for finding an element by its accessibility identifier is AppiumBy.ACCESSIBILITY_ID.
    # It targets the 'name', 'label', and 'value' attributes on iOS.

    print("Finding the 'Date Picker' element by Accessibility ID...")
    date_picker_locator = (AppiumBy.ACCESSIBILITY_ID, "Date Picker")

    # --- Other Locator Examples (from instructor's script) ---
    # By XPath (using name attribute):
    # date_picker_locator = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Date Picker"]')

    # By XPath (using label attribute):
    # date_picker_locator = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@label="Date Picker"]')

    # Wait for the element to be clickable and then perform the action
    date_picker_button = wait.until(EC.element_to_be_clickable(date_picker_locator))
    date_picker_button.click()
    print("Successfully clicked the 'Date Picker' button.")

    print("\n✅ Test Passed: Element was found and clicked successfully.")
    input("\nScript finished. Press Enter to quit...")

except TimeoutException:
    print("\n❌ Test Failed: A timeout occurred while waiting for an element.")
except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")

finally:
    # --- 4. Teardown Phase ---
    if driver:
        print("Closing session...")
        driver.quit()
        print("Driver session closed.")
