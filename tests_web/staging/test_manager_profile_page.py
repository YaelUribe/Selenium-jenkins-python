import pytest
from pages_web.staging.manager_profile_page import ProfileManager
from tests_web.staging.test_base_page import BaseTest
from selenium.common.exceptions import TimeoutException


class TestProfileManager(BaseTest):
    """Profile module tests for Tenants"""

    def test_go_to_profile_page(self):
        self.profile_manager = ProfileManager(self.driver)
        self.profile_manager.go_to_profile_page()
        assert self.profile_manager.is_visible(ProfileManager.my_profile)

    def test_update_profile_picture(self):
        self.profile_manager = ProfileManager(self.driver)
        self.profile_manager.go_to_profile_page()
        self.profile_manager.update_profile_picture()

    def test_update_profile_info(self):
        self.profile_manager = ProfileManager(self.driver)
        self.profile_manager.go_to_profile_page()
        assert self.profile_manager.update_info()

    def test_see_my_properties(self):
        self.profile_manager = ProfileManager(self.driver)
        self.profile_manager.go_to_profile_page()
        assert self.profile_manager.see_my_properties()

    """def test_change_password(self):
        self.profile_manager = ProfileManager(self.driver)
        self.profile_manager.go_to_profile_page()
        assert self.profile_manager.change_password()"""

    def test_switch_on_notifications(self):
        self.profile_manager = ProfileManager(self.driver)
        self.profile_manager.go_to_profile_page()
        self.profile_manager.switch_on_notifications()

    def test_switch_off_notifications(self):
        self.profile_manager = ProfileManager(self.driver)
        self.profile_manager.go_to_profile_page()
        self.profile_manager.switch_off_notifications()

    def test_preferences(self):
        self.profile_manager = ProfileManager(self.driver)
        self.profile_manager.go_to_profile_page()
        return self.profile_manager.preferences()
