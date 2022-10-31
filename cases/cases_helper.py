import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def sign_in(driver: webdriver, login_info: dict) -> str:
    # wait sign in button
    WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((AppiumBy.ID, "com.ivuu:id/btn_sign_in_email")))
    # click on sign in with email
    mail_button = driver.find_element(AppiumBy.ID, "com.ivuu:id/btn_sign_in_email")
    mail_button.click()
    # wait page redirect
    WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((AppiumBy.ID, "com.ivuu:id/edt_content")))
    # enter mail
    email_account_text = driver.find_element(AppiumBy.ID, "com.ivuu:id/edt_content")
    email_account_text.set_text(login_info["account"])
    # click continue button
    email_continue_button = driver.find_element(AppiumBy.ID, "com.ivuu:id/alfredButtonText")
    email_continue_button.click()
    # wait page redirect
    WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((AppiumBy.ID, "com.ivuu:id/til_password")))
    # enter pw and confirm pw
    pw_texts = driver.find_elements(AppiumBy.ID, "com.ivuu:id/edt_content")
    for pw_text in pw_texts:
        pw_text.set_text(login_info["password"])
    pw_continue_button = driver.find_element(AppiumBy.ID, "com.ivuu:id/btn_sign_in")
    pw_continue_button.click()
    # wait page redirect
    WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((AppiumBy.ID, "com.ivuu:id/edt_content")))
    # enter username
    user_name_text = driver.find_element(AppiumBy.ID, "com.ivuu:id/edt_content")
    user_name_text.set_text(login_info["username"])
    usr_continue_button = driver.find_element(AppiumBy.ID, "com.ivuu:id/btn_sign_in")
    usr_continue_button.click()
    # wait loading page disappear
    time.sleep(3 * 1000)
    # wait page redirect
    WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((AppiumBy.ID, "com.ivuu:id/txt_title")))
    verify_text = driver.find_element(AppiumBy.ID, "com.ivuu:id/txt_title")
    return verify_text.text
    # Todo : after login success, find account info and return as string
