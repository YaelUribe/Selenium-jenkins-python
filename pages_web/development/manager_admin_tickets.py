import os
import random
import pytest
from pages_web.development.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import util.web_utils_development as util
"""Administrative tickets module, locators and actions"""

class AdminTicketsManager(BasePage):
    """Locators and constants"""
    all_tickets_tag = (By.XPATH, "//h2[contains(text(), ' All Administrative Tickets')]")
    category_filter =(By.XPATH, "//app-manager-home-admin-ticket[1]//ng-select[@formcontrolname= 'category']")
    status_filter =(By.XPATH, "//app-manager-home-admin-ticket[1]//ng-select[@formcontrolname= 'status']")
    advanced_filter =(By.XPATH, "//app-manager-home-admin-ticket[1]//input[@formcontrolname= 'query']")
    own_category_filter =(By.XPATH, "//app-manager-home-admin-ticket[2]//ng-select[@formcontrolname= 'category']")
    own_status_filter =(By.XPATH, "//app-manager-home-admin-ticket[2]//ng-select[@formcontrolname= 'status']")
    own_advanced_filter =(By.XPATH, "//app-manager-home-admin-ticket[2]//input[@formcontrolname= 'query']")
    dropdown_options = (By.XPATH, "//ng-dropdown-panel//div[@role= 'option']")
    filter_btn_1 = (By.XPATH, "//app-manager-home-admin-ticket[1]//span[contains(text(), 'Filter')]")
    filter_btn_2 = (By.XPATH, "//app-manager-home-admin-ticket[2]//span[contains(text(), 'Filter')]")
    ticket_record = (By.XPATH, "//app-manager-home-admin-ticket[1]//tbody/tr")
    ticket_record_2 = (By.XPATH, "//app-manager-home-admin-ticket[2]//tbody/tr")
    create_chat_btn = (By.XPATH, "//a[contains(text(), 'Create Chat')]")
    property_selector = (By.XPATH, "//ng-select[@formcontrolname= 'building_id']//input")
    resident_selector = (By.XPATH, "//ng-select[@formcontrolname= '_tenant']//input")
    category_selector = (By.XPATH, "//ng-select[@formcontrolname= 'category_id']//div[@class= 'ng-value-container']")
    subcategory_selector = (By.XPATH, "//ng-select[@formcontrolname= 'subcategory_id']//div[@class= 'ng-value-container']")
    create_chat_btn_2 = (By.XPATH, "//button[contains(text(), 'Create Chat')]")
    category_options = (By.XPATH, "//ng-select//ng-dropdown-panel/div/div[2]/div")
    subcategory_options = (By.XPATH, "//ng-select//ng-dropdown-panel/div/div[2]/div")
    text_area_chat = (By.XPATH, "//app-conversation-chat//textarea")
    attachment_input = (By.XPATH, "//app-conversation-chat//input[@formcontrolname='attachments']")
    send_message_btn = (By.XPATH, "//app-conversation-chat//span[contains(text(), 'Send')]")
    more_options_btn = (By.XPATH, "//span[contains(text(), 'More Options')]")
    create_ticket_option = (By.XPATH, "//a[contains(text(), 'Create Ticket')]")
    ticket_type = (By.XPATH, "//ng-select[@formcontrolname= 'request_type']//div[@class= 'ng-value-container']")
    admin_ticket_option = (By.XPATH, "//ng-dropdown-panel//div[@role= 'option'][1]")
    create_btn = (By.XPATH, "//button[contains(text(), 'Create')]")
    ticket_category_selector = (By.XPATH, "//app-request-create-admin-ticket//ng-select[@formcontrolname= 'category']")
    ticket_category_options = (By.XPATH, "//ng-dropdown-panel//div[@role= 'option']")
    details_text_area = (By.XPATH, "//app-request-create-admin-ticket//textarea[@formcontrolname='details']")
    confirm_btn = (By.XPATH, "//button[contains(text(), 'Confirm')]")
    ticket_created = (By.XPATH, "//h3[contains(text(), 'Ticket Created')]")
    pending_ticket = (By.XPATH, "//app-manager-home-admin-ticket//td//span[contains(text(), 'Pending')][1]")
    start_ticket_btn = (By.XPATH, "//app-request-detail-admin-ticket//button[contains(text(), 'Start')]")
    resolution_details = (By.XPATH, "//app-request-detail-admin-ticket//textarea[@formcontrolname= 'resolutionDetails']")
    notes_text_area = (By.XPATH, "//app-request-detail-admin-ticket//input[@formcontrolname= 'note']")
    add_note_btn = (By.XPATH, "//app-request-detail-admin-ticket//button[contains(text(), 'Add Note')]")
    complete_btn = (By.XPATH, "//app-request-detail-admin-ticket//button[contains(text(), 'Complete')]")
    ticket_completed_msg = (By.XPATH, "//div[contains(text(), 'Ticket Completed')]")
    cancel_btn = (By.XPATH, "//button[contains(text(), 'Cancel Ticket')]")
    reason_cancel = (By.XPATH, "//textarea[@formcontrolname= 'inputText']")
    submit_btn = (By.XPATH, "//button[contains(text(), 'Submit')]")
    ticket_canceled_msg = (By.XPATH, "//div[contains(text(), 'Ticket Canceled')]")

    message = "Admin Ticket test Admin Ticket test Admin Ticket test Admin Ticket test Admin Ticket test Admin Ticket test"
    details = "Admin Ticket details test Admin Ticket details test Admin Ticket details test Admin Ticket details test Admin Ticket details test "
    resolution_details_text = "Completing Admin Ticket test Completing Admin Ticket test Completing Admin Ticket test Completing Admin Ticket test "
    note = "Note Test, Note Test, Note Test, Note Test, Note Test, Note Test, Note Test, Note Test"
    reason_text = "Admin Ticket Canceling test Admin Ticket Canceling test Admin Ticket Canceling test Admin Ticket Canceling test "

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(util.base_url)

    def go_to_admin_tickets_page(self):
        try:
            time.sleep(4)
            self.is_visible(util.manager_home_icon)
        except TimeoutException:
            self.send_keys(util.email_locator, util.manager_email)
            self.do_click(util.next_btn)
            time.sleep(0.8)
            self.send_keys(util.password_locator, util.manager_password)
            self.do_click(util.next_btn)
            time.sleep(5)
        time.sleep(6)
        self.driver.get(util.manager_admin_tickets_url)
        time.sleep(6)

    def filter_by_category(self):
        time.sleep(1)
        clicks = [self.category_filter, self.dropdown_options, self.filter_btn_1]
        for i in clicks:
            if i == self.dropdown_options:
                self.click_single_random_option_web(i)
                time.sleep(1)
            else:
                self.do_click(i)
                time.sleep(1)
        try:
            return self.is_visible(self.ticket_record)
        except TimeoutException:
            pytest.skip("No tickets available for this category")


    def filter_by_status(self):
        time.sleep(1)
        clicks = [self.status_filter, self.dropdown_options, self.filter_btn_1]
        for i in clicks:
            if i == self.dropdown_options:
                self.click_single_random_option_web(i)
                time.sleep(1)
            else:
                self.do_click(i)
                time.sleep(1)
        try:
            return self.is_visible(self.ticket_record)
        except TimeoutException:
            pytest.skip("No tickets available for this status")

    def filter_by_advanced(self):
        time.sleep(1)
        self.send_keys(self.advanced_filter, "Ashley Rathappillil")
        time.sleep(1)
        self.do_click(self.filter_btn_1)
        time.sleep(1.2)
        try:
            return self.is_visible(self.ticket_record)
        except TimeoutException:
            pytest.skip("No tickets registered for the search terms")

    def filter_by_own_category(self):
        time.sleep(1)
        clicks = [self.own_category_filter, self.dropdown_options, self.filter_btn_2]
        for i in clicks:
            if i == self.dropdown_options:
                self.click_single_random_option_web(i)
                time.sleep(1)
            else:
                self.do_click(i)
                time.sleep(1)
        try:
            return self.is_visible(self.ticket_record_2)
        except TimeoutException:
            pytest.skip("No tickets available for this category")

    def filter_by_own_status(self):
        time.sleep(1)
        clicks = [self.own_status_filter, self.dropdown_options, self.filter_btn_2]
        for i in clicks:
            if i == self.dropdown_options:
                self.click_single_random_option_web(i)
                time.sleep(1)
            else:
                self.do_click(i)
                time.sleep(1)
        try:
            return self.is_visible(self.ticket_record_2)
        except TimeoutException:
            pytest.skip("No tickets available for this status")

    def filter_by_own_advanced(self):
        time.sleep(1)
        self.send_keys(self.own_advanced_filter, "Ashley Rathappillil")
        time.sleep(1)
        self.do_click(self.filter_btn_2)
        time.sleep(1.2)
        try:
            return self.is_visible(self.ticket_record_2)
        except TimeoutException:
            pytest.skip("No tickets registered for the search terms")

    def new_admin_ticket(self):
        self.driver.get(util.manager_chat_url)
        time.sleep(2)
        time.sleep(2)
        clicks = [self.create_chat_btn, self.property_selector, self.resident_selector,
                  self.category_selector, self.subcategory_selector, self.create_chat_btn_2
                  ]
        for i in clicks:
            if i == self.property_selector:
                time.sleep(0.5)
                self.send_keys(i, "DVORA 175")
                time.sleep(1)
                self.press_enter_web()
                time.sleep(8.5)
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
        time.sleep(2.5)
        messages = [(self.text_area_chat, self.message), (self.attachment_input, os.getcwd() + '/photo6.jpg')]
        for i in messages:
            time.sleep(1)
            self.send_keys(i[0], i[1])
            time.sleep(1.5)
        time.sleep(1.8)
        self.do_click(self.send_message_btn)
        time.sleep(0.8)
        clicks_2 = [self.more_options_btn, self.create_ticket_option, self.ticket_type,
                    self.admin_ticket_option, self.create_btn]
        for x in clicks_2:
            self.do_click(x)
            time.sleep(0.8)
        time.sleep(2)
        clicks_3 = [self.ticket_category_selector, self.details_text_area,
                    self.create_btn, self.confirm_btn]
        for x in clicks_3:
            if x == self.ticket_category_selector:
                self.do_click(x)
                time.sleep(0.8)
                self.click_single_random_option_web(self.ticket_category_options)
                time.sleep(1)
            elif x == self.details_text_area:
                self.send_keys(x, self.details)
                time.sleep(1)
            else:
                self.do_click(x)
                time.sleep(1)
        time.sleep(1)
        return self.is_visible(self.ticket_created)

    def complete_admin_ticket(self):
        self.driver.get(util.manager_admin_tickets_url)
        time.sleep(1)
        clicks = [self.pending_ticket, self.start_ticket_btn, self.resolution_details,
                  self.notes_text_area, self.add_note_btn, self.complete_btn, self.confirm_btn]
        for i in clicks:
            self.scroll_to_location_web(i)
            if i == self.resolution_details:
                self.send_keys(i, self.resolution_details_text)
                time.sleep(0.8)
            elif i == self.notes_text_area:
                self.send_keys(i, self.note)
                time.sleep(0.8)
            else:
                self.do_click(i)
                time.sleep(1.2)
        return self.is_visible(self.ticket_completed_msg)

    def cancel_admin_ticket(self):
        self.driver.get(util.manager_admin_tickets_url)
        time.sleep(5)
        clicks = [self.pending_ticket, self.start_ticket_btn, self.resolution_details,
                  self.notes_text_area, self.add_note_btn, self.cancel_btn, self.reason_cancel,
                  self.submit_btn]
        for i in clicks:
            self.scroll_to_location_web(i)
            if i == self.resolution_details:
                self.send_keys(i, self.resolution_details_text)
                time.sleep(0.8)
            elif i == self.notes_text_area:
                self.send_keys(i, self.note)
                time.sleep(0.8)
            elif i == self.reason_cancel:
                self.send_keys(i, self.reason_text)
                time.sleep(0.8)
            else:
                self.do_click(i)
                time.sleep(1.2)
        time.sleep(0.8)
        return self.is_visible(self.ticket_canceled_msg)

