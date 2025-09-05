from appium import webdriver
import time

'platformName': 'Android',
    'appium:automationName': 'UIAutomator2',
    'appium:platformVersion': '16', # Fixed typo: 'platformVersion'
    'appium:deviceName': 'Pixel 9 Pro API 36',
    # Use forward slashes for file paths to avoid errors
    'appium:app': 'C:/Users/vmoor/OneDrive/Desktop/Android_Demo_App.apk',
    'appium:appPackage': 'com.code2lead.kwad',
    'appium:appActivity': 'com.code2lead.kwad.MainActivity'

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '16'
desired_caps['deviceName'] = 'Pixel 9 Pro API 36'
desired_caps['app'] = ('C:/Users/vmoor/OneDrive/Desktop/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(5)

driver.quit()