from POM.pages.base_page import BasePage
from POM.utils.locators import LoginPageLocators


class LoginPage(BasePage):

    # define login actions
    def login(self, username, password):
        self.input_text(*LoginPageLocators.USERNAME_INPUT, username)
        self.input_text(*LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(*LoginPageLocators.LOGIN_BUTTON)
