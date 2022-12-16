import os
import pytest
from pages_web.staging.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import util.web_utils_staging as util


class ProfileManager(BasePage):
    """Locators"""
    profile_icon = (By.XPATH, "//div[@class='user-profile']")
    profile_picture = (By.XPATH, "//input[@name='newImage']")
    my_profile = (By.XPATH, "//div[@class= 'user-profile']")
    save_icon = (By.XPATH, "//mat-icon[contains(text(), 'save')]")
    first_name = (By.XPATH, "//input[@formcontrolname='first_name']")
    last_name = (By.XPATH, "//input[@formcontrolname='last_name']")
    cell_phone = (By.XPATH, "//input[@formcontrolname='cell_phone']")
    work_phone = (By.XPATH, "//input[@formcontrolname='work_phone']")
    home_phone = (By.XPATH, "//input[@formcontrolname='home_phone']")
    save_changes_btn = (By.XPATH, "//button[contains(text(), 'Save Changes')]")
    success_notification = (By.XPATH, "//div[@class='notification is-success']")
    my_properties = (By.XPATH, "//span[contains(text(), 'My Properties')]")
    all_my_properties = (By.XPATH, "//h1[contains(text(), 'All My Properties')]")
    security_icon = (By.XPATH, "//span[contains(text(), 'Security')]")
    current_pass = (By.XPATH, "//input[@formcontrolname='currentPassword']")
    new_pass = (By.XPATH, "//input[@formcontrolname='password1']")
    c_new_pass = (By.XPATH, "//input[@formcontrolname='password2']")
    notifications = (By.XPATH, "//span[contains(text(), 'Notifications')]")
    email_switch = (By.XPATH, "//input[@id='email_notifications']")
    push_switch = (By.XPATH, "//input[@id='push_notifications']")
    sms_switch = (By.XPATH, "//input[@id='sms_notifications']")
    preferences_icon = (By.XPATH, "//span[contains(text(), 'Preferences')]")
    preferences_input = (By.XPATH, "//input[@aria-autocomplete='list']")
    preferences_lang = (By.XPATH, "//span[@class='ng-option-label']")

    manager_fname = "Yael"
    manager_lname = "CE"
    manager_cell_phone = "(551)260-1963"
    manager_work_phone = "(222)555-2222"
    manager_home_phone = "(340)987-5587"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(util.base_url)

    def go_to_profile_page(self):
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
        self.driver.get(util.manager_profile_url)
        time.sleep(1)

    def update_profile_picture(self):
        self.send_keys(self.profile_picture, os.getcwd() + '/photo2.jpeg')
        self.do_click(self.save_icon)
        time.sleep(2)

    def update_info(self):
        self.do_click(self.profile_icon)
        fields_list = [(self.first_name, self.manager_fname),
                       (self.last_name, self.manager_lname),
                       (self.cell_phone, self.manager_cell_phone),
                       (self.work_phone, self.manager_work_phone),
                       (self.home_phone, self.manager_home_phone)
                       ]
        for values in fields_list:
            self.clear(values[0])
            self.send_keys(values[0], values[1])
        time.sleep(2)
        self.do_click(self.save_changes_btn)
        time.sleep(1.5)
        return self.is_visible(self.success_notification)

    def see_my_properties(self):
        self.do_click(self.my_properties)
        return self.is_visible(self.all_my_properties)

    def change_password(self):
        self.do_click(self.security_icon)
        self.send_keys(self.current_pass, util.manager_password)
        self.send_keys(self.new_pass, util.manager_password)
        self.send_keys(self.c_new_pass, util.manager_password)
        self.do_click(self.save_changes_btn)
        time.sleep(1.2)
        return self.is_visible(self.success_notification)

    def switch_on_notifications(self):
        toggle_list = [self.email_switch,
                       self.push_switch,
                       self.sms_switch
                       ]
        self.do_click(self.notifications)
        time.sleep(1)
        for element in toggle_list:
            toggle = self.switches_on_off(element)
            if toggle is not None and toggle == "true":
                continue
            else:
                self.do_click(element)
                time.sleep(2)

    def switch_off_notifications(self):
        toggle_list = [self.email_switch,
                       self.push_switch,
                       self.sms_switch
                       ]
        self.do_click(self.notifications)
        time.sleep(1)
        for element in toggle_list:
            toggle = self.switches_on_off(element)
            if toggle is not None and toggle == "false":
                continue
            else:
                self.do_click(element)
                time.sleep(1)

    def preferences(self):
        self.do_click(self.preferences_icon)
        time.sleep(0.5)
        self.do_click(self.preferences_input)
        time.sleep(1)
        return self.is_visible(self.preferences_lang)
