from pages_web.staging.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from util import web_utils_staging as util

"""Login page actions"""


class LoginPage(BasePage):
    """Class LoginPage, contains methods to execute in such module"""
    email = (By.XPATH, "//input[@formcontrolname='email']")
    password = (By.XPATH, "//input[@formcontrolname='password']")
    forgot_password = (By.XPATH, "//a[contains(text(), 'Forgot password?')]")
    terms_conditions = (By.LINK_TEXT, "Terms & Conditions")
    privacy_policy = (By.LINK_TEXT, "Privacy Policy")
    faqs = (By.LINK_TEXT, "Frequently Asked Questions")
    err_msj = (By.XPATH, "//span[contains(text(), 'Incorrect username or password.')]")
    close_err_button = (By.XPATH, "//button[@class= 'delete']")
    sumbit_button = (By.XPATH, "//button[contains(text(),'Submit')]")
    back_to_login = (By.XPATH, "//a[contains(text(),'Back  to Login')]")
    invalid_email = (By.XPATH, "//span[contains(text(),'invalid user')]")
    close_invalid_email = (By.XPATH, "//button[@class= 'delete']")
    next_btn = (By.XPATH, "//button[contains(text(), 'Next')]")
    wrong_email_err = (By.XPATH, "//span[contains(text(), 'invalid user')]")
    wrong_pass_err = (By.XPATH, "//span[contains(text(), 'Incorrect username or password.')]")
    reset_sent = (By.XPATH, "//a[contains(text(),'Back to Login')]")
    logout_btn = (By.XPATH, "//span[contains(text(), 'Log out')]")
    confirm_btn = (By.XPATH, "//button[contains(text(),'Confirm')]")

    tenant_email = "ashleyratha@g8p3c.com"
    tenant_pass = "Dvora123456!"
    wrong_email = "abc@ab.com"
    wrong_pass = "12344321"
    login_page_title = "DVORA | Welcome to your place"

    def __init__(self, driver):
        """Constructor for Class LoginPage"""
        super().__init__(driver)
        self.driver.get(util.base_url)

    def get_login_page_title(self, title):
        """get page title"""
        return self.get_title(title)

    def go_to_login_page(self):
        self.go_to_address(util.base_url)

    def forgot_pass_link_exists(self):
        """Check availability of forgot password"""
        return self.is_visible(self.forgot_password)

    def login_error_msj(self, by_locator):
        """wrong login message"""
        return self.is_visible(by_locator)

    def login(self):
        """login method"""
        self.send_keys(self.email, self.tenant_email)
        self.do_click(self.next_btn)
        time.sleep(0.8)
        self.send_keys(self.password, self.tenant_pass)
        self.do_click(self.next_btn)
        time.sleep(2)
        assert self.is_visible(util.home_icon)
        self.do_click(self.logout_btn)
        time.sleep(0.5)
        self.do_click(self.confirm_btn)
        time.sleep(1)
        return self.is_visible(self.email)

    def wrong_user_login(self):
        self.send_keys(self.email, self.wrong_email)
        self.do_click(self.next_btn)
        time.sleep(0.5)
        return self.is_visible(self.wrong_email_err)

    def wrong_pass_login(self):
        self.send_keys(self.email, self.tenant_email)
        self.do_click(self.next_btn)
        time.sleep(0.8)
        self.send_keys(self.password, self.wrong_pass)
        self.do_click(self.next_btn)
        time.sleep(2)
        return self.is_visible(self.wrong_pass_err)

    def reset_password(self):
        self.do_click(self.forgot_password)
        time.sleep(0.5)
        self.send_keys(self.email, self.wrong_email)
        self.press_enter_web()
        time.sleep(0.5)
        flag = self.is_visible(self.invalid_email)
        assert flag
        self.do_click(self.close_invalid_email)
        time.sleep(0.5)
        self.clear(self.email)
        self.send_keys(self.email, self.tenant_email)
        self.press_enter_web()
        time.sleep(0.8)
        return self.is_visible(self.reset_sent)

