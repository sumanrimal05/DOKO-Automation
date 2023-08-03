from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder

import random
import time


class AssignQuestion:

    def __init__(self, driver, episode_id, number_of_question, env) -> None:
        self.driver = driver
        self.episode_id = episode_id
        self.number_of_question = number_of_question
        self.env = env

        self.wait = WebDriverWait(driver, 10)

    def handle_dropdown(self, dropdown_click_xpath):
        try:
            get_dropdown = self.driver.find_element(
                By.XPATH, dropdown_click_xpath)

            self.driver.execute_script(
                "arguments[0].click();", get_dropdown)

        except Exception as e:
            InterruptedError(e)

    def question_type(self, question_number):
        # wait = WebDriverWait(self.driver, 10)
        # time.sleep(.5)
        BASE_URL = f"//div[contains(@class,'theme-form mega-form')]/div[h4/text()=' Question {question_number}']/following-sibling::div[contains(@class,'mb-3')]//div[contains(@class,'multiselect question-type-{question_number}')]"
        question_type_xpath = f"{BASE_URL}//div[contains(@class,'multiselect__content-wrapper')]//li[@id='null-0']/span/span"
        dropdown_click_xpath = f"{BASE_URL}//div[contains(@class,'multiselect__select')]"

        # CLick the drop down
        self.handle_dropdown(dropdown_click_xpath)

        question_type_value = self.driver.find_element(
            By.XPATH, question_type_xpath)
        self.driver.execute_script(
            "arguments[0].click();", question_type_value)
        # question_type_value.click()

    def question_category(self, question_number):
        BASE_URL = f"//div[contains(@class,'theme-form mega-form')]/div[h4/text()=' Question {question_number}']/following-sibling::div[contains(@class,'mb-3')]//div[contains(@class,'multiselect category-{question_number}')]"
        dropdown_click_xpath = f"{BASE_URL}//div[contains(@class,'multiselect__select')]"
        all_item_xpath = f"{BASE_URL}//div[contains(@class,'multiselect__content-wrapper')]//li"

        # wait = WebDriverWait(self.driver, 10)

        self.handle_dropdown(dropdown_click_xpath)

        # Find all li elements
        li_elements = self.driver.find_elements(By.XPATH, all_item_xpath)

        # Initialize an empty list to store the matching li ids
        matching_li_ids = []

        # Loop through the li elements and check for the specified criteria
        for li in li_elements:
            # Check if the li contains a span tag with data-select="true"
            span_with_data_select = li.find_elements(
                By.XPATH, ".//span[@data-selected]")
            if span_with_data_select:
                # If the criteria is met, extract the number from the li id attribute and save it
                li_id = int(li.get_attribute('id').split('-')[1])
                matching_li_ids.append(li_id)

        # Randomly select one of the indices
        selected_index = random.choice(matching_li_ids)
        random_question_select_xpath = f"{BASE_URL}//div[contains(@class,'multiselect__content-wrapper')]//li[@id='null-{selected_index}']/span/span"

        question_category_value = self.driver.find_element(
            By.XPATH, random_question_select_xpath)

        self.driver.execute_script(
            "arguments[0].click();", question_category_value)
        # question_category_value.click()

    def question_difficulty(self, question_number):
        BASE_URL = f"//div[contains(@class,'theme-form mega-form')]/div[h4/text()=' Question {question_number}']/following-sibling::div[contains(@class,'mb-3')]//div[contains(@class,'multiselect difficulty-level-{question_number}')]"
        question_difficulty_xpath = f"{BASE_URL}//div[contains(@class,'multiselect__content-wrapper')]//li[@id='null-0']/span/span"
        dropdown_click_xpath = f"{BASE_URL}//div[contains(@class,'multiselect__select')]"

        # wait = WebDriverWait(self.driver, 10)
        self.handle_dropdown(dropdown_click_xpath)

        question_difficulty_value = self.driver.find_element(
            By.XPATH, question_difficulty_xpath)

        self.driver.execute_script(
            "arguments[0].click();", question_difficulty_value)
        # question_difficulty_value.click()

    def question_select(self, question_number):
        BASE_URL = f"//div[contains(@class,'theme-form mega-form')]/div[h4/text()=' Question {question_number}']/following-sibling::div[contains(@class,'mb-3')]//div[contains(@class,'multiselect question-{question_number}')]"
        question_select_xpath = f"{BASE_URL}//div[contains(@class,'multiselect__content-wrapper')]//li"

        # wait = WebDriverWait(self.driver, 10)

        # CLick the drop down
        dropdown_click_xpath = f"{BASE_URL}//div[contains(@class,'multiselect__select')]"
        self.handle_dropdown(dropdown_click_xpath)

        # Find all li elements
        li_elements = self.driver.find_elements(
            By.XPATH, question_select_xpath)

        # Initialize an empty list to store the matching li ids
        matching_li_ids = []

        # Loop through the li elements and check for the specified criteria
        for li in li_elements:
            # Check if the li contains a span tag with data-select="true"
            span_with_data_select = li.find_elements(
                By.XPATH, ".//span[@data-selected]")
            if span_with_data_select:
                # If the criteria is met, extract the number from the li id attribute and save it
                li_id = int(li.get_attribute('id').split('-')[1])
                matching_li_ids.append(li_id)

        # Randomly select one of the indices
        selected_index = random.choice(matching_li_ids)
        random_question_select_xpath = f"{BASE_URL}//div[contains(@class,'multiselect__content-wrapper')]//li[@id='null-{selected_index}']/span/span"

        question_select_value = self.driver.find_element(
            By.XPATH, random_question_select_xpath)

        self.driver.execute_script(
            "arguments[0].click();", question_select_value)
        # question_select_value.click()

    def question_timer(self, question_number, duration):
        # wait = WebDriverWait(self.driver, 10)
        question_timer_xpath = f"//div[contains(@class,'theme-form mega-form')]/div[h4/text()=' Question {question_number}']/following-sibling::div[contains(@class,'mb-3')]//input[contains(@class, 'question-timer-{question_number}')]"
        question_timer_element = self.driver.find_element(
            By.XPATH, question_timer_xpath)
        question_timer_element.clear()
        question_timer_element.send_keys(duration)

    def question_prize(self, question_number, prize):
        # wait = WebDriverWait(self.driver, 10)
        question_prize_xpath = f"//div[contains(@class,'theme-form mega-form')]/div[h4/text()=' Question {question_number}']/following-sibling::div[contains(@class,'mb-3')]//input[contains(@class, 'question-prize-{question_number}')]"
        question_prize_element = self.driver.find_element(
            By.XPATH, question_prize_xpath)
        question_prize_element.clear()
        question_prize_element.send_keys(prize)

    def assign_questions(self):
        print('_______________________ASSIGN QUESTION_________________________')
        # Validation check if user inputs more number of question than 15
        if (self.number_of_question < 2):
            self.number_of_question = 2
        if (self.number_of_question > 15):
            self.number_of_question = 15
        # Get site URL"
        dev_URL = f'https://cms.doko-quiz.ekbana.net/episode-question/set-question/{self.episode_id}'
        uat_URL = f'https://uat-cms.doko-quiz.ekbana.net/episode-question/set-question/{self.episode_id}'
        # manage_question_url = f'https://cms.doko-quiz.ekbana.net/episode-question/set-question/{self.episode_id}'

        if self.env == 0:
            manage_question_url = dev_URL
        else:
            manage_question_url = uat_URL

        self.driver.get(manage_question_url)
        prizes = [1000, 3000, 5000, 10000, 15000,
                  30000, 50000, 80000, 100000, 200000, 300000, 500000, 700000, 1000000, 5000000, 10000000]
        for question in range(1, self.number_of_question+1):
            # Select Question type for question 1
            print(f"Question is {question}")
            self.question_type(question_number=question)
            time.sleep(0.1)
            self.question_category(question_number=question)
            time.sleep(0.1)
            self.question_difficulty(question_number=question)
            time.sleep(0.5)
            self.question_select(question_number=question)
            # time.sleep(1)
            self.question_timer(question_number=question, duration=20)
            self.question_prize(question_number=question,
                                prize=prizes[question])
            time.sleep(0.1)

        # Save
        submit_button_xpath = "//button[text()='Save']"
        submit_button_element = self.driver.find_element(
            By.XPATH, submit_button_xpath)
        self.driver.execute_script(
            "arguments[0].click();", submit_button_element)
        # submit_button_element.click()

        # confirm
        confirm_button_xpath = "//button[text()='Confirm']"
        confirm_button_element = self.driver.find_element(
            By.XPATH, confirm_button_xpath)
        self.driver.execute_script(
            "arguments[0].click();", confirm_button_element)

        return 1
