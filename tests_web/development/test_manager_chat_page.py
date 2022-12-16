from pages_web.development.manager_chat_page import ChatManager
from tests_web.development.test_base_page import BaseTest
from selenium.common.exceptions import TimeoutException
import pytest
import time


class TestChatManager(BaseTest):
    """Test suite for Manager's chat module"""

    def test_go_to_chat_page(self):
        self.manager_chat = ChatManager(self.driver)
        self.manager_chat.go_to_chat_page()
        assert self.manager_chat.is_visible(ChatManager.status_tag)

    def test_new_chat_message(self):
        self.manager_chat = ChatManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.new_chat()
        assert self.manager_chat.new_message()

    def test_update_chat_category(self):
        self.manager_chat = ChatManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.open_existing_chat()
        assert self.manager_chat.update_category()

    def test_resolve_chat(self):
        self.manager_chat = ChatManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.new_chat()
        assert self.manager_chat.new_message()
        assert self.manager_chat.resolve_chat()

    def test_transfer_chat(self):
        self.manager_chat = ChatManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.new_chat()
        assert self.manager_chat.new_message()
        self.manager_chat.transfer_chat()

    def test_see_full_history(self):
        self.manager_chat = ChatManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.open_existing_chat()
        assert self.manager_chat.see_full_history()

    def test_look_for_resident_tickets(self):
        self.manager_chat = ChatManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.open_existing_chat()
        assert self.manager_chat.look_for_resident_tickets()

    def test_look_for_resident_reservations(self):
        self.manager_chat = ChatManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.open_existing_chat()
        assert self.manager_chat.look_for_resident_reservations()

    def test_look_for_resident_bookings(self):
        self.manager_chat = ChatManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.open_existing_chat()
        assert self.manager_chat.look_for_resident_bookings()

    def test_look_for_resident_event_bookings(self):
        self.manager_chat = ChatManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.open_existing_chat()
        assert self.manager_chat.look_for_resident_event_bookings()

    def test_look_for_resident_announcements(self):
        self.manager_chat = ChatManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.open_existing_chat()
        assert self.manager_chat.look_for_resident_announcements()

    def test_look_for_resident_notifications(self):
        self.manager_chat = ChatManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.open_existing_chat()
        assert self.manager_chat.look_for_resident_notifications()

    def test_filter_by_status(self):
        self.manager_chat = ChatManager(self.driver)
        self.manager_chat.go_to_chat_page()
        assert self.manager_chat.filter_by_status()

    def test_filter_by_assigned_to(self):
        self.manager_chat = ChatManager(self.driver)
        self.manager_chat.go_to_chat_page()
        assert self.manager_chat.filter_by_assigned_to()

    def test_filter_by_chat_id(self):
        self.manager_chat = ChatManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.filter_by_chat_id()

    def test_filter_by_advanced(self):
        self.manager_chat = ChatManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.filter_by_advanced()

    def test_filter_by_own_status(self):
        self.manager_chat = ChatManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.filter_by_own_status()

    def test_filter_by_own_advanced(self):
        self.manager_chat = ChatManager(self.driver)
        self.manager_chat.go_to_chat_page()
        self.manager_chat.filter_by_own_advanced()
