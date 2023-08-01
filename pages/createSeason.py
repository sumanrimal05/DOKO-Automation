import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from pages.createGame import Game


class Season:
    season_ids = []
    payment_providers = ["Free Play", "Esewa"]
    lifelines = ["50/50", "Audience Poll", "Skip Question"]
    total_number_of_season_winner = 5
    total_number_of_episode = 7
    sponsor_title = "Test Season"
    season_prizes = ["1 Lucky winner will win Samsung Galaxy S23",
                     "5 Lucky winner will win Samsung Galaxy A30s",
                     "10 Lucky winner will win Samsung Gift Hampers",
                     "50 Lucky winner will win RS 100  Recharge Cards",
                     "100 Lucky winner will win RS 50  Recharge Cards"]

    def __init__(self, driver, game_id, name_of_season) -> None:
        self.driver = driver
        self.game_id = game_id
        self.name_of_season = name_of_season

    def generate_random_number(self):
        return random.randint(1, 1000)

    def select_random_ads(self, selector_element, num_ads=3):
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
        while len(selected_options) >= num_ads:
            option_to_deselect = random.choice(selected_options)
            select.deselect_by_visible_text(option_to_deselect.text)
            selected_options.remove(option_to_deselect)

        # Get the remaining options (options that are not selected and not disabled)
        remaining_options = [
            option for option in all_options if option not in selected_options and option not in non_disabled_options]

        # Randomly select additional ads to reach the required number of 'num_ads'
        ads_to_select = min(num_ads - len(selected_options),
                            len(remaining_options))
        options_to_select = random.sample(remaining_options, ads_to_select)

        for option in options_to_select:
            select.select_by_visible_text(option.text)

    def fill_season_prizes(self):
        season_price_button = self.driver.find_element(By.ID, "season-prize")
        for index, item in enumerate(self.season_prizes):
            prize_xpath = f"//div[@id ='seasonPrizesContainer']/input[{index + 1}]"

            # Get season element
            season_prizes = self.driver.find_element(By.XPATH, prize_xpath)

            # Fill season element
            season_prizes.clear()
            season_prizes.send_keys(item)
            self.driver.execute_script(
                "arguments[0].click();", season_price_button)

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

        # Get elements
        season_name = self.driver.find_element(By.ID, "name")
        season_code = self.driver.find_element(By.ID, "slug")
        season_position = self.driver.find_element(
            By.CLASS_NAME, "number-position")
        season_detail = self.driver.find_element(By.NAME, "detail")
        season_lifeline = self.driver.find_element(By.NAME, "lifeline")
        payment_provider = self.driver.find_element(By.NAME, "paymentProvider")
        season_winners = self.driver.find_element(By.NAME, "winnerNumber")
        episode_winners = self.driver.find_element(
            By.NAME, "episodeForSeasonWin")
        sponsor_title = self.driver.find_element(By.NAME, "sponsorTitle")
        season_ad = self.driver.find_element(By.NAME, "seasonAdvertisement")
        powered_by_logos = self.driver.find_element(By.NAME, "poweredByLogo")
        season_banner_image = self.driver.find_element(By.NAME, "bannerImage")
        sponsor_logo = self.driver.find_element(By.NAME, "sponsorLogo")
        season_banner_ad = self.driver.find_element(By.NAME, "bannerAd")

        # Fill season details
        season_name.send_keys(self.name_of_season + " " + str(season_number))
        random_number = str(self.generate_random_number())
        season_code_format = "sel" + random_number
        season_code.send_keys(season_code_format)
        season_position.send_keys(random_number)
        season_detail_format = f"This is season detail of {self.name_of_season}. This is automatically generated season by selenium"
        season_detail.send_keys(season_detail_format)
        season_winners.clear()
        season_winners.send_keys(self.total_number_of_season_winner)
        episode_winners.clear()
        episode_winners.send_keys(self.total_number_of_episode)
        sponsor_title.clear()
        sponsor_title.send_keys(self.sponsor_title)

        # Selecting season lifelines
        select = Select(season_lifeline)
        select.select_by_visible_text(self.lifelines[0])
        select.select_by_visible_text(self.lifelines[1])
        select.select_by_visible_text(self.lifelines[2])

        # Upload powered by images
        folder_path = 'assets/season'
        image_names = ['season_baner_image.jpg']
        Game.upload_images(folder_path, image_names, season_banner_image)

        # Selecting season lifelines1
        select = Select(payment_provider)
        select.select_by_visible_text(self.payment_providers[0])
        select.select_by_visible_text(self.payment_providers[1])

        # Select random season ad
        self.select_random_ads(selector_element=season_ad, num_ads=3)

        # Upload powered by images
        folder_path = 'assets/season'
        image_names = ['sponsor_logo.png']
        Game.upload_images(folder_path, image_names, sponsor_logo)

        # Upload powered by images
        folder_path = 'assets/season'
        image_names = ['season_banner_ad.jpg']
        Game.upload_images(folder_path, image_names, season_banner_ad)

        # Upload powered by images
        folder_path = 'assets/season'
        image_names = ['poweredBy_1.jpg', 'poweredBy_2.jpg']
        Game.upload_images(folder_path, image_names, powered_by_logos)

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
        # manage_episode_button.click()

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
            game_url = f'https://cms.doko-quiz.ekbana.net/season/{self.game_id}'
            self.driver.get(game_url)

            # Check if there is episodes already on the seasons
            # And if there is add to it
            total_seasons = self.check_if_season_present()
            print("Total season is", total_seasons)

            episode_time = 0
            if total_seasons == 0:
                season_start = 1

            else:
                season_start = total_seasons + 1

            # season_end = season_start + number_of_seasons

            season_id = self.create_single_season(season_number=season_start)

            return season_id

        except ValueError as e:
            print("Error", e)
            return 0
