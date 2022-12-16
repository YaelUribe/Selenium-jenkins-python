from pages_web.staging.manager_chat_tickets_and_bookings import ChatTicketsManager
from tests_web.staging.test_base_page import BaseTest
from selenium.common.exceptions import TimeoutException
import util.web_utils_development as util
import pytest
import time


class TestChatManager(BaseTest):
    """Test suite for Manager's chat module"""

    def test_go_to_chat_page(self):
        self.manager_chat = ChatTicketsManager(self.driver)
        self.manager_chat.go_to_chat_page()
        assert self.manager_chat.is_visible(ChatTicketsManager.status_filter)

    def test_new_chat_message(self):
        self.manager_chat = ChatTicketsManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.new_chat()
        assert self.manager_chat.new_message()

    def test_new_in_unit_rm_ticket(self):
        self.manager_chat = ChatTicketsManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.new_chat()
        assert self.manager_chat.new_message()
        assert self.manager_chat.create_iu_ticket()

    def test_new_common_area_rm_ticket(self):
        self.manager_chat = ChatTicketsManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.new_chat()
        assert self.manager_chat.new_message()
        assert self.manager_chat.create_carea_ticket()

    def test_new_move_in_ticket(self):
        self.manager_chat = ChatTicketsManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.new_chat()
        assert self.manager_chat.new_message()
        assert self.manager_chat.create_movein_ticket("new_m_chat_ticket")

    def test_new_move_out_rm_ticket(self):
        self.manager_chat = ChatTicketsManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.new_chat()
        assert self.manager_chat.new_message()
        assert self.manager_chat.create_moveout_ticket("new_m_chat_ticket")

    def test_book_event(self):
        self.manager_chat = ChatTicketsManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.open_existing_chat()
        assert self.manager_chat.book_event()

    def test_reserve_a_space(self):
        self.manager_chat = ChatTicketsManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.open_existing_chat()
        assert self.manager_chat.reserve_a_space()

    def test_request_service(self):
        self.manager_chat = ChatTicketsManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.open_existing_chat()
        assert self.manager_chat.request_service()

    def test_leave_chat(self):
        self.manager_chat = ChatTicketsManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.open_existing_chat()
        assert self.manager_chat.leave_chat()
