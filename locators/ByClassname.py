from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# This script demonstrates finding an element by its class name.

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

driver = None  # Initialize driver
try:
    # --- 2. Action Phase ---
    print("Connecting to Appium server...")
    driver = webdriver.Remote('http://127.0.0.1:4723', options=appium_options)
    print("Driver session started.")

    # First, navigate to the screen that has an EditText field
    enter_value_button = driver.find_element(by=AppiumBy.ID, value="com.code2lead.kwad:id/EnterValue")
    enter_value_button.click()
    print("Navigated to the 'Enter Value' screen.")

    # Now, find the element using its Class Name.
    # On this screen, there is only one 'android.widget.EditText', so this will work.
    print("Finding the element by class name 'android.widget.EditText'...")
    text_field = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")

    # A more realistic action for an EditText is to type in it.
    text_field.send_keys("Hello from Appium!")
    print("Successfully typed into the element found by class name.")

    input("App is running. Press Enter to quit...")

finally:
    # --- 3. Teardown Phase ---
    if driver:
        driver.quit()
        print("Driver session closed.")