import time
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# This script is a modern version for performing element actions like getting text and attributes on iOS.

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
    # The instructor's script used "AAPLDatePickerController", but in the current
    # UICatalog app, the accessibility ID is "Date Picker".
    date_picker_locator = (AppiumBy.ACCESSIBILITY_ID, "Date Picker")
    element = wait.until(EC.visibility_of_element_located(date_picker_locator))
    print("Element found.\n")

    # --- 4. Get Text and Attribute ---
    # The instructor's script demonstrates getting the element's text in two ways.
    # On iOS, for simple static text elements, these often return the same value.
    print("--- Element Actions/Properties ---")

    # .text: Gets the visible text of the element.
    element_text = element.text
    print(f"Text from .text property: '{element_text}'")

    # .get_attribute("name"): Gets the value of the 'name' attribute from the element's source.
    # On iOS, this is often the same as the accessibility label.
    element_name_attr = element.get_attribute("name")
    print(f"Text from .get_attribute('name'): '{element_name_attr}'")

    print("--------------------------------")

    # --- 5. Perform a Click Action ---
    print("\nPerforming a click action on the element...")
    element.click()
    print("Successfully clicked the 'Date Picker' button.")

    print("\n✅ Test Passed: Successfully demonstrated element actions.")
    input("\nScript finished. Press Enter to quit...")

except (TimeoutException, NoSuchElementException):
    print("\n❌ Test Failed: Could not find the specified element.")
except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")

finally:
    # --- 6. Teardown Phase ---
    if driver:
        print("Closing session...")
        driver.quit()
        print("Driver session closed.")
