from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def authenticate(driver, username, password):
    # Get site URL
    driver.get('https://cms.doko-quiz.ekbana.net/')

    try:
        # Locate username and password fields
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")

        # Pass login cred
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit
        submit_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        submit_button.click()

    except NoSuchElementException:
        return True
