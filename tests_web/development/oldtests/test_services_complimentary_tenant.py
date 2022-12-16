import allure
import pytest
from datetime import datetime, timedelta
import os
import unittest
from allure_commons.types import AttachmentType
from selenium import webdriver
import time
from timeit import default_timer as timer
import random
import sys
import warnings

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import util.web as util


def test_open_complimentary_services():
    global driver

    def test_open_chat():
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
        except:
            print("Log in Error")
            raise
        try:
            time.sleep(1)
            events = util.wait_xpath(driver, util.xpath_contains("span", "Services"))
            events.click()
            time.sleep(2)
        except:
            driver.refresh()
            time.sleep(1)
            chat = util.wait_xpath(driver, util.xpath_contains("span", "Services"))
            chat.click()
            time.sleep(2)
        try:
            util.wait_xpath(driver, util.xpath_contains("div", "Complimentary Services")).click()
            time.sleep(1)
        except:
            assert False


# @pytest.mark.skip
def test_weekly_refresh_toggle_on_off():
    time.sleep(3)
    try:
        value = driver.find_element_by_xpath("//input[@id='enableService0']")
    except TimeoutException:
        time.sleep(3)
        value = util.wait_xpath(driver, "//input[@id='enableService0']")
    except:
        assert False
        raise
    if not value.is_selected():
        try:
            driver.find_element_by_class_name("switch-container").click()
            time.sleep(1)
            save = util.wait_xpath(driver, "//button[contains(text(),'Save')]")
            save.location_once_scrolled_into_view
            save.click()
            time.sleep(1)
            util.wait_xpath(driver, "//button[contains(text(),'Ok')]").click()
            time.sleep(2)
        except:
            assert False
            raise
    else:
        try:
            driver.find_element_by_class_name("switch-container").click()
            time.sleep(1)
            util.wait_xpath(driver, "//button[contains(text(),'Confirm')]").click()
            time.sleep(1)
            util.wait_xpath(driver, "//button[contains(text(),'Ok')]").click()
        except:
            assert False
            raise
    time.sleep(3)
    try:
        value = driver.find_element_by_xpath("//input[@id='enableService0']")
    except TimeoutException:
        time.sleep(3)
        value = util.wait_xpath(driver, "//input[@id='enableService0']")
    except:
        assert False
    if not value.is_selected():
        try:
            driver.find_element_by_class_name("switch-container").click()
            time.sleep(1)
            save = util.wait_xpath(driver, "//button[contains(text(),'Save')]")
            save.location_once_scrolled_into_view
            save.click()
            time.sleep(1)
            util.wait_xpath(driver, "//button[contains(text(),'Ok')]").click()
            time.sleep(2)
        except:
            assert False
    else:
        try:
            driver.find_element_by_class_name("switch-container").click()
            time.sleep(1)
            util.wait_xpath(driver, "//button[contains(text(),'Confirm')]").click()
            time.sleep(1)
            util.wait_xpath(driver, "//button[contains(text(),'Ok')]").click()
        except:
            assert False


# @pytest.mark.skip
def test_in_unit_package_toggle_on_off():
    time.sleep(3)
    try:
        value = driver.find_element_by_xpath("//input[@id='enableService1']")
    except TimeoutException:
        time.sleep(3)
        value = util.wait_xpath(driver, "//input[@id='enableService1']")
    except:
        assert False
        raise
    if not value.is_selected():
        try:
            driver.find_elements_by_class_name("switch-container")[1].click()
            time.sleep(1)
            save = util.wait_xpath(driver, "//button[contains(text(),'Save')]")
            save.location_once_scrolled_into_view
            save.click()
            time.sleep(1)
            util.wait_xpath(driver, "//button[contains(text(),'Ok')]").click()
            time.sleep(2)
        except:
            assert False
            raise
    else:
        try:
            driver.find_elements_by_class_name("switch-container")[1].click()
            time.sleep(1)
            util.wait_xpath(driver, "//button[contains(text(),'Confirm')]").click()
            time.sleep(1)
            util.wait_xpath(driver, "//button[contains(text(),'Ok')]").click()
        except:
            assert False
            raise
    time.sleep(3)
    try:
        value = driver.find_element_by_xpath("//input[@id='enableService1']")
    except TimeoutException:
        time.sleep(3)
        value = driver.find_element_by_xpath("//input[@id='enableService1']")
    except:
        assert False
    if not value.is_selected():
        try:
            driver.find_element_by_class_name("switch-container").click()
            time.sleep(1)
            save = util.wait_xpath(driver, "//button[contains(text(),'Save')]")
            save.location_once_scrolled_into_view
            save.click()
            time.sleep(1)
            util.wait_xpath(driver, "//button[contains(text(),'Ok')]").click()
            time.sleep(2)
        except:
            assert False
    else:
        try:
            driver.find_element_by_class_name("switch-container").click()
            time.sleep(1)
            util.wait_xpath(driver, "//button[contains(text(),'Confirm')]").click()
            time.sleep(1)
            util.wait_xpath(driver, "//button[contains(text(),'Ok')]").click()
        except:
            assert False


