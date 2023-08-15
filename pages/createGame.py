from selenium.webdriver.common.by import By
from utilities.handleAlert import handle_alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random

from utilities.imageUploader import upload_images
from constants import constants


class Game:
    def __init__(self, driver, BASE_URL) -> None:
        self.driver = driver
        self.BASE_URL = BASE_URL

    def generate_random_number(self):
        return random.randint(1, 1000)

    def create_game(self):
        print('_______________________GAME_________________________')

        try:
            # Get site URL
            GAME_URL = self.BASE_URL + 'game-management'

            self.driver.get(GAME_URL)

        except Exception as e:
            print(f"Cannot visit game url, {e}")

        random_number = str(self.generate_random_number())

        # Click on Add New button
        add_new_button = self.driver.find_element(By.CLASS_NAME, "main-pg-btn")
        add_new_button.click()

        # Game Name
        game_name = self.driver.find_element(By.ID, "name")
        game_name.clear()
        game_name.send_keys(constants.game_name)

        # Game Code
        game_code = self.driver.find_element(By.ID, "slug")
        game_code_format = "sel" + random_number
        game_code.clear()
        game_code.send_keys(game_code_format)

        # Game Position
        game_position = self.driver.find_element(
            By.CLASS_NAME, "number-position")
        game_position.clear()
        game_position.send_keys(random_number)

        # Game Detail
        game_detail = self.driver.find_element(By.NAME, "detail")
        game_detail.clear()
        game_detail_format = f"This is game detail of {constants.game_name}. This is automatically generated game for selenium"
        game_detail.send_keys(game_detail_format)

        # Game Banner Image
        game_banner_image = self.driver.find_element(By.NAME, "bannerImage")
        folder_path = 'assets/game'
        image_names = ['game_image.jpg']
        upload_images(folder_path, image_names, game_banner_image)

        # Save Game
        save_button = self.driver.find_element(By.CLASS_NAME, "submit")
        self.driver.execute_script("arguments[0].click();", save_button)

        # Get Season ID
        manage_season_xpath = f"//td[contains(text(), {game_code_format})]/following-sibling::td//a[contains(@class, 'btn-primary')]"
        manage_season_button = self.driver.find_element(
            By.XPATH, manage_season_xpath)
        season_url = manage_season_button.get_attribute("href")
        season_id = season_url.split("/")[-1]
        print("Season Id is", season_id)

        return season_id
