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
    username_field_enable_state = username_field.is_enabled()

    if username_field_enable_state:
        username_field.clear()
        username_field.send_keys("Admin")
    else:
        print("Username field is not enabled.Test Failed.")

    # Step 4: Enter Password
    password_field = driver.find_element(By.NAME, "password")
    password_field_enable_state = password_field.is_enabled()

    if password_field_enable_state:
        password_field.clear()
        password_field.send_keys("admin123")
    else:
        print("Password field is not enabled.Test Failed")

    # Step 5: Click Login button
    login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
    login_button.click()
    time.sleep(5)

    # verify login or not
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    actual_url = driver.current_url

    if expected_url == actual_url:
        print("Test Passed. Login successful.")
    else:
        print("Test Failed. Login failed.")

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
    username_field_enable_state = username_field.is_enabled()

    if username_field_enable_state:
        username_field.clear()
        username_field.send_keys("Admin123")
    else:
        print("Username field is not enabled.Test Failed.")

    # Step 4: Enter Password
    password_field = driver.find_element(By.NAME, "password")
    password_field_enable_state = password_field.is_enabled()

    if password_field_enable_state:
        password_field.clear()
        password_field.send_keys("admin123")
    else:
        print("Password field is not enabled.Test Failed")

    # Step 5: Click Login button
    login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
    login_button.click()
    time.sleep(5)

    # verify login or not by check error message
    error_message = driver.find_element(By.CSS_SELECTOR, ".oxd-alert-content-text")
    actual_error_message_text = error_message.text

    expected_error_message = "Invalid credentials"

    if expected_error_message == actual_error_message_text:
        print("Test Passed. Login failed.Error message: " + expected_error_message)
    else:
        print("Test Failed. Did not get expected error message: " + expected_error_message)

    driver.close()


login_testCase1_valid()
login_testCase2_invalid()
