import pytest
from selenium import webdriver
from POM.pages.login_page import LoginPage
from POM.pages.login_page import BasePage


@pytest.fixture
def setup():
    driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    yield driver
    driver.quit()


def test_login_valid(setup):
    login_page = LoginPage(setup)
    login_page.login("Admin", "admin123")


def test_login_invalid(setup):
    login_page = LoginPage(setup)
    login_page.login("Admin12", "admin1232333")
