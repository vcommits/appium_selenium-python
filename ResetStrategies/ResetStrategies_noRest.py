import time
from appium import webdriver
from appium.options.android import UiAutomator2Options

# --- 1. Setup Phase ---
print("Defining capabilities with noReset strategy...")
capabilities = {
    'platformName': 'Android',
    'appium:automationName': 'UiAutomator2',
    'appium:platformVersion': '16',
    'appium:deviceName': 'Pixel 9 Pro API 36',
    'appium:app': 'C:/Users/vmoor/OneDrive/Desktop/Android_Demo_App.apk',
    # This is the key for a no reset. It keeps the app installed and preserves its data.
    'appium:noReset': True
}
appium_options = UiAutomator2Options().load_capabilities(capabilities)

driver = None  # Initialize driver
try:
    # --- 2. Action Phase ---
    print("Connecting to Appium server...")
    driver = webdriver.Remote('http://1227.0.0.1:4723', options=appium_options)
    print("Driver session started successfully. The app was launched without clearing data.")

    # Pause so you can see the app launched
    time.sleep(5)
    print("Test complete.")

finally:
    # --- 3. Teardown Phase ---
    if driver:
        print("Closing session.")
        driver.quit()
        print("Driver session closed.")