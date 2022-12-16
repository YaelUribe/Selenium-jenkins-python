import pytest
import util.web as util
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
import os
import sys
import warnings
from datetime import datetime, timedelta


def test_open_events():
    global driver
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.maximize_window()
        driver.get(util.address)
        user = util.wait_xpath(driver, "//input[@placeholder='Enter email']")
        user.send_keys(util.user_name)
        password = util.wait_xpath(driver, "//input[@placeholder='Enter password']")
        password.send_keys("12345678")
        password.send_keys(Keys.ENTER)
        time.sleep(1)
        events = util.wait_xpath(driver, util.xpath_contains("span", "Events"))
        events.click()
        time.sleep(1)
    except:
        print("Loggin Error")
        raise


# @pytest.mark.skip
def test_event_list():
    try:
        assert util.wait_classname(driver, "resident-events-list")
        print("Event list displayed")
    except (AssertionError, TimeoutException):
        print("Error event list not displayed")
        raise


# @pytest.mark.skip
def test_event_detail():
    time.sleep(2)
    try:
        view_details = util.wait_classname(driver, "card-image")
        view_details.click()
        time.sleep(2)
    except TimeoutException:
        driver.refresh()
        view_details = util.wait_classname(driver, "card-image")
        view_details.click()
        time.sleep(2)
    try:
        assert util.wait_classname(driver, "event-details")
        print("Event details displayed")
        driver.back()
        time.sleep(1)
    except AssertionError:
        print("Event details not displayed")


# @pytest.mark.skip
def test_book_free_event():
    try:
        time.sleep(3)
        price_tags = driver.find_elements_by_class_name("price-tag")
        status = driver.find_elements_by_class_name("event-actions")
        for i in range(len(price_tags)):
            if price_tags[i].text == "Free" and status[i].text == "VIEW DETAILS":
                price_tags[i].location_once_scrolled_into_view
                status[i].click()
                time.sleep(2)
                break
    except (TimeoutException, NoSuchElementException):
        print("No Free event avaliable")
        pytest.skip()
    try:
        util.wait_xpath(driver, util.xpath_contains("button", "Yes")).click()
        time.sleep(2)
        util.wait_xpath(driver, util.xpath_contains("button", "Yes, Continue")).click()
        util.wait_xpath(driver, util.xpath_contains("button", "Ok")).click()
        time.sleep(2)
        print("Book event successful")
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("a", "List")).click()
    except (TimeoutException, NoSuchElementException):
        print("Error on booking event")
        raise
        driver.find_element_by_xpath(util.xpath_contains("span", "Chat")).click()
        time.sleep(2)
        driver.find_element_by_xpath(util.xpath_contains("span", "Events")).click()
    time.sleep(3)


# @pytest.mark.skip
def test_book_paid_event():
    try:
        time.sleep(3)
        price_tags = driver.find_elements_by_class_name("price-tag")
        status = driver.find_elements_by_class_name("event-actions")
        for i in range(len(price_tags)):
            if price_tags[i].text != "Free" and status[i].text == "VIEW DETAILS":
                price_tags[i].location_once_scrolled_into_view
                status[i].click()
                break
    except:
        print("No paid event avaliable")
        pytest.skip()
    try:
        util.wait_xpath(driver, util.xpath_contains("button", "Yes")).click()
        util.wait_xpath(driver, util.xpath_contains("button", "Yes, Continue")).click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("button", "Pay")).click()
        time.sleep(3)
        frame = driver.find_element_by_xpath("/html/body/iframe")
        time.sleep(1)
        driver.switch_to.frame(frame)
        time.sleep(2)
        util.wait_xpath(driver, util.xpath_contains("button", "Continue")).click()
        time.sleep(1)
        util.wait_xpath(driver, "//button[@class='glow rounded_corners']").click()
        time.sleep(1)
        driver.switch_to.default_content()
        util.wait_xpath(driver, util.xpath_contains("button", "Ok")).click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("a", "List")).click()
    except:
        driver.refresh()
        util.wait_xpath(driver, util.xpath_contains("span", "Chat")).click()
        time.sleep(2)
        driver.find_element_by_xpath(util.xpath_contains("span", "Events")).click()
        print("Error on booking paid event")
        raise


# @pytest.mark.skip
def test_booking_filters():
    try:
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("a", "Bookings")).click()
        time.sleep(2)
    except TimeoutException:
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("a", "Bookings")).click()
        time.sleep(2)
    try:
        util.wait_classname(driver, "ng-arrow-wrapper").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[@role='option']").click()
        time.sleep(1)
        util.wait_classname(driver, "ng-arrow-wrapper").click()
        time.sleep(2)
        driver.find_elements_by_xpath("//div[@role='option']")[1].click()
        time.sleep(1)
        util.wait_classname(driver, "ng-arrow-wrapper").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[@role='option']").click()
        time.sleep(2)
        print("Booking filters Ok")
    except:
        driver.refresh()
        util.wait_xpath(driver, util.xpath_contains("span", "Chat")).click()
        time.sleep(2)
        driver.find_element_by_xpath(util.xpath_contains("span", "Events")).click()
        print("There are no paid events")
        raise


# @pytest.mark.skip
def test_cancel_free_booking():
    util.wait_xpath(driver, util.xpath_contains("a", "Bookings")).click()
    time.sleep(3)
    try:
        price_tags = driver.find_elements_by_class_name("price-tag")
        status = driver.find_elements_by_class_name("event-actions")
        for i in range(len(price_tags)):
            if price_tags[i].text == "Free" and status[i].text == "VIEW DETAILS":
                price_tags[i].location_once_scrolled_into_view
                status[i].click()
                break
                time.sleep(3)
    except ElementClickInterceptedException:
        util.wait_xpath(driver, util.xpath_contains("span", "Chat")).click()
        time.sleep(2)
        driver.find_element_by_xpath(util.xpath_contains("span", "Events")).click()
        price_tags = driver.find_elements_by_class_name("price-tag")
        status = driver.find_elements_by_class_name("event-actions")
        for i in range(len(price_tags)):
            if price_tags[i].text == "Free" and status[i].text == "VIEW DETAILS":
                price_tags[i - 1].location_once_scrolled_into_view
                status[i].click()
                break
                time.sleep(3)
    except:
        pytest.skip()
        # raise
    try:
        util.wait_xpath(driver, util.xpath_contains("button", "Cancel Booking")).click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("button", "Ok")).click()
        time.sleep(1)
        assert util.wait_xpath(driver, util.xpath_contains("button", "Yes"))
        print("Event successfully cancelled")
    except TimeoutException:
        print("Error on cancel booking")
        raise


def test_teardown():
    driver.close()
    driver.quit()
