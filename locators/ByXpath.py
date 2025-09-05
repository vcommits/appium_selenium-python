from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This script demonstrates finding elements using various XPath strategies.

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

    # --- Find and click the first element using XPath ---
    # The instructor demonstrated multiple ways to write an XPath for the same elements.
    # We will use the first one (by content-desc) to perform the action.

    # XPath by content-desc (the one we will use)
    xpath_con_desc = '//android.widget.Button[@content-desc="Btn1"]'
    # XPath by resource-id
    # xpath_res_id = '//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]'
    # XPath by text
    # xpath_text = '//android.widget.Button[@text="ENTER SOME VALUE"]'

    print(f"Finding and clicking element with XPath: {xpath_con_desc}")
    element_to_click = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_con_desc)))
    element_to_click.click()
    print("Element clicked successfully.")

    # --- Find and type into the second element ---
    # After the click, we are on a new screen. Now we find the EditText field.
    print("Finding the EditText field on the new screen...")
    edit_text_xpath = '//android.widget.EditText'
    text_field = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, edit_text_xpath)))

    text_to_send = "Skill2lead.com"
    print(f"Typing '{text_to_send}' into the field...")
    text_field.send_keys(text_to_send)
    print("Text sent successfully.")

    input("\nScript finished. Press Enter to quit...")

finally:
    # --- 3. Teardown Phase ---
    if driver:
        driver.quit()
        print("Driver session closed.")
