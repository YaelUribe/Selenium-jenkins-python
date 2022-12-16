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

"""BasePage Class, methods and common utilities for all web modules """


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
        total_options = len(options)
        num = random.choice(range(total_options))
        if num == 0:
            num += 1
        for x in range(num):
            options[random.choice(range(total_options))].click()
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
        return "{}/{}/{}".format(date_input.month, date_input.day + 6, date_input.year)

    @staticmethod
    def date_calendar_2(ticket):
        if ticket == "new_m_ticket":
            date_input = datetime.now()
            return "{}/{}/{}".format(date_input.month, date_input.day + 5, date_input.year)
        elif ticket == "cancel_m_ticket":
            date_input = datetime.now()
            return "{}/{}/{}".format(date_input.month, date_input.day + 6, date_input.year)
        elif ticket == "new_m_chat_ticket":
            date_input = datetime.now()
            return "{}/{}/{}".format(date_input.month, date_input.day + 7, date_input.year)
        else:
            date_input = datetime.now()
            return "{}/{}/{}".format(date_input.month + 1, date_input.day, date_input.year)

    @staticmethod
    def reports_dates():
        date_input = datetime.now()
        if date_input.month == 1:
            start_date = "{}/{}/{}".format(date_input.month + 11, date_input.day, date_input.year - 1)
            end_date = "{}/{}/{}".format(date_input.month, date_input.day - 1, date_input.year)
            return (start_date, end_date)
        else:
            start_date = "{}/{}/{}".format(date_input.month - 1, date_input.day, date_input.year)
            end_date = "{}/{}/{}".format(date_input.month, date_input.day - 1, date_input.year)
            return (start_date, end_date)

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

    @staticmethod
    def date_picker(date, weekday, day_to):
        date_increasing = {"Tuesday": {"Monday": 1, "Tuesday": 7, "Wednesday": 6, "Thursday": 5,
                                       "Friday": 4, "Saturday": 3, "Sunday": 2},
                           "Wednesday": {"Monday": 2, "Tuesday": 1, "Wednesday": 7, "Thursday": 6,
                                         "Friday": 5, "Saturday": 4, "Sunday": 3},
                           "Thursday": {"Monday": 3, "Tuesday": 2, "Wednesday": 1, "Thursday": 7,
                                        "Friday": 6, "Saturday": 5, "Sunday": 4}
                           }
        if date.month in [1, 3, 5, 7, 8, 10, 12]:
            if (date.day + date_increasing[day_to][weekday]) > 31:
                if date.month == 12:
                    return "{}/{}/{}".format(date.month - 11, date.day + date_increasing[day_to][weekday] - 31,
                                             date.year + 1)
                else:
                    return "{}/{}/{}".format(date.month + 1, date.day + date_increasing[day_to][weekday] - 31,
                                             date.year)
            else:
                return "{}/{}/{}".format(date.month, date.day + date_increasing[day_to][weekday], date.year)
        elif date.month in [4, 6, 9, 11]:
            if (date.day + date_increasing[day_to][weekday]) > 30:
                return "{}/{}/{}".format(date.month + 1, date.day + date_increasing[day_to][weekday] - 30, date.year)
            else:
                return "{}/{}/{}".format(date.month, date.day + date_increasing[day_to][weekday], date.year)
        else:
            if (date.day + date_increasing[day_to][weekday]) > 28:
                return "{}/{}/{}".format(date.month + 1, date.day + date_increasing[day_to][weekday] - 28, date.year)
            else:
                return "{}/{}/{}".format(date.month, date.day + date_increasing[day_to][weekday], date.year)

    def tickets_calendar(self, ticket):
        if ticket == "new_m_ticket":  # Tuesdays
            date_input = datetime.now()
            weekday = date_input.strftime('%A')
            date_output = self.date_picker(date=date_input, weekday=weekday, day_to="Tuesday")
            return date_output
        elif ticket == "cancel_m_ticket":  # Wednesdays
            date_input = datetime.now()
            weekday = date_input.strftime('%A')
            date_output = self.date_picker(date=date_input, weekday=weekday, day_to="Wednesday")
            return date_output
        elif ticket == "new_m_chat_ticket":  # Thursdays
            date_input = datetime.now()
            weekday = date_input.strftime('%A')
            date_output = self.date_picker(date=date_input, weekday=weekday, day_to="Thursday")
            return date_output
        else:
            date_input = datetime.now()
            return "{}/{}/{}".format(date_input.month + 1, date_input.day, date_input.year)

    @staticmethod
    def date_incrementer(date_to_increase):
        date = datetime.strptime(date_to_increase, "%m/%d/%Y")
        if date.month in [1, 3, 5, 7, 8, 10, 12]:
            if (date.day + 7) > 31:
                if date.month == 12:
                    return "{}/{}/{}".format(date.month - 11, date.day + 7 - 31, date.year + 1)
                else:
                    return "{}/{}/{}".format(date.month + 1, date.day + 7 - 31, date.year)
            else:
                return "{}/{}/{}".format(date.month, date.day + 7, date.year)
        elif date.month in [4, 6, 9, 11]:
            if (date.day + 7) > 30:
                return "{}/{}/{}".format(date.month + 1, date.day + 7 - 30, date.year)
            else:
                return "{}/{}/{}".format(date.month, date.day + 7, date.year)
        else:
            if (date.day + 7) > 28:
                return "{}/{}/{}".format(date.month + 1, date.day + 7 - 28, date.year)
            else:
                return "{}/{}/{}".format(date.month, date.day + 7, date.year)
