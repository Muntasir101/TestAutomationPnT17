from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Define locators
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".orangehrm-login-button")


class RegistrationPageLocators:
    # Define locators
    FIRSTNAME_INPUT = (By.NAME, "firstname")

