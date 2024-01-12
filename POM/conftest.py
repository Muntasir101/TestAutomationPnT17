import pytest
from selenium import webdriver
from POM.utils.config import login_url
from POM.utils.config import BROWSER


@pytest.fixture
def setup():
    if BROWSER == 'chrome':
        driver = webdriver.Chrome()
    elif BROWSER == 'firefox':
        driver = webdriver.Firefox()
    elif BROWSER == 'edge':
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser:" + BROWSER)

    driver.get(login_url)

    yield driver
    driver.quit()
