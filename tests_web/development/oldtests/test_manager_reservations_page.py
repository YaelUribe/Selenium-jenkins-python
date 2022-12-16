import pytest
from pages_web.manager_reservations_page import ManagerAmenities
from tests_web.test_base_page import BaseTest


class TestManagerAmenities(BaseTest):
    """Manager Reservations/amenities module test"""

    def test_go_to_reservations(self):
        self.amenities_manager = ManagerAmenities(self.driver)
        self.amenities_manager.go_to_reservations_page()
        assert self.amenities_manager.is_visible(ManagerAmenities.reservations_calendar)

    def test_create_amenity(self):
        self.amenities_manager = ManagerAmenities(self.driver)
        self.amenities_manager.go_to_reservations_page()
        self.amenities_manager.create_amenity()

    def test_publish_amenity(self):
        self.amenities_manager = ManagerAmenities(self.driver)
        self.amenities_manager.go_to_reservations_page()
        self.amenities_manager.publish_amenity()

    def test_filter_published(self):
        self.amenities_manager = ManagerAmenities(self.driver)
        self.amenities_manager.go_to_reservations_page()
        assert self.amenities_manager.filter_published()

    def test_filter_unpublished(self):
        self.amenities_manager = ManagerAmenities(self.driver)
        self.amenities_manager.go_to_reservations_page()
        assert self.amenities_manager.filter_unpublished()

    def test_unpublish_amenity(self):
        self.amenities_manager = ManagerAmenities(self.driver)
        self.amenities_manager.go_to_reservations_page()
        assert self.amenities_manager.unpublish_amenity()
