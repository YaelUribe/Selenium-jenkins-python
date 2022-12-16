import os
import json
import random
import pytest
from pages_web.staging.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import util.web_utils_staging as util
"""R&M tickets module for Manager, locators and actions"""


class RMTicketsManager(BasePage):
    """Locators"""
    all_tickets = (By.XPATH, "//button[contains(text(), 'All Tickets')]")
    open_tickets = (By.XPATH, "//button[contains(text(), 'Open Tickets')]")
    in_proposal = (By.XPATH, "//button[contains(text(), 'In Proposal')]")
    child_tickets = (By.XPATH, "//button[contains(text(), 'Child Tickets')]")
    create_new_rm = (By.XPATH, "//button[contains(text(), 'Create New Ticket')]")
    tickets_found = (By.XPATH, "//div/span[contains(text(), 'Tickets Found')]")
    select_ticket_type = (By.XPATH, "//ng-select[@formcontrolname='request_type']//div[@role='combobox']/input")
    in_unit_rm = (By.XPATH, "//ng-dropdown-panel//div[@class='ng-option ng-option-selected ng-star-inserted']")
    common_area_rm = (By.XPATH, "//ng-dropdown-panel//div[@class='ng-option ng-star-inserted']")
    create_btn = (By.XPATH, "//app-new-ticket-dialog//button[contains(text(), 'Create')]")
    select_member = (By.XPATH, "//app-tenant-dropdown/ng-select/div/div/div[2]/input")
    permission_to_enter = (By.XPATH, "//input[@class='ml-2']")
    select_category = (By.XPATH, "//ng-select[@formcontrolname='category_id']/div/div/div[2]")
    category_list = (By.XPATH, "//ng-select[@formcontrolname='category_id']/ng-dropdown-panel/div/div[2]/div")
    select_subcategory = (By.XPATH, "//ng-select[@formcontrolname='subcategory_id']/div/div/div[2]")
    subcategory_list = (By.XPATH, "//ng-select[@formcontrolname='subcategory_id']/ng-dropdown-panel/div/div[2]/div")
    ticket_details = (By.XPATH, "//textarea[@formcontrolname='detail']")
    add_image_icon = (By.XPATH, "//a[contains(text(), 'Add Image')]")
    file_input = (By.XPATH, "//input[@formcontrolname= 'attachment']")
    technician_select = (By.XPATH, "//ng-select[@formcontrolname='assignedTo']/div/div")
    technician_name = (By.XPATH, "//ng-dropdown-panel//span[contains(text(),'Automation Technician')]")
    date_input = (By.XPATH, "//input[@formcontrolname='tentativelyTechnicianWalkThroughDate']")
    time_input = (By.XPATH, "//input[@formcontrolname='tentativelyTechnicianWalkThroughTime']")
    duration_input = (By.XPATH, "//ng-select[@formcontrolname='technicianDuration']")
    duration_time = (By.XPATH, "//ng-dropdown-panel[@class='ng-dropdown-panel ng-star-inserted ng-select-top']/div/div/div[1]")
    unit_member = (By.XPATH, "//app-tenant-dropdown/ng-select/div/div/div[2]/input")
    create_ticket_btn = (By.XPATH, "//button[@type='submit'][contains(text(), 'Create')]")
    confirm_btn = (By.XPATH, "//button[contains(text(), 'Confirm')]")
    ok_btn = (By.XPATH, "//button[contains(text(), 'Ok')]")
    latest_ticket = (By.XPATH, "//table/tbody/tr[1]/td[7]/span")
    cancel_ticket_btn = (By.XPATH, "//button[contains(text(), 'Cancel Ticket')]")
    reason_to_cancel = (By.XPATH, "//textarea[@formcontrolname= 'diagnosticNotes']")
    labor_minutes = (By.XPATH, "//input[@formcontrolname= 'labour']")
    submit_btn = (By.XPATH, "//button[contains(text(), 'Submit')]")
    denied_entry_btn = (By.XPATH, "//button[contains(text(), 'Denied Entry')]")
    diagnostic_chckbx = (By.XPATH, "//form/div/div[3]/div[1]/div[2]/div[3]/label[1]/input")
    notes_txt_area = (By.XPATH, "//textarea[@formcontrolname='diagnosticNotes']")
    attachment_input = (By.XPATH, "//input[@formcontrolname= 'attachment']")
    complete_btn = (By.XPATH, "//button[contains(text(),'Complete')]")
    enter_btn = (By.XPATH, "//button[contains(text(),'Enter')]")
    item_input = (By.XPATH, "//input[@formcontrolname='item']")
    price_input = (By.XPATH, "//input[@formcontrolname='price']")
    w_n_t_checkbox = (By.XPATH, "//input[@formcontrolname='wt']")
    add_button = (By.XPATH, "//mat-icon[contains(text(),'add')]")
    proposal_btn = (By.XPATH, "//button[contains(text(), 'Proposal')]")
    filter_icon = (By.XPATH, "//button[@class='button is-light ml-2']")
    ticket_status_filter = (By.XPATH, "//ng-select[@formcontrolname='status']//div[@class='ng-value-container']")
    ticket_status_options = (By.XPATH, "//ng-dropdown-panel/div/div[2]/div")
    property_filter = (By.XPATH, "//ng-select[@formcontrolname='property']//div[@class='ng-select-container']")
    property_options = (By.XPATH, "//ng-dropdown-panel/div/div[2]/div")
    assigned_technician_filter = (By.XPATH, "//ng-select[@formcontrolname='assignedTechnician']//div[@class='ng-select-container']")
    assigned_technician_options = (By.XPATH, "//ng-dropdown-panel/div/div[2]/div")
    ticket_type_filter = (By.XPATH, "//ng-select[@formcontrolname='type']//div[@class='ng-select-container']")
    ticket_type_options = (By.XPATH, "//ng-dropdown-panel/div/div[2]/div")
    unit_member_filter = (By.XPATH, "//div/input[@formcontrolname='query']")
    filter_btn = (By.XPATH, "//button[contains(text(),'Filter')]")
    new_ticket_btn = (By.XPATH, "//button[contains(text(), 'New Ticket')]")
    select_category_2 = (By.XPATH, "//ng-select[@formcontrolname='category_id']//div[@role='combobox']")
    category_list_2 = (By.XPATH, "//ng-select[@formcontrolname='category_id']/ng-dropdown-panel/div/div[2]/div")
    select_subcategory_2 = (By.XPATH, "//ng-select[@formcontrolname='subcategory_id']/div/div/div[2]")
    subcategory_list_2 = (By.XPATH, "//ng-select[@formcontrolname='subcategory_id']/ng-dropdown-panel/div/div[2]/div")
    comment_text_area = (By.XPATH, "//textarea[@formcontrolname='comment']")
    comment_file_input = (By.XPATH, "//textarea[@formcontrolname='comment']")
    send_btn = (By.XPATH, "//button/span[contains(text(),'Send')]")
    success_note = (By.XPATH, "//app-display-comment-messages/div/div[2]/div")

    repair_maintenance_url = "https://staging.dvoraliving.com/m/work-orders/list"
    member_text = "Ashley Rathappillil"
    in_unit_text = "In Unit R&M"
    common_area_text = "Common Area R&M"
    cat_list = ['Inspection Deficiency']
    details_text = "Test new In Unit R&M ticket"
    unit_member_text = "Ashley Rathappillil"
    reason_to_cancel_text = "Cancelling ticket test"
    notes_area_text = "Denied entry Test"
    notes_area_text_2 = "Completing ticket Test"
    item_input_text = "Test Item for proposal"
    price_input_text = str(random.randint(50, 250))
    comment_text_area_text = "Test comment"
    hours_list = {'n_iu': "700A", 'n_ca': "730A", 'cancel_iu': "800A", 'cancel_ca': "830A",
                  'denied_ca': "900A", 'denied_iu': "930A", 'complete_ca': "1000A",
                  'complete_iu': "1030A", 'child_ti': "1100A", 'send_prop': "1130A", 'new_child': "1200P"}

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(util.base_url)

    def go_to_rm_tickets_page(self):
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
        self.driver.get(util.repair_maintenance_url)
        time.sleep(1)

    def new_in_unit_rm_ticket(self, hour):
        clicks_1 = [self.create_new_rm, (self.select_ticket_type, self.in_unit_text),
                    self.create_btn]
        time.sleep(0.5)
        for i in clicks_1:
            if type(i) is tuple and i[0] == self.select_ticket_type:
                self.send_keys(i[0], i[1])
                time.sleep(1)
                self.press_enter_web()
                time.sleep(0.5)
            else:
                self.do_click(i)
                time.sleep(0.5)
        clicks_2 = [self.unit_member,
                    self.permission_to_enter, self.select_category, self.select_subcategory,
                    self.ticket_details, self.add_image_icon, self.technician_select,
                    self.technician_name, self.date_input, self.time_input, self.duration_input,
                    self.duration_time, self.create_ticket_btn, self.confirm_btn
                    ]
        for x in clicks_2:
            self.scroll_to_location_web(x)
            if x == self.unit_member:
                self.send_keys(self.unit_member, self.unit_member_text)
                time.sleep(2)
                self.press_enter_web()
                time.sleep(0.5)
            elif x == self.permission_to_enter:
                toggle = self.checkbox_checker(x)
                if toggle is not None and toggle is False:
                    self.do_click(x)
                    time.sleep(0.5)
                else:
                    pass
            elif x == self.select_category or x == self.select_subcategory:
                self.do_click(x)
                time.sleep(0.5)
                if x == self.select_category:
                    self.click_single_random_option_web(self.category_list)
                    time.sleep(0.5)
                else:
                    self.click_single_random_option_web(self.subcategory_list)
                    time.sleep(0.5)
            elif x == self.ticket_details:
                self.send_keys(x, self.details_text)
                time.sleep(0.5)
            elif x == self.add_image_icon:
                self.do_click(x)
                time.sleep(0.5)
                self.send_keys(self.file_input, os.getcwd() + '/photo6.jpg')
                time.sleep(1)
            elif x == self.date_input:
                self.do_click(x)
                time.sleep(0.5)
                self.send_keys(x, self.date_calendar())
                time.sleep(0.5)
            elif x == self.time_input:
                self.do_click(x)
                time.sleep(0.5)
                self.send_keys(x, self.hours_list[hour])
                time.sleep(0.5)
            else:
                self.do_click(x)
                time.sleep(0.5)
        time.sleep(0.5)
        return self.is_visible(self.ok_btn)

    def new_common_rm_ticket(self, hour):
        clicks_1 = [self.create_new_rm, (self.select_ticket_type, self.common_area_text),
                    self.create_btn]
        time.sleep(0.5)
        for i in clicks_1:
            if type(i) is tuple and i[0] == self.select_ticket_type:
                self.send_keys(i[0], i[1])
                time.sleep(1)
                self.press_enter_web()
                time.sleep(0.5)
            else:
                self.do_click(i)
                time.sleep(0.5)
        clicks_2 = [self.unit_member,
                    self.permission_to_enter, self.select_category, self.select_subcategory,
                    self.ticket_details, self.add_image_icon, self.technician_select,
                    self.technician_name, self.date_input, self.time_input, self.duration_input,
                    self.duration_time, self.create_ticket_btn, self.confirm_btn
                    ]
        for x in clicks_2:
            self.scroll_to_location_web(x)
            if x == self.unit_member:
                self.send_keys(self.unit_member, self.unit_member_text)
                time.sleep(2)
                self.press_enter_web()
                time.sleep(0.5)
            elif x == self.permission_to_enter:
                toggle = self.checkbox_checker(x)
                if toggle is not None and toggle is True:
                    self.do_click(x)
                    time.sleep(0.5)
                else:
                    pass
            elif x == self.select_category or x == self.select_subcategory:
                self.do_click(x)
                time.sleep(0.5)
                if x == self.select_category:
                    self.click_single_random_option_web(self.category_list)
                    time.sleep(0.5)
                else:
                    self.click_single_random_option_web(self.subcategory_list)
                    time.sleep(0.5)
            elif x == self.ticket_details:
                self.send_keys(x, self.details_text)
                time.sleep(0.5)
            elif x == self.add_image_icon:
                self.do_click(x)
                time.sleep(0.5)
                self.send_keys(self.file_input, os.getcwd() + '/photo6.jpg')
                time.sleep(1)
            elif x == self.date_input:
                self.do_click(x)
                time.sleep(0.5)
                self.send_keys(x, self.date_calendar())
                time.sleep(0.5)
            elif x == self.time_input:
                self.do_click(x)
                time.sleep(0.5)
                self.send_keys(x, self.hours_list[hour])
                time.sleep(0.5)
            else:
                self.do_click(x)
                time.sleep(0.5)
        time.sleep(0.5)
        return self.is_visible(self.ok_btn)

    def cancel_in_unit_rm(self):
        self.do_click(self.ok_btn)
        time.sleep(3)
        self.do_click(self.latest_ticket)
        time.sleep(1)
        self.do_click(self.cancel_ticket_btn)
        time.sleep(0.5)
        self.send_keys(self.reason_to_cancel, self.reason_to_cancel_text)
        time.sleep(0.5)
        self.send_keys(self.labor_minutes, str(random.choice(range(5, 360, 5))))
        time.sleep(0.5)
        self.do_click(self.submit_btn)
        time.sleep(0.5)
        self.do_click(self.confirm_btn)
        time.sleep(0.5)
        return self.is_visible(self.ok_btn)

    def cancel_common_rm_ticket(self):
        self.do_click(self.ok_btn)
        time.sleep(3)
        self.do_click(self.latest_ticket)
        time.sleep(1)
        self.do_click(self.cancel_ticket_btn)
        time.sleep(0.5)
        self.send_keys(self.reason_to_cancel, self.reason_to_cancel_text)
        time.sleep(0.5)
        self.send_keys(self.labor_minutes, str(random.choice(range(5, 360, 5))))
        time.sleep(0.5)
        self.do_click(self.submit_btn)
        time.sleep(0.5)
        self.do_click(self.confirm_btn)
        time.sleep(0.5)
        return self.is_visible(self.ok_btn)

    def diened_entry_ticket(self):
        clicks = [self.ok_btn, self.latest_ticket, self.denied_entry_btn,
                  self.diagnostic_chckbx, self.notes_txt_area, self.labor_minutes,
                  self.attachment_input, self.complete_btn, self.confirm_btn]
        for x in clicks:
            if x == self.diagnostic_chckbx:
                toggle = self.checkbox_checker(x)
                if toggle is not None and toggle is False:
                    self.do_click(x)
                    time.sleep(0.5)
                else:
                    time.sleep(0.5)
            elif x == self.notes_txt_area:
                self.send_keys(x, self.notes_area_text)
                time.sleep(0.5)
            elif x == self.labor_minutes:
                self.send_keys(x, str(random.choice(range(5, 360, 5))))
                time.sleep(0.5)
            elif x == self.attachment_input:
                self.send_keys(x, os.getcwd() + '/photo1.jpeg')
                time.sleep(1)
            else:
                self.do_click(x)
                time.sleep(0.5)
        return self.is_visible(self.ok_btn)

    def complete_ticket(self):
        clicks = [self.ok_btn, self.latest_ticket, self.enter_btn,
                  self.confirm_btn, self.ok_btn, self.diagnostic_chckbx,
                  self.notes_txt_area, self.labor_minutes,
                  self.attachment_input, self.complete_btn, self.confirm_btn]
        for i in clicks:
            self.scroll_to_location_web(i)
            if i == self.diagnostic_chckbx:
                toggle = self.checkbox_checker(i)
                if toggle is not None and toggle is False:
                    self.do_click(i)
                    time.sleep(0.5)
                else:
                    time.sleep(0.5)
            elif i == self.notes_txt_area:
                self.send_keys(i, self.notes_area_text_2)
                time.sleep(0.8)
            elif i == self.labor_minutes:
                self.send_keys(i, str(random.choice(range(5, 360, 5))))
                time.sleep(0.8)
            elif i == self.attachment_input:
                self.send_keys(i, os.getcwd() + '/photo6.jpg')
                time.sleep(1)
            else:
                self.do_click(i)
                time.sleep(0.8)
        return self.is_visible(self.ok_btn)

    def send_proposal(self):
        clicks = [self.ok_btn, self.latest_ticket, self.enter_btn,
                  self.confirm_btn, self.ok_btn, self.diagnostic_chckbx,
                  self.notes_txt_area, self.labor_minutes, self.item_input,
                  self.attachment_input, self.proposal_btn, self.confirm_btn]
        for i in clicks:
            self.scroll_to_location_web(i)
            if i == self.diagnostic_chckbx:
                toggle = self.checkbox_checker(i)
                if toggle is not None and toggle is False:
                    self.do_click(i)
                    time.sleep(0.5)
                else:
                    time.sleep(0.5)
            elif i == self.notes_txt_area:
                self.send_keys(i, self.notes_area_text_2)
                time.sleep(0.5)
            elif i == self.labor_minutes:
                self.send_keys(i, str(random.choice(range(5, 360, 5))))
                time.sleep(0.5)
            elif i == self.item_input:
                x = random.randint(1, 5)
                for y in range(x):
                    self.send_keys(i, self.item_input_text)
                    time.sleep(0.5)
                    self.send_keys(self.price_input, self.price_input_text)
                    time.sleep(0.5)
                    toggle = self.checkbox_checker(self.w_n_t_checkbox)
                    if toggle is not None and toggle is True:
                        self.do_click(self.w_n_t_checkbox)
                        time.sleep(0.5)
                    else:
                        time.sleep(0.5)
                    self.do_click(self.add_button)
                    time.sleep(0.8)
            elif i == self.attachment_input:
                self.send_keys(i, os.getcwd() + '/photo6.jpg')
                time.sleep(1)
            else:
                self.do_click(i)
                time.sleep(0.5)
        return self.is_visible(self.ok_btn)

    def filter_by_ticket_status(self):
        clicks = [self.filter_icon, self.ticket_status_filter,
                  self.ticket_status_options, self.filter_btn]
        for x in clicks:
            if x == self.ticket_status_options:
                self.click_single_random_option_web(x)
                time.sleep(0.5)
            else:
                self.do_click(x)
                time.sleep(0.5)

    def filter_by_property(self):
        clicks = [self.filter_icon, self.property_filter,
                  self.property_options, self.filter_btn]
        for x in clicks:
            if x == self.property_options:
                self.click_single_random_option_web(x)
                time.sleep(0.5)
            else:
                self.do_click(x)
                time.sleep(0.5)

    def filter_by_assigned_technician(self):
        clicks = [self.filter_icon, self.assigned_technician_filter,
                  self.ticket_status_options, self.filter_btn]
        for x in clicks:
            if x == self.ticket_status_options:
                self.click_single_random_option_web(x)
                time.sleep(0.5)
            else:
                self.do_click(x)
                time.sleep(0.5)

    def filter_by_ticket_type(self):
        clicks = [self.filter_icon, self.ticket_type_filter,
                  self.ticket_status_options, self.filter_btn]
        for x in clicks:
            if x == self.ticket_type_options:
                self.click_single_random_option_web(x)
                time.sleep(0.5)
            else:
                self.do_click(x)
                time.sleep(0.5)

    def filter_by_unit_member(self):
        clicks = [self.filter_icon, self.ticket_status_filter,
                  self.filter_btn]
        for x in clicks:
            if x == self.ticket_type_filter:
                self.send_keys(x, self.member_text)
                time.sleep(0.5)
            else:
                self.do_click(x)
                time.sleep(0.5)

    def create_child_ticket(self, hour):
        clicks = [self.ok_btn, self.latest_ticket, self.enter_btn,
                  self.confirm_btn, self.ok_btn, self.diagnostic_chckbx,
                  self.notes_txt_area, self.labor_minutes,
                  self.attachment_input, self.new_ticket_btn, self.confirm_btn]
        for i in clicks:
            self.scroll_to_location_web(i)
            if i == self.diagnostic_chckbx:
                toggle = self.checkbox_checker(i)
                if toggle is not None and toggle is False:
                    self.do_click(i)
                    time.sleep(0.5)
                else:
                    time.sleep(0.5)
            elif i == self.notes_txt_area:
                self.send_keys(i, self.notes_area_text_2)
                time.sleep(0.5)
            elif i == self.labor_minutes:
                self.send_keys(i, str(random.choice(range(5, 360, 5))))
                time.sleep(0.5)
            elif i == self.attachment_input:
                self.send_keys(i, os.getcwd() + '/photo6.jpg')
                time.sleep(1)
            else:
                self.do_click(i)
                time.sleep(0.5)
        clicks_2 = [self.unit_member, self.permission_to_enter, self.select_category_2, self.select_subcategory_2,
                    self.ticket_details, self.add_image_icon, self.technician_select,
                    self.technician_name, self.date_input, self.time_input, self.duration_input,
                    self.duration_time, self.create_ticket_btn, self.confirm_btn
                    ]
        for x in clicks_2:
            self.scroll_to_location_web(x)
            if x == self.unit_member:
                self.send_keys(self.unit_member, self.unit_member_text)
                time.sleep(2)
                self.press_enter_web()
                time.sleep(0.5)
            elif x == self.permission_to_enter:
                toggle = self.checkbox_checker(x)
                if toggle is not None and toggle is False:
                    self.do_click(x)
                    time.sleep(0.5)
                else:
                    pass
            elif x == self.select_category_2 or x == self.select_subcategory_2:
                self.do_click(x)
                time.sleep(0.5)
                if x == self.select_category_2:
                    self.click_single_random_option_web(self.category_list_2)
                    time.sleep(0.5)
                else:
                    self.click_single_random_option_web(self.subcategory_list_2)
                    time.sleep(0.5)
            elif x == self.ticket_details:
                self.send_keys(x, self.details_text)
                time.sleep(0.5)
            elif x == self.add_image_icon:
                self.do_click(x)
                time.sleep(0.5)
                self.send_keys(self.file_input, os.getcwd() + '/photo6.jpg')
                time.sleep(1)
            elif x == self.date_input:
                self.do_click(x)
                time.sleep(0.5)
                self.send_keys(x, self.date_calendar())
                time.sleep(0.5)
            elif x == self.time_input:
                self.do_click(x)
                time.sleep(0.5)
                self.send_keys(x, self.hours_list[hour])
                time.sleep(0.5)
            else:
                self.do_click(x)
                time.sleep(0.5)
        time.sleep(0.5)
        return self.is_visible(self.ok_btn)

    def add_ce_notes(self):
        clicks = [self.latest_ticket, self.comment_text_area, self.comment_file_input, self.send_btn ]
        for i in clicks:
            self.scroll_to_location_web(i)
            if i == self.comment_text_area:
                self.send_keys(i, self.comment_text_area_text)
                time.sleep(0.5)
            elif i == self.comment_file_input:
                self.send_keys(i, os.getcwd() + '/photo6.jpg')
                time.sleep(0.5)
            else:
                self.do_click(i)
                time.sleep(0.5)
        return self.is_visible(self.success_note)
