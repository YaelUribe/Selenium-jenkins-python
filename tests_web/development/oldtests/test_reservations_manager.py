import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, \
    ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import time
from timeit import default_timer as timer
import random
import sys
import warnings
from selenium.webdriver.chrome.options import Options
import util.mobile as util

"""
def test_reservationss(self):
"""
"""
    print("Test for manager reservations Mobile")
    driver = self.driver
    login(driver, self.dir, self.user_name, self.key)
    time.sleep(4)
    menu = wait_xpath(driver, self.path["menu"])
    menu.click()
    time.sleep(3)
    services = driver.find_element_by_class_name("icon-reservations")
    try:
        driver.implicitly_wait(10)
        services.click()
    except (ElementClickInterceptedException, ElementNotInteractableException):
        services = wait_link_text(driver, "RESERVATIONS")
        services.click()
    # Test view all recent reservations
    time.sleep(3)
    try:
        wait_all_css(driver, ".reservations-container")
        print("Reservations displayed")
    except TimeoutException:
        print("Reservations not displayed")
        raise
    # Test Reservations Filters
    time.sleep(3)
    inputs = driver.find_elements_by_xpath("//input")
    inputs[0].send_keys("Test")
    inputs[0].clear()
    print("Filter by Resident OK")
    dropdowns = wait_all_css(driver, ".item-dropdown")
    dropdowns[0].click()
    choices = wait_all_css(driver, "ion-item.newrequest-type.item.ng-binding")
    for i in range(len(choices) - 1):
        text = choices[i].text
        choices[i].click()
        time.sleep(4)
        print("Reservations with filter {} displayed".format(text))
        dropdowns[0].click()
        choices = wait_all_css(driver, "ion-item.newrequest-type.item.ng-binding")
    print("Filter by status OK")
    time.sleep(3)
    choices[0].click()"""
'''# Test Accept reservation ONLY ON WEB ??
    time.sleep(6)
    try:
        wait_xpath(driver, "//div[@placeholder='Status']").click()
        choices = driver.find_elements_by_class_name("ui-select-choices-row-inner")
        choices[1].click()
        time.sleep(1)
    except (TimeoutException, IndexError):
        time.sleep(18)
        wait_xpath(driver, "//div[@placeholder='Status']").click()
        choices = driver.find_elements_by_class_name("ui-select-choices-row-inner")
        choices[1].click()
        time.sleep(1)
    try:
        wait_xpath(driver, xpath_contains("a", "Accept")).click()
        time.sleep(1)
        wait_classname(driver, "confirm").click()
        time.sleep(5)
        driver.find_element_by_xpath(xpath_contains("button", "OK")).click()
        time.sleep(1)
        cost = driver.find_element_by_name("cost")
        cost.clear()
        cost.send_keys("0")
        wait_classname(driver, "confirm").click()
        time.sleep(1)
    except (NoSuchElementException, TimeoutException):
        pass
    try:
        driver.find_element_by_xpath(xpath_contains("button", "OK")).click()
        driver.find_element_by_class_name("ion-android-close").click()
    except NoSuchElementException:
        pass
    # print("Accept reservation Ok")
    # Test add blocked day
    wait_xpath(driver, xpath_contains("span", "Reservations")).click()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 1000);")
    wait_xpath(driver, xpath_contains("button", "Add Blocked Day ")).click()
    time.sleep(2)
    inputs = wait_xpaths(driver, ("//input"))
    inputs[0].send_keys("Christmas")
    time.sleep(1)
    inputs[1].send_keys("12/25/2020")
    wait_xpath(driver, xpath_contains("span", "Create")).click()
    time.sleep(2)
    print("Add blocked day Ok")
    # Test Remove Blocked day
    driver.execute_script("window.scrollTo(0, 1000);")
    remove = wait_xpaths(driver, xpath_contains("a", "Remove"))
    remove[1].click()
    time.sleep(1)
    print("Remove Blocked day Ok")
    # Test amenities display details
    driver.execute_script("window.scrollTo(0, -100);")
    wait_xpath(driver, "//a[@ng-click='goToAmenitiesList()']").click()
    time.sleep(3)
    amenities = wait_xpaths(driver, "//a[@ng-click='goToAmenity(amenity.id)']")
    num = random.choice(range(len(amenities)))
    amenities[num].click()
    try:
        wait_classname(driver, "amenity-info-section")
        print("Amenity info displayed")
    except TimeoutException:
        print("Selected amenitie display error")
        raise'''
