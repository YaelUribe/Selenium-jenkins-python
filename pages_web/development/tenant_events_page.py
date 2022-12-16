from pages_web.development.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException
from util import web_utils_development as util
"""Events module actions"""


class EventsPage(BasePage):
    """Methods to execute in events module as Tenant"""
    email = (By.CSS_SELECTOR, "input[placeholder='Email']")
    password = (By.CSS_SELECTOR, "input[placeholder='Password']")
    login_button = (By.CSS_SELECTOR, "button.button.is-fullwidth.is-primary")
    forgot_password = (By.CSS_SELECTOR, "a.button.is-white.is-small")
    terms_conditions = (By.LINK_TEXT, "Terms & Conditions")
    privacy_policy = (By.LINK_TEXT, "Privacy Policy")
    faqs = (By.LINK_TEXT, "Frequently Asked Questions")
    home_icon = (By.XPATH, "//span[contains(text(), 'Home')]")
    events_icon = (By.XPATH, "//span[contains(text(),'Events')]")
    no_events_available = (By.XPATH, "//*[@id='resident-scrolling-reference']/section/div/app-events-root/app-events-list/div/app-empty-section-card/div/div/figure")
    no_bookings_available = (By.XPATH, "//app-empty-section-card/div/div/h2")
    list = (By.XPATH, "//a[contains(text(), 'List')]")
    bookings = (By.XPATH, "//a[contains(text(), 'Bookings')]")
    event_1 = (By.XPATH, "//span[contains(text(), 'View Details')]")
    attending_button = (By.XPATH, "//button[contains(text(),'Yes')]")
    confirm_guest_btn = (By.XPATH, "//button[contains(text(),'Yes, Continue')]")
    cancel_guest_btn = (By.XPATH, "//button[contains(text(),'No, cancel')]")
    add_guest_btn = (By.XPATH, "//button[contains(text(),'+')]")
    minus_guest_btn = (By.XPATH, "//button[contains(text(),'-')]")
    ok_button = (By.XPATH, "//button[contains(text(), 'Ok')]")
    booking_selector_upcoming = (By.XPATH, "//span[contains(text(), 'Upcoming')]")
    booking_selector_past = (By.XPATH, "//span[contains(text(), 'Past')]")
    booking_selector = (By.XPATH, "//div[@class='ng-input']")
    view_details = (By.XPATH, "//span[contains(text(), 'View Details')]")
    cancel_booking = (By.XPATH, "//button[contains(text(), 'Cancel Booking')]")

    tenant_email = "ashleyratha@g8p3c.com"
    tenant_pass = "Dvora123456!"
    base_url = "http://development.dvoraliving.com/login"
    events_url = "http://development.dvoraliving.com/r/events/list"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.base_url)

    def login(self, email, password):
        """Login method"""
        self.send_keys(self.email, email)
        self.send_keys(self.password, password)
        self.do_click(self.login_button)

    def go_to_events_page(self):
        """Go to events module"""
        try:
            self.is_visible(self.home_icon)
        except TimeoutException:
            self.send_keys(util.email_locator, util.tenant_email)
            self.do_click(util.next_btn)
            time.sleep(0.8)
            self.send_keys(util.password_locator, util.tenant_password)
            self.do_click(util.next_btn)
            time.sleep(2)
        time.sleep(9)
        self.driver.get(self.events_url)
        time.sleep(3)

    def list_visible(self):
        """Check on visibility for List"""
        return self.is_visible(self.list)

    def booking_visible(self):
        return self.is_visible(self.bookings)

    def select_event_from_list(self):
        """Clicking on an event from list"""
        self.do_click(self.event_1)
        time.sleep(1)

    def book_event_from_list(self):
        self.do_click(self.attending_button)
        self.do_click(self.add_guest_btn)
        time.sleep(1)
        self.do_click(self.minus_guest_btn)
        time.sleep(1)
        self.do_click(self.confirm_guest_btn)
        time.sleep(1)

    def go_to_bookings(self):
        """ click on bookings"""
        self.do_click(self.bookings)
        time.sleep(1)

    def go_to_past_bookings(self):
        self.do_click(self.booking_selector)
        time.sleep(1)
        self.do_click(self.booking_selector_past)
        time.sleep(1)

    def cancel_upcoming_booking(self):
        self.do_click(self.view_details)
        time.sleep(1)
        self.do_click(self.cancel_booking)
        time.sleep(1)
        self.do_click(self.ok_button)
