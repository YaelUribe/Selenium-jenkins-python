import os
import pytest
from pages_web.development.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import util.web_utils_development as util
"""Chat module for tenant, locators and actions"""


class ChatTenant(BasePage):
    """locators and constants"""
    all_chats_tag = (By.XPATH, "//h2[contains(text(), 'All Chats')]")
    filter_by_dropdown = (By.XPATH, "//ng-select//div[@class= 'ng-value-container']")
    filter_options_open = (By.XPATH, "//ng-dropdown-panel/div/div[2]//span[contains(text(), 'Open')]")
    filter_options_closed = (By.XPATH, "//ng-dropdown-panel/div/div[2]//span[contains(text(), 'Closed')]")
    new_chat_options = (By.XPATH, "//mat-tab-body//button/span")
    new_chat_options_2 = (By.XPATH, "//mat-tab-body//button/span[@class= 'mr-2']")
    chat_text_area = (By.XPATH, "//textarea[@formcontrolname= 'comment']")
    chat_file_input = (By.XPATH, "//input[@formcontrolname='attachments']")
    send_message_btn = (By.XPATH, "//button/span[contains(text(), 'Send')]")
    chat_body = (By.XPATH, "//div[@infinitescroll]/div")
    last_open_chat = (By.XPATH, "//app-chat-conversations//a")
    last_closed_chat = (By.XPATH, "//app-chat-conversations//a//div[@class= 'blue-dot ng-star-inserted']")
    reopen_btn = (By.XPATH, "//button[contains(text(), 'Reopen Chat')]")
    rating_stars = (By.XPATH, "//div[@class='stars']/div")
    submit_btn = (By.XPATH, "//button[contains(text(), 'Submit')]")
    popup = (By.XPATH, "//div[contains(text(), 'Thank You!')]")
    events_promos = (By.XPATH, "//div[@class='event-list']")

    chat_text = "Test Test Test Test Test "
    chat_attachment = os.getcwd() + '/photo6.jpg'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(util.base_url)

    def go_to_chat_page(self):
        try:
            self.is_visible(util.home_icon)
        except TimeoutException:
            self.send_keys(util.email_locator, util.tenant_email)
            self.do_click(util.next_btn)
            time.sleep(0.8)
            self.send_keys(util.password_locator, util.tenant_password)
            self.do_click(util.next_btn)
            time.sleep(9)
        time.sleep(3)
        self.driver.get(util.tenant_chat_url)
        time.sleep(1)

    def filter_chats_open(self):
        self.do_click(self.filter_by_dropdown)
        time.sleep(0.5)
        self.click_random_option_web(self.filter_options_open)
        time.sleep(1)

    def filter_chats_closed(self):
        self.do_click(self.filter_by_dropdown)
        time.sleep(0.5)
        self.click_random_option_web(self.filter_options_closed)
        time.sleep(1)

    def start_new_chat(self):
        random = [self.new_chat_options, self.new_chat_options_2]
        for i in random:
            self.click_single_random_option_web(i)
            time.sleep(0.8)
        return self.is_visible(self.chat_text_area)

    def write_attach_send(self):
        try:
            start = self.messages_in_chat(self.chat_body)
        except TimeoutException:
            start = 0
        messages = [(self.chat_text_area, self.chat_text),
                    (self.chat_file_input, self.chat_attachment)]
        for x in messages:
            self.send_keys(x[0], x[1])
            time.sleep(1.5)
        time.sleep(1.8)
        self.do_click(self.send_message_btn)
        time.sleep(0.7)
        end = self.messages_in_chat(self.chat_body)
        time.sleep(1)
        return end >= start

    def open_existing(self):
        self.filter_chats_open()
        time.sleep(1)
        try:
            self.click_single_random_option_web(self.last_open_chat)
            time.sleep(0.5)
        except TimeoutException:
            pytest.skip("No open chats available")

    def reopen_closed(self):
        self.filter_chats_closed()
        time.sleep(1)
        try:
            self.click_single_random_option_web(self.last_closed_chat)
            time.sleep(0.5)
            self.scroll_to_location_web(self.reopen_btn)
            self.do_click(self.reopen_btn)
            time.sleep(0.5)
        except TimeoutException:
            pytest.skip("No closed chats available")

    def submit_rating(self):
        self.filter_chats_closed()
        time.sleep(0.5)
        try:
            self.click_single_random_option_web(self.last_closed_chat)
            time.sleep(0.5)
            try:
                self.scroll_to_location_web(self.rating_stars)
                self.click_single_random_option_web(self.rating_stars)
                time.sleep(0.5)
                self.do_click(self.submit_btn)
                time.sleep(0.5)
                return self.is_visible(self.popup)
            except TimeoutException:
                pytest.skip("Chat Rating not available")
        except TimeoutException:
            pytest.skip("No closed chats available")

    def upcoming_events_promos(self):
        try:
            return self.is_visible(self.events_promos)
        except TimeoutException:
            pytest.skip("No Events or Promotions available")
