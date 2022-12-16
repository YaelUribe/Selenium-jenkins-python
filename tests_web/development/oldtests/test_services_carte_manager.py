from datetime import datetime, timedelta
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, \
    ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
import time
from timeit import default_timer as timer
import random
import sys
import warnings
from selenium.webdriver.chrome.options import Options
import util.mobile as util
from selenium.webdriver import ActionChains


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
        # driver.refresh()
        util.wait_xpath(driver, "//h1[contains(text(),'A La Carte')]").click()
        time.sleep(3)
        driver.refresh()
    except:
        raise


# @pytest.mark.skip
def test_manage_submitted():
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//ion-select[@name='statusSelect']").click()
        time.sleep(3)
        elements = driver.find_elements_by_xpath("//button[@role='checkbox']")
        elements[1].click()
        elements[2].click()
        elements[0].click()
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
        util.wait_xpath(driver, "//app-alacarte[@class='ion-page']//ion-grid[1]").click()
        time.sleep(1)
    except:
        raise
    try:
        util.wait_xpath(driver, util.xpath_contains("ion-button", "MANAGE SERVICE")).click()
        time.sleep(2)
    except:
        driver.get("http://localhost:8100/manager/services/alacarte")
        raise
    try:
        util.wait_xpath(driver, "//ion-icon[@name='calendar-outline']").click()
        time.sleep(2)
        tomorrow = datetime.now() + timedelta(days=1)
        time.sleep(1)
        tomorrow_formatted = tomorrow.strftime('%d')
        driver.find_element_by_xpath("//body//ion-button[3]").click()
        driver.find_element_by_xpath("//div[18]//button[1]//p[1]").click()
        util.wait_xpath(driver, "//ion-input[@placeholder='set duration']").send_keys("60")
        time.sleep(1)
        util.wait_xpath(driver, "//ion-select[@placeholder='Select Manager']").click()
        # pending bug tu be fixed
        driver.get("http://localhost:8100/manager/services/alacarte")
    except:
        driver.get("http://localhost:8100/manager/services/alacarte")
        raise
        assert False


# @pytest.mark.skip
def test_manage_scheduled():
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//ion-select[@name='statusSelect']").click()
        time.sleep(3)
        elements = driver.find_elements_by_xpath("//button[@role='checkbox']")
        elements[2].click()
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
    except:
        raise
    try:
        util.wait_xpath(driver, "//app-alacarte[@class='ion-page']//ion-grid[1]").click()
        time.sleep(1)
    except:
        driver.get("http://localhost:8100/manager/services/alacarte")
        pytest.skip()
    try:
        util.wait_xpath(driver, util.xpath_contains("ion-button", "MANAGE SERVICE")).click()
        time.sleep(2)
    except:
        driver.get("http://localhost:8100/manager/services/alacarte")
        raise
    try:
        util.wait_xpath(driver, "//ion-select[@ng-reflect-model='scheduled']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'In Progress')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//ion-select[@placeholder='Rate room conditions']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'2 - Normal')]").click()
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//ion-button[contains(text(),'SAVE UPDATES')]").click()
        time.sleep(3)
        driver.get(util.address + "/manager/services/alacarte")
    except:
        assert False
        raise


# @pytest.mark.skip
def test_manage_in_progress():
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//ion-select[@name='statusSelect']").click()
        time.sleep(3)
        elements = driver.find_elements_by_xpath("//button[@role='checkbox']")
        elements[1].click()
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
    except:
        raise
    try:
        util.wait_xpath(driver, "//app-alacarte[@class='ion-page']//ion-grid[1]").click()
        time.sleep(1)
    except:
        driver.get(util.address + "/manager/services/alacarte")
        pytest.skip()
    try:
        util.wait_xpath(driver, util.xpath_contains("ion-button", "MANAGE SERVICE")).click()
        time.sleep(2)
    except:
        driver.get(util.address + "/manager/services/alacarte")
        raise
    try:
        util.wait_xpath(driver, "//ion-select[@ng-reflect-model='in_progress']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'Completed')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//textarea[@placeholder='Enter completion notes']").send_keys("test comment")
        time.sleep(1)
        util.wait_xpath(driver, "//ion-button[contains(text(),'SAVE UPDATES')]").click()
        time.sleep(3)
        driver.get("http://localhost:8100/manager/services/alacarte")
    except:
        assert False
        raise


