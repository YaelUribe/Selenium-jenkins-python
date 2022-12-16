import allure
import pytest
from datetime import datetime, timedelta
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
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


def test_open_reservations():
    global driver
    chrome_options = util.chrome_options
    driver = webdriver.Chrome(options=chrome_options)
    try:
        util.login(driver, util.address, util.user_name, util.password)
    except:
        print("login error")
        raise
    try:
        # util.wait_xpath(driver, util.xpath_contains("span", "OK")).click()
        menu = util.wait_xpath(driver, "//ion-buttons[@slot='start']")
        menu.click()
        time.sleep(2)
        util.wait_xpath(driver, util.xpath_contains("ion-label", "RESERVATIONS")).click()
        time.sleep(3)
    except:
        assert False
        raise


# @pytest.mark.skip
def test_book_amenity():
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//ion-icon[@name='add']").click()
        time.sleep(3)
    except:
        raise
    try:
        amenities = util.wait_xpaths(driver, util.xpath_contains("p", "View Details"))
        num = random.choice(range(len(amenities)))
        amenities[num].location_once_scrolled_into_view
        amenities[num].click()
        time.sleep(3)
    except:
        driver.get(util.address + "/tenant/reservations/upcoming")
        raise
    try:
        driver.find_element_by_xpath("//span[contains(text(),'OK')]").click()
        time.sleep(1)
    except:
        pass
    try:
        scroll = driver.find_element_by_class_name("amenity-days-open")
        scroll.location_once_scrolled_into_view
        time.sleep(1)
        start_date = driver.find_elements_by_xpath("//ion-icon[@ng-reflect-name='calendar-outline']")
        time.sleep(1)
        start_date[1].click()
        time.sleep(2)
        tomorrow = datetime.now() + timedelta(days=1)
        time.sleep(1)
        tomorrow_formatted = tomorrow.strftime('%d')
        util.wait_xpath(driver, util.xpath_contains("p", tomorrow_formatted)).click()
        time.sleep(2)
        #driver.find_element_by_xpath("//body//ion-button[3]").click()
        #time.sleep(1)
        #driver.find_element_by_xpath("//div[18]//button[1]//p[1]").click()
        # driver.execute_script("arguments[0].click();", day)
        # driver.find_element_by_xpath("//div[26]//button[1]//p[1]").click()
        time.sleep(1)
    except:
        driver.get(util.address + "/tenant/reservations/upcoming")
        raise
    try:
        driver.find_element_by_xpath("//span[contains(text(),'OK')]").click()
        time.sleep(1)
        start_date = driver.find_elements_by_xpath("//ion-icon[@ng-reflect-name='calendar-outline']")
        time.sleep(1)
        start_date[1].click()
        time.sleep(1)
        tomorrow = datetime.now() + timedelta(days=2)
        time.sleep(1)
        tomorrow_formatted = tomorrow.strftime('%d')
        util.wait_xpath(driver, util.xpath_contains("p", tomorrow_formatted)).click()
    except:
        pass
    try:
        driver.find_element_by_xpath("//span[contains(text(),'OK')]").click()
        time.sleep(1)
        start_date = driver.find_elements_by_xpath("//ion-icon[@ng-reflect-name='calendar-outline']")
        time.sleep(1)
        start_date[1].click()
        time.sleep(1)
        tomorrow = datetime.now() + timedelta(days=3)
        time.sleep(1)
        tomorrow_formatted = tomorrow.strftime('%d')
        util.wait_xpath(driver, util.xpath_contains("p", tomorrow_formatted)).click()
    except:
        pass
    try:
        util.wait_xpath(driver, "//ion-col[7]//div[1]").click()
    except:
        driver.get(util.address + "/tenant/reservations/upcoming")
        raise
    try:
        button = driver.find_elements_by_xpath("//ion-button")
        button[1].click()
        time.sleep(3)
        driver.find_element_by_xpath("//span[contains(text(),'Close')]").click()
    except:
        driver.get(util.address + "/tenant/reservations/upcoming")
        # raise
        assert False


# @pytest.mark.skip
def test_reservation_detail_display():
    time.sleep(1)
    try:
        util.wait_classname(driver, "margin_img")
    except:
        assert False
        raise


# @pytest.mark.skip
def test_reservations_filters():
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//ion-select[@name='statusSelect']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'Pending')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(1)
    except:
        util.take_picture(driver, "filter")
        raise
    try:
        util.wait_xpath(driver, "//ion-select[@name='statusSelect']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'Approved')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(1)
    except:
        util.take_picture(driver, "filter")
        raise
    try:
        util.wait_xpath(driver, "//ion-select[@name='statusSelect']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'Declined')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(1)
    except:
        util.take_picture(driver, "filter")
        raise
    try:
        util.wait_xpath(driver, "//ion-select[@name='statusSelect']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'Cancelled')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(1)
    except:
        util.take_picture(driver, "filter")
        assert False
    try:
        util.wait_xpath(driver, "//ion-select[@name='statusSelect']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'All status')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(1)
    except:
        util.take_picture(driver, "filter")
        assert False


# @pytest.mark.skip
def test_past_reservation_display():
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//h1[contains(text(),'Past')]").click()
        time.sleep(2)
    except:
        util.take_picture(driver, "past")
        raise
    try:
        util.wait_xpath(driver, "//app-past-list//ion-grid[1]//ion-row[1]//ion-col[1]//div[1]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//h2")
    except:
        assert False


def test_teardown():
    driver.close()
    driver.quit()
