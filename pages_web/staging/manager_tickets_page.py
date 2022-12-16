import os
import json
import random
import pytest
from pages_web.staging.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import util.web_utils_staging as util
"""Tickets module for Manager, locators and actions"""


class TicketsManager(BasePage):
    """locators"""
    all_tickets = (By.XPATH, "//span[contains( text(), 'All Tickets')]")
    open_tickets = (By.XPATH, "//span[contains( text(), 'Open Tickets')]")
    child_tickets = (By.XPATH, "//span[contains( text(), 'Child Tickets')]")
    ticket_status = (By.XPATH, "//div[contains( text(), 'Ticket Status')]")
    ticket_types = (By.XPATH, "//div[contains( text(), 'Ticket Types')]")
    property_dropdown = (By.XPATH, "//div[contains( text(), 'Property')]")
    search_unit_member = (By.XPATH, "//input[@placeholder='Search Unit/Member']")
    assigned_technician = (By.XPATH, "//app-all-rm/div/form/div[1]/div[3]/ng-select")
    filter_btn = (By.XPATH, "//form/div[2]/div[3]/button")
    tickets_found = (By.XPATH, "//span[contains(text(), 'Results')]")
    new_ticket_btn = (By.XPATH, "//form//button/span[contains(text(), 'New Ticket')]")
    ticket_type_drpdwn = (By.XPATH, "//ng-select/div/div/div[2]")
    move_out_ticket = (By.XPATH, "//div[@role='option']/span[contains(text(), 'Move Out')]")
    move_in_ticket = (By.XPATH, "//div[@role='option']/span[contains(text(), 'Move In')]")
    create_btn = (By.XPATH, "//button[contains(text(), 'Create')]")
    unit_member = (By.XPATH, "//app-tenant-dropdown/ng-select/div/div/div[2]/input")
    move_out_date = (By.XPATH, "//input[@formcontrolname='selectedDate']")
    time_slot = (By.XPATH, "//ng-select[@formcontrolname='selectedTimeSlot']/div/div/div[2]/input")
    confirm_btn = (By.XPATH, "//button[contains(text(), 'Confirm')]")
    ok_btn = (By.XPATH, "//button[contains(text(), 'Ok')]")
    moving_type = (By.XPATH, "//h2[contains(text(), 'Moving Type')]")
    select_moving_type = (By.XPATH, "//ng-select[@formcontrolname='movingType']//div[@class='ng-value-container']")
    self_move = (By.XPATH, "//ng-dropdown-panel//span[contains(text(), 'Self Move')]")
    moving_company = (By.XPATH, "//ng-dropdown-panel//span[contains(text(), 'Moving Company')]")
    renters_insurance = (By.XPATH, "//div/div/div[3]/div/app-inline-file-input-form-field/div/div/label/input")
    hold_harmless_2 = (By.XPATH, "//div/div/div[3]/div/app-inline-file-input-form-field/div/div/label/input")
    hold_harmless = (By.XPATH, "//div/div/div[4]/div/app-inline-file-input-form-field/div/div/label/input")
    renters_insurance_tag = (By.XPATH, "//h2[contains(text(), 'Renters Insurance')]")
    renters_insurance_2 = (By.XPATH, "//div/div/div/div/app-inline-file-input-form-field/div/div/label/input")
    c_o_i = (By.XPATH, "//div[@id='cdk-accordion-child-21']/div/div/div[5]//input")
    disconnect_utilities = (By.XPATH, "//h2[contains(text(), 'Disconnect Utilities')]")
    connect_utilities = (By.XPATH, "//h2[contains(text(), 'Connect Utilities')]")
    disconnect_utilities_chkbx = (By.XPATH, "//input[@id='remindDisconnect']")
    connect_utilities_chkbx = (By.XPATH, "//input[@id='remindConnect']")
    connect_water_account = (By.XPATH, "//div/div/div/div[2]/div/div/input[@formcontrolname='suezAccount']")
    complete_ticket_btn = (By.XPATH, "//button[contains(text(),'Complete Ticket')]")
    save_changes_btn = (By.XPATH, "//button[contains(text(),'Save Changes')]")
    cancel_ticket = (By.XPATH, "//button[contains(text(),'Cancel Ticket')]")
    book_inspection = (By.XPATH, "//form//mat-accordion/mat-expansion-panel[5]")
    assigned_technician_2 = (By.XPATH, "//div/ng-select[@formcontrolname='assignedTo']/div/div")
    technician_name = (By.XPATH, "//ng-dropdown-panel//span[contains(text(),'Automation Technician')]")
    inspection_date = (By.XPATH, "//mat-expansion-panel[5]/div/div//div[@class='columns']/div[1]//input")
    inspection_time = (By.XPATH, "//mat-expansion-panel[5]/div/div//div[@class='columns']/div[2]//input")
    inspection_duration = (By.XPATH, "//mat-expansion-panel[5]/div/div//div[@class='columns']/div[3]//input")
    move_in_list = (By.XPATH, "//div[@class='subtitle']/span[contains(text(), 'Move In')]")
    mo_ticket_id = (By.XPATH, "//h2[@class='subtitle mb-4']")
    mi_ticket_id = (By.XPATH, "//h2[@class='subtitle mb-4']")
    table_ticket_id = (By.XPATH, "//table/tbody/tr[1]/td[1]")
    edit_ticket_icon = (By.XPATH, "//table/tbody/tr[1]")
    edit_ticket_tag = (By.XPATH, "//app-request-detail-move-out-v2//a[contains(text(), ' Edit Ticket ')]")
    edit_ticket_tag_2 = (By.XPATH, "//app-request-detail-move-in-v2/div//a[contains(text(), ' Edit Ticket ')]")
    list_btn = (By.XPATH, "//app-picker-menu//span[contains(text(), 'List')]")
    duration_option = (By.XPATH, "//ng-dropdown-panel//span[contains(text(), '30 Min')]")
    connect_electric_account = (By.XPATH, "//input[@formcontrolname= 'psegAccount']")
    move_in_warning = (By.XPATH, "//div[contains(text(), 'A Move-In already exists for this member.')]")
    move_out_warning = (By.XPATH, "//div[contains(text(), 'A Move-Out already exists for this member.')]")
    id_tag = (By.XPATH, "//th//div[contains(text(), 'ID')]")
    sort_arrow = (By.XPATH, "//th/div/div[2]")

    move_in_url = "https://staging.dvoraliving.com/m/move-in/list"
    move_out_url = "https://staging.dvoraliving.com/m/move-out/list"
    unit_member_text = "Ashley Rathappillil"
    time_slot_text = "9"
    time_slot_text_2 = "1"
    inspection_time_text = str(random.randint(7, 12)) + "00A"
    connect_water_account_text = "010111-123"
    connect_electric_account_text = "01202002-22"
    move_out_id = ""
    move_in_id = ""
    mi_id = "mi_id"
    mo_id = "mo_id"
    input_date = ""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(util.base_url)

    def go_to_tickets_page(self):
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
        self.driver.get(util.manager_tickets_url)
        time.sleep(4)

    def go_to_move_out(self):
        self.driver.get(self.move_out_url)
        time.sleep(1)

    def go_to_move_in(self):
        self.driver.get(self.move_in_url)
        time.sleep(1)

    def get_ticket_id(self, locator):
        locator_str = self.get_text(locator)
        ticket_id = ""
        for x in locator_str:
            if (57 >= ord(x) >= 48) or ord(x) == 35:
                ticket_id += x
            else:
                continue
        return ticket_id

    def store_id(self, key, value):
        json_file = "./ticket_ids.json"
        with open(json_file, 'r') as f:
            id_dict = json.load(f)
        id_dict[key] = value
        with open(json_file, 'w') as f:
            json.dump(id_dict, f)

    def id_fetch(self, key):
        json_file = "./ticket_ids.json"
        with open(json_file, 'r') as f:
            id_dict = json.load(f)
        id_number = str(id_dict[key])
        return id_number

    def new_move_out_ticket(self, hour):
        self.go_to_move_out()
        time.sleep(10)
        self.do_click(self.new_ticket_btn)
        time.sleep(0.5)
        fields = [(self.unit_member, self.unit_member_text),
                  (self.move_out_date,),
                  (self.time_slot, self.time_slot_text)
                  ]
        for x in fields:
            if x[0] == self.move_out_date:
                try:
                    if self.is_visible(self.move_out_warning):
                        self.do_click(self.ok_btn)
                        time.sleep(1)
                except TimeoutException:
                    continue
                self.input_date = self.tickets_calendar(hour)
                self.send_keys(x[0], self.input_date)
                time.sleep(0.5)
            else:
                self.send_keys(x[0], x[1])
                time.sleep(4)
                self.press_enter_web()
                time.sleep(0.5)
        clicks_2 = [self.create_btn, self.confirm_btn, self.ok_btn,
                    self.moving_type, self.select_moving_type, self.self_move, self.renters_insurance,
                    self.disconnect_utilities, self.disconnect_utilities_chkbx,
                    self.book_inspection, self.assigned_technician_2, self.technician_name,
                    self.inspection_date, self.inspection_time
                    ]
        for y in clicks_2:
            self.scroll_to_location_web(y)
            if y == self.renters_insurance:
                self.send_keys(y, os.getcwd() + '/testpdf.pdf')
                time.sleep(4)
            elif y == self.disconnect_utilities_chkbx:
                checkbox = self.switches_on_off(y)
                if checkbox is not None and checkbox == "true":
                    continue
                else:
                    self.do_click(y)
                    time.sleep(0.5)
            elif y == self.inspection_date:
                self.send_keys(y, self.date_calendar())
                time.sleep(0.5)
            elif y == self.inspection_time:
                self.send_keys(y, self.random_time_duration())
                time.sleep(0.5)
            else:
                self.do_click(y)
                time.sleep(1)
        self.move_out_id = self.get_ticket_id(self.mo_ticket_id)
        self.store_id(self.mo_id, self.move_out_id)
        self.do_click(self.complete_ticket_btn)
        time.sleep(0.5)
        self.do_click(self.confirm_btn)
        time.sleep(0.5)
        try:
            return self.is_visible(self.ok_btn)
        except TimeoutException:
            self.date_switcher(self.input_date)

    def date_switcher(self, date):
        input_date = self.date_incrementer(date)
        self.send_keys(self.move_out_date, input_date)
        time.sleep(0.5)
        self.scroll_to_location_web(self.create_btn)
        try:
            return self.is_visible(self.ok_btn)
        except TimeoutException:
            self.date_switcher(input_date)
        self.do_click(self.ok_btn)

    def new_move_in_ticket(self, hour):
        self.go_to_move_in()
        time.sleep(10)
        self.do_click(self.new_ticket_btn)
        time.sleep(0.5)
        fields = [(self.unit_member, self.unit_member_text),
                  (self.move_out_date, self.tickets_calendar(hour)),
                  (self.time_slot, self.time_slot_text_2),
                  self.book_inspection, self.assigned_technician_2, self.technician_name,
                  self.inspection_date, self.inspection_time, self.inspection_duration
                  ]
        for x in fields:
            if x[0] == self.move_out_date:
                try:
                    if self.is_visible(self.move_in_warning):
                        self.do_click(self.ok_btn)
                        time.sleep(1)
                except TimeoutException:
                    continue
                self.send_keys(x[0], x[1])
                time.sleep(0.5)
            elif x == self.book_inspection or x == self.assigned_technician_2 or x == self.technician_name:
                self.do_click(x)
                time.sleep(1.5)
            elif x == self.inspection_date:
                self.send_keys(x, self.date_calendar())
                time.sleep(0.5)
            elif x == self.inspection_time:
                self.send_keys(x, self.random_time_duration())
                time.sleep(0.5)
            elif x == self.inspection_duration:
                self.do_click(x)
                time.sleep(0.8)
                self.do_click(self.duration_option)
                time.sleep(1)
            else:
                self.send_keys(x[0], x[1])
                time.sleep(4)
                self.press_enter_web()
                time.sleep(0.5)
        clicks_2 = [self.create_btn, self.confirm_btn, self.ok_btn,
                    self.moving_type, self.select_moving_type, self.self_move, self.hold_harmless_2,
                    self.renters_insurance_tag, self.renters_insurance_2,
                    self.connect_utilities, self.connect_water_account
                    ]
        for y in clicks_2:
            self.scroll_to_location_web(y)
            if y == self.renters_insurance_2:
                self.send_keys(y, os.getcwd() + '/testpdf.pdf')
                time.sleep(4)
            elif y == self.hold_harmless_2:
                self.send_keys(y, os.getcwd() + '/testpdf.pdf')
                time.sleep(4)
            elif y == self.connect_water_account:
                self.clear(y)
                time.sleep(0.5)
                self.clear(self.connect_electric_account)
                self.send_keys(y, self.connect_water_account_text)
                self.send_keys(self.connect_electric_account, self.connect_electric_account_text)
                time.sleep(0.5)
            elif y == self.inspection_date:
                self.send_keys(y, self.date_calendar())
                time.sleep(0.5)
            elif y == self.inspection_time:
                self.send_keys(y, self.random_time_duration())
                time.sleep(0.5)
            else:
                self.do_click(y)
                time.sleep(1)
        self.move_in_id = self.get_ticket_id(self.mi_ticket_id)
        self.store_id(self.mi_id, self.move_in_id)
        self.do_click(self.complete_ticket_btn)
        time.sleep(0.5)
        self.do_click(self.confirm_btn)
        time.sleep(0.5)
        return self.is_visible(self.ok_btn)

    def cancel_move_out(self):
        time.sleep(3)
        self.do_click(self.ok_btn)
        move_out_id = self.id_fetch(self.mo_id)
        time.sleep(2)
        self.do_click(self.list_btn)
        time.sleep(2)
        self.do_click(self.id_tag)
        time.sleep(1.5)
        self.do_click(self.sort_arrow)
        time.sleep(1.5)
        ticket_id = self.get_text(self.table_ticket_id)
        if move_out_id == ticket_id:
            self.do_click(self.edit_ticket_icon)
            time.sleep(0.5)
        self.do_click(self.edit_ticket_tag)
        time.sleep(0.5)
        self.do_click(self.cancel_ticket)
        time.sleep(0.5)
        self.do_click(self.confirm_btn)
        time.sleep(0.5)
        return self.is_visible(self.ok_btn)

    def cancel_move_in(self):
        time.sleep(3)
        self.do_click(self.ok_btn)
        time.sleep(2)
        move_in_id = self.id_fetch(self.mi_id)
        time.sleep(0.5)
        self.do_click(self.list_btn)
        time.sleep(2)
        self.do_click(self.id_tag)
        time.sleep(1.5)
        self.do_click(self.sort_arrow)
        time.sleep(1.5)
        ticket_id = self.get_text(self.table_ticket_id)
        if move_in_id == ticket_id:
            self.do_click(self.edit_ticket_icon)
            time.sleep(0.5)
        self.do_click(self.edit_ticket_tag_2)
        time.sleep(0.5)
        self.do_click(self.cancel_ticket)
        time.sleep(0.5)
        self.do_click(self.confirm_btn)
        time.sleep(0.5)
        return self.is_visible(self.ok_btn)