# @pytest.mark.skip
def test_charge_service():
    time.sleep(1)
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//ion-select[@name='statusSelect']").click()
        time.sleep(3)
        elements = driver.find_elements_by_xpath("//button[@role='checkbox']")
        elements[1].click()
        elements[2].click()
        elements[3].click()
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
    except:
        raise
    try:
        util.wait_xpath(driver, "//app-alacarte[@class='ion-page']//ion-grid[1]").click()
        time.sleep(1)
    except:
        driver.get(util.address + "/manager/services/alacarte")
        pytest.skip()
    try:
        driver.refresh()
        util.wait_xpath(driver, util.xpath_contains("ion-button", "CHARGE SERVICE")).click()
        time.sleep(2)
    except:
        driver.refresh()
        driver.get(util.address + "/manager/services/alacarte")
        raise
    try:
        element = util.wait_xpaths(driver, "//ion-footer")[1]
        ActionChains(driver).click(element).perform()
        driver.get("http://localhost:8100/manager/services/alacarte")
    except:
        assert False
        raise


# @pytest.mark.skip
def test_cancel_service():
    time.sleep(1)
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//ion-select[@name='statusSelect']").click()
        time.sleep(3)
        elements = driver.find_elements_by_xpath("//button[@role='checkbox']")
        elements[1].click()
        elements[2].click()
        elements[0].click()
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
    except:
        raise
    try:
        util.wait_xpath(driver, "//app-alacarte[@class='ion-page']//ion-grid[1]").click()
        time.sleep(1)
    except:
        driver.get(util.address + "/manager/services/alacarte")
        pytest.skip()
    try:
        driver.refresh()
        util.wait_xpath(driver, "//ion-button[contains(text(),'CANCEL THIS SERVICE')]").click()
        time.sleep(2)
    except:
        driver.refresh()
        driver.get(util.address + "/manager/services/alacarte")
        raise
    try:
        util.wait_xpath(driver, "//span[contains(text(),'Confirm')]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[contains(text(),'canceled')]")
        driver.get(util.address + "/manager/services/alacarte")
    except:
        driver.get(util.address + "/manager/services/alacarte")
        assert False
        raise


# @pytest.mark.skip
def test_add_new_note():
    time.sleep(1)
    time.sleep(1)
    try:
        util.wait_xpath(driver, "//ion-select[@name='statusSelect']").click()
        time.sleep(3)
        elements = driver.find_elements_by_xpath("//button[@role='checkbox']")
        elements[1].click()
        elements[2].click()
        elements[0].click()
        util.wait_xpath(driver, "//span[contains(text(),'OK')]").click()
        time.sleep(2)
    except:
        raise
    try:
        util.wait_xpath(driver, "//app-alacarte[@class='ion-page']//ion-grid[1]").click()
        time.sleep(1)
    except:
        driver.get(util.address + "/manager/services/alacarte")
        pytest.skip()
    try:
        util.wait_xpath(driver, "//ion-icon[@name='reader-outline']").click()
        time.sleep(1)
        util.wait_xpath(driver, "//textarea[@name='noteField']").send_keys("test comment")
        util.wait_xpath(driver, "//body//ion-toolbar//ion-col[2]").click()
        time.sleep(3)
        driver.get(util.address + "/manager/services/alacarte")
    except:
        driver.get(util.address + "/manager/services/alacarte")
        assert False
        raise


def test_teardown():
    driver.close()
    driver.quit()
