import time
from pages_web.development.tenant_chat_page import ChatTenant
from tests_web.development.test_base_page import BaseTest


class TestChatTenant(BaseTest):
    """Test suite for Tenant's Chat Module"""

    def test_go_to_chat_page(self):
        self.tenant_chat = ChatTenant(self.driver)
        self.tenant_chat.go_to_chat_page()
        assert self.tenant_chat.is_visible(ChatTenant.all_chats_tag)

    def test_filter_chats_open(self):
        self.tenant_chat = ChatTenant(self.driver)
        self.tenant_chat.go_to_chat_page()
        self.tenant_chat.filter_chats_open()

    def test_filter_chats_closed(self):
        self.tenant_chat = ChatTenant(self.driver)
        self.tenant_chat.go_to_chat_page()
        self.tenant_chat.filter_chats_closed()

    def test_start_new_chat(self):
        self.tenant_chat = ChatTenant(self.driver)
        self.tenant_chat.go_to_chat_page()
        assert self.tenant_chat.start_new_chat()

    def test_start_attach_send(self):
        self.tenant_chat = ChatTenant(self.driver)
        self.tenant_chat.go_to_chat_page()
        assert self.tenant_chat.start_new_chat()
        assert self.tenant_chat.write_attach_send()

    def test_open_existing_send(self):
        self.tenant_chat = ChatTenant(self.driver)
        self.tenant_chat.go_to_chat_page()
        self.tenant_chat.open_existing()
        assert self.tenant_chat.write_attach_send()

    def test_reopen_closed_send(self):
        self.tenant_chat = ChatTenant(self.driver)
        self.tenant_chat.go_to_chat_page()
        self.tenant_chat.reopen_closed()
        assert self.tenant_chat.write_attach_send()

    def test_submit_rating(self):
        self.tenant_chat = ChatTenant(self.driver)
        self.tenant_chat.go_to_chat_page()
        assert self.tenant_chat.submit_rating()

    def test_upcoming_events_promos(self):
        self.tenant_chat = ChatTenant(self.driver)
        self.tenant_chat.go_to_chat_page()
        assert self.tenant_chat.upcoming_events_promos()
