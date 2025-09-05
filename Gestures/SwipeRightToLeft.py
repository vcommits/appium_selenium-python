from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# This script demonstrates how to perform swipe gestures.

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
    wait = WebDriverWait(driver, 20)
    print("Driver session started successfully.\n")

    # --- 3. Navigate to the Swipeable Screen ---
    # The "VIEW PAGER" button leads to a screen with swipeable tabs.
    print("Scrolling to find the 'VIEW PAGER' button...")
    scroll_locator_string = 'new UiScrollable(new UiSelector()).scrollIntoView(text("VIEW PAGER"))'
    view_pager_button = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=scroll_locator_string)
    view_pager_button.click()
    print("Navigated to the View Pager screen.\n")

    # --- 4. Perform a Swipe Gesture (Right to Left) ---
    # We will swipe from the 'HOME' tab to the 'SPORT' tab.
    print("Finding the 'HOME' tab element to use as an anchor for the swipe...")
    home_tab_locator = (AppiumBy.XPATH, "//*[@text='HOME']")
    home_tab_element = wait.until(EC.visibility_of_element_located(home_tab_locator))

    # This is a modern Appium 2.x gesture command.
    # It's powerful because it's precise and works relative to an element.
    print("Performing a swipe from right to left...")
    driver.execute_script("mobile: swipeGesture", {
        'elementId': home_tab_element.id,
        'direction': 'left',
        'percent': 0.75  # The swipe speed and distance (0.0 to 1.0)
    })
    print("Swipe left performed.\n")
    time.sleep(2)  # Pause to visually see the result

    # --- 5. Perform a Swipe Gesture (Left to Right) ---
    # Now we will swipe back from the 'SPORT' tab to the 'HOME' tab.
    print("Finding the 'SPORT' tab element to use as an anchor for the swipe back...")
    sport_tab_locator = (AppiumBy.XPATH, "//*[@text='SPORT']")
    sport_tab_element = wait.until(EC.visibility_of_element_located(sport_tab_locator))

    print("Performing a swipe from left to right...")
    driver.execute_script("mobile: swipeGesture", {
        'elementId': sport_tab_element.id,
        'direction': 'right',
        'percent': 0.75
    })
    print("Swipe right performed.\n")
    time.sleep(2)  # Pause to visually see the result

    print("✅ Test Passed: Swipe gestures were performed successfully.")
    input("\nScript finished. Press Enter to quit...")

except TimeoutException:
    print("\n❌ Test Failed: A timeout occurred while waiting for an element.")
except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")

finally:
    # --- 6. Teardown Phase ---
    if driver:
        driver.quit()
        print("Driver session closed.")
