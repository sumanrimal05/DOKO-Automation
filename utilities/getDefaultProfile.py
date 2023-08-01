from selenium.webdriver.common.by import By


def get_default_profile(driver):
    driver.get('edge://version')
    profile_path_element = driver.find_element(By.ID, "profile_path")
    profile_path = profile_path_element.text

    return profile_path
