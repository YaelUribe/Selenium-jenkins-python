import pytest
from pages_web.staging.manager_visitors_page import VisitorsManager
from tests_web.staging.test_base_page import BaseTest


class TestVisitorsTenant(BaseTest):
    """Tests Module for manager's Visitors module"""

    def test_go_to_visitors_page(self):
        self.visitors_page = VisitorsManager(self.driver)
        self.visitors_page.go_to_visitors_page()
        assert self.visitors_page.is_visible(VisitorsManager.new_visitor_btn)

    def test_see_visitor_info_manager(self):
        self.visitors_page = VisitorsManager(self.driver)
        self.visitors_page.go_to_visitors_page()
        assert self.visitors_page.see_visitor_info()
