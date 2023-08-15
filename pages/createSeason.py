import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from utilities.imageUploader import upload_images
from constants import constants


class Season:
    def __init__(self, driver, game_id, BASE_URL) -> None:
        self.driver = driver
        self.game_id = game_id
        self.BASE_URL = BASE_URL

    def generate_random_number(self):
        return random.randint(1, 1000)

    def select_random_ads(self, selector_element):
        try:
            select = Select(selector_element)
            all_options = select.options

            # Filter out disabled options
            non_disabled_options = [
                option for option in all_options if not option.is_enabled()]

            # Get the selected options
            selected_options = [
                option for option in all_options if option.is_selected()]

            # If the number of selected options is greater than or equal to the required number of ads,
            # deselect the extra selected options randomly to have exactly 'num_ads' selected ads
            while len(selected_options) >= constants.number_of_ads:
                option_to_deselect = random.choice(selected_options)
                select.deselect_by_visible_text(option_to_deselect.text)
                selected_options.remove(option_to_deselect)

            # Get the remaining options (options that are not selected and not disabled)
            remaining_options = [
                option for option in all_options if option not in selected_options and option not in non_disabled_options]

            # Randomly select additional ads to reach the required number of 'num_ads'
            ads_to_select = min(constants.number_of_ads - len(selected_options),
                                len(remaining_options))
            options_to_select = random.sample(remaining_options, ads_to_select)

            for option in options_to_select:
                select.select_by_visible_text(option.text)

        except Exception as e:
            print(f"Error whhile selecting ad, Error: {e} ")

    def fill_season_prizes(self):
        try:
            season_price_button = self.driver.find_element(
                By.ID, "season-prize")
            for index, item in enumerate(constants.season_prizes):
                prize_xpath = f"//div[@id ='seasonPrizesContainer']/input[{index + 1}]"

                # Fill Season prize
                season_prizes = self.driver.find_element(By.XPATH, prize_xpath)
                season_prizes.clear()
                season_prizes.send_keys(item)
                self.driver.execute_script(
                    "arguments[0].click();", season_price_button)

        except Exception as e:
            print("Failed to set season prizes, Error: {e}")

    def publish_season(self, season_number):
        try:
            status_xpath = f"//table/tbody//tr[{season_number}]//select[@name = 'status']"
            select_status = self.driver.find_element(By.XPATH, status_xpath)
            select = Select(select_status)
            select.select_by_value('published')

            time.sleep(0.5)
            confirm_button = self.driver.find_element(
                By.XPATH, "//button[text()='Confirm']")
            confirm_button.click()
        except Exception as e:
            print("Already Published or Completed")

    def create_single_season(self, season_number):
        print('_______________________SEASON_________________________')

        # Click on Add New button
        add_new_button = self.driver.find_element(By.CLASS_NAME, "main-pg-btn")
        add_new_button.click()

        # Fill Season Name
        season_name = self.driver.find_element(By.ID, "name")
        season_name.send_keys(constants.season_name + " " + str(season_number))

        # Fill Season Code
        season_code = self.driver.find_element(By.ID, "slug")
        random_number = str(self.generate_random_number())
        season_code_format = "sel" + random_number
        season_code.send_keys(season_code_format)

        # Fill Season position
        season_position = self.driver.find_element(
            By.CLASS_NAME, "number-position")
        season_position.send_keys(random_number)

        # Fill Season Detail
        season_detail = self.driver.find_element(By.NAME, "detail")
        season_detail_format = f"This is season detail of {constants.season_name}. This is automatically generated season by selenium"
        season_detail.send_keys(season_detail_format)

        # Select Season lifeline
        season_lifeline = self.driver.find_element(By.NAME, "lifeline")
        select = Select(season_lifeline)
        for index, lifeline in enumerate(constants.lifelines):
            select.select_by_visible_text(constants.lifelines[index])

        # Select Payment Provider
        payment_provider = self.driver.find_element(By.NAME, "paymentProvider")
        select = Select(payment_provider)
        for index, payment in enumerate(constants.payment_providers):
            select.select_by_visible_text(constants.payment_providers[index])

        # Set Season Winners
        total_number_of_season_winner = self.driver.find_element(
            By.NAME, "winnerNumber")
        total_number_of_season_winner.clear()
        total_number_of_season_winner.send_keys(
            constants.total_number_of_season_winner)

        # Total number of episode
        total_number_of_episode = self.driver.find_element(
            By.NAME, "episodeForSeasonWin")
        total_number_of_episode.clear()
        total_number_of_episode.send_keys(constants.total_number_of_episode)

        # Set Sponsor Title
        sponsor_title = self.driver.find_element(By.NAME, "sponsorTitle")
        sponsor_title.clear()
        sponsor_title.send_keys(constants.sponsor_title)

        # Set Season Ad
        season_ad = self.driver.find_element(By.NAME, "seasonAdvertisement")
        # Select random season ad
        self.select_random_ads(selector_element=season_ad)

        # Upload Powered by images
        powered_by_logos = self.driver.find_element(By.NAME, "poweredByLogo")
        folder_path = 'assets/season'
        image_names = ['poweredBy_1.jpg', 'poweredBy_2.jpg']
        upload_images(folder_path, image_names, powered_by_logos)

        # Upload season banner images
        season_banner_image = self.driver.find_element(By.NAME, "bannerImage")
        folder_path = 'assets/season'
        image_names = ['season_baner_image.jpg']
        upload_images(folder_path, image_names, season_banner_image)

        # Upload sponsor logo
        sponsor_logo = self.driver.find_element(By.NAME, "sponsorLogo")
        folder_path = 'assets/season'
        image_names = ['sponsor_logo.png']
        upload_images(folder_path, image_names, sponsor_logo)

        # Upload season banner ad images
        season_banner_ad = self.driver.find_element(By.NAME, "bannerAd")
        folder_path = 'assets/season'
        image_names = ['season_banner_ad.jpg']
        upload_images(folder_path, image_names, season_banner_ad)

        # Fill season prizes
        self.fill_season_prizes()

        # Save Season
        element = self.driver.find_element(By.CLASS_NAME, "submit")
        self.driver.execute_script("arguments[0].click();", element)

        manage_season_xpath = "//a[text()='Episodes']"
        manage_season_button = self.driver.find_element(
            By.XPATH, manage_season_xpath)
        season_url = manage_season_button.get_attribute("href")
        season_id = season_url.split("/")[-1]
        print("Season Id is", season_id)

        return season_id

    def check_if_season_present(self):
        tbody = self.driver.find_element(By.TAG_NAME, 'tbody')

        try:
            # Check the first element of the table
            self.driver.find_element(
                By.XPATH, "//table//tbody/tr//td[text() = 'No Records found.']")

            number_of_seasons = 0
            return number_of_seasons

        except Exception as e:
            tr_elements = tbody.find_elements(By.TAG_NAME, 'tr')
            number_of_seasons = len(tr_elements)

            return number_of_seasons

    def create_seasons(self):

        try:
            # Package is called here so every time you update episode_numbers, you also update packages
            time.sleep(0.5)
            # Get site URL
            SEASON_URL = self.BASE_URL + f'season/{self.game_id}'
            self.driver.get(SEASON_URL)

            # Check if there is episodes already on the seasons
            # And if there is add to it
            existing_season_number = self.check_if_season_present()
            print("Total season is", existing_season_number)

            if existing_season_number == 0:
                season_number = 1
            else:
                season_number = existing_season_number + 1

            season_id = self.create_single_season(season_number)

            return season_id

        except ValueError as e:
            print("Error", e)
            return 0
