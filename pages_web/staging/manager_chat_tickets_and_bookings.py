import os
import random
import pytest
from pages_web.staging.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import util.web_utils_staging as util
"""Chat module for Manager, locators and actions"""


class ChatTicketsManager(BasePage):
    """Locators and constants"""
    status_filter = (By.XPATH, "//app-conversations-list//label[contains(text(),'Status')]")
    status_tag = (By.XPATH, "//label[contains(text(),'Status')]")
    property_selector = (By.XPATH, "//ng-select[@formcontrolname= 'building_id']//input")
    property_option = (By.XPATH, "//ng-select//ng-dropdown-panel/div/div[2]/div")
    resident_selector = (By.XPATH, "//ng-select[@formcontrolname= '_tenant']//input")
    resident_options = (By.XPATH, "//ng-select//ng-dropdown-panel/div/div[2]/div")
    category_selector = (By.XPATH, "//ng-select[@formcontrolname= 'category_id']//div[@class= 'ng-value-container']")
    category_options = (By.XPATH, "//ng-select//ng-dropdown-panel/div/div[2]/div")
    subcategory_selector = (By.XPATH, "//ng-select[@formcontrolname= 'subcategory_id']//div[@class= 'ng-value-container']")
    subcategory_options = (By.XPATH, "//ng-select//ng-dropdown-panel/div/div[2]/div")
    create_chat_btn = (By.XPATH, "//a[contains(text(), 'Create Chat')]")
    create_chat_btn_2 = (By.XPATH, "//button[contains(text(), 'Create Chat')]")
    text_area_chat = (By.XPATH, "//app-conversation-chat//textarea")
    attachment_input = (By.XPATH, "//app-conversation-chat//input[@formcontrolname='attachments']")
    send_message_btn = (By.XPATH, "//app-conversation-chat//span[contains(text(), 'Send')]")
    chat_body = (By.XPATH, "//div[@infinitescroll]/div")
    first_my_chats = (By.XPATH, "//app-active-conversations//div[@infinitescroll]/a")
    more_options_btn = (By.XPATH, "//span[contains(text(), 'More Options')]")
    create_ticket_option = (By.XPATH, "//a[contains(text(), 'Create Ticket')]")
    book_event_option = (By.XPATH, "//a[contains(text(), 'Book Event')]")
    reserve_space_option = (By.XPATH, "//a[contains(text(), 'Reserve A Space')]")
    request_service_option = (By.XPATH, "//a[contains(text(), 'Request A Service')]")
    leave_chat_option = (By.XPATH, "//a[contains(text(), 'Leave Chat')]")
    ticket_type = (By.XPATH, "//ng-select[@formcontrolname= 'request_type']//div[@class= 'ng-value-container']")
    iu_rm_option = (By.XPATH, "//ng-dropdown-panel//div[@role= 'option'][3]")
    carea_rm_option = (By.XPATH, "//ng-dropdown-panel//div[@role= 'option'][2]")
    movein_option = (By.XPATH, "//ng-dropdown-panel//div[@role= 'option'][4]")
    moveout_option = (By.XPATH, "//ng-dropdown-panel//div[@role= 'option'][5]")
    create_btn = (By.XPATH, "//button[contains(text(), 'Create')]")
    permission_to_enter_chckbx = (By.XPATH, "//label[contains(text(), ' Yes:')]/input")
    select_category = (By.XPATH, "//ng-select[@formcontrolname= 'category_id']/div/div")
    select_category_options = (By.XPATH, "//ng-dropdown-panel[@role= 'listbox']//div[@role= 'option']")
    select_subcategory = (By.XPATH, "//ng-select[@formcontrolname= 'subcategory_id']/div/div")
    select_subcategory_options = (By.XPATH, "//ng-dropdown-panel[@role= 'listbox']//div[@role= 'option']")
    detail_textarea = (By.XPATH, "//textarea[@formcontrolname='detail']")
    select_technician = (By.XPATH, "//ng-select[@formcontrolname='assignedTo']/div/div")
    select_technician_option = (By.XPATH, "//ng-dropdown-panel//span[contains(text(), 'Automation Technician')]")
    date_input = (By.XPATH, "//input[@formcontrolname='tentativelyTechnicianWalkThroughDate']")
    time_input = (By.XPATH, "//input[@formcontrolname='tentativelyTechnicianWalkThroughTime']")
    select_duration = (By.XPATH, "//ng-select[@formcontrolname= 'technicianDuration']/div/div")
    select_duration_option = (By.XPATH, "//ng-dropdown-panel[@role= 'listbox']//div[@role= 'option'][1]")
    confirm_btn = (By.XPATH, "//button[contains(text(), 'Confirm')]")
    ok_btn = (By.XPATH, "//button[contains(text(), 'Ok')]")
    select_date_input = (By.XPATH, "//input[@formcontrolname= 'selectedDate']")
    select_time_slot = (By.XPATH, "//ng-select[@formcontrolname= 'selectedTimeSlot']/div/div")
    time_slot_movein = (By.XPATH, "//ng-dropdown-panel//div[@role= 'option'][2]")
    time_slot_moveout = (By.XPATH, "//ng-dropdown-panel//div[@role= 'option'][1]")
    moving_type_tag = (By.XPATH, "//div[@class= 'manager-overlay-container active']//h2[contains(text(), 'Moving Type')]")
    renters_insurance_tag = (By.XPATH, "//div[@class= 'manager-overlay-container active']//h2[contains(text(), 'Renters Insurance')]")
    disconnect_utilities_tag = (By.XPATH, "//app-request-create-move-out-v2//h2[contains(text(), 'Disconnect Utilities')]")
    connect_utilities_tag = (By.XPATH, "//div[@class='manager-overlay-container active']//h2[contains(text(), 'Connect Utilities')]")
    book_inspection_tag = (By.XPATH, "//div[@class= 'manager-overlay-container active']//h2[contains(text(), 'Book Inspection')]")
    select_moving_type = (By.XPATH, "//div[@class= 'manager-overlay-container active']//ng-select[@formcontrolname= 'movingType']/div/div")
    select_moving_type_option = (By.XPATH, "//ng-dropdown-panel//div[@role= 'option'][1]")
    renters_insurance_input = (By.XPATH, "//div[@class= 'manager-overlay-container active']//app-inline-file-input-form-field[@formcontrolname='renters_insurance']//input ")
    hold_harmless_input = (By.XPATH, "//app-inline-file-input-form-field[@formcontrolname= 'self_move_harmless']//input")
    connect_utilities_water = (By.XPATH, "//div[@class='manager-overlay-container active']//input[@formcontrolname='suezAccount']")
    connect_utilities_electric = (By.XPATH, "//div[@class='manager-overlay-container active']//input[@formcontrolname='psegAccount']")
    disconnect_chckbx = (By.XPATH, "//div[@class='manager-overlay-container active']//input[@formcontrolname='remindDisconnect']")
    select_technician_2 = (By.XPATH, "//div[@class='manager-overlay-container active']//ng-select[@formcontrolname='assignedTo']/div/div")
    select_date_input_2 = (By.XPATH, "//div[@class='manager-overlay-container active']//input[@formcontrolname= 'tentativelyTechnicianWalkThroughDate']")
    time_input_2 = (By.XPATH, "//div[@class='manager-overlay-container active']//input[@formcontrolname= 'tentativelyTechnicianWalkThroughTime']")
    select_duration_2 = (By.XPATH, "//div[@class='manager-overlay-container active']//ng-select[@formcontrolname= 'technicianDuration']/div/div")
    select_duration_option_2 = (By.XPATH, "//ng-dropdown-panel//div[@role= 'option'][1]")
    save_changes_btn = (By.XPATH, "//div[@class= 'manager-overlay-container active']//button[contains(text(), 'Save Changes')]")
    complete_ticket_btn = (By.XPATH, "//div[@class= 'manager-overlay-container active']//button[contains(text(), 'Complete Ticket')]")
    property_selector_event = (By.XPATH, "//ng-select[@formcontrolname= 'building_id']//div[@class= 'ng-value-container']")
    dropdown_options = (By.XPATH, "//ng-dropdown-panel//div[@role= 'option']")
    unit_member = (By.XPATH, "//ng-select[@formcontrolname= '_resident']//div[@class= 'ng-value-container']")
    event_selector = (By.XPATH, "//ng-select[@formcontrolname= 'event_id']//div[@class= 'ng-value-container']")
    assistants = (By.XPATH, "//input[@formcontrolname= 'assistants']")
    create_event_booking_btn = (By.XPATH, "//button[contains(text(), 'Create Event Booking')]")
    amenity_selector = (By.XPATH, "//ng-select[@formcontrolname= '_amenity']//div[@class= 'ng-value-container']")
    party_size = (By.XPATH, "//input[@formcontrolname= 'additional_unit_occupants']")
    reservation_details = (By.XPATH, "//textarea[@formcontrolname= 'details']")
    reservation_calendar = (By.XPATH, "//full-calendar")
    start_time = (By.XPATH, "//tr[15]/td[2]")
    end_time = (By.XPATH, "//tr[17]/td[2]")
    create_reserv_btn = (By.XPATH, "//button[contains(text(), 'Create Reservation')]")
    reservation_status = (By.XPATH, "//h2[contains(text(), 'Amenity Reservation Details')]")
    property_selector_service = (By.XPATH, "//ng-select[@formcontrolname= 'property']//div[@class= 'ng-value-container']")
    unit_service = (By.XPATH, "//ng-select[@formcontrolname= 'unit']//div[@class= 'ng-value-container']")
    resident_service = (By.XPATH, "//ng-select[@formcontrolname= 'resident']//div[@class= 'ng-value-container']")
    service_type = (By.XPATH, "//ng-select[@formcontrolname= 'serviceId']//div[@class= 'ng-value-container']")
    service_frequency = (By.XPATH, "//ng-select[@formcontrolname= 'frequency']//div[@class= 'ng-value-container']")
    pricing = (By.XPATH, "//ng-select[@formcontrolname= 'variant']//div[@class= 'ng-value-container']")
    preferred_service_days = (By.XPATH, "//div[@class= 'column']/button")
    order_btn = (By.XPATH, "//button[contains(text(), 'Order')]")
    service_orders = (By.XPATH, "//h1[contains(text(), 'Service Orders')]")
    start_chat_btn = (By.XPATH, "//button[contains(text(), 'Start Chat')]")
    member_name = (By.XPATH, "//app-conversation-detail/div/div/div/div/div[1]/div/div/a")
    member_select = (By.XPATH, "//app-tenant-dropdown//input")
    payment_warning = (By.XPATH, "//div[contains(text(), 'Warning')]")
    booking_building = (By.XPATH, "//div[@role='option']/span[contains(text(), 'DVORA 175')]")
    booking_resident = (By.XPATH, "//div[@role='option']/span[contains(text(), 'Ashley Rathappillil')]")
    booking_event = (By.XPATH, "//div[@role='option']/span[contains(text(), 'Automation Test Event')]")
    move_in_warning = (By.XPATH, "//div[contains(text(), 'A Move-In already exists for this member.')]")
    move_out_warning = (By.XPATH, "//div[contains(text(), 'A Move-Out already exists for this member.')]")

    message = """Tickets & Bookings Test message Tickets & Bookings Test message Tickets & Bookings Test message\
    Tickets & Bookings Test message Tickets & Bookings Test message Tickets & Bookings Test message\
    Tickets & Bookings Test message Tickets & Bookings Test message Tickets & Bookings Test message Tickets & Bookings Test message\
    Tickets & Bookings Test message Tickets & Bookings Test message"""
    ticket_detail_content = "New ticket test message New ticket test message New ticket test message New ticket test message\
                            New ticket test message New ticket test message New ticket test message New ticket test message\
                            New ticket test message New ticket test message New ticket test message New ticket test message"
    reservation_details_text = "TestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTest"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(util.base_url)

    def go_to_chat_page(self):
        try:
            self.is_visible(util.manager_home_icon)
        except TimeoutException:
            self.send_keys(util.email_locator, util.manager_email)
            self.do_click(util.next_btn)
            time.sleep(0.8)
            self.send_keys(util.password_locator, util.manager_password)
            self.do_click(util.next_btn)
            time.sleep(3)
        time.sleep(8)
        self.driver.get(util.manager_chat_url)
        time.sleep(1)

    def new_chat(self):
        time.sleep(2)
        clicks = [self.create_chat_btn, self.property_selector, self.resident_selector,
                  self.category_selector, self.subcategory_selector, self.create_chat_btn_2
                  ]
        for i in clicks:
            if i == self.property_selector:
                time.sleep(0.5)
                self.send_keys(i, "DVORA 175")
                time.sleep(1)
                self.press_enter_web()
                time.sleep(8.5)
            elif i == self.resident_selector:
                try:
                    time.sleep(0.5)
                    self.send_keys(i, "Ashley Rathappillil")
                    time.sleep(3)
                    self.press_enter_web()
                    time.sleep(0.5)
                except TimeoutException:
                    pytest.skip("No residents found in this building")
            elif i == self.category_selector:
                self.do_click(i)
                time.sleep(0.5)
                self.click_single_random_option_web(self.category_options)
                time.sleep(0.5)
            elif i == self.subcategory_selector:
                self.do_click(i)
                time.sleep(0.5)
                self.click_single_random_option_web(self.subcategory_options)
                time.sleep(0.5)
            else:
                self.do_click(i)
                time.sleep(0.8)
        time.sleep(1)

    def new_message(self):
        time.sleep(2)
        try:
            start = self.messages_in_chat(self.chat_body)
        except TimeoutException:
            start = 0
        messages = [(self.text_area_chat, self.message)]
        """(self.attachment_input, os.getcwd() + '/photo6.jpg')"""
        for i in messages:
            time.sleep(1)
            self.send_keys(i[0], i[1])
            time.sleep(1.5)
        time.sleep(1.8)
        self.do_click(self.send_message_btn)
        time.sleep(0.8)
        end = self.messages_in_chat(self.chat_body)
        return end >= start

    def open_existing_chat(self):
        try:
            self.do_click(self.first_my_chats)
            time.sleep(0.8)
        except TimeoutException:
            pytest.skip("No active conversation available")

    def create_iu_ticket(self):
        time.sleep(1)
        tenant_name = self.get_text(self.member_name)
        clicks = [self.more_options_btn, self.create_ticket_option, self.ticket_type,
                  self.iu_rm_option, self.create_btn]
        for x in clicks:
            self.do_click(x)
            time.sleep(0.8)
        time.sleep(1)
        clicks_2 = [self.member_select, self.permission_to_enter_chckbx,
                    self.select_category, self.select_subcategory,
                    self.detail_textarea, self.select_technician, self.select_technician_option,
                    self.date_input, self.time_input, self.select_duration, self.select_duration_option,
                    self.create_btn, self.confirm_btn]
        for y in clicks_2:
            self.scroll_to_location_web(y)
            if y == self.select_category or y == self.select_subcategory:
                self.do_click(y)
                time.sleep(0.8)
                try:
                    self.click_single_random_option_web(self.select_category_options)
                    time.sleep(0.8)
                except TimeoutException:
                    self.press_escape()
            elif y == self.member_select:
                self.send_keys(y, tenant_name)
                time.sleep(0.8)
                self.press_enter_web()
                time.sleep(0.5)
            elif y == self.detail_textarea:
                self.send_keys(y, self.ticket_detail_content)
                time.sleep(0.8)
            elif y == self.date_input:
                self.send_keys(y, self.date_calendar())
                time.sleep(0.8)
            elif y == self.time_input:
                self.send_keys(y, "500P")
                time.sleep(0.8)
            else:
                self.do_click(y)
                time.sleep(0.8)
        time.sleep(1)
        try:
            return self.is_visible(self.ok_btn)
        except TimeoutException:
            pytest.skip("Technician not available in scheduled time")

    def create_carea_ticket(self):
        time.sleep(1)
        tenant_name = self.get_text(self.member_name)
        clicks = [self.more_options_btn, self.create_ticket_option, self.ticket_type,
                  self.carea_rm_option, self.create_btn]
        for x in clicks:
            self.do_click(x)
            time.sleep(0.8)
        time.sleep(1)
        clicks_2 = [self.member_select, self.permission_to_enter_chckbx,
                    self.select_category, self.select_subcategory,
                    self.detail_textarea, self.select_technician, self.select_technician_option,
                    self.date_input, self.time_input, self.select_duration, self.select_duration_option,
                    self.create_btn, self.confirm_btn]
        for y in clicks_2:
            self.scroll_to_location_web(y)
            if y == self.select_category or y == self.select_subcategory:
                self.do_click(y)
                time.sleep(0.8)
                try:
                    self.click_single_random_option_web(self.select_category_options)
                    time.sleep(0.8)
                except TimeoutException:
                    self.press_escape()
            elif y == self.member_select:
                self.send_keys(y, tenant_name)
                time.sleep(0.8)
                self.press_enter_web()
                time.sleep(0.5)
            elif y == self.detail_textarea:
                self.send_keys(y, self.ticket_detail_content)
                time.sleep(0.8)
            elif y == self.date_input:
                self.send_keys(y, self.date_calendar())
                time.sleep(0.8)
            elif y == self.time_input:
                self.send_keys(y, "515P")
                time.sleep(0.8)
            else:
                self.do_click(y)
                time.sleep(0.8)
        time.sleep(1)
        try:
            return self.is_visible(self.ok_btn)
        except TimeoutException:
            pytest.skip("Technician not available in scheduled time")

    def create_movein_ticket(self, hour):
        time.sleep(2)
        tenant_name = self.get_text(self.member_name)
        clicks = [self.more_options_btn, self.create_ticket_option, self.ticket_type,
                  self.movein_option, self.create_btn]
        for x in clicks:
            self.do_click(x)
            time.sleep(1)
        if self.is_visible(self.move_in_warning):
            self.do_click(self.ok_btn)
            time.sleep(1)
        time.sleep(1)
        clicks_2 = [self.member_select, self.select_date_input,
                    self.select_time_slot, self.time_slot_movein, self.book_inspection_tag,
                    self.select_technician_2, self.select_technician_option,
                    self.select_date_input_2, self.time_input_2, self.select_duration_2, self.select_duration_option_2,
                    self.create_btn, self.confirm_btn, self.ok_btn, self.moving_type_tag,
                    self.select_moving_type, self.select_moving_type_option, self.hold_harmless_input,
                    self.renters_insurance_tag, self.renters_insurance_input,
                    self.connect_utilities_tag, self.connect_utilities_electric, self.connect_utilities_water,
                    self.complete_ticket_btn, self.confirm_btn
                    ]
        for y in clicks_2:
            self.scroll_to_location_web(y)
            if y == self.select_date_input:
                self.send_keys(y, self.date_calendar_2(hour))
                time.sleep(0.8)
            elif y == self.member_select:
                self.send_keys(y, tenant_name)
                time.sleep(0.8)
                self.press_enter_web()
                time.sleep(0.5)
            elif y == self.renters_insurance_input or y == self.hold_harmless_input:
                self.send_keys(y, os.getcwd() + '/testpdf.pdf')
                time.sleep(2)
            elif y == self.connect_utilities_electric or y == self.connect_utilities_water:
                self.clear(y)
                time.sleep(0.8)
                self.send_keys(y, "333211-" + str(random.choice(range(10))))
            elif y == self.select_date_input_2:
                self.send_keys(y, self.date_calendar())
                time.sleep(0.8)
            elif y == self.time_input_2:
                self.send_keys(y, "545P")
                time.sleep(0.8)
            else:
                self.do_click(y)
                time.sleep(1)
        time.sleep(3)
        return self.is_visible(self.ok_btn)

    def create_moveout_ticket(self, hour):
        tenant_name = self.get_text(self.member_name)
        clicks = [self.more_options_btn, self.create_ticket_option, self.ticket_type,
                  self.moveout_option, self.create_btn]
        for x in clicks:
            self.do_click(x)
            time.sleep(0.8)
        time.sleep(1)
        clicks_2 = [self.member_select, self.select_date_input, self.select_time_slot, self.time_slot_moveout,
                    self.create_btn, self.confirm_btn, self.ok_btn, self.moving_type_tag,
                    self.select_moving_type, self.select_moving_type_option, self.hold_harmless_input,
                    self.disconnect_utilities_tag, self.disconnect_chckbx,
                    self.book_inspection_tag, self.select_technician_2, self.select_technician_option,
                    self.select_date_input_2, self.time_input_2, self.select_duration_2, self.select_duration_option_2,
                    self.complete_ticket_btn, self.confirm_btn]
        for y in clicks_2:
            self.scroll_to_location_web(y)
            if y == self.select_date_input:
                try:
                    if self.is_visible(self.move_out_warning):
                        self.do_click(self.ok_btn)
                        time.sleep(1)
                except TimeoutException:
                    continue
                self.send_keys(y, self.date_calendar_2(hour))
                time.sleep(0.8)
            elif y == self.member_select:
                self.send_keys(y, tenant_name)
                time.sleep(0.8)
                self.press_enter_web()
                time.sleep(0.5)
            elif y == self.hold_harmless_input:
                self.send_keys(y, os.getcwd() + '/testpdf.pdf')
                time.sleep(2)
            elif y == self.select_date_input_2:
                self.send_keys(y, self.date_calendar())
                time.sleep(0.8)
            elif y == self.time_input_2:
                self.send_keys(y, "600P")
                time.sleep(0.8)
            else:
                self.do_click(y)
                time.sleep(1)
        time.sleep(2)
        return self.is_visible(self.ok_btn)

    def reserve_a_space(self):
        time.sleep(1)
        clicks = [self.more_options_btn, self.reserve_space_option]
        for x in clicks:
            self.do_click(x)
            time.sleep(0.8)
        time.sleep(1)
        clicks_2 = [self.property_selector_event, self.unit_member, self.amenity_selector]
        for y in clicks_2:
            self.scroll_to_location_web(y)
            if y == self.unit_member:
                try:
                    self.do_click(y)
                    time.sleep(1.2)
                    self.do_click(self.booking_resident)
                    time.sleep(1)
                except TimeoutException:
                    pytest.skip("No resident Available for this building")
            elif y == self.property_selector_event:
                self.do_click(y)
                time.sleep(1.2)
                self.scroll_to_location_web(self.booking_building)
                self.do_click(self.booking_building)
                time.sleep(3)
            else:
                self.do_click(y)
                time.sleep(1.3)
                self.click_single_random_option_web(self.dropdown_options)
                time.sleep(1.3)
        try:
            self.send_keys(self.reservation_details, self.reservation_details_text)
            time.sleep(0.8)
            self.scroll_to_location_web(self.reservation_calendar)
            time.sleep(0.5)
        except:
            self.scroll_to_location_web(self.reservation_calendar)
            time.sleep(0.5)
        self.drag_and_drop(self.start_time, self.end_time)
        time.sleep(0.5)
        self.scroll_to_location_web(self.create_reserv_btn)
        self.do_click(self.create_reserv_btn)
        time.sleep(1)
        self.do_click(self.ok_btn)
        time.sleep(1.2)
        return self.is_visible(self.reservation_status)


    def book_event(self):
        time.sleep(1)
        clicks = [self.more_options_btn, self.book_event_option]
        for x in clicks:
            self.do_click(x)
            time.sleep(0.8)
        time.sleep(1)
        clicks_2 = [self.property_selector_event, self.unit_member, self.event_selector]
        for y in clicks_2:
            self.scroll_to_location_web(y)
            if y == self.event_selector:
                try:
                    self.do_click(y)
                    time.sleep(1.2)
                    self.do_click(self.booking_event)
                    time.sleep(1.2)
                except TimeoutException:
                    pytest.skip("No events Available")
            elif y == self.unit_member:
                try:
                    self.do_click(y)
                    time.sleep(1.2)
                    self.scroll_to_location_web(self.booking_resident)
                    self.do_click(self.booking_resident)
                    time.sleep(1.2)
                except TimeoutException:
                    pytest.skip("No resident Available for this building")
            else:
                self.scroll_to_location_web(y)
                self.do_click(y)
                time.sleep(1.3)
                self.do_click(self.booking_building)
        self.send_keys(self.assistants, str(random.choice(range(5))))
        time.sleep(0.5)
        self.do_click(self.create_event_booking_btn)
        time.sleep(1)
        return self.is_visible(self.ok_btn)

    def request_service(self):
        time.sleep(1)
        clicks = [self.more_options_btn, self.request_service_option]
        for x in clicks:
            self.do_click(x)
            time.sleep(0.8)
        time.sleep(1)
        clicks_2 = [self.property_selector_service, self.unit_service, self.resident_service,
                    self.service_type, self.service_frequency, self.pricing, self.preferred_service_days]
        for y in clicks_2:
            self.scroll_to_location_web(y)
            if y == self.preferred_service_days:
                self.click_single_random_option_web(y)
                time.sleep(0.5)
            elif y == self.unit_service:
                try:
                    self.do_click(y)
                    time.sleep(0.8)
                    self.click_single_random_option_web(self.dropdown_options)
                    time.sleep(1.2)
                except TimeoutException:
                    pytest.skip("No units available for this building")
            elif y == self.resident_service:
                try:
                    self.do_click(y)
                    time.sleep(0.8)
                    self.click_single_random_option_web(self.dropdown_options)
                    time.sleep(1.2)
                except TimeoutException:
                    pytest.skip("No resident available for this unit")
            elif y == self.service_type:
                try:
                    if self.is_visible(self.payment_warning):
                        pytest.skip("Warning,This user doesn't have autopay on.")
                except TimeoutException:
                    self.do_click(y)
                    time.sleep(0.8)
                    self.click_single_random_option_web(self.dropdown_options)
                    time.sleep(1.2)
            else:
                self.do_click(y)
                time.sleep(0.8)
                self.click_single_random_option_web(self.dropdown_options)
                time.sleep(1.2)
        time.sleep(1)
        self.scroll_to_location_web(self.order_btn)
        self.do_click(self.order_btn)
        time.sleep(0.8)
        self.do_click(self.ok_btn)
        time.sleep(1.2)
        return self.is_visible(self.service_orders)

    def leave_chat(self):
        time.sleep(1)
        clicks = [self.more_options_btn, self.leave_chat_option, self.confirm_btn]
        for x in clicks:
            self.do_click(x)
            time.sleep(0.8)
        time.sleep(1)
        return self.is_visible(self.ok_btn)
