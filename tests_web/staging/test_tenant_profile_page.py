import pytest
from pages_web.staging.tenant_profile_page import ProfileTenant
from tests_web.staging.test_base_page import BaseTest
from selenium.common.exceptions import TimeoutException


class TestProfile(BaseTest):
    """Profile module tests for Tenants"""

    def test_go_to_profile_page(self):
        self.profile_tenant = ProfileTenant(self.driver)
        self.profile_tenant.go_to_profile_page()
        assert self.profile_tenant.is_visible(ProfileTenant.my_profile)

    def test_update_info(self):
        self.profile_tenant = ProfileTenant(self.driver)
        self.profile_tenant.go_to_profile_page()
        self.profile_tenant.update_info()
        assert self.profile_tenant.is_visible(ProfileTenant.success_notification)

    def test_update_profile_picture(self):
        self.profile_tenant = ProfileTenant(self.driver)
        self.profile_tenant.go_to_profile_page()
        self.profile_tenant.update_profile_picture()

    def test_see_my_unit(self):
        self.profile_tenant = ProfileTenant(self.driver)
        self.profile_tenant.go_to_profile_page()
        assert self.profile_tenant.see_my_unit()

    def test_switch_off_notifications(self):
        self.profile_tenant = ProfileTenant(self.driver)
        self.profile_tenant.go_to_profile_page()
        self.profile_tenant.switch_off_notifications()

    def test_switch_on_notifications(self):
        self.profile_tenant = ProfileTenant(self.driver)
        self.profile_tenant.go_to_profile_page()
        self.profile_tenant.switch_on_notifications()

    def test_preferences(self):
        self.profile_tenant = ProfileTenant(self.driver)
        self.profile_tenant.go_to_profile_page()
        return self.profile_tenant.preferences()

    def test_turn_off_autopay(self):
        self.profile_tenant = ProfileTenant(self.driver)
        self.profile_tenant.go_to_profile_page()
        self.profile_tenant.turn_off_autopay()

    def test_turn_on_autopay(self):
        self.profile_tenant = ProfileTenant(self.driver)
        self.profile_tenant.go_to_profile_page()
        self.profile_tenant.turn_on_autopay()
