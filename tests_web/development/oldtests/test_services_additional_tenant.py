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
from selenium.webdriver.chrome.options import Options
import util.web as util


def test_open_complimentary_services():
    global driver
    chrome_options = util.chrome_options
    driver = webdriver.Chrome(options=chrome_options)
    try:
        util.login(driver, util.address, util.user_name, util.password)
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
        util.wait_xpath(driver, "//h3[contains(text(),'ADDITIONAL SERVICES ')]").click()
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
    except:
        util.take_picture(driver, "open")
        assert False


def test_services_display():
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//ion-button[contains(text(),'Additional services')]").click()
        time.sleep(1)
    except:
        assert False
        raise


def test_teardown():
    driver.close()
    driver.quit()
