import pytest
from pages_web.development.tenant_events_page import EventsPage
from tests_web.development.test_base_page import BaseTest
from selenium.common.exceptions import TimeoutException


class TestEvents(BaseTest):
    """Events Module tests"""

    def test_go_to_events_page(self):
        self.events_tenant = EventsPage(self.driver)
        self.events_tenant.go_to_events_page()
        assert self.events_tenant.is_visible(EventsPage.events_icon)
        self.events_tenant.do_click(EventsPage.events_icon)

    def test_select_event_from_list(self):
        self.events_tenant = EventsPage(self.driver)
        self.events_tenant.go_to_events_page()
        try:
            self.events_tenant.is_visible(EventsPage.no_events_available)
            pytest.skip("No events available")
        except:
            assert self.events_tenant.is_visible(EventsPage.event_1)
            self.events_tenant.select_event_from_list()

    def test_book_event_from_list(self):
        self.events_tenant = EventsPage(self.driver)
        self.events_tenant.go_to_events_page()
        try:
            self.events_tenant.select_event_from_list()
            self.events_tenant.book_event_from_list()
            self.events_tenant.do_click(EventsPage.ok_button)
        except TimeoutException:
            self.events_tenant.is_visible(EventsPage.no_events_available)
            pytest.skip("No events available")

    def test_cancel_booking(self):
        self.events_tenant = EventsPage(self.driver)
        self.events_tenant.go_to_events_page()
        self.events_tenant.go_to_bookings()
        try:
            self.events_tenant.cancel_upcoming_booking()
        except TimeoutException:
            self.events_tenant.is_visible(EventsPage.no_bookings_available)
            pytest.skip("No Bookings available")

    def test_go_to_bookings(self):
        self.events_tenant = EventsPage(self.driver)
        self.events_tenant.go_to_events_page()
        assert self.events_tenant.is_visible(EventsPage.bookings)
        self.events_tenant.do_click(EventsPage.bookings)

    def test_see_past_bookings(self):
        self.events_tenant = EventsPage(self.driver)
        self.events_tenant.go_to_events_page()
        self.events_tenant.go_to_bookings()
        self.events_tenant.go_to_past_bookings()
