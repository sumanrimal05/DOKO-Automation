from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def authenticate(driver, username, password, BASE_URL):
    # Get site URL
    driver.get(BASE_URL)

    try:
        # Set Username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys(username)

        # Set Password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        # Submit
        submit_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        submit_button.click()

    except NoSuchElementException:
        return True
