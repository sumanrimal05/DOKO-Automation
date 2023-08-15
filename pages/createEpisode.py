from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import random
from datetime import datetime, timedelta

from utilities.setEpisodeType import set_episode_type
from utilities.handleAlert import handle_alert
from pages.createGame import Game
from pages.assignQuestion import AssignQuestion
from pages.createPackage import Package
from utilities.imageUploader import upload_images
import time


class Episode:
    episode_ids = []
    episode_numbers = []

    def __init__(self, driver, season_id, name_of_episode, season_episode_type, BASE_URL, game_host_name="", game_manager_name="") -> None:
        self.driver = driver
        self.season_id = season_id
        self.name_of_episode = name_of_episode
        self.season_episode_type = season_episode_type
        self.game_host_name = game_host_name
        self.game_manager_name = game_manager_name
        self.BASE_URL = BASE_URL

    def get_start_air_datetime(self, number_of_episodes, episode_date):
        future_date = episode_date + \
            timedelta(days=number_of_episodes - 1, hours=5)
        formatted_date = future_date.strftime("%m/%d/%Y")
        formatted_time = future_date.strftime("%I:%M %p")
        return formatted_date, formatted_time

    def get_last_datetime(self):
        pass

    def compare_current_last_episode_datetime(self, last_episode_date):
        episode_date = datetime.strptime(last_episode_date, "%Y-%m-%d")

        current_date = datetime.now()

        if episode_date > current_date:
            return episode_date

        else:
            return current_date

    def generate_random_number(self):
        return random.randint(1, 1000)

    def check_if_episode_present(self):
        tbody = self.driver.find_element(By.TAG_NAME, 'tbody')

        try:
            # Check the first element of the table
            self.driver.find_element(
                By.XPATH, "//table//tbody/tr//td[text() = 'No Records found.']")

            number_of_episodes = 0
            return number_of_episodes

        except Exception as e:
            tr_elements = tbody.find_elements(By.TAG_NAME, 'tr')
            number_of_episodes = len(tr_elements)

            return number_of_episodes

    def get_last_episode_airdate(self):
        episode_number = self.check_if_episode_present()
        if episode_number > 0:
            # last episode element
            last_episode_xpath = f"//tbody//tr[{episode_number}]//td[4]"
            last_episode = self.driver.find_element(
                By.XPATH, last_episode_xpath)
            last_air_date = last_episode.text
            return last_air_date
        else:
            return datetime.now()

 # Select a provided option based on option text or select any random value if it is not found
    def select_option_by_partial_text_or_random(self, dropdown_element, option_text):
        select = Select(dropdown_element)

    # Extract the first word before space and strip leading/trailing whitespaces
        target_text = option_text.split(' ')[0].strip()

        option_found = False
        for option in select.options:
            # Extract the first word of the option and strip leading/trailing whitespaces
            option_first_word = option.text.split(' ')[0].strip()
            if option_first_word == target_text:
                select.select_by_visible_text(option.text)
                option_found = True
                break

        if not option_found:
            random_index = random.randint(1, len(select.options) - 1)
            select.select_by_index(random_index)

    def create_single_episode(self, episode_number, episode_URL, episode_air_datetime):
        print('_______________________SINGLE Episode_________________________')

        # Click on Add New button
        add_new_button = self.driver.find_element(By.CLASS_NAME, "main-pg-btn")
        self.driver.execute_script(
            "arguments[0].click();", add_new_button)
        # add_new_button.click()

        # Set Episode Name
        episode_name = self.driver.find_element(By.ID, "name")
        episode_name.send_keys(self.name_of_episode +
                               " " + str(episode_number))
        # Set Episode Code
        episode_code = self.driver.find_element(By.ID, "slug")
        random_number = str(self.generate_random_number())
        episode_code_format = "sel" + random_number
        episode_code.send_keys(episode_code_format)

        # Set Episode Air Date time
        air_date = self.driver.find_element(By.ID, "start-date")
        air_time = self.driver.find_element(By.NAME, "airTime")
        episode_air_date, episode_air_time = self.get_start_air_datetime(
            number_of_episodes=episode_number, episode_date=episode_air_datetime)
        self.driver.execute_script(
            "arguments[0].value = arguments[1]", air_date, episode_air_date)
        self.driver.execute_script(
            "arguments[0].value = arguments[1]", air_time, episode_air_time)

        # Set Participant limit
        participant_limit = self.driver.find_element(
            By.NAME, "participantsLimit")
        participant_limit.send_keys(0)

        # Set Episode type
        episode_type_option, episode_type_text = set_episode_type(
            self.driver, self.season_episode_type)
        ActionChains(self.driver).move_to_element(
            episode_type_option).click().perform()

        if episode_type_text == "manual":
            # Choose game host
            game_host = self.driver.find_element(By.ID, "game-host")
            self.select_option_by_partial_text_or_random(
                dropdown_element=game_host, option_text=self.game_host_name)

            # Choose game manager
            game_manager = self.driver.find_element(By.ID, "game-manager")
            self.select_option_by_partial_text_or_random(
                dropdown_element=game_manager, option_text=self.game_manager_name)

        if episode_type_text == "custom-auto":
            # Set End Date time
            end_date = self.driver.find_element(By.ID, "end-date")

            end_time = self.driver.find_element(By.NAME, "endTime")
            # Choose game manager
            game_manager = self.driver.find_element(By.ID, "game-manager")
            self.select_option_by_partial_text_or_random(
                dropdown_element=game_manager, option_text=self.game_manager_name)

        # Set Episode Live URL
        episode_live_URL = self.driver.find_element(By.NAME, "liveURL")
        # episode_live_URL.clear()
        episode_live_URL.send_keys(episode_URL)

        # Set total number of winner
        winner_number = self.driver.find_element(By.NAME, "winnerNumber")
        winner_number.clear()
        winner_number.send_keys(5)

        # Upload episode image
        episode_image = self.driver.find_element(By.NAME, "image")
        folder_path = 'assets/episode'
        image_names = ['episode_image.jpg']
        upload_images(folder_path, image_names, episode_image)

        # Set Episode Detail
        episode__detail_format = f"This is episode detail of {self.name_of_episode}. This is automatically generated season by selenium"
        episode_detail = self.driver.find_element(
            By.XPATH, "//textarea[@name ='description']")
        episode_detail.send_keys(episode__detail_format)

        # Set Winner Criteria
        winner_criteria = self.driver.find_element(By.NAME, "winnerCriteria")
        winner_criteria.send_keys(5)

        # Save episode
        element = self.driver.find_element(By.CLASS_NAME, "submit")
        self.driver.execute_script("arguments[0].click();", element)

        manage_question_xpath = f"//table/tbody//tr[{episode_number}]//a[text()=' Manage Question']"
        manage_question_button = self.driver.find_element(
            By.XPATH, manage_question_xpath)
        episode_url = manage_question_button.get_attribute("href")
        episode_id = episode_url.split("/")[-1]
        print("Episode Id is", episode_id)
        # manage_episode_button.click()
        self.episode_ids.append(episode_id)
        return 1

    def publish_episode(self, episode_numbers, season_id):
        # Get site URL"
        EPISODE_URL = self.BASE_URL + f"episode/{season_id}"
        self.driver.get(EPISODE_URL)

        for episode_number in episode_numbers:
            try:
                status_xpath = f"//table/tbody//tr[{episode_number}]//select[@name = 'status']"
                select_status = self.driver.find_element(
                    By.XPATH, status_xpath)
                select = Select(select_status)
                select.select_by_value('published')

                time.sleep(0.5)
                confirm_button = self.driver.find_element(
                    By.XPATH, "//button[text()='Confirm']")
                confirm_button.click()
            except Exception as e:
                print("Already Published or Completed")

    def create_episodes(self, number_of_episodes, episode_live_URL):
        if number_of_episodes < 1:
            raise ValueError(
                "Episode number must be greater than or equal to 1")

        try:
            # Package is called here so every time you update episode_numbers, you also update packages
            time.sleep(0.5)
            # Get site URL"
            EPISODE_URL = self.BASE_URL + f"episode/{self.season_id}"
            self.driver.get(EPISODE_URL)

            # Check if there is episodes already on the seasons
            # And if there is add to it
            total_episode_number = self.check_if_episode_present()
            print("Total episode is", total_episode_number)
            # new_episode_number = number_of_episodes + total_episode_number

            episode_air_datetime = 0
            if total_episode_number == 0:
                episode_start_number = 1
                episode_air_datetime = datetime.now()
                print("Episode Type", type(episode_air_datetime))
                print("Episode time is", episode_air_datetime)

            else:
                episode_start_number = total_episode_number + 1
                last_episode_datetime = self.get_last_episode_airdate()
                episode_air_datetime = self.compare_current_last_episode_datetime(
                    last_episode_datetime)
                print("Episode Type", type(episode_air_datetime))
                print("Episode time is", episode_air_datetime)

            episode_end_number = episode_start_number + number_of_episodes

            print('_______________________MultiEPISODE_________________________')
            for episode_number in range(episode_start_number, episode_end_number):
                self.create_single_episode(
                    episode_number, episode_live_URL, episode_air_datetime)
                time.sleep(0.5)
                self.episode_numbers.append(episode_number)
            return self.episode_ids, self.episode_numbers

        except ValueError as e:
            print("Error", e)
            return 0, 0
