from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def set_episode_type(driver, season_episode_type):
    auto_episode_Xpath = "//ul[@id='select2-episode-type-results']/li[2]"
    manual_episode_Xpath = "//ul[@id='select2-episode-type-results']/li[3]"
    custom_auto_episode_Xpath = "//ul[@id='select2-episode-type-results']/li[4]"

    dropdown_span = driver.find_element(
        By.XPATH, "//span[@id='select2-episode-type-container']")

    # Click the <span> element to open the dropdown
    dropdown_span.click()
    option = ''
    text_value = ''

    if (season_episode_type == 'auto'):
        option = driver.find_element(
            By.XPATH, auto_episode_Xpath)
        text_value = option.text.lower()
        # return option, text_value

    elif (season_episode_type == 'manual'):
        option = driver.find_element(
            By.XPATH, manual_episode_Xpath)
        text_value = option.text.lower()

    elif (season_episode_type == 'custom-auto'):
        option = driver.find_element(
            By.XPATH, custom_auto_episode_Xpath)
        text_value = option.text.lower()

    return option, text_value
