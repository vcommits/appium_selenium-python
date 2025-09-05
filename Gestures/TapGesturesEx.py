from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# This script demonstrates how to perform a tap gesture by coordinates,
# specifically by tapping the center of a found element.

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

    # --- 3. Navigate to the Login Screen ---
    print("Navigating to the login page...")
    login_page_button = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.code2lead.kwad:id/Login")))
    login_page_button.click()
    print("On the login page.\n")

    # --- 4. Find the Target Element and Calculate its Center ---
    print("Finding the 'LOGIN' button to tap...")
    login_button_locator = (AppiumBy.ID, "com.code2lead.kwad:id/Btn3")
    login_button = wait.until(EC.visibility_of_element_located(login_button_locator))

    # Get the location and size of the button
    location = login_button.location
    size = login_button.size

    # Calculate the center coordinates
    center_x = location['x'] + size['width'] / 2
    center_y = location['y'] + size['height'] / 2
    print(f"Calculated button center at (x={center_x}, y={center_y})\n")

    # --- 5. Perform the Tap Gesture ---
    print("Performing tap gesture on the button's center...")
    driver.tap([(center_x, center_y)])
    print("Tap gesture performed successfully.\n")

    # --- 6. Assert the Outcome ---
    print("Verifying that the tap resulted in an error message...")
    error_message = wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.code2lead.kwad:id/Tv8")))

    assert "Wrong Credentials" in error_message.text
    print("✅ Test Passed: The tap was successful and the error message appeared.")

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