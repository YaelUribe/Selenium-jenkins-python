import allure
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


def test_open_deliveries():
    global driver
    chrome_options = util.chrome_options
    driver = webdriver.Chrome(options=chrome_options)
    try:
        util.login(driver, util.address, util.manager_name, util.password)
    except:
        print("login error")
        raise
    try:
        menu = util.wait_xpath(driver, "//ion-buttons[@slot='start']")
        menu.click()
        time.sleep(2)
        util.wait_xpath(driver, util.xpath_contains("ion-label", "DELIVERIES")).click()
        time.sleep(1)
        driver.refresh()
        time.sleep(3)
    except:
        raise


def test_deliveries_display():
    try:
        util.wait_xpath(driver, "//body//app-new-deliveries//ion-item[1]")
    except:
        assert False
        raise


def test_package_detail_display():
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//body//app-new-deliveries//ion-item[1]").click()
        time.sleep(1)
    except:
        assert False
        raise
    try:
        util.wait_xpath(driver, "//ion-card-subtitle[contains(text(),'Package Detail')]")
        time.sleep(1)
        driver.back()
    except:
        assert False
        raise


def test_mark_as_dropped_off():
    time.sleep(1)
    try:
        util.wait_xpath(driver, util.xpath_contains("p", "Ready For Pickup")).click()
        time.sleep(1)
    except:
        raise
    try:
        util.wait_xpath(driver, "//ion-button[contains(text(),'MARK AS DROPPED')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//canvas").click()
        util.wait_xpath(driver, "//ion-text[contains(text(),'SUBMIT')]").click()
        time.sleep(1)
    except:
        driver.back()
        raise
    try:
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
    except:
        assert False
        raise


def test_past_deliveries_display():
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//h2[contains(text(),'PAST DELIVERIES')]").click()
        time.sleep(1)
    except:
        raise
    try:
        util.wait_xpath(driver, "//body//app-old-deliveries//ion-item[1]").click()
        time.sleep(1)
    except:
        raise
    try:
        util.wait_xpath(driver, "//ion-card-subtitle[contains(text(),'Package Detail')]")
        time.sleep(1)
        driver.back()
    except:
        assert False
        raise


def test_teardown():
    driver.close()
    driver.quit()
