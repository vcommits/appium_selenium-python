import time
from appium import webdriver
from appium.options.ios import XCUITestOptions # Import the correct iOS options class
# from appium.webdriver.common.appiumby import AppiumBy # Not needed for launch, but good to have for next steps

# This script is a modern version for launching a simple iOS app.

# --- 1. Setup Phase ---
print("Defining iOS capabilities...")
capabilities = {
    'platformName': 'iOS',
    'appium:automationName': 'XCUITest',
    # IMPORTANT: These must match your simulator in Xcode exactly
    'appium:platformVersion': '18.6',
    'appium:deviceName': 'iPhone 16e',
    # IMPORTANT: This path must point to the .app file that was built
    # specifically for a SIMULATOR, not a physical device.
    'appium:app': '/Users/Shawn/Library/Developer/Xcode/DerivedData/UICatalog-ghtojoxoetvchgdtznkfuvyhhopt/Build/Products/Debug-iphonesimulator/UICatalog.app'
}

# Convert the dictionary into the correct XCUITestOptions object
appium_options = XCUITestOptions().load_capabilities(capabilities)

driver = None  # Initialize driver
try:
    # --- 2. Action Phase ---
    print("Connecting to Appium server...")
    # Use the modern 'options=' argument
    driver = webdriver.Remote('http://127.0.0.1:4723', options=appium_options)
    print("Driver session started successfully. The UICatalog app should be running on your simulator.")

    # Pause to see the app before it closes
    time.sleep(10)

finally:
    # --- 3. Teardown Phase ---
    if driver:
        print("Closing session...")
        driver.quit()
        print("Driver session closed.")

