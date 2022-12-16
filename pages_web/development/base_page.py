import random
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# import util.web as util

"""BasePage Class, methods and common utilities for all web pages """


class BasePage:
    """BasePage Class"""

    def __init__(self, driver):
        self.driver = driver

    def chrome_connection(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def go_to_address(self, base_url):
        self.driver.get(base_url)

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(by_locator)).click()

    def do_click_2(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def do_click_at_index(self, by_locator, index):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        element[index].click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).send_keys(text)

    def clear(self, locator):
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(locator)).clear()

    def get_text(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        return element.text

    def press_enter(self, locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator)).send_keys(Keys.ENTER)

    def get_title(self, title):
        WebDriverWait(self.driver, 5).until(EC.title_is(title))
        return self.driver.title

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(by_locator))
        return element

    def is_enabled(self, locator):
        pass

    def is_visible_fast(self, by_locator):
        element = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located(by_locator))
        return element

    def switches_on_off(self, by_locator, text="checked"):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).get_attribute(text)
        return element

    def scroll_to_location(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        element.location_once_scrolled_into_view

    def click_random_option(self, locator):
        options = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        num = random.choice(range(len(options)))
        options[num].location_once_scrolled_into_view
        options[num].click()
        time.sleep(0.5)

    def click_random_option_fast(self, locator):
        options = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        num = random.choice(range(len(options)))
        options[num].location_once_scrolled_into_view
        options[num].click()

    def drag_and_drop(self, by_locator1, by_locator2):
        start_element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(by_locator1))
        end_element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(by_locator2))
        action = ActionChains(self.driver)
        action.drag_and_drop(start_element, end_element).perform()


    def click_single_random_option_web(self, locator):
        options = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(locator))
        randint = random.choice(range(len(options)))
        options[randint].click()

    def click_random_option_web(self, locator):
        options = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(locator))
        num = random.choice(range(len(options)))
        if num == 0:
            num += 1
        for x in range(num):
            options[x].click()
            time.sleep(0.2)

    def press_escape(self):
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def scroll_to_location_web(self, by_locator):
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(false);", element)

    def scroll_to_bottom(self):
        webdriver.ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()

    def press_enter_web(self):
        webdriver.ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    @staticmethod
    def date_calendar():
        date_input = datetime.now()
        return "{}/{}/{}".format(date_input.month, date_input.day + 10, date_input.year)

    @staticmethod
    def date_calendar_2(ticket):
        if ticket == "new_m_ticket":
            date_input = datetime.now()
            return "{}/{}/{}".format(date_input.month, date_input.day + 8, date_input.year)
        elif ticket == "cancel_m_ticket":
            date_input = datetime.now()
            return "{}/{}/{}".format(date_input.month, date_input.day + 9, date_input.year)
        elif ticket == "new_m_chat_ticket":
            date_input = datetime.now()
            return "{}/{}/{}".format(date_input.month, date_input.day + 10, date_input.year)
        else:
            date_input = datetime.now()
            return "{}/{}/{}".format(date_input.month + 1, date_input.day, date_input.year)

    def checkbox_checker(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        return element.is_selected()

    @staticmethod
    def random_time_duration():
        hour = random.choice(range(1, 13))
        minutes = random.choice(range(10, 60, 5))
        if (hour >= 7) and (hour < 12):
            return "{}{}A".format(hour, minutes)
        else:
            return "{}{}P".format(hour, minutes)

    def messages_in_chat(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(locator))
        length = len(element)
        return length
