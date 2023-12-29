import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def login_testCase1_valid():
    # Step 1: Launch Browser
    driver = webdriver.Firefox()
    driver.maximize_window()

    # Step 2: Open URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)

    # Step 3: Enter Username
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("Admin")
    # Step 4: Enter Password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("admin123")
    # Step 5: Click Login button
    login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
    login_button.click()
    time.sleep(5)
    driver.close()


def login_testCase2_invalid():
    # Step 1: Launch Browser
    driver = webdriver.Firefox()
    driver.maximize_window()

    # Step 2: Open URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)

    # Step 3: Enter Username
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("Admin123")
    # Step 4: Enter Password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("admin122333")
    # Step 5: Click Login button
    login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
    login_button.click()
    time.sleep(5)
    driver.close()


login_testCase1_valid()
login_testCase2_invalid()
