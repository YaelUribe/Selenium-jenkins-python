import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import util.mobile as util


def test_open_deliveries():
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
        util.wait_xpath(driver, util.xpath_contains("ion-label", "DELIVERIES")).click()
        time.sleep(3)
    except:
        raise


def test_deliveries_display():
    try:
        util.wait_xpath(driver, "//ion-item[1]//ion-grid[1]//ion-row[1]").click()
        time.sleep(1)
        driver.back()
    except TimeoutException:
        pytest.skip()
    except:
        util.take_picture(driver, "deliveries_display")
        assert False


def test_package_detail_display():
    try:
        util.wait_xpath(driver, "//ion-item[1]//ion-grid[1]//ion-row[1]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//ion-card-subtitle[contains(text(),'Package Detail')]")
        driver.back()
    except:
        util.take_picture(driver, "deliveries_display")
        assert False


def test_past_deliveries():
    try:
        util.wait_xpath(driver, "//ion-tab-button[@id='tab-button-old-deliveries']").click()
        time.sleep(1)
    except TimeoutException:
        assert False
    try:
        util.wait_xpath(driver, "//app-old-deliveries[@class='ion-page']//ion-item[1]")
        time.sleep(1)
    except:
        util.take_picture(driver, "deliveries_display")
        assert False


def test_past_package_detail():
    try:
        util.wait_xpath(driver, "//app-old-deliveries[@class='ion-page']//ion-item[1]").click()
        time.sleep(1)
        util.wait_xpath(driver, "//ion-card-subtitle[contains(text(),'Package Detail')]")
    except:
        util.take_picture(driver, "deliveries_display")
        assert False


def test_teardown():
    driver.close()
    driver.quit()
