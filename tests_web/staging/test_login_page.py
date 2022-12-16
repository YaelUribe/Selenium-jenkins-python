from pages_web.staging.login_page import LoginPage
from tests_web.staging.test_base_page import BaseTest


class TestLogin(BaseTest):
    """"""
    def test_forgot_pass_link_exists(self):
        self.login_page = LoginPage(self.driver)
        assert self.login_page.forgot_pass_link_exists()

    def test_login_page_title(self):
        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_title(LoginPage.login_page_title)
        assert title == LoginPage.login_page_title

    def test_login(self):
        self.login_page = LoginPage(self.driver)
        assert self.login_page.login()

    def test_login_wrong_username(self):
        self.login_page = LoginPage(self.driver)
        assert self.login_page.wrong_user_login()

    def test_login_wrong_pass(self):
        self.login_page = LoginPage(self.driver)
        assert self.login_page.wrong_pass_login()

    def test_faqs(self):
        self.login_page = LoginPage(self.driver)
        assert self.login_page.is_visible(LoginPage.faqs)
        self.login_page.do_click(LoginPage.faqs)

    def test_privacy_policy(self):
        self.login_page = LoginPage(self.driver)
        assert self.login_page.is_visible(LoginPage.privacy_policy)
        self.login_page.do_click(LoginPage.privacy_policy)

    def test_terms_and_conditions(self):
        self.login_page = LoginPage(self.driver)
        assert self.login_page.is_visible(LoginPage.terms_conditions)
        self.login_page.do_click(LoginPage.terms_conditions)

    def test_forgot_password(self):
        self.login_page = LoginPage(self.driver)
        assert self.login_page.reset_password()
