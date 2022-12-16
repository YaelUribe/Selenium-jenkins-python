from pages_web.login_page import LoginPage
from tests_web.test_base_page import BaseTest


class TestLogin(BaseTest):
    """"""
    def test_forgot_pass_link_exists(self):
        self.login_page = LoginPage(self.driver)
        flag = self.login_page.forgot_pass_link_exists()
        assert flag

    def test_login_page_title(self):
        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_title(LoginPage.login_page_title)
        assert title == LoginPage.login_page_title

    def test_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login(LoginPage.tenant_email, LoginPage.tenant_pass)

    def test_login_wrong_username(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login(LoginPage.wrong_email, LoginPage.wrong_pass)  # it doesn't make any difference
        self.login_page.login_error_msj(LoginPage.err_msj)                  # in this particular test
        self.login_page.login_error_msj(LoginPage.password)
        self.login_page.do_click(LoginPage.close_err_button)

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
        self.login_page.is_visible(LoginPage.forgot_password)
        self.login_page.do_click(LoginPage.forgot_password)
        flag = self.login_page.is_visible(LoginPage.forgot_password_email)
        assert flag
        flag = self.login_page.is_visible(LoginPage.sumbit_button)
        assert flag
        flag = self.login_page.is_visible(LoginPage.back_to_login)
        assert flag
        self.login_page.send_keys(LoginPage.forgot_password_email, LoginPage.wrong_email)
        self.login_page.do_click(LoginPage.sumbit_button)
        flag = self.login_page.is_visible(LoginPage.invalid_email)
        assert flag
        self.login_page.do_click(LoginPage.close_invalid_email)
        self.login_page.send_keys(LoginPage.forgot_password_email, LoginPage.tenant_email)
        self.login_page.do_click(LoginPage.sumbit_button)
        flag = self.login_page.is_visible(LoginPage.back_to_login)
        assert flag
        self.login_page.do_click(LoginPage.back_to_login)
