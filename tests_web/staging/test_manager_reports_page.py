from pages_web.staging.manager_reports_page import ReportsManager
from tests_web.staging.test_base_page import BaseTest
import time


class TestReportsManager(BaseTest):
    """Reports module test for Manager"""
    def test_go_to_reports_page(self):
        self.manager_reports = ReportsManager(self.driver)
        self.manager_reports.go_to_reports_page()
        assert self.manager_reports.is_visible(ReportsManager.all_reports)

    def test_create_unit_report(self):
        self.manager_reports = ReportsManager(self.driver)
        self.manager_reports.go_to_reports_page()
        assert self.manager_reports.create_report("unit")

    def test_create_moving_report(self):
        self.manager_reports = ReportsManager(self.driver)
        self.manager_reports.go_to_reports_page()
        assert self.manager_reports.create_report("moving")

    def test_create_turnover_report(self):
        self.manager_reports = ReportsManager(self.driver)
        self.manager_reports.go_to_reports_page()
        assert self.manager_reports.create_report("turnover")

    def test_create_invoices_report(self):
        self.manager_reports = ReportsManager(self.driver)
        self.manager_reports.go_to_reports_page()
        assert self.manager_reports.create_report("invoices")

    def test_create_a_la_carte_report(self):
        self.manager_reports = ReportsManager(self.driver)
        self.manager_reports.go_to_reports_page()
        assert self.manager_reports.create_report("carte")

    def test_create_dry_cleaning_report(self):
        self.manager_reports = ReportsManager(self.driver)
        self.manager_reports.go_to_reports_page()
        assert self.manager_reports.create_report("dry")

    def test_create_packages_report(self):
        self.manager_reports = ReportsManager(self.driver)
        self.manager_reports.go_to_reports_page()
        assert self.manager_reports.create_report("packages")

    def test_create_random_report(self):
        self.manager_reports = ReportsManager(self.driver)
        self.manager_reports.go_to_reports_page()
        assert self.manager_reports.create_random_report()

    def test_delete_report(self):
        self.manager_reports = ReportsManager(self.driver)
        self.manager_reports.go_to_reports_page()
        self.manager_reports.create_random_report()
