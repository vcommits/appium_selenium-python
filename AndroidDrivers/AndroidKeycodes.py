import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This script demonstrates using press_keycode to simulate hardware button presses.

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
    print("Driver session started.")

    # Navigate to the screen with the EditText field
    enter_value_button = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")))
    enter_value_button.click()

    # Find the text field and type into it
    text_field = wait.until(EC.visibility_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText")))
    text_to_send = "Hello from Appium!"
    text_field.send_keys(text_to_send)
    print(f"Typed '{text_to_send}' into the field.")
    time.sleep(2)

    # --- 3. Use press_keycode ---
    # Keycode 67 is for the 'DELETE' or 'Backspace' key.
    # We will press it twice to delete the last two characters ("m!").
    print("Pressing 'DELETE' key twice...")
    driver.press_keycode(67)
    driver.press_keycode(67)
    time.sleep(2)

    # Keycode 4 is for the physical 'BACK' button on an Android device.
    # Pressing it will take us back to the app's home screen.
    print("Pressing 'BACK' button...")
    driver.press_keycode(4)
    print("Navigated back to the home screen.")
    time.sleep(2)

    input("\nScript finished. Press Enter to quit...")

finally:
    # --- 4. Teardown Phase ---
    if driver:
        driver.quit()
        print("Driver session closed.")
