import os
import pytest
from pages_web.development.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import util.web_utils_development as util
"""Reservations/amenities module for Manager, locators and actions"""


class ManagerAmenities(BasePage):
    """locators"""
    reservations_calendar = (By.XPATH, "//h1[contains(text(), 'Reservations Calendar')]")
    amenity_list = (By.XPATH, "//a[contains(text(), 'Amenity List')]")
    add_amenity = (By.XPATH, "//a[contains(text(), 'Add Amenity')]")
    amenity_blocked_slots = (By.XPATH, "//a[contains(text(), 'Amenity Blocked Slots')]")
    create_reservation = (By.XPATH, "//a[contains(text(), 'Create Reservation')]")
    add_blocked_slot = (By.XPATH, "//a[contains(text(), 'Add Blocked Slot')]")
    property_selector = (By.XPATH, "//div[@role= 'combobox']")
    amenity_properties = (By.XPATH, "//div[@class= 'ng-dropdown-panel-items scroll-host']/div[2]/div[@role='option']")
    amenity_name = (By.XPATH, "//input[@formcontrolname='name']")
    form = (By.XPATH, "//form[@class= 'section-content has-padding ng-invalid ng-dirty ng-touched']")
    amenity_capacity = (By.XPATH, "//input[@formcontrolname='capacity']")
    minimum_time = (By.XPATH, "//ng-select[@formcontrolname='minimum_time']")
    minimum_time_label = (By.XPATH, "//label[@class= 'label is-required'][contains(text(), 'Minimum time')]")
    maximum_time = (By.XPATH, "//ng-select[@formcontrolname='maximum_time']")
    available_min_time = (By.XPATH, "//ng-dropdown-panel/div[@class='ng-dropdown-panel-items scroll-host']//div[@role='option']")
    available_max_time = (By.XPATH, "//ng-dropdown-panel/div[@class='ng-dropdown-panel-items scroll-host']//div[@role='option']")
    amenity_description = (By.XPATH, "//div[@class='ck ck-editor__main']//p")
    business_days = (By.XPATH, "//div[@class= 'buttons']//input")
    business_start = (By.XPATH, "//input[@formcontrolname= '_business_start_time']")
    business_end = (By.XPATH, "//input[@formcontrolname= '_business_end_time']")
    publish_amenity_btn = (By.XPATH, "//button[@class='button'][contains(text(), 'Publish Amenity')]")
    create_amenity_btn = (By.XPATH, "//div[@class= 'buttons']/button[@class= 'button is-primary'][contains(text(), 'Create Amenity')]")
    auto_approve_btn = (By.XPATH, "//input[@name= 'auto_approve']")
    ok_btn = (By.XPATH, "//button[contains(text(), 'Ok')]")
    status_select = (By.XPATH, "//ng-select//span[@class = 'ng-arrow-wrapper']")
    published_am = (By.XPATH, "//ng-dropdown-panel//span[contains(text(), 'Published')]")
    unpublished_am = (By.XPATH, "//ng-dropdown-panel//span[contains(text(), 'Unpublished')]")
    published_item = (By.XPATH, "//table[@class= 'table is-fullwidth is-hoverable']//span[contains(text(), 'Published')]")
    unpublished_item = (By.XPATH, "//table[@class= 'table is-fullwidth is-hoverable']//span[contains(text(), 'Unpublished')]")
    edit_am_btn = (By.XPATH, "//mat-icon[contains(text(), 'edit')]")
    unpublish_amenity_locator = (By.XPATH, "//button[contains(text(), 'Unpublish Amenity')]")
    filter_btn = (By.XPATH, "//button[contains(text(), 'Filter')]")

    amenity_name_text = "Amenity Test 1"
    amenity_name_text2 = "Amenity Test 2"
    amenity_capacity_text = "30"
    amenity_description_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor" \
                               "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud" \
                               "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    business_start_text = "1000A"
    business_end_text = "600P"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(util.base_url)

    def go_to_reservations_page(self):
        try:
            time.sleep(8)
            self.is_visible(util.manager_home_icon)
        except TimeoutException:
            self.send_keys(util.email_locator, util.manager_email)
            self.do_click(util.next_btn)
            time.sleep(0.8)
            self.send_keys(util.password_locator, util.manager_password)
            self.do_click(util.next_btn)
            time.sleep(5)
        time.sleep(6)
        self.driver.get(util.manager_amenities_url)
        time.sleep(3)

    def create_amenity(self):
        self.do_click(self.amenity_list)
        self.do_click(self.add_amenity)
        self.do_click(self.property_selector)
        self.click_random_option_web(self.amenity_properties)
        time.sleep(2)
        self.press_escape()
        time.sleep(2)
        required_fields = [(self.amenity_name, self.amenity_name_text),
                           (self.amenity_capacity, self.amenity_capacity_text),
                           (self.minimum_time, self.available_min_time),
                           (self.maximum_time, self.available_max_time),
                           (self.amenity_description, self.amenity_description_text),
                           (self.business_days,),
                           (self.business_start, self.business_start_text),
                           (self.business_end, self.business_end_text),
                           (self.create_amenity_btn,)
                           ]
        for fields in required_fields:
            if fields[0] == self.minimum_time or fields[0] == self.maximum_time:
                self.do_click(fields[0])
                self.click_random_option(fields[1])
                time.sleep(0.5)
                self.press_escape()
                time.sleep(0.5)
                self.scroll_to_location_web(self.minimum_time_label)
                time.sleep(1)
            elif fields[0] == self.business_days:
                self.scroll_to_location_web(fields[0])
                self.click_random_option_web(fields[0])
                time.sleep(1)
            elif fields[0] == self.create_amenity_btn:
                self.scroll_to_location_web(fields[0])
                time.sleep(3)
                self.do_click(fields[0])
            else:
                self.scroll_to_location_web(fields[0])
                self.do_click(fields[0])
                self.send_keys(fields[0], fields[1])
                self.press_escape()
                time.sleep(0.5)
        time.sleep(2)
        self.do_click(self.ok_btn)
        time.sleep(1)

    def publish_amenity(self):
        self.do_click(self.amenity_list)
        self.do_click(self.add_amenity)
        self.do_click(self.property_selector)
        self.click_random_option_web(self.amenity_properties)
        time.sleep(3)
        self.press_escape()
        required_fields = [(self.amenity_name, self.amenity_name_text2),
                           (self.amenity_capacity, self.amenity_capacity_text),
                           (self.minimum_time, self.available_min_time),
                           (self.maximum_time, self.available_max_time),
                           (self.amenity_description, self.amenity_description_text),
                           (self.business_days,),
                           (self.business_start, self.business_start_text),
                           (self.business_end, self.business_end_text),
                           (self.publish_amenity_btn,)
                           ]
        for fields in required_fields:
            if fields[0] == self.minimum_time or fields[0] == self.maximum_time:
                self.do_click(fields[0])
                self.click_random_option(fields[1])
                self.press_escape()
                time.sleep(0.5)
                self.scroll_to_location_web(self.minimum_time_label)
                time.sleep(1)
            elif fields[0] == self.business_days:
                self.scroll_to_location_web(fields[0])
                self.click_random_option_web(fields[0])
                time.sleep(2)
            elif fields[0] == self.auto_approve_btn:
                self.scroll_to_location_web(fields[0])
                if self.switches_on_off(self.auto_approve_btn) == 'false':
                    self.do_click(self.auto_approve_btn)
                    time.sleep(1)
                else:
                    continue
            elif fields[0] == self.publish_amenity_btn:
                self.scroll_to_location_web(fields[0])
                time.sleep(5)
                self.do_click(fields[0])
            else:
                self.scroll_to_location_web(fields[0])
                self.do_click(fields[0])
                self.send_keys(fields[0], fields[1])
                self.press_escape()
                time.sleep(0.5)
        time.sleep(1)
        self.do_click(self.ok_btn)

    def filter_published(self):
        self.do_click(self.amenity_list)
        self.do_click(self.status_select)
        time.sleep(2)
        self.do_click(self.published_am)
        time.sleep(2)
        self.do_click(self.filter_btn)
        time.sleep(1)
        return self.is_visible(self.published_item)

    def filter_unpublished(self):
        self.do_click(self.amenity_list)
        self.do_click(self.status_select)
        time.sleep(2)
        self.do_click(self.unpublished_am)
        time.sleep(2)
        self.do_click(self.filter_btn)
        time.sleep(4)
        return self.is_visible(self.unpublished_item)

    def unpublish_amenity(self):
        locators = [self.amenity_list,
                    self.status_select,
                    self.published_am,
                    self.edit_am_btn,
                    self.unpublish_amenity_locator
                    ]
        for i in locators:
            if i == self.unpublish_amenity_locator:
                self.scroll_to_location_web(i)
                self.scroll_to_bottom()
                time.sleep(0.5)
                self.do_click(i)
                time.sleep(0.5)
            else:
                self.do_click(i)
                time.sleep(2)
        return self.is_visible(self.ok_btn)
