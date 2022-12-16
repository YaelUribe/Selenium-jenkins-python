import random
from datetime import datetime
from pages_web.staging.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import os
import time
import util.web_utils_staging as util


class ReportsManager(BasePage):
    """Locators and constants"""
    all_reports = (By.XPATH, "//span[contains(text(), 'All Reports')]")
    create_custom_report_btn = (By.XPATH, "//button/span[contains(text(), 'Create Custom Report ')]")
    in_unit_ca_report = (By.XPATH, "//a[contains(text(), 'In Unit R&M & Common Area R&M')]")
    move_in_out_report = (By.XPATH, "//a[contains(text(), 'Move In & Move Out')]")
    turnover_report = (By.XPATH, "//a[contains(text(), 'Turnover')]")
    invoices_report = (By.XPATH, "//a[contains(text(), 'Invoices')]")
    a_la_carte_report = (By.XPATH, "//a[contains(text(), 'A la Carte')]")
    dry_cleaning_report = (By.XPATH, "//a[contains(text(), 'Dry Cleaning')]")
    packages_report = (By.XPATH, "//a[contains(text(), 'Packages')]")
    select_dates_tag = (By.XPATH, "//h2[contains(text(), 'Select Dates')]")
    start_date = (By.XPATH, "//input[@formcontrolname = 'start_date']")
    end_date = (By.XPATH, "//input[@formcontrolname = 'end_date']")
    property_tag = (By.XPATH, "//h2[contains(text(), 'Property')]")
    filter_by_property = (By.XPATH, "//ng-select[@formcontrolname = 'building_ids']")
    building_options = (By.XPATH, "//div[@role = 'option']")
    building_175_option = (By.XPATH, "//div[@role = 'option']/span[contains(text(),'DVORA 175')]")
    status_tag = (By.XPATH, "//h2[contains(text(), 'Status')]")
    filter_by_status = (By.XPATH, "//ng-select[@formcontrolname = 'status']")
    status_options = (By.XPATH, "//div[@role = 'option']")
    additional_attr_tag = (By.XPATH, "//h2[contains(text(), 'Additional Attributes')]")
    additional_attributes_checkbox = (By.XPATH, "//input[@type= 'checkbox']")
    generate_report_btn = (By.XPATH, "//button[contains(text(), 'Generate Report')]")
    name_custom_report = (By.XPATH, "//input[@formcontrolname = 'csv_name']")
    details_custom_report = (By.XPATH, "//input[@formcontrolname = 'description']")
    save_btn = (By.XPATH, "//button[contains(text(),'Save')]")
    ok_btn = (By.XPATH, "//button[contains(text(),'Ok')]")
    last_report = (By.XPATH, "//tbody/tr[1]/td[2]")

    report_type = {"unit": in_unit_ca_report, "moving": move_in_out_report, "turnover": turnover_report,
                   "invoices": invoices_report, "carte": a_la_carte_report, "dry": dry_cleaning_report,
                   "packages": packages_report}
    details_report = "Automation Test generated report"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(util.base_url)

    def go_to_reports_page(self):
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
        self.driver.get(util.manager_reports_url)
        time.sleep(4)

    def create_report(self, report_type):
        self.do_click(self.create_custom_report_btn)
        time.sleep(0.8)
        self.do_click(self.report_type[report_type])
        time.sleep(0.5)
        clicks = [self.select_dates_tag, self.start_date, self.property_tag, self.filter_by_property,
                  self.building_175_option, self.status_tag, self.filter_by_status, self.additional_attr_tag,
                  self.generate_report_btn]
        for x in clicks:
            if x == self.start_date:
                dates = self.reports_dates()
                self.do_click(x)
                time.sleep(1)
                self.clear(x)
                time.sleep(0.5)
                self.send_keys(x, dates[0])
                time.sleep(0.5)
                self.do_click(self.end_date)
                time.sleep(1)
                self.clear(self.end_date)
                time.sleep(0.5)
                self.send_keys(self.end_date, dates[1])
                time.sleep(0.7)
            elif x == self.filter_by_status:
                self.do_click(x)
                time.sleep(0.5)
                self.click_single_random_option_web(self.status_options)
                time.sleep(0.5)
            else:
                self.do_click(x)
                time.sleep(0.8)
        time.sleep(0.5)
        date_now = datetime.now()
        report_name = "Automation Custom Report " + "{}-{}-{}".format(date_now.month, date_now.day, date_now.year)
        actions = [(self.name_custom_report, report_name), (self.details_custom_report, self.details_report),
                   self.save_btn, self.ok_btn]
        for y in actions:
            if y[0] == self.name_custom_report or y[0] == self.details_custom_report:
                self.send_keys(y[0], y[1])
                time.sleep(0.5)
            else:
                self.do_click(y)
                time.sleep(0.8)
        report_name_2 = self.get_text(self.last_report)
        return report_name_2 == report_name + ".Csv"

    def create_random_report(self):
        self.do_click(self.create_custom_report_btn)
        time.sleep(0.8)
        self.do_click(random.choice(list(self.report_type.values())))
        time.sleep(0.5)
        clicks = [self.select_dates_tag, self.start_date, self.property_tag, self.filter_by_property,
                  self.status_tag, self.filter_by_status, self.additional_attr_tag,
                  self.generate_report_btn]
        for x in clicks:
            if x == self.start_date:
                dates = self.reports_dates()
                self.send_keys(self.start_date, dates[0])
                time.sleep(0.5)
                self.send_keys(self.end_date, dates[1])
                time.sleep(0.7)
            elif x == self.filter_by_property:
                self.do_click(x)
                time.sleep(0.5)
                self.click_random_option_web(self.building_options)
            elif x == self.filter_by_status:
                self.do_click(x)
                time.sleep(0.5)
                self.click_random_option_web(self.status_options)
                time.sleep(0.5)
            elif x == self.additional_attr_tag:
                self.do_click(x)
                time.sleep(0.5)
                self.click_random_option_web(self.additional_attributes_checkbox)
            else:
                self.do_click(x)
                time.sleep(0.8)
        time.sleep(0.5)
        date_now = datetime.now()
        report_name = "Automation Random Custom Report " + "{}-{}-{}".format(date_now.month, date_now.day, date_now.year)
        actions = [(self.name_custom_report, report_name), (self.details_custom_report, self.details_report),
                   self.save_btn, self.ok_btn]
        for y in actions:
            if y[0] == self.name_custom_report or y[0] == self.details_custom_report:
                self.send_keys(y[0], y[1])
                time.sleep(0.5)
            else:
                self.do_click(y)
                time.sleep(0.8)
        report_name_2 = self.get_text(self.last_report)
        return report_name_2 == report_name + ".Csv"
