from appium import webdriver
from appium.options.android import UiAutomator2Options

# This script demonstrates a small set of Android Driver Methods
# that can be used to get diagnostic information about the App Under Test.

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
    print("Driver session started successfully.\n")

    # --- 3. Get and Print Driver Properties ---
    print("--- Driver Diagnostic Information ---")
    print(f"Is device locked? : {driver.is_locked()}")
    print(f"Device orientation: {driver.orientation}")
    print(f"Current package   : {driver.current_package}")
    print(f"Current activity  : {driver.current_activity}")

    # This shows the full set of capabilities the server is running with
    # print("Full session capabilities:", driver.capabilities)

    input("\nScript finished. Press Enter to quit...")

finally:
    # --- 4. Teardown Phase ---
    if driver:
        driver.quit()
        print("Driver session closed.")