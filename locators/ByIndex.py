from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# This script is a modern version of finding an element by its index.

# --- 1. Setup Phase ---
print("Defining capabilities...")
capabilities = {
    'platformName': 'Android',
    'appium:automationName': 'UiAutomator2',
    'appium:platformVersion': '16',
    'appium:deviceName': 'Pixel 9 Pro API 36',
    'appium:app': 'C:/Users/vmoor/OneDrive/Desktop/Android_Demo_App.apk',
    'appium:appPackage': 'com.code2lead.kwad',
    'appium:appActivity': 'com.code2lead.kwad.MainActivity'
}
appium_options = UiAutomator2Options().load_capabilities(capabilities)

driver = None  # Initialize driver
try:
    # --- 2. Action Phase ---
    print("Connecting to Appium server...")
    driver = webdriver.Remote('http://127.0.0.1:4723', options=appium_options)
    print("Driver session started.")

    # Find the element using the Android UIAutomator strategy, by its index.
    # This finds the 5th element on the screen (indexes start at 0).
    print("Finding the element at index 4...")
    element_by_index = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='UiSelector().index(4)')
    element_by_index.click()
    print("Successfully clicked the element at index 4.")

    input("App is running. Press Enter to quit...")

finally:
    # --- 3. Teardown Phase ---
    if driver:
        driver.quit()
        print("Driver session closed.")