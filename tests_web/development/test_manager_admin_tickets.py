from pages_web.development.manager_admin_tickets import AdminTicketsManager
from tests_web.development.test_base_page import BaseTest


class TestAdminTicketsManager(BaseTest):
    """Test suite for Manager's Admin tickets"""

    def test_go_to_admin_tickets_page(self):
        self.manager_admin_ticket = AdminTicketsManager(self.driver)
        self.manager_admin_ticket.go_to_admin_tickets_page()
        assert self.manager_admin_ticket.is_visible(AdminTicketsManager.all_tickets_tag)

    def test_filter_by_category(self):
        self.manager_admin_ticket = AdminTicketsManager(self.driver)
        self.manager_admin_ticket.go_to_admin_tickets_page()
        assert self.manager_admin_ticket.filter_by_category()

    def test_filter_by_status(self):
        self.manager_admin_ticket = AdminTicketsManager(self.driver)
        self.manager_admin_ticket.go_to_admin_tickets_page()
        assert self.manager_admin_ticket.filter_by_status()

    def test_filter_by_advanced(self):
        self.manager_admin_ticket = AdminTicketsManager(self.driver)
        self.manager_admin_ticket.go_to_admin_tickets_page()
        assert self.manager_admin_ticket.filter_by_advanced()

    def test_filter_by_own_category(self):
        self.manager_admin_ticket = AdminTicketsManager(self.driver)
        self.manager_admin_ticket.go_to_admin_tickets_page()
        assert self.manager_admin_ticket.filter_by_own_category()

    def test_filter_by_own_status(self):
        self.manager_admin_ticket = AdminTicketsManager(self.driver)
        self.manager_admin_ticket.go_to_admin_tickets_page()
        assert self.manager_admin_ticket.filter_by_own_status()

    def test_filter_by_own_advanced(self):
        self.manager_admin_ticket = AdminTicketsManager(self.driver)
        self.manager_admin_ticket.go_to_admin_tickets_page()
        assert self.manager_admin_ticket.filter_by_own_advanced()

    def test_new_admin_ticket(self):
        self.manager_admin_ticket = AdminTicketsManager(self.driver)
        self.manager_admin_ticket.go_to_admin_tickets_page()
        assert self.manager_admin_ticket.new_admin_ticket()

    def test_complete_admin_ticket(self):
        self.manager_admin_ticket = AdminTicketsManager(self.driver)
        self.manager_admin_ticket.go_to_admin_tickets_page()
        assert self.manager_admin_ticket.new_admin_ticket()
        assert self.manager_admin_ticket.complete_admin_ticket()

    def test_cancel_admin_ticket(self):
        self.manager_admin_ticket = AdminTicketsManager(self.driver)
        self.manager_admin_ticket.go_to_admin_tickets_page()
        assert self.manager_admin_ticket.new_admin_ticket()
        assert self.manager_admin_ticket.cancel_admin_ticket()
