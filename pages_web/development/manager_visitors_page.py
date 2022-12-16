import os
import pytest
from pages_web.development.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import util.web_utils_development as util
"""Visitors module for manager, locators and actions"""


class VisitorsManager(BasePage):
    """Locators"""
    new_visitor_btn = (By.XPATH, "//span[contains(text(), 'Filter')]")
    allow_keys_chkbx = (By.XPATH, "//input[@formcontrolname = 'allowKeys']")
    image_loader = (By.XPATH, "//input[@type = 'file']")
    save_icon = (By.XPATH, "//button[@class = 'button is-success']")
    resident_name = (By.XPATH, "//div[@role= 'combobox']/input")
    ok_btn = (By.XPATH, "//button[contains(text(),  'Ok')]")
    visitor_name = (By.XPATH, "//input[@formcontrolname = 'visitorName']")
    arrival_date = (By.XPATH, "//input[@formcontrolname = 'visitorStartDate']")
    departure_date = (By.XPATH, "//input[@formcontrolname = 'visitorEndDate']")
    time_arrival = (By.XPATH, "//input[@formcontrolname = 'visitorStartTime']")
    time_departure = (By.XPATH, "//input[@formcontrolname = 'visitorEndTime']")
    add_new_visitor_btn = (By.XPATH, "//button[@type = 'submit']")
    visitor_name_list = (By.XPATH, "//tbody/tr[1]/td[1]")
    relationship_tag = (By.XPATH, "//div[@class= 'line']/b[contains(text(), 'Relationship/')]")

    resident_name_text = "Abimbola Osunsanya"
    visitor_image = os.getcwd() + '/photo6.jpg'
    visitor_name_text = "Manager Visitor test"
    arrival_date_text = "06/03/2022"
    departure_date_text = "10/02/2022"
    time_arrival_text = "1000A"
    time_departure_text = "300P"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(util.base_url)

    def go_to_visitors_page(self):
        try:
            self.is_visible(util.manager_home_icon)
        except TimeoutException:
            self.send_keys(util.email_locator, util.manager_email)
            self.do_click(util.next_btn)
            time.sleep(0.8)
            self.send_keys(util.password_locator, util.manager_password)
            self.do_click(util.next_btn)
            time.sleep(9)
        time.sleep(3)
        self.driver.get(util.manager_visitors_url)
        time.sleep(1)

    def new_visitor(self):
        self.do_click(self.new_visitor_btn)
        time.sleep(1)
        fields = [self.allow_keys_chkbx, self.image_loader,
                  (self.resident_name, self.resident_name_text),
                  (self.visitor_name, self.visitor_name_text),
                  (self.arrival_date, self.arrival_date_text),
                  (self.departure_date, self.departure_date_text),
                  (self.time_arrival, self.time_arrival_text),
                  (self.time_departure, self.time_departure_text),
                  self.add_new_visitor_btn
                  ]
        for f in fields:
            if f == self.allow_keys_chkbx:
                self.do_click(f)
                time.sleep(0.5)
            elif f == self.image_loader:
                self.send_keys(f, self.visitor_image)
                time.sleep(1)
                self.do_click(self.save_icon)
                time.sleep(0.5)
            elif f == self.add_new_visitor_btn:
                self.scroll_to_location_web(f)
                time.sleep(2)
                self.do_click(f)
            elif f[0] == self.resident_name:
                self.send_keys(f[0], f[1])
                time.sleep(2)
                self.press_enter_web()
                time.sleep(0.5)
            else:
                self.scroll_to_location_web(f[0])
                time.sleep(0.5)
                self.send_keys(f[0], f[1])
                self.press_escape()
        return self.is_visible(self.ok_btn)

    def see_visitor_info(self):
        try:
            self.do_click(self.visitor_name_list)
            time.sleep(0.5)
            return self.is_visible(self.relationship_tag)
        except TimeoutException:
            pytest.skip("No visitors available in current time line")
