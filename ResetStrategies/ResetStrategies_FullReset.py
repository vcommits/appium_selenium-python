import time
from appium import webdriver
from appium.options.android import UiAutomator2Options

# --- 1. Setup Phase ---
print("Defining capabilities with fullReset strategy...")
capabilities = {
    'platformName': 'Android',
    'appium:automationName': 'UiAutomator2',
    'appium:platformVersion': '16',
    'appium:deviceName': 'Pixel 9 Pro API 36',
    'appium:app': 'C:/Users/vmoor/OneDrive/Desktop/Android_Demo_App.apk',
    # This is the key for a full reset. It uninstalls and reinstalls the app.
    'appium:fullReset': True
}
appium_options = UiAutomator2Options().load_capabilities(capabilities)

driver = None  # Initialize driver
try:
    # --- 2. Action Phase ---
    print("Connecting to Appium server...")
    # Use the modern 'options=' argument and remove '/wd/hub'
    driver = webdriver.Remote('http://127.0.0.1:4723', options=appium_options)
    print("Driver session started successfully. The app was reinstalled.")

    # Pause so you can see that the app launched
    time.sleep(5)
    print("Test complete.")

finally:
    # --- 3. Teardown Phase ---
    if driver:
        print("Closing session.")
        driver.quit()
        print("Driver session closed.")