from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import math
import time


class Package:
    # minimum_number_of_episodes = 5
    season_episode_number = 0
    monthly_episode_number = 0
    weelkly_episode_number = 0
    daily_episode_number = 0

    payment_methods = ["Free Play", "Esewa"]

    def __init__(self, driver, season_id, number_of_episodes, BASE_URL) -> None:
        self.driver = driver
        self.season_id = season_id
        self.BASE_URL = BASE_URL

        if number_of_episodes < 5:
            self.number_of_episodes = 5
        else:
            self.number_of_episodes = number_of_episodes

    def calculate_package_number(self):
        self.season_episode_number = self.number_of_episodes
        self.monthly_episode_number = math.ceil(self.season_episode_number/2)
        self.weekly_episode_number = math.ceil(self.monthly_episode_number/2)
        self.daily_episode_number = 1

    def update_package_details(self, package_episodes, price, discount):
        # Get elements
        number_of_episodes = self.driver.find_element(By.NAME, "episodeNumber")
        package_price = self.driver.find_element(By.NAME, "price")
        discount_percentage = self.driver.find_element(
            By.NAME, "discountPercentage")
        payment_providers = self.driver.find_element(
            By.NAME, "paymentProviders")

        # Update details
        if (package_episodes == 1):
            pass
        else:
            number_of_episodes.clear()
            number_of_episodes.send_keys(package_episodes)

        package_price.clear()
        package_price.send_keys(price)

        discount_percentage.clear()
        discount_percentage.send_keys(discount)

        # Creating a select element
        select = Select(payment_providers)
        select.select_by_visible_text(self.payment_methods[0])
        select.select_by_visible_text(self.payment_methods[1])

    def update_season_package(self):
        price = 200
        discount = 10

        # Click on Edit Season Package
        package_edit_xpath = "//tbody/tr[1]//a"
        package_edit_button = self.driver.find_element(
            By.XPATH, package_edit_xpath)
        self.driver.execute_script(
            "arguments[0].click();", package_edit_button)
        # package_edit_button.click()

        # Update package details
        self.update_package_details(
            package_episodes=self.season_episode_number, price=price, discount=discount)

        # Save the result
        submit_button_xpath = "//button[text()='Save']"
        submit_button_element = self.driver.find_element(
            By.XPATH, submit_button_xpath)
        self.driver.execute_script(
            "arguments[0].click();", submit_button_element)

    def update_monthly_package(self):
        price = 75
        discount = 5

        # Click on Edit Season Package
        package_edit_xpath = "//tbody/tr[2]//a"
        package_edit_button = self.driver.find_element(
            By.XPATH, package_edit_xpath)
        self.driver.execute_script(
            "arguments[0].click();", package_edit_button)
        # package_edit_button.click()

        # Update package details
        self.update_package_details(
            package_episodes=self.monthly_episode_number, price=price, discount=discount)

        # Save the result
        submit_button_xpath = "//button[text()='Save']"
        submit_button_element = self.driver.find_element(
            By.XPATH, submit_button_xpath)
        self.driver.execute_script(
            "arguments[0].click();", submit_button_element)

    def update_weekly_package(self):
        price = 50
        discount = 00

        # Click on Edit Season Package
        package_edit_xpath = "//tbody/tr[3]//a"
        package_edit_button = self.driver.find_element(
            By.XPATH, package_edit_xpath)

        self.driver.execute_script(
            "arguments[0].click();", package_edit_button)
        # package_edit_button.click()

        # Update package details
        self.update_package_details(
            package_episodes=self.weekly_episode_number, price=price, discount=discount)

        # Save the result
        submit_button_xpath = "//button[text()='Save']"
        submit_button_element = self.driver.find_element(
            By.XPATH, submit_button_xpath)
        self.driver.execute_script(
            "arguments[0].click();", submit_button_element)

    def update_daily_package(self):
        price = 20
        discount = 0

        # Click on Edit Season Package
        package_edit_xpath = "//tbody/tr[4]//a"
        package_edit_button = self.driver.find_element(
            By.XPATH, package_edit_xpath)
        self.driver.execute_script(
            "arguments[0].click();", package_edit_button)
        # package_edit_button.click()

        # Update package details
        self.update_package_details(
            package_episodes=self.daily_episode_number, price=price, discount=discount)

        # Save the result
        submit_button_xpath = "//button[text()='Save']"
        submit_button_element = self.driver.find_element(
            By.XPATH, submit_button_xpath)
        self.driver.execute_script(
            "arguments[0].click();", submit_button_element)

    def publish_package(self, package_number):
        try:
            status_xpath = f"//table/tbody//tr[{package_number}]//select[@name = 'status']"
            select_status = self.driver.find_element(By.XPATH, status_xpath)
            select = Select(select_status)
            select.select_by_value('published')

            time.sleep(0.5)
            confirm_button = self.driver.find_element(
                By.XPATH, "//button[text()='Confirm']")
            confirm_button.click()
        except Exception as e:
            print("Already Published or Completed")

    def update_packages(self):
        time.sleep(0.5)

        print('_______________________PACKAGE_________________________')
        # Get site URL"
        PACKAGE_URL = self.BASE_URL + f'/package/{self.season_id}'

        self.driver.get(PACKAGE_URL)

        self.calculate_package_number()
        self.update_season_package()
        time.sleep(0.5)
        self.update_monthly_package()
        time.sleep(0.5)
        self.update_weekly_package()
        time.sleep(0.5)
        self.update_daily_package()
        time.sleep(0.5)

        # publish packages
        for package_number in range(1, 5):

            self.publish_package(package_number)
            time.sleep(0.5)
