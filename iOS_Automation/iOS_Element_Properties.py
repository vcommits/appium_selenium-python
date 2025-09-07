import time
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# This script is a modern version for getting various properties from an iOS element.

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

    # --- 3. Find the Target Element ---
    print("Finding the 'Date Picker' element...")
    # We'll use the "Date Picker" table cell as our example element.
    date_picker_locator = (AppiumBy.ACCESSIBILITY_ID, "Date Picker")
    element = wait.until(EC.visibility_of_element_located(date_picker_locator))
    print("Element found.\n")

    # --- 4. Get and Print Element Properties ---
    # These methods are essential for creating assertions in your tests.
    print("--- Element Properties ---")

    # .is_displayed(): Returns True if the element is visible on the screen.
    print(f"Is Displayed: {element.is_displayed()}")

    # .is_enabled(): Returns True if the element is interactive (not greyed out).
    print(f"Is Enabled: {element.is_enabled()}")

    # .is_selected(): Returns True for elements like switches or checkboxes that are 'on'.
    # A table cell is not selectable, so this will be False.
    print(f"Is Selected: {element.is_selected()}")

    # .size: Returns a dictionary with the element's width and height in pixels.
    print(f"Size: {element.size}")

    # .location: Returns a dictionary with the element's X and Y coordinates on the screen.
    print(f"Location: {element.location}")

    print("--------------------------")

    print("\n✅ Test Passed: Successfully retrieved element properties.")
    input("\nScript finished. Press Enter to quit...")

except (TimeoutException, NoSuchElementException):
    print("\n❌ Test Failed: Could not find the specified element.")
except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")

finally:
    # --- 5. Teardown Phase ---
    if driver:
        print("Closing session...")
        driver.quit()
        print("Driver session closed.")
