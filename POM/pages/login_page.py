from POM.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # Define locators
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".orangehrm-login-button")

    # define login actions
    def login(self, username, password):
        self.input_text(*self.USERNAME_INPUT, username)
        self.input_text(*self.PASSWORD_INPUT, password)
        self.click_element(*self.LOGIN_BUTTON)
