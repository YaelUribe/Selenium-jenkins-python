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


def test_open_complimentary_services():
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
        util.wait_xpath(driver, util.xpath_contains("ion-label", "SERVICES")).click()
        time.sleep(2)
        driver.refresh()
        time.sleep(3)
    except:
        raise


#@pytest.mark.skip
def test_complimentary_list_display():
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//app-complimentary[@class='ion-page']//ion-item[3]")
    except:
        raise
        assert False


#@pytest.mark.skip
def test_complimentary_detail_display():
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//app-complimentary[@class='ion-page']//ion-item[3]").click()
        time.sleep(1)
    except TimeoutException:
        time.sleep(2)
        util.wait_xpath(driver, "//app-complimentary[@class='ion-page']//ion-item[3]").click()
    except:
        raise
        assert False
    try:
        util.wait_xpath(driver, "//body//app-complimentary-detail//ion-content//ion-row[1]")
        driver.back()
    except:
        raise
        assert False
        driver.back()


#@pytest.mark.skip
def test_filter_select_day():
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//ion-select[@placeholder='All Week Days']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'Sunday')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
    except:
        raise
        assert False
    try:
        util.wait_xpath(driver, "//ion-select[@placeholder='All Week Days']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'Monday')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
    except:
        raise
        assert False
    try:
        util.wait_xpath(driver, "//ion-select[@placeholder='All Week Days']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'Monday')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
    except:
        raise
        assert False
    try:
        util.wait_xpath(driver, "//ion-select[@placeholder='All Week Days']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'Tuesday')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
    except:
        raise
        assert False
    try:
        util.wait_xpath(driver, "//ion-select[@placeholder='All Week Days']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'Wednesday')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
    except:
        raise
        assert False

    try:
        util.wait_xpath(driver, "//ion-select[@placeholder='All Week Days']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'Wednesday')]").location_once_scrolled_into_view
        util.wait_xpath(driver, "//div[contains(text(),'Thursday')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
    except:
        raise
        assert False

    try:
        util.wait_xpath(driver, "//ion-select[@placeholder='All Week Days']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'Wednesday')]").location_once_scrolled_into_view
        util.wait_xpath(driver, "//div[contains(text(),'Friday')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
    except:
        raise
        assert False

    try:
        util.wait_xpath(driver, "//ion-select[@placeholder='All Week Days']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'Wednesday')]").location_once_scrolled_into_view
        util.wait_xpath(driver, "//div[contains(text(),'Saturday')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
    except:
        raise
        assert False

    try:
        util.wait_xpath(driver, "//ion-select[@placeholder='All Week Days']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'All Weekdays')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
    except:
        raise
        assert False


#@pytest.mark.skip
def test_filter_select_day():
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//ion-select[@placeholder='Select Status']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'Incomplete')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
    except:
        raise
        assert False

    try:
        util.wait_xpath(driver, "//ion-select[@placeholder='Select Status']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'Complete')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
    except:
        raise
        assert False

    try:
        util.wait_xpath(driver, "//ion-select[@placeholder='Select Status']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'All Status')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
    except:
        raise
        assert False


#@pytest.mark.skip
def test_complete_service():
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//ion-select[@placeholder='Select Status']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'Incomplete')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
    except:
        raise
        assert False
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//app-complimentary[@class='ion-page']//ion-item[3]").click()
        time.sleep(2)
    except:
        driver.back()
        raise
        assert False
    try:
        util.wait_xpath(driver, "//button[@class='ionic-selectable-cover']").click()
        time.sleep(2)
        util.wait_xpath(driver, "//ion-modal//ion-item[1]//ion-icon[1]").click()
    except:
        driver.back()
        raise
        assert False
    try:
        time.sleep(1)
        util.wait_xpath(driver, "//ion-button[contains(text(),'COMPLETE SERVICE')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
    except:
        driver.back()
        assert False
        raise


def test_comment_service():
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//app-complimentary[@class='ion-page']//ion-item[3]").click()
        time.sleep(1)
    except TimeoutException:
        time.sleep(2)
        util.wait_xpath(driver, "//app-complimentary[@class='ion-page']//ion-item[3]").click()
    except:
        raise
        assert False
    try:
        util.wait_xpath(driver, "//textarea[@name='commentField']").send_keys("test comment")
        time.sleep(1)
        util.wait_xpath(driver, "//ion-col[3]//img[1]").click()
        time.sleep(2)
        util.wait_xpath(driver, "//ion-text[contains(text(),'test comment')]")
        driver.back()
    except:
        driver.back()
        assert False
        raise


def test_teardown():
    driver.close()
    driver.quit()
