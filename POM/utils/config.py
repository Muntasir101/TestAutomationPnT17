import os

login_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

BROWSER = 'firefox'

import logging

# Logging configuration
LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGING_FILENAME = os.path.join(os.getcwd(), 'POM', 'Log', 'test.log')
