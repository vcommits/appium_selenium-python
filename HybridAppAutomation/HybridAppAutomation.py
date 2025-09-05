from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By  # IMPORTANT: Import By for web locators
import time

# This script demonstrates how to automate a hybrid app, switching between
# the NATIVE_APP context and the WEBVIEW context.
# In this example, we will automate the Chrome browser itself.

# --- 1. Setup Phase ---
print("Defining capabilities to launch the Chrome browser...")
capabilities = {
    'platformName': 'Android',
    'appium:automationName': 'UiAutomator2',
    'appium:platformVersion': '16',
    'appium:deviceName': 'Pixel 9 Pro API 36',
    # To automate a pre-installed app like Chrome, we use its package and activity
    'appium:appPackage': 'com.android.chrome',
    'appium:appActivity': 'com.google.android.apps.chrome.Main',
    # This is crucial for webview automation
    'appium:chromedriverExecutable': 'C:/path/to/your/chromedriver.exe'
}
# NOTE: You MUST provide the path to a chromedriver that matches the version of
# Chrome on your emulator. Download from: https://chromedriver.chromium.org/downloads
appium_options = UiAutomator2Options().load_capabilities(capabilities)

driver = None
try:
    # --- 2. Action Phase ---
    print("Connecting to Appium server...")
    driver = webdriver.Remote('http://127.0.0.1:4723', options=appium_options)
    wait = WebDriverWait(driver, 20)
    print("Driver session started successfully, Chrome is launched.\n")

    # --- 3. Initial Native App Interaction ---
    # These are native Android elements for Chrome's first-launch screen.
    print("Handling first-launch dialogs in NATIVE_APP context...")
    wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.android.chrome:id/terms_accept"))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.android.chrome:id/negative_button"))).click()

    # Navigate to a website
    url_bar = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.android.chrome:id/url_bar")))
    url_bar.send_keys("https://www.google.com")
    driver.press_keycode(66)  # Press the ENTER key
    print("Navigated to google.com.\n")
    time.sleep(5)  # Give the page time to load fully

    # --- 4. Switch to WebView Context ---
    print("Getting available contexts...")
    all_contexts = driver.contexts
    print(f"Available contexts: {all_contexts}")

    # Find the webview context and switch to it
    webview_context = None
    for context in all_contexts:
        if 'WEBVIEW' in context:
            webview_context = context
            break

    if webview_context:
        print(f"Switching to context: {webview_context}...")
        driver.switch_to.context(webview_context)
    else:
        raise Exception("WebView context not found.")

    # --- 5. Perform Actions in WebView Context ---
    # Now we are "inside" the webpage. We use WEB locators like By.XPATH or By.NAME.
    print("Performing search in WEBVIEW context...")
    # Note: We use By.NAME from Selenium, not AppiumBy
    search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
    search_box.send_keys("Skill2Lead")
    search_box.submit()
    print("Search performed successfully.\n")
    time.sleep(3)

    # --- 6. Switch Back to Native Context ---
    print("Switching back to NATIVE_APP context...")
    driver.switch_to.context("NATIVE_APP")

    # --- 7. Perform Final Actions in Native Context ---
    # Now we are back controlling the main app. We can interact with the URL bar again.
    print("Performing final action in NATIVE_APP context...")
    final_url_bar = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.android.chrome:id/search_box_text")))
    final_url_bar.click()  # This clears the search box text

    url_input = wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.android.chrome:id/url_bar")))
    url_input.send_keys("https://www.skill2lead.com")
    driver.press_keycode(66)
    print("Navigated to a new page.\n")

    print("✅ Test Passed: Hybrid automation workflow was successful.")
    input("\nScript finished. Press Enter to quit...")

except TimeoutException:
    print("\n❌ Test Failed: A timeout occurred while waiting for an element.")
except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")

finally:
    # --- 8. Teardown Phase ---
    if driver:
        driver.quit()
        print("Driver session closed.")
