from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException

#  Constants
email_locator = (By.XPATH, "//input[@formcontrolname='email']")
password_locator = (By.XPATH, "//input[@formcontrolname='password']")
next_btn = (By.XPATH, "//button[contains(text(), 'Next')]")
home_icon = (By.XPATH, "//span[contains(text(), 'Home')]")
manager_home_icon = (By.XPATH, "//a[contains(text(), 'My Dashboard')]")

tenant_email = "ashleyratha@g8p3c.com"
tenant_password = "Dvora123456!"
manager_email = "yael@dvoralife.com"
manager_password = "Dvora123456!"
base_url = "https://staging.dvoraliving.com/login"
events_url = "https://staging.dvoraliving.com/r/events/list"
manager_events_url = "https://staging.dvoraliving.com/m/events/list"
tenant_profile_url = "https://staging.dvoraliving.com/r/settings/profile"
tenant_amenities_url = "https://staging.dvoraliving.com/r/services/"
manager_profile_url = "https://staging.dvoraliving.com/m/settings/profile"
manager_amenities_url = "https://staging.dvoraliving.com/m/amenities/calendar"
tenant_visitors_url = "https://staging.dvoraliving.com/r/visitors"
manager_visitors_url = "https://staging.dvoraliving.com/m/visitors"
manager_tickets_url = "https://staging.dvoraliving.com/m/move-out/list"
repair_maintenance_url = "https://staging.dvoraliving.com/m/work-orders/list"
tenant_chat_url = "https://staging.dvoraliving.com/r/chat"
manager_chat_url = "https://staging.dvoraliving.com/m/chat/list"
manager_admin_tickets_url = "https://staging.dvoraliving.com/m/admin-tickets/list"
manager_reports_url = "https://staging.dvoraliving.com/m/reports"
