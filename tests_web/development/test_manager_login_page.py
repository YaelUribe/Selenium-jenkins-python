from pages_web.development.manager_login_page import ManagerLoginPage
from tests_web.development.test_base_page import BaseTest


class TestLogin(BaseTest):
    """"""
    def test_forgot_pass_link_exists(self):
        self.login_page = ManagerLoginPage(self.driver)
        flag = self.login_page.forgot_pass_link_exists()
        assert flag

    def test_login_page_title(self):
        self.login_page = ManagerLoginPage(self.driver)
        title = self.login_page.get_title(ManagerLoginPage.login_page_title)
        assert title == ManagerLoginPage.login_page_title

    def test_login_wrong_username(self):
        self.login_page = ManagerLoginPage(self.driver)
        assert self.login_page.wrong_user_login()

    def test_login_wrong_pass(self):
        self.login_page = ManagerLoginPage(self.driver)
        assert self.login_page.wrong_pass_login()

    def test_faqs(self):
        self.login_page = ManagerLoginPage(self.driver)
        assert self.login_page.is_visible(ManagerLoginPage.faqs)
        self.login_page.do_click(ManagerLoginPage.faqs)

    def test_privacy_policy(self):
        self.login_page = ManagerLoginPage(self.driver)
        assert self.login_page.is_visible(ManagerLoginPage.privacy_policy)
        self.login_page.do_click(ManagerLoginPage.privacy_policy)

    def test_terms_and_conditions(self):
        self.login_page = ManagerLoginPage(self.driver)
        assert self.login_page.is_visible(ManagerLoginPage.terms_conditions)
        self.login_page.do_click(ManagerLoginPage.terms_conditions)

    def test_forgot_password(self):
        self.login_page = ManagerLoginPage(self.driver)
        assert self.login_page.reset_password()

    def test_login(self):
        self.login_page = ManagerLoginPage(self.driver)
        assert self.login_page.login()

