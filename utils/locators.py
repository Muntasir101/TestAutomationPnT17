from selenium.webdriver.common.by import By


class LoginPageLocators:
    username_field = (By.NAME, "username")
    password_field = (By.NAME, "password")
    login_button = (By.CSS_SELECTOR, ".orangehrm-login-button")
