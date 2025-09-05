from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from docutils.nodes import description

# This script demonstrates finding an element by its text using the
# modern Android UIAutomator strategy.

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

    # Find the element by its visible text using the concise UIAutomator syntax.
    print("Finding the element with text 'ENTER SOME VALUE'...")
    locator_string = 'text("ENTER SOME VALUE")'
    element_by_text = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=description("Btn3"))

    element_by_text.click()
    print("Successfully clicked the element.")

    input("App is running. Press Enter to quit...")

finally:
    # --- 3. Teardown Phase ---
    if driver:
        driver.quit()
        print("Driver session closed.")