from pages_web.development.manager_rm_tickets_page import RMTicketsManager
from tests_web.development.test_base_page import BaseTest
from selenium.common.exceptions import TimeoutException
import pytest
import time


class TestRMTicketsManager(BaseTest):
    """Tickets module tests for manager"""

    def test_go_to_rm_tickets_page(self):
        self.manager_rm = RMTicketsManager(self.driver)
        self.manager_rm.go_to_rm_tickets_page()
        assert self.manager_rm.is_visible(RMTicketsManager.tickets_found)

    def test_new_in_unit_rm(self):
        self.manager_rm = RMTicketsManager(self.driver)
        self.manager_rm.go_to_rm_tickets_page()
        assert self.manager_rm.new_in_unit_rm_ticket('n_iu')

    def test_new_common_rm_ticket(self):
        self.manager_rm = RMTicketsManager(self.driver)
        self.manager_rm.go_to_rm_tickets_page()
        assert self.manager_rm.new_common_rm_ticket('n_ca')

    def test_cancel_in_unit_rm(self):
        self.manager_rm = RMTicketsManager(self.driver)
        self.manager_rm.go_to_rm_tickets_page()
        assert self.manager_rm.new_in_unit_rm_ticket('cancel_iu')
        assert self.manager_rm.cancel_in_unit_rm()

    def test_cancel_common_rm_ticket(self):
        self.manager_rm = RMTicketsManager(self.driver)
        self.manager_rm.go_to_rm_tickets_page()
        assert self.manager_rm.new_common_rm_ticket('cancel_ca')
        assert self.manager_rm.cancel_common_rm_ticket()

    def test_diened_entry_common_rm_ticket(self):
        self.manager_rm = RMTicketsManager(self.driver)
        self.manager_rm.go_to_rm_tickets_page()
        assert self.manager_rm.new_common_rm_ticket('denied_ca')
        assert self.manager_rm.diened_entry_ticket()

    def test_diened_entry_iu_rm_ticket(self):
        self.manager_rm = RMTicketsManager(self.driver)
        self.manager_rm.go_to_rm_tickets_page()
        assert self.manager_rm.new_in_unit_rm_ticket('denied_iu')
        assert self.manager_rm.diened_entry_ticket()

    def test_complete_common_rm_ticket(self):
        self.manager_rm = RMTicketsManager(self.driver)
        self.manager_rm.go_to_rm_tickets_page()
        assert self.manager_rm.new_common_rm_ticket('complete_ca')
        assert self.manager_rm.complete_ticket()

    def test_complete_entry_iu_rm_ticket(self):
        self.manager_rm = RMTicketsManager(self.driver)
        self.manager_rm.go_to_rm_tickets_page()
        assert self.manager_rm.new_in_unit_rm_ticket('complete_iu')
        assert self.manager_rm.complete_ticket()

    def test_child_ticket_iu_rm(self):
        self.manager_rm = RMTicketsManager(self.driver)
        self.manager_rm.go_to_rm_tickets_page()
        assert self.manager_rm.new_in_unit_rm_ticket('child_ti')
        assert self.manager_rm.create_child_ticket('new_child')

    def test_send_proposal(self):
        self.manager_rm = RMTicketsManager(self.driver)
        self.manager_rm.go_to_rm_tickets_page()
        assert self.manager_rm.new_in_unit_rm_ticket('send_prop')
        assert self.manager_rm.send_proposal()

    def test_filter_by_ticket_status(self):
        self.manager_rm = RMTicketsManager(self.driver)
        self.manager_rm.go_to_rm_tickets_page()
        self.manager_rm.filter_by_ticket_status()

    def test_filter_by_property(self):
        self.manager_rm = RMTicketsManager(self.driver)
        self.manager_rm.go_to_rm_tickets_page()
        self.manager_rm.filter_by_property()

    def test_filter_by_assigned_technician(self):
        self.manager_rm = RMTicketsManager(self.driver)
        self.manager_rm.go_to_rm_tickets_page()
        self.manager_rm.filter_by_assigned_technician()

    def test_filter_by_ticket_type(self):
        self.manager_rm = RMTicketsManager(self.driver)
        self.manager_rm.go_to_rm_tickets_page()
        self.manager_rm.filter_by_ticket_type()

    def test_filter_by_unit_member(self):
        self.manager_rm = RMTicketsManager(self.driver)
        self.manager_rm.go_to_rm_tickets_page()
        self.manager_rm.filter_by_unit_member()

