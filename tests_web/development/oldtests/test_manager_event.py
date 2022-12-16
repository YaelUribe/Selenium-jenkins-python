from pages_web.manager_events_page import EventsManager
from tests_web.test_base_page import BaseTest


class TestEventManager(BaseTest):
    """Manager Event Module Tests"""

    def test_event_list_display(self):
        self.event_manager = EventsManager(self.driver)
        assert self.event_manager.are_events_displayed()

    def test_event_list_past_display(self):
        self.event_manager = EventsManager(self.driver)
        self.event_manager.filter_past_event()
        assert self.event_manager.are_events_displayed()

    def test_event_bookings_display(self):
        self.event_manager = EventsManager(self.driver)
        self.event_manager.click_event_booking()
        assert self.event_manager.are_event_bookings_displayed()

    def test_event_past_bookings_display(self):
        self.event_manager = EventsManager(self.driver)
        self.event_manager.click_event_booking()
        self.event_manager.filter_past_event()
        assert self.event_manager.are_event_bookings_displayed()

    def test_create_event_booking(self):
        self.event_manager = EventsManager(self.driver)
        self.event_manager.click_create_event_booking()
        self.event_manager.create_event_booking_add_random_choices()
        assert self.event_manager.is_event_successfully_booked_popup_displayed()
        self.event_manager.click_ok()

    def test_create_event(self):
        self.event_manager = EventsManager(self.driver)
        self.event_manager.click_add_event()
        self.event_manager.add_details_create_event()
        assert self.event_manager.is_event_successfully_created_popup_displayed()
        self.event_manager.click_ok()

    def test_delete_event(self):
        self.event_manager = EventsManager(self.driver)
        self.event_manager.click_view_details()
        self.event_manager.click_delete_event()
        assert self.event_manager.is_event_successfully_deleted_displayed()
        self.event_manager.click_ok()

