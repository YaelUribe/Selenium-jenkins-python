import os
import random
import pytest
from pages_web.staging.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import util.web_utils_staging as util
"""Chat module for Manager, locators and actions"""


class ChatManager(BasePage):
    """Locators and constants"""
    status_tag = (By.XPATH, "//label[contains(text(),'Status')]")
    status_filter = (By.XPATH, "//app-conversations-list//label[contains(text(),'Status')]")
    status_option = (By.XPATH, "//app-conversations-list//app-picker-menu/div/div")
    assigned_to_filter = (By.XPATH, "//ng-select[@formcontrolname='assignedManagerId']")
    assigned_option = (By.XPATH, "//div[@role='option']//span[contains(text(), 'Yael CE')]")
    chat_number_filter = (By.XPATH, "//input[@formcontrolname='id']")
    advance_filter = (By.XPATH, "//div[@class='cdk-overlay-pane']//input[@formcontrolname='query']")
    advance_my_filter = (By.XPATH, "//app-active-conversations//form/div[1]//input")
    status_my_filter = (By.XPATH, "//app-active-conversations//ng-select/div/div")
    create_btn = (By.XPATH, "//a[contains(text(), 'Create Chat')]")
    property_selector = (By.XPATH, "//ng-select[@formcontrolname= 'building_id']//input")
    property_options = (By.XPATH, "//ng-select//ng-dropdown-panel/div/div[2]/div")
    resident_selector = (By.XPATH, "//ng-select[@formcontrolname= '_tenant']//input")
    resident_options = (By.XPATH, "//ng-select//ng-dropdown-panel/div/div[2]/div")
    category_selector = (By.XPATH, "//ng-select[@formcontrolname= 'category_id']//div[@class= 'ng-value-container']")
    category_options = (By.XPATH, "//ng-select//ng-dropdown-panel/div/div[2]/div")
    subcategory_selector = (By.XPATH, "//ng-select[@formcontrolname= 'subcategory_id']//div[@class= 'ng-value-container']")
    subcategory_options = (By.XPATH, "//ng-select//ng-dropdown-panel/div/div[2]/div")
    create_chat_btn = (By.XPATH, "//a[contains(text(), 'Create Chat')]")
    create_chat_btn_2 = (By.XPATH, "//button[contains(text(), 'Create Chat')]")
    text_area_chat = (By.XPATH, "//app-conversation-chat//textarea")
    attachment_input = (By.XPATH, "//app-conversation-chat//input[@formcontrolname='attachments']")
    send_message_btn = (By.XPATH, "//app-conversation-chat//span[contains(text(), 'Send')]")
    chat_body = (By.XPATH, "//div[@infinitescroll]/div")
    first_my_chats = (By.XPATH, "//app-active-conversations//div[@infinitescroll]/a")
    text_area_notes = (By.XPATH, "//app-conversation-notes-widget//textarea")
    attachment_input_note = (By.XPATH, "//app-conversation-notes-widget//input[@formcontrolname='attachments']")
    send_note_btn = (By.XPATH, "//app-conversation-notes-widget//span[contains(text(), 'Send')]")
    notes_body = (By.XPATH, "//div[@class= 'dvora-manager-card']/div/div")
    category_list = (By.XPATH, "//ng-select[1]//div[@class= 'ng-value-container']")
    category_options_2 = (By.XPATH, "//ng-dropdown-panel//div[@role='option']")
    subcategory_list = (By.XPATH, "//ng-select[2]//div[@class= 'ng-value-container']")
    subcategory_options_2 = (By.XPATH, "//ng-dropdown-panel//div[@role='option']")
    update_categories_btn = (By.XPATH, "//button[contains(text(), 'Update Categories')]")
    ok_btn = (By.XPATH, "//button[contains(text(), 'Ok')]")
    add_participant_btn = (By.XPATH, "//button[contains(text(),'Add Participant')]")
    transfer_chat_btn = (By.XPATH, "//button[contains(text(),'Assign Chat')]")
    user_type = (By.XPATH, "//div[@class='control']//ng-select")
    user_manager = (By.XPATH, "//span[contains(text(), 'Manager')]")
    user_member = (By.XPATH, "//span[contains(text(), 'Member')]")
    member_building = (By.XPATH, "//ng-select[@formcontrolname='building_id']/div/div")
    member_building_options = (By.XPATH, "//ng-dropdown-panel//div[@role='option']")
    select_member = (By.XPATH, "//ng-select[@bindlabel='nameWithUnit']/div/div")
    select_member_options = (By.XPATH, "//ng-dropdown-panel//div[@role='option']")
    confirm_btn = (By.XPATH, "//button[contains(text(), 'Confirm')]")
    select_manager = (By.XPATH, "//div[@class='control']//ng-select[@bindlabel= 'full_name']")
    select_manager_options = (By.XPATH, "//ng-dropdown-panel//span[contains(text(), 'Mauricio Suaza')]")
    resolve_chat_btn = (By.XPATH, "//button[contains(text(), 'Resolve Chat')]")
    select_manager_transfer = (By.XPATH, "//ng-select[@bindlabel= 'full_name']/div/div")
    see_full_history_btn = (By.XPATH, "//a[contains(text(), 'See Full History')]")
    resident_details = (By.XPATH, "//app-member-detail/div/div")
    resident_filter = (By.XPATH, "//div[@class='tabs-selector']/div[1]/span[@class='mr-2']")
    resident_filter_tickets = (By.XPATH, "//div[@role='menu']/div/button[contains(text(), 'Tickets')]")
    resident_filter_reservations = (By.XPATH, "//div[@role='menu']/div/button[contains(text(), 'Reservations')]")
    resident_filter_bookings = (By.XPATH, "//div[@role='menu']/div/button[contains(text(), 'Bookings')][1]")
    resident_filter_event_bookings = (By.XPATH, "//div[@role='menu']/div/button[contains(text(), 'Event Bookings')]")
    resident_filter_announcements = (By.XPATH, "//div[@role='menu']/div/button[contains(text(), 'Announcements')]")
    resident_filter_notifications = (By.XPATH, "//div[@role='menu']/div/button[contains(text(), 'Notifications')]")
    resident_content_tickets = (By.XPATH, "//app-member-requests-widget//input")
    resident_content_reservations = (By.XPATH, "//app-member-spaces-widget//table")
    resident_content_bookings = (By.XPATH, "//app-member-services-widget//table")
    resident_content_event_bookings = (By.XPATH, "//app-member-events-widget//table")
    resident_content_announcements = (By.XPATH, "//app-member-announcements-widget//a")
    resident_content_notifications = (By.XPATH, "//app-member-messages-widget//div[@class='message-items']/div")
    first_chat = (By.XPATH, "//app-conversations-list//div[@infinitescroll]//a")
    start_chat_btn = (By.XPATH, "//button[contains(text(), 'Start Chat')]")
    filter_btn = (By.XPATH, "//app-conversations-list//button/mat-icon")
    category_filter = (By.XPATH, "//ng-select[@formcontrolname='category_id']")
    subcategory_filter = (By.XPATH, "//ng-select[@formcontrolname='subcategory_id']")
    filter_btn_2 = (By.XPATH, "//button[contains(text(), 'Filter')]")
    status_option_2 = (By.XPATH, "//app-active-conversations//app-picker-menu/div/div")

    message = "Test message Test message Test message Test message Test message Test message Test message"
    note = "Test Note Test Note Test Note Test Note Test Note Test Note Test Note Test Note Test Note Test Note "

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(util.base_url)

    def go_to_chat_page(self):
        try:
            self.is_visible(util.manager_home_icon)
        except TimeoutException:
            self.send_keys(util.email_locator, util.manager_email)
            self.do_click(util.next_btn)
            time.sleep(0.8)
            self.send_keys(util.password_locator, util.manager_password)
            self.do_click(util.next_btn)
            time.sleep(2)
        time.sleep(2)
        self.driver.get(util.manager_chat_url)
        time.sleep(3)

    def new_chat(self):
        clicks = [self.create_chat_btn, self.property_selector, self.resident_selector,
                  self.category_selector, self.subcategory_selector, self.create_chat_btn_2
                  ]
        for i in clicks:
            if i == self.property_selector:
                time.sleep(0.5)
                self.send_keys(i, "DVORA 175")
                time.sleep(1)
                self.press_enter_web()
                time.sleep(6.5)
            elif i == self.resident_selector:
                try:
                    time.sleep(0.5)
                    self.send_keys(i, "Ashley Rathappillil")
                    time.sleep(3)
                    self.press_enter_web()
                    time.sleep(0.5)
                except TimeoutException:
                    pytest.skip("No residents found in this building")
            elif i == self.category_selector:
                self.do_click(i)
                time.sleep(0.5)
                self.click_single_random_option_web(self.category_options)
                time.sleep(0.5)
            elif i == self.subcategory_selector:
                self.do_click(i)
                time.sleep(0.5)
                self.click_single_random_option_web(self.subcategory_options)
                time.sleep(0.5)
            else:
                self.do_click(i)
                time.sleep(0.8)
        time.sleep(1)

    def new_message(self):
        try:
            start = self.messages_in_chat(self.chat_body)
        except TimeoutException:
            start = 0
        messages = [(self.text_area_chat, self.message), (self.attachment_input, os.getcwd() + '/photo6.jpg')]
        for i in messages:
            self.send_keys(i[0], i[1])
            time.sleep(1.5)
        time.sleep(1.8)
        self.do_click(self.send_message_btn)
        time.sleep(0.8)
        end = self.messages_in_chat(self.chat_body)
        return end >= start

    def open_existing_chat(self):
        time.sleep(2)
        try:
            self.do_click(self.first_my_chats)
            time.sleep(0.8)
        except TimeoutException:
            pytest.skip("No active conversation available")

    def send_note(self):
        note = [(self.text_area_notes, self.note), (self.attachment_input_note, os.getcwd() + '/photo6.jpg')]
        try:
            start = self.messages_in_chat(self.notes_body)
        except TimeoutException:
            start = 0
        for n in note:
            self.send_keys(n[0], n[1])
            time.sleep(1.8)
        self.do_click(self.send_note_btn)
        time.sleep(0.7)
        end = self.messages_in_chat(self.notes_body)
        return end >= start

    def update_category(self):
        time.sleep(0.8)
        clicks = [(self.category_list, self.category_options_2),
                  (self.subcategory_list, self.subcategory_options_2)]
        for click in clicks:
            self.do_click(click[0])
            time.sleep(0.7)
            self.click_single_random_option_web(click[1])
            time.sleep(0.7)
        self.do_click(self.update_categories_btn)
        time.sleep(2)
        return self.is_visible(self.ok_btn)

    def add_manager(self):
        self.do_click(self.add_participant_btn)
        time.sleep(0.5)
        clicks = [(self.user_type, self.user_manager), (self.select_manager, self.select_manager_options)]
        for click in clicks:
            self.do_click(click[0])
            time.sleep(0.7)
            self.do_click(click[1])
            time.sleep(0.7)
        self.do_click(self.confirm_btn)
        return self.is_visible(self.ok_btn)

    def add_resident(self):
        self.do_click(self.add_participant_btn)
        time.sleep(0.5)
        clicks = [(self.member_building, self.member_building_options),
                  (self.select_member, self.select_member_options)]
        for click in clicks:
            if click[0] is self.user_type:
                self.do_click(click[0])
                time.sleep(0.7)
                try:
                    self.do_click(click[1])
                    time.sleep(0.7)
                except TimeoutException:
                    self.press_enter_web()
                    time.sleep(0.8)
            else:
                self.do_click(click[0])
                time.sleep(1)
                self.click_single_random_option_web(click[1])
                time.sleep(4)
        self.do_click(self.confirm_btn)
        return self.is_visible(self.ok_btn)

    def resolve_chat(self):
        time.sleep(0.8)
        self.do_click(self.resolve_chat_btn)
        time.sleep(0.8)
        self.do_click(self.confirm_btn)
        time.sleep(0.8)
        return self.is_visible(self.status_filter)

    def transfer_chat(self):
        clicks = [self.transfer_chat_btn, self.select_manager_transfer,
                  self.select_manager_options, self.confirm_btn]
        for y in clicks:
            if y == self.select_manager_options:
                self.scroll_to_location_web(y)
                self.do_click(y)
                time.sleep(1.2)
            else:
                self.do_click(y)
                time.sleep(1.2)
        time.sleep(0.5)

    def see_full_history(self):
        self.scroll_to_location_web(self.see_full_history_btn)
        time.sleep(0.5)
        self.do_click(self.see_full_history_btn)
        time.sleep(0.8)
        return self.is_visible(self.resident_details)

    def look_for_resident_tickets(self):
        time.sleep(0.8)
        clicks = [self.resident_filter, self.resident_filter_tickets]
        for x in clicks:
            self.scroll_to_location_web(x)
            time.sleep(0.5)
            self.do_click(x)
            time.sleep(0.8)
        try:
            return self.is_visible(self.resident_content_tickets)
        except TimeoutException:
            pytest.skip("No tickets available for this resident")

    def look_for_resident_reservations(self):
        time.sleep(0.8)
        clicks = [self.resident_filter, self.resident_filter_reservations]
        for x in clicks:
            self.scroll_to_location_web(x)
            time.sleep(0.5)
            self.do_click(x)
            time.sleep(2)
        try:
            return self.is_visible(self.resident_content_reservations)
        except TimeoutException:
            pytest.skip("No reservations available for this resident")

    def look_for_resident_bookings(self):
        time.sleep(0.8)
        clicks = [self.resident_filter, self.resident_filter_bookings]
        for x in clicks:
            self.scroll_to_location_web(x)
            time.sleep(0.5)
            self.do_click(x)
            time.sleep(2)
        try:
            return self.is_visible(self.resident_content_bookings)
        except TimeoutException:
            pytest.skip("No bookings available for this resident")

    def look_for_resident_event_bookings(self):
        time.sleep(0.8)
        clicks = [self.resident_filter, self.resident_filter_event_bookings]
        for x in clicks:
            self.scroll_to_location_web(x)
            time.sleep(0.5)
            self.do_click(x)
            time.sleep(0.8)
        try:
            return self.is_visible(self.resident_content_event_bookings)
        except TimeoutException:
            pytest.skip("No event bookings available for this resident")

    def look_for_resident_announcements(self):
        time.sleep(0.8)
        clicks = [self.resident_filter, self.resident_filter_announcements]
        for x in clicks:
            self.scroll_to_location_web(x)
            time.sleep(0.5)
            self.do_click(x)
            time.sleep(0.8)
        try:
            return self.is_visible(self.resident_content_announcements)
        except TimeoutException:
            pytest.skip("No announcements available for this resident")

    def look_for_resident_notifications(self):
        time.sleep(0.8)
        clicks = [self.resident_filter, self.resident_filter_notifications]
        for x in clicks:
            self.scroll_to_location_web(x)
            time.sleep(0.5)
            self.do_click(x)
            time.sleep(0.8)
        try:
            return self.is_visible(self.resident_content_notifications)
        except TimeoutException:
            pytest.skip("No notifications available for this resident")

    def filter_by_status(self):
        time.sleep(2)
        self.click_single_random_option_web(self.status_option)
        time.sleep(0.8)
        try:
            return self.is_visible(self.first_chat)
        except TimeoutException:
            pytest.skip("No Conversations registered")

    def filter_by_assigned_to(self):
        time.sleep(2)
        self.do_click(self.filter_btn)
        time.sleep(0.8)
        self.do_click(self.assigned_to_filter)
        time.sleep(0.8)
        self.click_single_random_option_web(self.assigned_option)
        time.sleep(0.8)
        self.do_click(self.filter_btn_2)
        time.sleep(0.8)
        try:
            return self.is_visible(self.first_chat)
        except TimeoutException:
            pytest.skip("No Conversations registered")

    def filter_by_chat_id(self):
        time.sleep(2)
        self.do_click(self.filter_btn)
        time.sleep(0.8)
        self.send_keys(self.chat_number_filter, "635")
        time.sleep(1)
        self.do_click(self.filter_btn_2)
        time.sleep(0.8)
        try:
            return self.is_visible(self.first_chat)
        except TimeoutException:
            pytest.skip("No Conversations registered")

    def filter_by_advanced(self):
        time.sleep(2)
        self.do_click(self.filter_btn)
        time.sleep(0.8)
        self.send_keys(self.advance_filter, "Rathappillil")
        self.press_enter_web()
        time.sleep(1)
        try:
            return self.is_visible(self.first_chat)
        except TimeoutException:
            pytest.skip("No Conversations registered")

    def filter_by_own_status(self):
        time.sleep(2)
        self.click_single_random_option_web(self.status_option_2)
        time.sleep(2)
        try:
            return self.is_visible(self.first_my_chats)
        except TimeoutException:
            pytest.skip("No Conversations registered")

    def filter_by_own_advanced(self):
        time.sleep(0.8)
        self.send_keys(self.advance_my_filter, "Rathappillil")
        self.press_enter_web()
        time.sleep(1)
        try:
            return self.is_visible(self.first_my_chats)
        except TimeoutException:
            pytest.skip("No Conversations registered")
