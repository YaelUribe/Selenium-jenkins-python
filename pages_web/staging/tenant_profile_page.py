import os
import pytest
from pages_web.staging.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import util.web_utils_staging as util
"""Profile module for tenant, specific locators and module actions"""


class ProfileTenant(BasePage):
    """Locators"""
    profile_icon = (By.XPATH, "//div[@class='user-profile']")
    profile_picture = (By.XPATH, "//input[@name='newImage']")
    my_profile = (By.XPATH, "//span[contains(text(), 'My Profile')]")
    my_unit = (By.XPATH, "//span[contains(text(), 'My Unit')]")
    payments_icon = (By.XPATH, "//span[contains(text(), 'Payments')]")
    autopay_toggle = (By.XPATH, "//input[@id='paymentToggle']")
    iframe = (By.XPATH, "/html/body/iframe")
    autopay_toggle2 = (By.XPATH, "//input[@type='checkbox']")
    autopay_toggle3 = (By.XPATH, "//input[@type='checkbox'][@class='toggle_switch']")
    card_btn = (By.XPATH, "//button[@class='dropdown_list_button rounded_corners jtk_btn']")
    close_btn = (By.XPATH, "//div[@class='float_right button ha_center unselectable']")
    continue_btn = (By.XPATH, "//button[contains(text(), 'Continue')]")
    confirm_btn = (By.XPATH, "//button[contains(text(), 'Confirm')]")
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
    save_changes_btn = (By.XPATH, "//button[contains(text(), 'Save Changes')]")
    save_icon = (By.XPATH, "//mat-icon[contains(text(), 'save')]")
    cell_phone = (By.XPATH, "//input[@formcontrolname='cell_phone']")
    work_phone = (By.XPATH, "//input[@formcontrolname='work_phone']")
    home_phone = (By.XPATH, "//input[@formcontrolname='home_phone']")
    emergency_name = (By.XPATH, "//input[@formcontrolname='emergency_contact_name']")
    emergency_email = (By.XPATH, "//input[@formcontrolname='emergency_contact_email']")
    emergency_cell_phone = (By.XPATH, "//input[@formcontrolname='emergency_contact_phone']")
    emergency_work_phone = (By.XPATH, "//input[@formcontrolname='emergency_contact_work_phone']")
    emergency_home_phone = (By.XPATH, "//input[@formcontrolname='emergency_contact_home_phone']")
    success_notification = (By.XPATH, "//div[@class='notification is-success']")
    unit_residents = (By.XPATH, "//div[@class='section-content']")
    autopay_enabled = (By.XPATH, "//h1[contains(text(), 'Automatic Payments Enabled')]")
    autopay_disabled = (By.XPATH, "//h1[contains(text(), 'Automatic Payments Disabled')]")
    pending_payments = (By.XPATH, "//h3[contains(text(), 'Pending Payments')]")
    tenant_cell_phone = "2220000055"
    tenant_work_phone = "(222)555-555-52"
    tenant_home_phone = "(333)456-78-29"
    e_name = "Dvora Meltrozo"
    e_email = "yael+visitor@dvoralife.com"
    e_cell_phone = "555-444-3210"
    e_work_phone = "(477)456-7890"
    e_home_phone = "(669)789-0123"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(util.base_url)

    def go_to_profile_page(self):
        """Go to profile module"""
        try:
            self.is_visible(util.home_icon)
        except TimeoutException:
            self.send_keys(util.email_locator, util.tenant_email)
            self.do_click(util.next_btn)
            time.sleep(0.8)
            self.send_keys(util.password_locator, util.tenant_password)
            self.do_click(util.next_btn)
            time.sleep(2)
        time.sleep(2)
        self.driver.get(util.tenant_profile_url)
        time.sleep(1)

    def update_profile_picture(self):
        self.send_keys(self.profile_picture, os.getcwd() + '/photo1.jpeg')
        self.do_click(self.save_icon)
        time.sleep(3)

    def update_info(self):
        self.do_click(self.profile_icon)

        fields_list = [(self.cell_phone, self.tenant_cell_phone),
                       (self.work_phone, self.tenant_work_phone),
                       (self.home_phone, self.tenant_home_phone),
                       (self.emergency_name, self.e_name),
                       (self.emergency_email, self.e_email),
                       (self.emergency_cell_phone, self.e_cell_phone),
                       (self.emergency_work_phone, self.e_work_phone),
                       (self.emergency_home_phone, self.e_home_phone)
                       ]
        for values in fields_list:
            self.clear(values[0])
            self.send_keys(values[0], values[1])
        time.sleep(3)
        self.do_click(self.save_changes_btn)
        time.sleep(1.2)

    def see_my_unit(self):
        self.do_click(self.my_unit)
        return self.is_visible(self.unit_residents)

    def change_password(self):
        self.do_click(self.security_icon)
        self.send_keys(self.current_pass, util.tenant_password)
        self.send_keys(self.new_pass, util.tenant_password)
        self.send_keys(self.c_new_pass, util.tenant_password)
        self.do_click(self.save_changes_btn)
        time.sleep(1)
        return self.is_visible(self.success_notification)

    def switch_off_notifications(self):
        toggle_list = [self.email_switch,
                       self.push_switch,
                       self.sms_switch
                       ]
        self.do_click(self.notifications)
        time.sleep(0.5)
        for element in toggle_list:
            toggle = self.switches_on_off(element)
            if toggle is not None and toggle == "false":
                continue
            else:
                self.do_click(element)
                time.sleep(0.5)

    def switch_on_notifications(self):
        toggle_list = [self.email_switch,
                       self.push_switch,
                       self.sms_switch
                       ]
        self.do_click(self.notifications)
        time.sleep(0.5)
        for element in toggle_list:
            toggle = self.switches_on_off(element)
            if toggle is not None and toggle == "true":
                continue
            else:
                self.do_click(element)
                time.sleep(0.5)

    def preferences(self):
        self.do_click(self.preferences_icon)
        time.sleep(0.5)
        self.do_click(self.preferences_input)
        time.sleep(1)
        return self.is_visible(self.preferences_lang)

    def turn_off_autopay(self):
        self.do_click(self.payments_icon)
        time.sleep(0.5)
        toggle = self.switches_on_off(self.autopay_toggle)
        if toggle is not None and toggle == "false":
            pass
        else:
            self.do_click(self.autopay_toggle)
            time.sleep(1)
            if self.is_visible(self.pending_payments):
                pytest.skip("Autopay must remain activated")
            time.sleep(0.7)
            self.do_click(self.continue_btn)
            time.sleep(1)
            frame = self.is_visible(self.iframe)
            self.driver.switch_to.frame(frame)
            toggle2 = self.switches_on_off(self.autopay_toggle2)
            if toggle2 is not None and toggle2 == "false":
                pass
            else:
                try:
                    time.sleep(1)
                    self.do_click(self.card_btn)
                    time.sleep(1)
                    self.do_click(self.autopay_toggle2)
                    time.sleep(1)
                    assert self.is_visible(self.autopay_disabled)
                    self.do_click(self.close_btn)
                except TimeoutException:
                    pytest.skip("Autopay already disabled")

    def turn_on_autopay(self):
        self.do_click(self.payments_icon)
        time.sleep(0.5)
        toggle = self.switches_on_off(self.autopay_toggle)
        if toggle is not None and toggle == "true":
            pass
        else:
            self.do_click(self.autopay_toggle)
            time.sleep(0.7)
            frame = self.is_visible(self.iframe)
            self.driver.switch_to.frame(frame)
            toggle2 = self.switches_on_off(self.autopay_toggle2)
            print(toggle2)
            if toggle2 is not None and toggle2 == "true":
                pass
            try:
                self.do_click(self.card_btn)
                time.sleep(0.2)
                self.press_escape()
                self.do_click(self.autopay_toggle2)
                time.sleep(1)
                self.do_click(self.confirm_btn)
                time.sleep(0.5)
                assert self.is_visible(self.autopay_enabled)
                self.do_click(self.close_btn)
            except TimeoutException:
                pytest.skip("Autopay already enabled")
