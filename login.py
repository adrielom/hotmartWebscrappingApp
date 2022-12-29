from selenium_helper import wait_for_element
from selenium.webdriver.common.by import By
import sys


def login():
    login_field = wait_for_element(By.CSS_SELECTOR, ".login-email")
    login_field.send_keys("")

    password_field = wait_for_element(By.CSS_SELECTOR, ".login-password")
    password_field.send_keys("")

    login_button = wait_for_element(By.CSS_SELECTOR, ".btn-login")
    login_button.click()


sys.modules[__name__] = login
