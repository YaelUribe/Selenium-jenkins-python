import pytest
from selenium.webdriver.common.keys import Keys
import util.web_utils_development as util
from pages_web.development.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver import ActionChains

"""Events module actions for Manager"""


class EventsManager(BasePage):
    """Locators & Methods for Manager"""
    event_list = (By.XPATH, "//app-events-list//div[@class= 'section-content has-padding ng-star-inserted']/div/div")
    event_list_tag = (By.XPATH, "//h1[contains(text(), 'Event List')]")
    event_bookings = (By.XPATH, "//a[contains(text(), 'Event Bookings')]")
    create_event_booking = (By.XPATH, "//a[contains(text(), 'Create Event Booking')]")
    add_event = (By.XPATH, "//a[contains(text(), 'Add Event')]")
    upcoming_events = (By.XPATH, "//span[contains(text(), 'Upcoming')]")
    past_events = (By.XPATH, "//span[contains(text(), 'Past')]")
    filter_events = (By.XPATH, "//button[contains(text(), 'Filter')]")
    filter_arrow = (By.CSS_SELECTOR, "span.ng-arrow-wrapper")
    no_events_icon = (By.XPATH, "//*[@id='Layer_1']")
    view_details = (By.XPATH, "//span[contains(text(), 'View Details')]")
    events_booked_index = (By.CSS_SELECTOR, "tr.clickable")
    select_property_locator = (By.XPATH, "//ng-select[@formcontrolname='building_id']//div[@class='ng-value-container']")
    select_resident = (By.CSS_SELECTOR, "ng-select[bindlabel='nameWithUnit']")
    select_event = (By.CSS_SELECTOR, "ng-select[bindlabel='title']")
    assistants = (By.XPATH, "input[formcontrolname='assistants']")
    create_event_booking_button = (By.CSS_SELECTOR, "button.button.is-primary")
    back_button = (By.CSS_SELECTOR, "a.button.is-white.back-button")
    event_title = (By.XPATH, "//input[@formcontrolname='title']")
    event_properties = (By.XPATH, "//app-events-create//ng-select//input")
    free_event_price = (By.XPATH, "//span[contains(text(), 'Free')]")
    paid_event_price = (By.XPATH, "//input[contains(text(), 'Paid')]")
    event_link = (By.CSS_SELECTOR, "input[formcontrolname='event_link']")
    event_capacity = (By.CSS_SELECTOR, "input[formcontrolname='capacity']")
    start_date = (By.XPATH, "//input[@formcontrolname= 'startDate']")
    start_date_time = (By.CSS_SELECTOR, "input[formcontrolname='startTime']")
    end_date = (By.XPATH, "//input[@formcontrolname= 'endDate']")
    end_date_next_month = (By.CSS_SELECTOR, "button.mat-focus-indicator.mat-calendar-next-button.mat-icon-button.mat-button-base")
    end_date_time = (By.CSS_SELECTOR, "input[formcontrolname='endTime']")
    location_address = (By.CSS_SELECTOR, "input[formcontrolname='address']")
    city = (By.CSS_SELECTOR, "input[formcontrolname='city']")
    state = (By.CSS_SELECTOR, "input[formcontrolname='state']")
    zipcode = (By.CSS_SELECTOR, "input[formcontrolname='zip']")
    event_category = (By.CSS_SELECTOR, "ng-select[formcontrolname='event_type_ids']")
    community_toggle = (By.CSS_SELECTOR, "input[name='is_community']")
    allow_bookings = (By.CSS_SELECTOR, "input[formcontrolname='is_booking_active']")
    event_description = (By.CSS_SELECTOR, "div[role='textbox']")
    input_photos = (By.CSS_SELECTOR, "input[formcontrolname='attachmentCropTool']")
    dvora_175_locator = (By.XPATH, "//span[contains(text(), 'DVORA 175')]")
    options_locators = (By.XPATH, "//ng-dropdown-panel//div[@role='option']")
    resident_options_locator = (By.XPATH, "//div[@class='ng-dropdown-panel-items scroll-host']")
    event_booked_successfully_locator = (By.XPATH, "//div[contains(text(), 'The event booking was created successfully')]")
    ok_button = (By.XPATH, "//button[contains(text(), 'Ok')]")
    number_calendar = (By.XPATH, "//div[contains(text(), '15')]")
    event_create_successfully = (By.XPATH, "//div[contains(text(), 'The event was created successfully')]")
    create_event_button = (By.XPATH, "//button[contains(text(), 'Create Event')]")
    delete_button = (By.CSS_SELECTOR, "button.button.is-danger")
    confirm_button = (By.XPATH, "//button[contains(text(), 'Confirm')]")
    event_successfully_delete = (By.XPATH, "//div[contains(text(), 'Event Deleted')]")
    err_message = (By.XPATH, "//app-simple-dialog/div/div[1]/div")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(util.base_url)
        time.sleep(1)
        self.go_to_events_page()

    def go_to_events_page(self):
        """Go to events module"""
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
        self.driver.get(util.manager_events_url)
        time.sleep(3)

    def click_event_list(self):
        self.do_click(self.event_list)

    def click_event_booking(self):
        time.sleep(1)
        self.do_click(self.event_bookings)

    def click_create_event_booking(self):
        time.sleep(2)
        self.do_click(self.create_event_booking)

    def click_add_event(self):
        time.sleep(1)
        self.do_click(self.add_event)

    def filter_past_event(self):
        time.sleep(1)
        self.do_click(self.filter_arrow)
        time.sleep(1)
        self.do_click(self.past_events)
        time.sleep(1)
        self.do_click(self.filter_events)

    def filter_upcoming_event(self):
        self.do_click(self.filter_arrow)
        time.sleep(1)
        self.do_click(self.upcoming_events)
        time.sleep(1)
        self.do_click(self.filter_events)

    def are_events_displayed(self):
        time.sleep(1)
        try:
            return self.is_visible(self.event_list)
        except TimeoutException:
            pytest.skip("No events available")

    def are_event_bookings_displayed(self):
        time.sleep(1)
        try:
            return self.is_visible(self.events_booked_index)
        except TimeoutException:
            pytest.skip("There are no event bookings")

    def click_create_booking(self):
        self.do_click(self.create_event_booking)

    def create_event_booking_add_random_choices(self):
        time.sleep(1)
        self.do_click(self.select_property_locator)
        time.sleep(1)
        self.scroll_to_location(self.dvora_175_locator)
        time.sleep(1)
        self.do_click(self.dvora_175_locator)
        time.sleep(5)
        self.do_click(self.select_resident)
        time.sleep(2)
        self.click_random_option_web(self.resident_options_locator)
        self.press_escape()
        time.sleep(2)
        self.do_click(self.select_event)
        time.sleep(1)
        self.do_click(self.options_locators)
        time.sleep(1)
        self.do_click(self.create_event_booking_button)
        time.sleep(1)

    def is_event_successfully_booked_popup_displayed(self):
        return self.is_visible(self.event_booked_successfully_locator)

    def click_ok(self):
        self.do_click(self.ok_button)
        time.sleep(1)

    def add_details_create_event(self):
        actions = [
            (self.event_title, "Automation Test Event"), (self.event_properties, "DVORA 175"),
            (self.event_link, "https://testautomationu.applitools.com/"),
            (self.event_capacity, "100"), (self.start_date, self.date_calendar()),
            (self.start_date_time, "1000A"), (self.end_date, self.date_calendar_2("event")),
            (self.end_date_time, "1000P"), (self.location_address, "175 2nd St"),
            (self.city, "Jersey City"), (self.state, "New York"), (self.zipcode, "07302"),
            self.event_category, (self.event_description, "Test Automation ")
        ]
        for filler in actions:
            if filler == (self.event_properties, "DVORA 175"):
                self.send_keys(filler[0], filler[1])
                time.sleep(0.5)
                self.press_enter_web()
                time.sleep(0.5)
                self.press_escape()
                time.sleep(0.6)
            elif filler == self.event_category:
                self.do_click(filler)
                time.sleep(0.5)
                self.click_random_option(self.options_locators)
                time.sleep(1)
            else:
                self.send_keys(filler[0], filler[1])
                time.sleep(0.8)
        time.sleep(1)
        self.do_click(self.create_event_button)
        time.sleep(1)

    def is_event_successfully_created_popup_displayed(self):
        return self.is_visible(self.event_create_successfully)

    def click_delete_event(self):
        self.do_click(self.delete_button)
        time.sleep(1)
        self.do_click_2(self.confirm_button)
        try:
            assert self.is_visible(self.err_message)
            pytest.skip("Can't destroy event with bookings!")
        except TimeoutException:
            time.sleep(1)

    def is_event_successfully_deleted_displayed(self):
        return self.is_visible(self.event_successfully_delete)

    def click_view_details(self):
        time.sleep(1)
        self.do_click_at_index(self.view_details, 1)

    def click_confirm_button(self):
        time.sleep(1)
        self.do_click(self.confirm_button)
