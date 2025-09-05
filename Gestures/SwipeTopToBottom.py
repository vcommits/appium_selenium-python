from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# This script is a boilerplate example for vertical swipe gestures (scrolling).

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

    # --- 3. Navigate to the Scrollable Screen ---
    print("Navigating to the ScrollView screen...")
    # The 'ScrollView' button is visible on the main screen, so we can click it directly.
    scroll_view_button = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.code2lead.kwad:id/ScrollView")))
    scroll_view_button.click()
    print("Navigated to the ScrollView screen.\n")

    # --- 4. Get Screen Dimensions ---
    print("Getting device screen size...")
    device_size = driver.get_window_size()
    screen_width = device_size['width']
    screen_height = device_size['height']
    print(f"Screen dimensions: {screen_width} x {screen_height}\n")

    # --- 5. Calculate Coordinates for Vertical Swipes ---
    # For a vertical swipe, the X coordinate remains constant (e.g., the middle of the screen)
    x = screen_width // 2

    # Bottom to Top Swipe (Scroll Down)
    start_y_btt = screen_height * 0.8  # Start near the bottom
    end_y_btt = screen_height * 0.2  # End near the top

    # Top to Bottom Swipe (Scroll Up)
    start_y_ttb = screen_height * 0.2  # Start near the top
    end_y_ttb = screen_height * 0.8  # End near the bottom

    # --- 6. Perform the Swipes ---
    print("Performing a swipe from bottom to top (scrolling down)...")
    driver.swipe(x, start_y_btt, x, end_y_btt, 500)  # 500ms duration

    # Assert that a button near the bottom is now visible
    button12 = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, "//*[@text='BUTTON12']")))
    assert button12.is_displayed()
    print("Successfully scrolled down.\n")
    time.sleep(2)

    print("Performing a swipe from top to bottom (scrolling up)...")
    driver.swipe(x, start_y_ttb, x, end_y_ttb, 500)

    # Assert that a button near the top is visible again
    button1 = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, "//*[@text='BUTTON1']")))
    assert button1.is_displayed()
    print("Successfully scrolled up.")

    print("\n✅ Test Passed: Vertical swipe gestures were successful.")
    input("\nScript finished. Press Enter to quit...")

except TimeoutException:
    print("\n❌ Test Failed: A timeout occurred while waiting for an element.")
except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")

finally:
    # --- 7. Teardown Phase ---
    if driver:
        driver.quit()
        print("Driver session closed.")

