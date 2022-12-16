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


def test_open_visitors():
    global driver
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(util.address)
        driver.maximize_window()
        user = util.wait_xpath(driver, "//input[@placeholder='Enter email']")
        user.send_keys(util.user_name)
        password = util.wait_xpath(driver, "//input[@placeholder='Enter password']")
        password.send_keys("12345678")
        password.send_keys(Keys.ENTER)
    except:
        print("Loggin Error")
        raise
    try:
        time.sleep(1)
        visitors = util.wait_xpath(driver, util.xpath_contains("span", "Visitors"))
        visitors.click()
        time.sleep(2)
    except:
        driver.refresh()
        time.sleep(1)
        events = util.wait_xpath(driver, util.xpath_contains("span", "Visitors"))
        events.click()
        time.sleep(2)


# @pytest.mark.skip
def test_create_new_visitor():
    try:
        new_visitor = util.wait_xpath(driver, util.xpath_contains("button", "New Visitor"))
        new_visitor.click()
        time.sleep(2)
    except:
        driver.refresh()
        new_visitor = util.wait_xpath(driver, util.xpath_contains("button", "New Visitor"))
        new_visitor.click()
        time.sleep(2)
    try:
        name = util.wait_xpath(driver, "//input[@placeholder='Type visitor name']")
        name.send_keys("My visitor")
        start_date = util.wait_xpath(driver, "//input[@formcontrolname='visitorStartDate']")
        start_date.click()
        time.sleep(2)
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_formatted = tomorrow.strftime('%m/%d/%Y')
        start_date.send_keys(tomorrow_formatted)
        enddate = util.wait_xpath(driver, "//input[@formcontrolname='visitorEndDate']")
        enddate.click()
        tomorrow = datetime.now() + timedelta(days=2)
        tomorrow_formatted = tomorrow.strftime('%m/%d/%Y')
        enddate.send_keys(tomorrow_formatted)
        startime = util.wait_xpath(driver, "//input[@formcontrolname='visitorStartTime']")
        startime.click()
        startime.send_keys(Keys.ARROW_LEFT)
        startime.send_keys(Keys.ARROW_LEFT)
        startime.send_keys("0530pm")
        time.sleep(2)
        endtime = util.wait_xpath(driver, "//input[@formcontrolname='visitorEndTime']")
        endtime.click()
        endtime.send_keys(Keys.ARROW_LEFT)
        endtime.send_keys(Keys.ARROW_LEFT)
        endtime.send_keys("0530pm")
        time.sleep(2)
        time.sleep(1)
        create = util.wait_xpath(driver, util.xpath_contains("button", "Add New Visitor"))
        create.click()
    except:
        driver.refresh()
        name = util.wait_xpath(driver, "//input[@placeholder='Type visitor name']")
        name.send_keys("My visitor")
        start_date = util.wait_xpath(driver, "//input[@formcontrolname='visitorStartDate']")
        start_date.click()
        time.sleep(2)
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_formatted = tomorrow.strftime('%m/%d/%Y')
        start_date.send_keys(tomorrow_formatted)
        enddate = util.wait_xpath(driver, "//input[@formcontrolname='visitorEndDate']")
        enddate.click()
        tomorrow = datetime.now() + timedelta(days=2)
        tomorrow_formatted = tomorrow.strftime('%m/%d/%Y')
        enddate.send_keys(tomorrow_formatted)
        startime = util.wait_xpath(driver, "//input[@formcontrolname='visitorStartTime']")
        startime.click()
        startime.send_keys(Keys.ARROW_LEFT)
        startime.send_keys(Keys.ARROW_LEFT)
        startime.send_keys("0530pm")
        time.sleep(2)
        endtime = util.wait_xpath(driver, "//input[@formcontrolname='visitorEndTime']")
        endtime.click()
        endtime.send_keys(Keys.ARROW_LEFT)
        endtime.send_keys(Keys.ARROW_LEFT)
        endtime.send_keys("0530pm")
        time.sleep(2)
        time.sleep(1)
        create = util.wait_xpath(driver, util.xpath_contains("button", "Add New Visitor"))
        create.click()
    try:
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("button", "Ok")).click()
        time.sleep(2)
        assert util.wait_xpath(driver, util.xpath_contains("td", "My Visitor"))
        print("Create visitor successful")
        time.sleep(2)
    except(TimeoutException, ElementClickInterceptedException):
        print("Error on create visitor")
        raise


# @pytest.mark.skip
def test_visitor_detail():
    try:
        util.wait_xpath(driver, util.xpath_contains("td", "My Visitor")).click()
        time.sleep(2)
    except:
        driver.refresh()
        print("No visitor")
        pytest.skip()
    try:
        assert util.wait_xpath(driver, util.xpath_contains("div", "My Visitor"))
        print("New Vistor detail displayed")
        driver.back()
        time.sleep(1)
    except TimeoutException:
        print("New Visitor not displayed")
        driver.back()
        raise


# @pytest.mark.skip
def test_selection_interval():
    time.sleep(1)
    try:
        util.wait_classname(driver, "ng-arrow-wrapper").click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("span", "Daily")).click()
        time.sleep(1)
        util.wait_classname(driver, "ng-arrow-wrapper").click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("span", "Weekly")).click()
        time.sleep(1)
        util.wait_classname(driver, "ng-arrow-wrapper").click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("span", "Monthly")).click()
        time.sleep(1)
        util.wait_classname(driver, "ng-arrow-wrapper").click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("span", "Daily")).click()
        print("Daily, Weekly and Monthly clicked")
        time.sleep(2)
    except:
        print("Error on selection interval")
        raise


def test_click_arrows():
    try:
        time.sleep(1)
        util.wait_classname(driver, "has-text-left").click()
        time.sleep(1)
        util.wait_classname(driver, "has-text-left").click()
        time.sleep(1)
        util.wait_classname(driver, "has-text-right").click()
        time.sleep(1)
        util.wait_classname(driver, "has-text-right").click()
        print("click left and right arrows")
    except:
        print("Error on clicking")
        raise


def test_teardown():
    driver.close()
    driver.quit()
