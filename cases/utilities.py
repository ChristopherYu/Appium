from appium import webdriver
import json


def get_driver(project_directory, setting) -> webdriver:
    try:
        with open(f"{project_directory}/configs/appium_config.{setting['mobile_os'].lower()}.json") as json_file:
            appium_caps = json.load(json_file)
            appium_caps["app"] = setting['app_path']
        desired_caps = appium_caps

    except Exception as e:
        # set as default
        desired_caps = {'platformName': 'Android', 'platformVersion': '13.0', 'deviceName': 'emulator-5554',
                        'automationName': "UiAutomator2", 'autoGrantPermissions': True, 'appPackage': 'com.ivuu',
                        'appActivity': '.BrandingActivityCompat', 'noReset': True, 'app': setting['app_path']}
        print("Cannot found configs", e)

    driver = webdriver.Remote(setting['appium_server'], desired_caps)
    return driver
