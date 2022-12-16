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
        user.send_keys(util.manager_name)
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


def test_event_list_display():
    try:
        events = wait_all_css(driver, ".event-image-container")
        print("{} events displayed".format(len(events)))
    except:
        print("No events displayed")
        # search bar
    search = wait_all_css(driver, ".icon-search.custom-dvora-icons")
    search[0].click()
    time.sleep(2)
    try:
        search_bar = wait_all_css(driver, ".ng-touched")
    except:
        search_bar = wait_all_css(driver, "input")
    search_bar[0].send_keys("test")
    try:
        wait_all_css(driver, ".event-image-container")
        print("test search bar OK")
    except:
        print("Error in test search bar")
        raise
    search_bar[0].clear()


def test_event_filters():
    dropdowns = wait_all_css(driver, ".item-dropdown")
    dropdowns[0].click()
    choices = wait_all_css(driver, "ion-item.newrequest-type.item.ng-binding")
    while True:
        num = random.choice(range(len(choices)))
        if choices[num].text != '':
            break
        else:
            continue
    choices[num].location_once_scrolled_into_view
    print("Property {} selected".format(choices[num].text))
    choices[num].click()
    try:
        wait_all_css(driver, ".event-image-container")
        print("test filter by property OK")
    except:
        print("no event displayed for property selected")


def test_event_detail_display():
    assert True


def test_event_bookings_list():
    assert True


def test_event_bookings_details():
    assert True


def test_add_event():
    assert True


def test_edit_event():
    assert True


def test_delete_event():
    assert False


def test_teardown():
    driver.close()
    driver.quit()