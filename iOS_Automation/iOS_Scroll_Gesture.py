import time
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# This script is a modern version for performing a scroll gesture on iOS.

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

    # --- 3. Perform the Scroll Gesture ---
    # The old driver.scroll() method is deprecated. The modern way is to use
    # the "mobile: scroll" gesture via execute_script.
    # This command tells Appium to scroll down until it finds an element
    # with the accessibility ID "Web View".

    print("Scrolling down to find the 'Web View' element...")
    scroll_args = {'direction': 'down', 'predicateString': 'label == "Web View"'}
    driver.execute_script("mobile: scroll", scroll_args)
    print("Scroll complete. 'Web View' should be visible.\n")

    # --- 4. Find and Click the Element ---
    # Now that the element is visible, we can find it and interact with it.
    print("Finding and clicking the 'Web View' button...")
    web_view_locator = (AppiumBy.ACCESSIBILITY_ID, "Web View")
    web_view_button = wait.until(EC.element_to_be_clickable(web_view_locator))
    web_view_button.click()
    print("Successfully clicked the 'Web View' button.")

    print("\n✅ Test Passed: Scroll gesture was successful.")
    input("\nScript finished. Press Enter to quit...")

except (TimeoutException, NoSuchElementException):
    print("\n❌ Test Failed: Could not find the element after scrolling.")
except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")

finally:
    # --- 5. Teardown Phase ---
    if driver:
        print("Closing session...")
        driver.quit()
        print("Driver session closed.")
