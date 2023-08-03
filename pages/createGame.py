from selenium.webdriver.common.by import By
from utilities.handleAlert import handle_alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random
import os


class Game:
    def __init__(self, driver, name_of_game, env) -> None:
        self.driver = driver
        self.name_of_game = name_of_game
        self.env = env

    def generate_random_number(self):
        return random.randint(1, 1000)

    @staticmethod
    def upload_images(folder_path, image_names, element):

        # Example of fiel_path and images_name
        # folder_path = 'assets/season'
        # image_names = ['image1.jpg', 'image2.jpg', 'image3.jpg']

        # folder_path = 'assets/season'

        # Create full file paths for each image in the list
        image_paths = [os.path.abspath(os.path.join(
            folder_path, image_name)) for image_name in image_names]

        # Send each file path to the file input element one by one
        for image_path in image_paths:
            element.send_keys(image_path)

    def create_game(self):
        print('_______________________GAME_________________________')
        # Get site URL
        uat_URL = 'https://uat-cms.doko-quiz.ekbana.net/game-management'
        dev_URL = 'https://cms.doko-quiz.ekbana.net/game-management'

        if self.env == 0:
            game_URL = dev_URL
        else:
            game_URL = uat_URL

        self.driver.get(game_URL)

        # Click on Add New button
        add_new_button = self.driver.find_element(By.CLASS_NAME, "main-pg-btn")
        add_new_button.click()

        # Get elements
        game_name = self.driver.find_element(By.ID, "name")
        game_code = self.driver.find_element(By.ID, "slug")
        game_position = self.driver.find_element(
            By.CLASS_NAME, "number-position")
        game_detail = self.driver.find_element(By.NAME, "detail")
        game_banner_image = self.driver.find_element(By.NAME, "bannerImage")

        # Fill game details
        game_name.clear()
        game_name.send_keys(self.name_of_game)

        random_number = str(self.generate_random_number())
        game_code_format = "sel" + random_number
        game_code.clear()
        game_code.send_keys(game_code_format)

        game_position.clear()
        game_position.send_keys(random_number)

        game_detail.clear()
        game_detail_format = f"This is game detail of {self.name_of_game}. This is automatically generated game for selenium"
        game_detail.send_keys(game_detail_format)

        # Upload episode image
        folder_path = 'assets/game'
        image_names = ['game_image.jpg']
        Game.upload_images(folder_path, image_names, game_banner_image)

        # Save
        save_button = self.driver.find_element(By.CLASS_NAME, "submit")
        self.driver.execute_script("arguments[0].click();", save_button)

        manage_season_xpath = f"//td[contains(text(), {game_code_format})]/following-sibling::td//a[contains(@class, 'btn-primary')]"
        print("Manage Season Xpath", manage_season_xpath)
        manage_season_button = self.driver.find_element(
            By.XPATH, manage_season_xpath)
        season_url = manage_season_button.get_attribute("href")
        season_id = season_url.split("/")[-1]
        print("Season Id is", season_id)
        # self.driver.execute_script(
        #     "arguments[0].click();", manage_season_button)

        return season_id
