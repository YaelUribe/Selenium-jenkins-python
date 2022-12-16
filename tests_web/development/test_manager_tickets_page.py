from pages_web.development.manager_tickets_page import TicketsManager
from tests_web.development.test_base_page import BaseTest
from selenium.common.exceptions import TimeoutException
import pytest
import time


class TestTicketsManager(BaseTest):
    """Tickets module tests for manager"""

    def test_go_to_tickets_page(self):
        self.manager_tickets = TicketsManager(self.driver)
        self.manager_tickets.go_to_tickets_page()
        assert self.manager_tickets.is_visible(TicketsManager.tickets_found)

    def test_new_move_out_ticket(self):
        self.manager_tickets = TicketsManager(self.driver)
        self.manager_tickets.go_to_tickets_page()
        self.manager_tickets.new_move_out_ticket("new_m_ticket")
        assert self.manager_tickets.is_visible(TicketsManager.ok_btn)

    def test_new_move_in_ticket(self):
        self.manager_tickets = TicketsManager(self.driver)
        self.manager_tickets.go_to_tickets_page()
        self.manager_tickets.new_move_in_ticket("new_m_ticket")
        assert self.manager_tickets.is_visible(TicketsManager.ok_btn)

    def test_cancel_move_out(self):
        self.manager_tickets = TicketsManager(self.driver)
        self.manager_tickets.go_to_tickets_page()
        assert self.manager_tickets.new_move_out_ticket("cancel_m_ticket")
        assert self.manager_tickets.cancel_move_out()

    def test_cancel_move_in(self):
        self.manager_tickets = TicketsManager(self.driver)
        self.manager_tickets.go_to_tickets_page()
        assert self.manager_tickets.new_move_in_ticket("cancel_m_ticket")
        assert self.manager_tickets.cancel_move_in()
