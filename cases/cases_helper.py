from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def sign_in(driver: webdriver, login_info: dict) -> str:
    WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((AppiumBy.ID, "com.ivuu:id/btn_sign_in_email")))
    gmail_button = driver.find_element(AppiumBy.ID, "com.ivuu:id/btn_sign_in_email")
    gmail_button.click()
    WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((AppiumBy.ID, "com.ivuu:id/edt_content")))
    email_account_text = driver.find_element(AppiumBy.ID, "com.ivuu:id/edt_content")
    email_account_text.set_text(login_info["account"])
    continue_button = driver.find_element(AppiumBy.ID, "com.ivuu:id/alfredButtonText")
    continue_button.click()
    WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((AppiumBy.ID, "com.ivuu:id/til_password")))
    pw_text = driver.find_element(AppiumBy.ID, "com.ivuu:id/til_password")
    pw_text.set_text(login_info["password"])
    confirm_pw_text = driver.find_element(AppiumBy.ID, "com.ivuu:id/til_confirm_password")
    confirm_pw_text.set_text(login_info["password"])
    return "expect_account_name"
    # Todo : after login success, find account info and return as string
