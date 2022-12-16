from pages_web.manager_login_page import ManagerLoginPage
from tests_web.test_base_page import BaseTest


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

    def test_login(self):
        self.login_page = ManagerLoginPage(self.driver)
        self.login_page.login(ManagerLoginPage.manager_email, ManagerLoginPage.manager_pass)

    def test_login_wrong_username(self):
        self.login_page = ManagerLoginPage(self.driver)
        self.login_page.login(ManagerLoginPage.wrong_email, ManagerLoginPage.wrong_pass)  # it doesn't make any difference
        self.login_page.login_error_msj(ManagerLoginPage.err_msj)                  # in this particular test
        self.login_page.login_error_msj(ManagerLoginPage.password)
        self.login_page.do_click(ManagerLoginPage.close_err_button)

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
        self.login_page.is_visible(ManagerLoginPage.forgot_password)
        self.login_page.do_click(ManagerLoginPage.forgot_password)
        flag = self.login_page.is_visible(ManagerLoginPage.forgot_password_email)
        assert flag
        flag = self.login_page.is_visible(ManagerLoginPage.sumbit_button)
        assert flag
        flag = self.login_page.is_visible(ManagerLoginPage.back_to_login)
        assert flag
        self.login_page.send_keys(ManagerLoginPage.forgot_password_email, ManagerLoginPage.wrong_email)
        self.login_page.do_click(ManagerLoginPage.sumbit_button)
        flag = self.login_page.is_visible(ManagerLoginPage.invalid_email)
        assert flag
        self.login_page.do_click(ManagerLoginPage.close_invalid_email)
        self.login_page.send_keys(ManagerLoginPage.forgot_password_email, ManagerLoginPage.manager_email)
        self.login_page.do_click(ManagerLoginPage.sumbit_button)
        flag = self.login_page.is_visible(ManagerLoginPage.back_to_login)
        assert flag
        self.login_page.do_click(ManagerLoginPage.back_to_login)
