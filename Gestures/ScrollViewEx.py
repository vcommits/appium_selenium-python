from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# This script demonstrates how to scroll to an element that is not initially visible.

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
    wait = WebDriverWait(driver, 20)  # Increased wait time for potentially slow scrolls
    print("Driver session started successfully.\n")

    # --- 3. Navigate to the Scrollable Screen ---
    print("Finding and clicking the 'ScrollView' button...")
    scroll_view_locator = (AppiumBy.ID, "com.code2lead.kwad:id/ScrollView")
    scroll_view_button = wait.until(EC.element_to_be_clickable(scroll_view_locator))
    scroll_view_button.click()
    print("Navigated to the scrollable view.\n")

    # --- 4. Scroll to an Element and Click It ---
    # This is a powerful, Android-only command using the UIAutomator strategy.
    # 'new UiScrollable(new UiSelector())' identifies a scrollable container.
    # '.scrollIntoView(text("BUTTON12"))' tells it to scroll until it finds an
    # element with the text "BUTTON12" and brings it into view.
    print("Scrolling to find the element with text 'BUTTON12'...")
    scroll_locator_string = 'new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON12"))'

    # We find the element using this command. The scroll action is part of the find.
    button12 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=scroll_locator_string)

    button12.click()
    print("Successfully scrolled to and clicked 'BUTTON12'.")

    input("\nScript finished. Press Enter to quit...")

except TimeoutException:
    print("\n❌ Test Failed: A timeout occurred while waiting for an element.")
except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")

finally:
    # --- 5. Teardown Phase ---
    if driver:
        driver.quit()
        print("Driver session closed.")
