import time
from appium import webdriver
from appium.options.ios import XCUITestOptions

# This script is a modern version for getting various diagnostic properties from the Appium driver on iOS.

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
    print("Driver session started successfully.\n")

    # --- 3. Get and Print Driver Properties ---
    # These methods provide information about the current state of the automation session.
    print("--- Driver Properties ---")

    # .current_context: Returns the current context ('NATIVE_APP' or 'WEBVIEW_...').
    print(f"Current Context: {driver.current_context}")

    # .orientation: Returns the current device orientation ('PORTRAIT' or 'LANDSCAPE').
    print(f"Device Orientation: {driver.orientation}")

    # .is_locked(): Returns True if the device is locked, False otherwise.
    print(f"Is Device Locked: {driver.is_locked()}")

    print("-------------------------")

    print("\n✅ Test Passed: Successfully retrieved driver properties.")
    input("\nScript finished. Press Enter to quit...")

except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")

finally:
    # --- 4. Teardown Phase ---
    if driver:
        print("Closing session...")
        driver.quit()
        print("Driver session closed.")
