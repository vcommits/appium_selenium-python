import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# Use AppiumOptions to set capabilities, which is the modern approach
capabilities = {
    'platformName': 'Android',
    'appium:automationName': 'UIAutomator2',
    'appium:platformVersion': '16', # Fixed typo: 'platformVersion'
    'appium:deviceName': 'Pixel 9 Pro API 36',
    # Use forward slashes for file paths to avoid errors
    'appium:app': 'C:/Users/vmoor/OneDrive/Desktop/Android_Demo_App.apk',
    'appium:appPackage': 'com.code2lead.kwad',
    'appium:appActivity': 'com.code2lead.kwad.MainActivity'
}

# Convert the dictionary to AppiumOptions
appium_options = UiAutomator2Options().load_capabilities(capabilities)

# The /wd/hub suffix is not needed for Appium 2.x
# Use 127.0.0.1 for the local server unless you have a specific reason
driver = webdriver.Remote('http://127.0.0.1:4723', options=appium_options)

# Add a short wait to ensure the app is fully loaded
time.sleep(5)

# Fixed method name: 'find_element' uses an underscore.  Find and validate Login button on test app
ele_id = assert driver.find_element(by=AppiumBy.ID, value="com.code2lead.kwad:id/Btn3").is_displayed()
login_visible = driver.find_element(by=AppiumBy.ID, value="com.code2lead.kwad:id/Btn3")
# Print value of asserted element (login)
print(login_visible)
# Target and click the Login Page button
ele_id = driver.find_element(by=AppiumBy.ID, value="com.code2lead.kwad:id/Login")
ele_id.click()
# Assert element clicked (login)
print("Element clicked successfully!")

# Account Creation Flow (username)
ele_id = driver.find_element(by=AppiumBy.ID, value="com.code2lead.kwad:id/Et4")
ele_id.send_keys("test@test.com")

# Account Creation Flow (pswd)
ele_id = driver.find_element(by=AppiumBy.ID, value="com.code2lead.kwad:id/Et5")
ele_id.send_keys("selenium")

# Click Login
ele_id = driver.find_element(by=AppiumBy.ID, value="com.code2lead.kwad:id/Btn3")
Wrong Credentials





# NEW: Add these lines to pause the script
print("App is running and paused. Press Enter in this terminal to quit the session.")
input() # The script will wait here until you press Enter


# It's a good practice to close the session
driver.quit()