# @pytest.mark.skip
def test_weekly_refresh_details():
    time.sleep(3)
    try:
        util.wait_xpath(driver, util.xpath_contains("a", "View Details")).click()
        time.sleep(1)
    except:
        time.sleep(2)
        util.wait_xpath(driver, util.xpath_contains("a", "View Details")).click()
    try:
        util.wait_xpath(driver, "//figure[@class='image service-img']")
        time.sleep(1)
        driver.back()
    except:
        util.take_picture(driver, "weekly_details")
        driver.back()
        assert False


# @pytest.mark.skip
def test_weekly_refresh_comment():
    time.sleep(3)
    try:
        value = driver.find_element_by_xpath("//input[@id='enableService0']")
    except TimeoutException:
        time.sleep(3)
        value = util.wait_xpath(driver, "//input[@id='enableService0']")
    except:
        assert False
        raise
    if not value.is_selected():
        try:
            driver.find_element_by_class_name("switch-container").click()
            time.sleep(1)
            save = util.wait_xpath(driver, "//button[contains(text(),'Save')]")
            save.location_once_scrolled_into_view
            save.click()
            time.sleep(1)
            util.wait_xpath(driver, "//button[contains(text(),'Ok')]").click()
            time.sleep(2)
        except:
            assert False
            raise
    try:
        util.wait_xpath(driver, util.xpath_contains("a", "View Details")).click()
        time.sleep(1)
    except:
        time.sleep(2)
        util.wait_xpath(driver, util.xpath_contains("a", "View Details")).click()
    try:
        util.wait_xpath(driver, "//textarea").send_keys("test comment")
        util.wait_xpath(driver,"//span[contains(text(),'Send')]").click()
        time.sleep(2)
        driver.back()
    except:
        util.take_picture(driver, "weekly_refresh_comments")
        driver.back()
        assert False


# @pytest.mark.skip
def test_in_unit_package_details():
    time.sleep(3)
    try:
        driver.find_elements_by_xpath(util.xpath_contains("a", "View Details"))[1].click()
        time.sleep(1)
    except:
        time.sleep(2)
        driver.find_elements_by_xpath(util.xpath_contains("a", "View Details"))[1].click()
    try:
        util.wait_xpath(driver, "//figure[@class='image service-img']")
        time.sleep(1)
        driver.back()
    except:
        util.take_picture(driver, "weekly_details")
        driver.back()
        assert False


# @pytest.mark.skip
def test_in_unit_package_comment():
    time.sleep(1)
    try:
        util.wait_xpaths(driver, util.xpath_contains("ion-text", "DETAILS"))[1].click()
        time.sleep(1)
    except:
        time.sleep(2)
        util.wait_xpaths(driver, util.xpath_contains("ion-text", "DETAILS"))[1].click()
    try:
        util.wait_xpath(driver, "//textarea").send_keys("test comment")
        util.wait_xpath(driver, "//app-simple-detail-services[@class='ion-page can-go-back']//ion-col[3]").click()
        driver.find_element_by_xpath("//span[@class='comment_title']").location_once_scrolled_into_view
        time.sleep(2)
        driver.back()
    except:
        util.take_picture(driver, "comment_in_unit")
        driver.back()
        assert False


@pytest.mark.skip
def test_weekly_refresh_special_instructions():
    time.sleep(3)
    try:
        driver.find_element_by_xpath("//ion-icon[@name='add-circle-outline']")
    except:
        util.wait_xpath(driver, "//ion-toggle").click()
        time.sleep(1)
        util.wait_xpath(driver, "//ion-button").click()
    try:
        util.wait_xpath(driver, "//ion-icon[@name='add-circle-outline']").click()
        time.sleep(2)
        text = driver.find_element_by_xpath("//textarea")
        text.clear()
        text.send_keys("Test comment")
        util.wait_xpath(driver, "//ion-button[contains(text(),'UPDATE SERVICE')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//ion-button").click()
        time.sleep(1)
    except:
        util.take_picture(driver, "weekly_special_instructions")
        assert False


@pytest.mark.skip
def test_in_unit_special_instructions():
    time.sleep(3)
    try:
        driver.find_elements_by_xpath("//ion-icon[@name='add-circle-outline']")[1]
    except:
        driver.find_elements_by_xpath("//ion-toggle")[1].click()
        time.sleep(1)
        util.wait_xpath(driver, "//ion-button").click()
        time.sleep(2)
    try:
        util.wait_xpaths(driver, "//ion-icon[@name='add-circle-outline']")[1].click()
        time.sleep(2)
        text = driver.find_element_by_xpath("//textarea")
        text.clear()
        text.send_keys("Test comment")
        util.wait_xpath(driver, "//ion-button[contains(text(),'UPDATE SERVICE')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//ion-button").click()
        time.sleep(1)
    except:
        util.take_picture(driver, "in_unit_special_instructions")
        assert False


def test_teardown():
    driver.close()
    driver.quit()
