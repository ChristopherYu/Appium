from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def login(driver: webdriver, account):
    WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((AppiumBy.ID, "com.ivuu:id/btn_sign_in_google")))
    gmail_button = driver.find_element(AppiumBy.ID, "com.ivuu:id/btn_sign_in_google")
    gmail_button.click()
    WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText")))
    enter_text = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
    enter_text.set_text(account)
    sign_in_buttons = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")
    for button in sign_in_buttons:
        if button.text == "Next":
            button.click()