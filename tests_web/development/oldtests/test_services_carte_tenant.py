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

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
import util.mobile as util


def test_open_a_la_carte_services():
    global driver
    chrome_options = util.chrome_options
    driver = webdriver.Chrome(options=chrome_options)
    try:
        util.login(driver, util.address, util.user_name1, util.password)
    except:
        print("login error")
        raise
    try:
        util.wait_xpath(driver, util.xpath_contains("span", "OK")).click()
        menu = util.wait_xpath(driver, "//ion-buttons[@slot='start']")
        menu.click()
        time.sleep(2)
        util.wait_xpath(driver, util.xpath_contains("ion-label", "SERVICES")).click()
        time.sleep(1)
        util.wait_xpath(driver, "//h3[contains(text(),'A LA CARTE SERVICES')]").click()
        time.sleep(1)
        driver.refresh()
        time.sleep(3)
    except:
        assert False


def test_book_with_no_day():
    try:
        items = util.wait_xpaths(driver, "//ion-thumbnail")
        num = random.choice(range(len(items)))
        items[num].location_once_scrolled_into_view
        items[num].click()
    except:
        raise
    try:
        util.wait_xpath(driver, "//ion-button[contains(text(),'BOOK SERVICE')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        driver.back()
        time.sleep(1)
    except:
        driver.back()
        assert False


def test_book_service():
    try:
        items = util.wait_xpaths(driver, "//ion-thumbnail")
        num = random.choice(range(len(items)))
        items[num].location_once_scrolled_into_view
        items[num].click()
        time.sleep(1)
    except:
        raise
    try:
        time.sleep(1)
        day = util.wait_xpath(driver, util.xpath_contains("div", "monday"))
        day.location_once_scrolled_into_view
        time.sleep(1)
        day.click()
    except:
        time.sleep(1)
        day = util.wait_xpath(driver, util.xpath_contains("div", "monday"))
        day.location_once_scrolled_into_view
        day.click()
    try:
        time.sleep(2)
        util.wait_xpath(driver, "//ion-button[contains(text(),'BOOK SERVICE')]").click()
        time.sleep(2)
        util.wait_xpath(driver, "//span[contains(text(),'Close')]").click()
        time.sleep(2)
        assert util.wait_xpath(driver, "//ion-title[contains(text(),'BOOKED A LA CARTE')]")
        util.wait_xpath(driver,
                        "//app-booked-lists[@class='ion-page can-go-back']//ion-icon[@name='chevron-back-outline']").click()
    except:
        driver.back()
        assert False


def test_booked_display():
    driver.refresh()
    try:
        util.wait_xpath(driver, "//ion-button[contains(text(),'Booked')]").click()
        time.sleep(1)
    except:
        raise
    try:
        assert util.wait_xpath(driver, "//ion-card")
        driver.back()
        time.sleep(2)
    except:
        assert False


def test_booked_detail_comment():
    driver.refresh()
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//ion-button[contains(text(),'Booked')]").click()
        time.sleep(1)
    except:
        time.sleep(2)
        util.wait_xpath(driver, "//ion-button[contains(text(),'Booked')]").click()
    try:
        time.sleep(2)
        util.wait_xpath(driver, "//ion-card").click()
        time.sleep(1)
    except:
        raise
    try:
        util.wait_xpath(driver, "//textarea").send_keys("test comment")
        util.wait_xpath(driver, "//ion-col[3]//img[1]").click()
        time.sleep(2)
        assert util.wait_xpath(driver, "//ion-text[contains(text(),'test comment')]")
        driver.back()
        time.sleep(1)
        driver.back()
    except:
        driver.get(util.address + "/tenant/services/alacarte-services")
        assert False


def test_book_subscription():
    driver.refresh()
    time.sleep(2)
    try:
        util.wait_xpaths(driver, "//ion-thumbnail")[0].click()
    except:
        time.sleep(2)
        util.wait_xpaths(driver, "//ion-thumbnail")[0].click()
    try:
        time.sleep(1)
        day = util.wait_xpath(driver, util.xpath_contains("div", "Weekly"))
        day.location_once_scrolled_into_view
        time.sleep(1.5)
        day.click()
        time.sleep(1)
        day = util.wait_xpath(driver, util.xpath_contains("div", "monday"))
        day.click()
        util.wait_xpath(driver, "//ion-button[contains(text(),'BOOK SERVICE')]").click()
        time.sleep(2)
        util.wait_xpath(driver, "//span[contains(text(),'Close')]").click()
        time.sleep(2)
        assert util.wait_xpath(driver, "//ion-title[contains(text(),'BOOKED A LA CARTE')]")
        util.wait_xpath(driver,
                        "//app-booked-lists[@class='ion-page can-go-back']//ion-icon[@name='chevron-back-outline']").click()
    except:
        driver.get(util.address+"/tenant/services/alacarte-services")
        assert False


def test_subscriptions_display():
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//ion-button[contains(text(),'Booked')]").click()
        time.sleep(1)
    except:
        raise
    try:
        util.wait_xpath(driver, "//h1[contains(text(),'SUBSCRIPTIONS')]").click()
        time.sleep(1)
    except:
        driver.back()
        raise
    try:
        assert util.wait_xpath(driver, "//ion-title[contains(text(),'BOOKED A LA CARTE')]")
        driver.get(util.address+"/tenant/services/alacarte-services")
    except:
        driver.get(util.address + "/tenant/services/alacarte-services")
        assert False


def test_book_no_autopay():
    time.sleep(1)
    try:
        driver.get(util.address + "/tenant/payments/history")
    except:
        raise
    try:
        time.sleep(2)
        util.wait_xpath(driver, "//ion-toggle").click()
        time.sleep(2)
    except:
        raise
    try:
        frame = util.wait_xpath(driver, "//iframe[@frameborder='true']")
    except TimeoutException:
        frame = util.wait_xpath(driver, "//iframe[@frameborder='true']")
    driver.switch_to.frame(frame)
    time.sleep(2)
    try:
        toggle = driver.find_element_by_name("_enable_autopay")
        toggle.click()
    except (NoSuchElementException, TimeoutException):
        toggle = driver.find_element_by_name("_enable_autopay")
        toggle.click()
    time.sleep(4)
    close = util.wait_classname(driver, "icon-cancel")
    close.click()
    driver.switch_to.default_content()
    driver.back()
    time.sleep(1)
    try:
        items = util.wait_xpaths(driver, "//ion-thumbnail")
        num = random.choice(range(len(items)))
        items[num].location_once_scrolled_into_view
        items[num].click()
        time.sleep(1)
    except:
        raise
    try:
        day = util.wait_xpath(driver, util.xpath_contains("div", "monday"))
        day.location_once_scrolled_into_view
        time.sleep(1)
        day.click()
        time.sleep(1)
        util.wait_xpath(driver, "//ion-button[contains(text(),'BOOK SERVICE')]").click()
        time.sleep(2)
        util.wait_xpath(driver, "//ion-toggle").click()
    except:
        raise
    try:
        frame = util.wait_xpath(driver, "//iframe[@frameborder='true']")
    except TimeoutException:
        frame = util.wait_xpath(driver, "//iframe[@frameborder='true']")
    driver.switch_to.frame(frame)
    time.sleep(4)
    try:
        driver.find_element_by_css_selector(".tooltip_content.message_bar_warning.rounded_corners").click()
        driver.find_element_by_css_selector(".rounded_corners.jtk_btn.invalid-input").click()
        time.sleep(1)
        driver.find_element_by_class_name("icon-ok").click()
    except NoSuchElementException:
        pass
    try:
        toggle = util.wait_xpath(driver, "/html/body/div[1]/div[2]/div/div/div/div[1]/div[5]/div[2]")
        toggle.click()
    except TimeoutException:
        time.sleep(2)
        toggle = util.wait_xpath(driver, "/html/body/div[1]/div[2]/div/div/div/div[1]/div[5]/div[2]")
        toggle.click()
    time.sleep(2)
    confirm = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/button[1]")
    confirm.click()
    driver.switch_to.default_content()
    try:
        util.wait_xpath(driver, "//span[contains(text(),'Close')]").click()
        time.sleep(2)
        assert util.wait_xpath(driver, "//ion-title[contains(text(),'BOOKED A LA CARTE')]")
        util.wait_xpath(driver,
                        "//app-booked-lists[@class='ion-page can-go-back']//ion-icon[@name='chevron-back-outline']").click()
    except:
        assert False


def test_teardown():
    driver.close()
    driver.quit()
