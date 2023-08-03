from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def authenticate(driver, username, password, env):
    uat_URL = "https://uat-cms.doko-quiz.ekbana.net/"
    dev_URL = "https://cms.doko-quiz.ekbana.net/"

    if env == 0:
        auth_URL = dev_URL
    else:
        auth_URL = uat_URL

    # Get site URL
    driver.get(auth_URL)

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
