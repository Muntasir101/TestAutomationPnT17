import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.bbc.com")
time.sleep(5)
driver.quit()



"""
# launch Browser
dhaka = webdriver.Firefox()
driver2 = webdriver.Chrome()
# open url
dhaka.get("https://www.google.com")
driver2.get("https://www.apple.com")
dhaka.close()
driver2.close()
"""

