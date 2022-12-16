import time
from pages_web.development.tenant_visitors_page import VisitorsTenant
from tests_web.development.test_base_page import BaseTest


class TestVisitorsTenant(BaseTest):
    """Tests module for tenant's Visitors Module"""

    def test_go_to_visitors_page(self):
        self.visitors_page = VisitorsTenant(self.driver)
        self.visitors_page.go_to_visitors_page()
        time.sleep(0.5)
        assert self.visitors_page.is_visible(VisitorsTenant.new_visitor_btn)

    def test_new_visitor(self):
        self.visitors_page = VisitorsTenant(self.driver)
        self.visitors_page.go_to_visitors_page()
        assert self.visitors_page.new_visitor()

    def test_see_visitor_info(self):
        self.visitors_page = VisitorsTenant(self.driver)
        self.visitors_page.go_to_visitors_page()
        assert self.visitors_page.see_visitor_info()
