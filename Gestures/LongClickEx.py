from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time

# This script demonstrates how to perform a gesture, specifically a "long click" or "long press".

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
    wait = WebDriverWait(driver, 20)
    print("Driver session started successfully.\n")

    # --- 3. Scroll to the Target Element ---
    print("Scrolling to find the 'LONG CLICK' button...")
    scroll_locator_string = 'new UiScrollable(new UiSelector()).scrollIntoView(text("LONG CLICK"))'
    long_click_button = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=scroll_locator_string)
    print("Element found.\n")

    # --- 4. Perform the Long Click Gesture ---
    # To perform gestures, we use the ActionChains class.
    # The older TouchAction class is deprecated and should not be used in modern scripts.
    print("Performing a long click on the button...")
    actions = ActionChains(driver)
    actions.click_and_hold(long_click_button).perform()
    print("Long click gesture performed successfully.\n")

    # --- 5. Assert the Outcome ---
    # A long click on this button opens a context menu. We can verify it appeared.
    print("Verifying that the context menu appeared...")
    context_menu_item_locator = (AppiumBy.XPATH, "//*[@text='Item 1']")
    context_menu_item = wait.until(EC.visibility_of_element_located(context_menu_item_locator))

    assert context_menu_item.is_displayed()
    print("✅ Test Passed: The context menu with 'Item 1' was displayed as expected.")

    input("\nScript finished. Press Enter to quit...")

except TimeoutException:
    print("\n❌ Test Failed: A timeout occurred while waiting for an element.")
except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")

finally:
    # --- 6. Teardown Phase ---
    if driver:
        driver.quit()
        print("Driver session closed.")
