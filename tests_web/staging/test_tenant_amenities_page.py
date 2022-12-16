import pytest
from pages_web.staging.tenant_amenities_page import AmenitiesTenant
from tests_web.staging.test_base_page import BaseTest
import time
from selenium.common.exceptions import TimeoutException
"""Tests for Amenities module for tenant user"""


class TestAmenitiesTenant(BaseTest):
    """Specific locators and actions for Amenities Module as Tenant"""

    def test_go_to_amenities_page(self):
        self.amenities_tenant = AmenitiesTenant(self.driver)
        self.amenities_tenant.go_to_amenities_page()
        assert self.amenities_tenant.is_visible(AmenitiesTenant.services_spaces)

    def test_service_bikestorage(self):
        self.amenities_tenant = AmenitiesTenant(self.driver)
        self.amenities_tenant.go_to_amenities_page()
        self.amenities_tenant.service_bikestorage()

    def test_colab_membership(self):
        self.amenities_tenant = AmenitiesTenant(self.driver)
        self.amenities_tenant.go_to_amenities_page()
        assert self.amenities_tenant.colab_membership()

    def test_s_bbq(self):
        self.amenities_tenant = AmenitiesTenant(self.driver)
        self.amenities_tenant.go_to_amenities_page()
        assert self.amenities_tenant.s_bbq()

    def test_s_la_playa_pool(self):
        self.amenities_tenant = AmenitiesTenant(self.driver)
        self.amenities_tenant.go_to_amenities_page()
        assert self.amenities_tenant.s_la_playa_pool()

    def test_s_sunset_lounge(self):
        self.amenities_tenant = AmenitiesTenant(self.driver)
        self.amenities_tenant.go_to_amenities_page()
        assert self.amenities_tenant.s_sunset_lounge()
        time.sleep(2)

    def test_s_rooftop(self):
        self.amenities_tenant = AmenitiesTenant(self.driver)
        self.amenities_tenant.go_to_amenities_page()
        assert self.amenities_tenant.s_rooftop()

    def test_s_fitness_center(self):
        self.amenities_tenant = AmenitiesTenant(self.driver)
        self.amenities_tenant.go_to_amenities_page()
        assert self.amenities_tenant.s_fitness_center()
