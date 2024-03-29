import os
import time

from POM.pages.login_page import LoginPage
from POM.data.login_data import LoginTestData
import logging
from POM.utils.config import LOGGING_LEVEL, LOGGING_FORMAT, LOGGING_FILENAME
from POM.utils.excel_utils import *

# Implement Logging interface
logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_LEVEL)

# Create a file handler and set the logging level
file_handler = logging.FileHandler(LOGGING_FILENAME)
file_handler.setLevel(LOGGING_LEVEL)

# Create a formatter and add it to the file handler
formatter = logging.Formatter(LOGGING_FORMAT)
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


def test_login_valid(setup):
    login_page = LoginPage(setup)
    logger.info("Valid test login page")
    login_page.login(LoginTestData.VALID_USERNAME, LoginTestData.VALID_PASSWORD)
    logger.info("Valid login page completed successfully")
    login_page.driver.get_screenshot_as_file(os.path.join(os.getcwd(),'POM','Screenshots'+"\\Valid_login.png"))


def test_login_invalid(setup):
    login_page = LoginPage(setup)
    logger.info("InValid test login page")
    login_page.login(LoginTestData.INVALID_USERNAME, LoginTestData.INVALID_PASSWORD)
    logger.info("InValid login page completed successfully")
    time.sleep(3)
    login_page.driver.get_screenshot_as_file(os.path.join(os.getcwd(), 'POM', 'Screenshots' + "\\inValid_login.png"))