from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

# This script demonstrates how to perform a "drag and drop" gesture.

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

    # --- 3. Navigate to the Drag and Drop Screen ---
    print("Scrolling to find the 'DRAGANDDROP' button...")
    scroll_locator_string = 'new UiScrollable(new UiSelector()).scrollIntoView(text("DRAGANDDROP"))'
    drag_and_drop_button = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=scroll_locator_string)
    drag_and_drop_button.click()
    print("Navigated to the drag and drop view.\n")

    # --- 4. Identify Source and Target Elements ---
    print("Finding the source and target elements...")
    source_element_locator = (AppiumBy.ID, "com.code2lead.kwad:id/ingvw")
    source_element = wait.until(EC.visibility_of_element_located(source_element_locator))

    target_element_locator = (AppiumBy.ID, "com.code2lead.kwad:id/layout2")
    target_element = wait.until(EC.visibility_of_element_located(target_element_locator))
    print("Source and target elements found.\n")

    # --- 5. Perform the Drag and Drop Gesture ---
    # The modern, W3C-compliant way to do this is with ActionChains.
    # The .drag_and_drop() method is a convenient, high-level command.
    print("Performing drag and drop gesture...")
    actions = ActionChains(driver)
    actions.drag_and_drop(source_element, target_element).perform()
    print("Drag and drop gesture performed successfully.\n")

    # --- 6. Assert the Outcome ---
    print("Verifying the success message...")
    success_message_locator = (AppiumBy.ID, "com.code2lead.kwad:id/tvDrop")
    success_message = wait.until(EC.visibility_of_element_located(success_message_locator))

    assert "Dropped!" in success_message.text
    print("✅ Test Passed: The success message was displayed as expected.")

    input("\nScript finished. Press Enter to quit...")

except TimeoutException:
    print("\n❌ Test Failed: A timeout occurred while waiting for an element.")
except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")

finally:
    # --- 7. Teardown Phase ---
    if driver:
        driver.quit()
        print("Driver session closed.")
