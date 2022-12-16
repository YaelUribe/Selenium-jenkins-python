import os
import pytest
from pages_web.development.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import util.web_utils_development as util
"""Amenities module for tenant, specific locators and module actions"""


class AmenitiesTenant(BasePage):
    """Locators"""
    services_spaces = (By.XPATH, "//a[contains(text(), 'Services & Spaces')]")
    bike_storage = (By.XPATH, "//span[contains(text(), 'Bike Storage')]")
    already_bstorage = (By.XPATH, "//div[contains(text(), 'Bike Storage')]")
    price_btn = (By.XPATH, "//button[@class='button price is-primary']")
    end_date = (By.XPATH, "//input[@class='mat-datepicker-input input ng-untouched ng-pristine ng-valid'][@formcontrolname='endDate']")
    terms_conditions = (By.XPATH, "//input[@class='ng-untouched ng-pristine ng-invalid']")
    attach_file = (By.XPATH, "//input[@class='file-input ng-untouched ng-pristine ng-valid']")
    send_btn = (By.XPATH, "//button[@class='button'][contains(text(), 'Add File')]")
    ok_button = (By.XPATH, "//button[contains(text(), 'Ok')]")
    order_btn = (By.XPATH, "//button[@class='button is-primary'][contains(text(), 'Order')]")
    selected_plan = (By.XPATH, "//div[contains(text(), 'Selected Plan')]")
    accept_terms_conditions = (By.XPATH, "//label[@class='button is-white checkbox-button']/input")
    colab_membership_ = (By.XPATH, "//span[contains(text(), 'Colab Membership')]")
    message_tag = (By.XPATH, "//span[@class='service-status ng-star-inserted'][contains(text(), ' - See you soon ')]")
    select_plan = (By.XPATH, "//div[@class= 'pricing-options']//button")
    elevator = (By.XPATH, "//span[contains(text(), 'Elevator')]")
    confirmation_pop = (By.XPATH, "//div[contains(text(), 'Your Amenity reservation was successfully created')]")
    make_reservation = (By.XPATH, "//button[contains(text(), 'Make a reservation')]")
    full_calendar = (By.XPATH, "//full-calendar[@class='fc fc-media-screen fc-direction-ltr fc-theme-standard']")
    start_date_calendar = (By.XPATH, "//td[@class='fc-timegrid-slot fc-timegrid-slot-lane '][@data-time='10:00:00']")
    start_time_pool = (By.XPATH, "//td[@class='fc-timegrid-slot fc-timegrid-slot-lane '][@data-time='13:00:00']")
    end_time_pool = (By.XPATH, "//td[@class='fc-timegrid-slot fc-timegrid-slot-lane '][@data-time='14:00:00']")
    calendar_date_fitness_center = (By.XPATH, "//td[@class='fc-timegrid-slot fc-timegrid-slot-lane '][@data-time='11:00:00']")
    end_date_calendar = (By.XPATH, "//td[@class='fc-timegrid-slot fc-timegrid-slot-lane '][@data-time='14:00:00']")
    end_date_calendar2 = (By.XPATH, "//td[@class='fc-timegrid-slot fc-timegrid-slot-lane '][@data-time='12:00:00']")
    end_date_calendar_rooftop = (By.XPATH, "//td[@class='fc-timegrid-slot fc-timegrid-slot-lane '][@data-time='17:00:00']")
    text_area = (By.XPATH, "//textarea")
    submit_reservation = (By.XPATH, "//button[contains(text(), 'Submit Reservation')]")
    la_playa_pool = (By.XPATH, "//span[contains(text(), 'La Playa Pool')]")
    agree_terms = (By.XPATH, "//label[@class='button checkbox is-white']")
    price_season = (By.XPATH, "//button[@class= 'button price is-primary']")
    agree_terms_buy = (By.XPATH, "//label[@class='button is-white checkbox-button']")
    purchase_confirm = (By.XPATH, "//div[@class= 'dialog-message content']")
    open_parking = (By.XPATH, "//span[contains(text(), 'Open Parking')]")
    start_date = (By.XPATH, "//input[@class='mat-datepicker-input input ng-untouched ng-pristine ng-valid'][@formcontrolname='startDate']")
    rooftop = (By.XPATH, "//span[contains(text(), 'Rooftop')]")
    fitness_center = (By.XPATH, "//span[contains(text(), 'Fitness Center')]")
    next_week_arrow_calendar = (By.XPATH, "//button[@class='fc-next-button fc-button fc-button-primary']")
    no_spot_banner = (By.XPATH, "//app-service-space-booking//p[@class='notification is-danger ng-star-inserted']")
    limit_excedeed = (By.XPATH, "//div[contains(text(), 'User reservations limit exceeded')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(util.base_url)

    def go_to_amenities_page(self):
        """Go to Amenities module"""
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
        self.driver.get(util.tenant_amenities_url)
        time.sleep(1)

    def service_bikestorage(self):
        """Check/buy Bike Storage space"""
        try:
            self.do_click(self.bike_storage)
            time.sleep(2)
            try:
                self.do_click(self.price_btn)
                self.send_keys(self.attach_file, os.getcwd() + '/photo4.jpeg')
                time.sleep(2)
                self.send_keys(self.end_date, self.date_calendar())
                self.do_click(self.terms_conditions)
                try:
                    self.scroll_to_location_web(self.order_btn)
                    self.do_click(self.order_btn)
                    self.do_click(self.ok_button)
                except TimeoutException:
                    pytest.skip("No spots Available")
            except TimeoutException:
                if self.is_visible(self.already_bstorage):
                    pytest.skip("Space already booked")
        except TimeoutException:
            pytest.skip("Space unavailable at this moment")

    def colab_membership(self):
        try:
            self.do_click(self.colab_membership_)
            try:
                if self.is_visible(self.selected_plan):
                    pytest.skip("Space already booked")
                    time.sleep(2)
            except TimeoutException:
                self.click_random_option(self.select_plan)
                self.do_click(self.accept_terms_conditions)
                time.sleep(0.5)
                self.do_click(self.order_btn)
                return self.is_visible(self.ok_button)
        except TimeoutException:
            pytest.skip("Space unavailable at this moment")


    def s_elevator(self):
        self.do_click(self.elevator)
        time.sleep(2)
        self.do_click(self.make_reservation)
        time.sleep(2)
        self.do_click(self.next_week_arrow_calendar)
        time.sleep(2)
        self.drag_and_drop(self.start_date_calendar, self.end_date_calendar)
        time.sleep(1)
        self.do_click(self.submit_reservation)
        return self.is_visible(self.confirmation_pop)

    def s_la_playa_pool(self):
        self.do_click(self.la_playa_pool)
        time.sleep(0.5)
        try:
            self.do_click(self.price_season)
            time.sleep(2)
            self.do_click(self.agree_terms_buy)
            self.do_click(self.order_btn)
            time.sleep(2)
            return self.is_visible(self.purchase_confirm)
        except TimeoutException:
            self.do_click(self.make_reservation)
            time.sleep(2)
            # self.do_click(self.next_week_arrow_calendar)
            time.sleep(2)
            self.do_click(self.start_time_pool)
            time.sleep(1)
            self.do_click(self.submit_reservation)
            time.sleep(1)
            try:
                self.is_visible(self.limit_excedeed)
                pytest.skip("User Reservations limit Exceeded")
            except TimeoutException:
                return self.is_visible(self.confirmation_pop)


    def s_open_parking(self):
        try:
            self.scroll_to_location_web(self.open_parking)
            self.do_click(self.open_parking)
            time.sleep(2)
            try:

                self.send_keys(self.start_date, "11/15/2022")
                self.send_keys(self.end_date, "12/14/2022")
                self.do_click(self.terms_conditions)
                time.sleep(2)
                self.send_keys(self.attach_file, os.getcwd() + '/photo2.jpeg')
                time.sleep(2)
                self.do_click(self.order_btn)
                time.sleep(2)
                return self.is_visible(self.purchase_confirm)
            except TimeoutException:
                if self.is_visible(self.selected_plan):
                    pytest.skip("Open parking already purchased")
        except TimeoutException:
            pytest.skip("Space unavailable ath this moment")

    def s_rooftop(self):
        time.sleep(2)
        try:
            self.scroll_to_location_web(self.rooftop)
            time.sleep(1)
            self.do_click(self.rooftop)
            time.sleep(1)
            self.do_click(self.make_reservation)
            time.sleep(1)
            self.do_click(self.next_week_arrow_calendar)
            time.sleep(2)
            self.drag_and_drop(self.start_date_calendar, self.end_date_calendar_rooftop)
            time.sleep(1)
            self.do_click(self.submit_reservation)
            time.sleep(3)
            return self.is_visible(self.confirmation_pop)
        except TimeoutException:
            pytest.skip("Space unavailable at the moment")

    def s_fitness_center(self):
        try:
            self.scroll_to_location_web(self.fitness_center)
            self.do_click(self.fitness_center)
            time.sleep(1)
            try:
                self.click_random_option(self.select_plan)
                time.sleep(0.5)
                self.do_click(self.accept_terms_conditions)
                time.sleep(0.2)
                self.do_click(self.order_btn)
                return self.is_visible(self.ok_button)
            except TimeoutException:
                self.do_click(self.make_reservation)
                time.sleep(2)
                self.do_click(self.calendar_date_fitness_center)
                time.sleep(1)
                self.do_click(self.submit_reservation)
                time.sleep(3)
                return self.is_visible(self.confirmation_pop)
        except TimeoutException:
            pytest.skip("Space not available")
