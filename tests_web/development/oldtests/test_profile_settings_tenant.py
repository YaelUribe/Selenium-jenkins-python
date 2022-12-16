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


def test_open_profile():
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
        util.wait_classname(driver, "name").click()
        time.sleep(1)
    except:
        print("Loggin Error")
        raise


# @pytest.mark.skip
def test_emergency_contacts_edit():
    try:
        util.wait_xpath(driver, util.xpath_contains("span", "My Profile")).click()
    except (TimeoutException, ElementClickInterceptedException):
        util.wait_xpath(driver, util.xpath_contains("span", "My Profile")).click()
    time.sleep(1)
    try:
        cellphone = util.wait_xpath(driver, "//input[@ng-reflect-name='cell_phone']")
        cellphone.clear()
        cellphone.send_keys("3145764839")
        time.sleep(1)
        work_phone = util.wait_xpath(driver, "//input[@ng-reflect-name='work_phone']")
        work_phone.clear()
        work_phone.send_keys("3283727382")
        name = util.wait_xpath(driver, "//input[@ng-reflect-name='emergency_contact_name']")
        name.clear()
        name.send_keys("name")
        email = util.wait_xpath(driver, "//input[@ng-reflect-name='emergency_contact_email']")
        email.clear()
        email.send_keys("email@gmail.com")
        cphone = util.wait_xpath(driver, "//input[@ng-reflect-name='emergency_contact_phone']")
        cphone.clear()
        cphone.send_keys("444 444-4444")
        wphone = util.wait_xpath(driver, "//input[@ng-reflect-name='emergency_contact_work_phone']")
        wphone.location_once_scrolled_into_view
        wphone.clear()
        wphone.send_keys("(555) 555-5333")
        hphone = util.wait_xpath(driver, "//input[@ng-reflect-name='emergency_contact_home_phone']")
        hphone.clear()
        hphone.send_keys("(555) 555-5333")
        driver.find_element_by_xpath(util.xpath_contains("button", "Save Changes")).click()
        time.sleep(1)
        assert util.wait_classname(driver, "notification-message")
        print("Emergency contact changes saved, banner displayed")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except TimeoutException:
        print("Emergency contact change error")


def test_my_unit():
    try:
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("span", "My Unit")).click()
        time.sleep(1)
        text = util.wait_css(driver, ".info.t-size-2")
        text2 = util.wait_classname(driver, "info")
        assert text.text in text2.text
        print("My unit info displayed")
    except:
        print("my unit info displayed")


def test_payment():
    payments = driver.find_elements_by_xpath(util.xpath_contains("span", "Payments"))
    payments[1].click()
    time.sleep(1)
    for x in range(2):
        time.sleep(3)
        toggle = driver.find_element_by_name("paymentToggle")
        status = toggle.get_attribute("checked")
        if status is not None and status == "true":
            toggle.click()
            time.sleep(2)
            frame = util.wait_xpath(driver, "/html/body/iframe")
            driver.switch_to.frame(frame)
            time.sleep(2)
            try:
                time.sleep(2)
                card = util.wait_css(driver, "button.dropdown_list_button.rounded_corners.jtk_btn")
                time.sleep(2)
                card.click()
                time.sleep(2)
                card.click()
            except:
                time.sleep(2)
                card = util.wait_css(driver, "button.dropdown_list_button.rounded_corners.jtk_btn")
                time.sleep(2)
                card.click()
                time.sleep(2)
                card.click()
            time.sleep(3)
            try:
                toggle = driver.find_element_by_name("_enable_autopay")
                toggle.click()
            except (NoSuchElementException, TimeoutException):
                toggle = util.wait_css(driver, ".ha_right.float_right")
                toggle.click()
            time.sleep(2)
            close = util.wait_classname(driver, "close")
            close.click()
            time.sleep(3)
            driver.switch_to.default_content()
            # print("Autopayment off succesfull")
        else:
            toggle.click()
            time.sleep(3)
            frame = util.wait_xpath(driver, "/html/body/iframe")
            driver.switch_to.frame(frame)
            time.sleep(2)
            try:
                time.sleep(2)
                card = util.wait_css(driver, "button.dropdown_list_button.rounded_corners.jtk_btn")
                time.sleep(2)
                card.click()
                time.sleep(2)
                card.click()
            except:
                time.sleep(2)
                card = util.wait_css(driver, "button.dropdown_list_button.rounded_corners.jtk_btn")
                time.sleep(2)
                card.click()
                time.sleep(2)
                card.click()
            time.sleep(2)
            try:
                toggle = driver.find_element_by_name("_enable_autopay")
                toggle.click()
            except TimeoutException:
                time.sleep(2)
                toggle = util.wait_xpath(driver,
                                    "//*[@id='win1']/div[1]/div/div/div/div/div/div[1]/div[5]/div[2]/label/input")
                toggle.click()
            time.sleep(2)
            try:
                confirm = util.wait_xpath_present(
                    driver,
                    "//*[@id='win1']/div[1]/div/div/div/div/div/div[3]/div[2]/div[2]/div/div/button[1]")
                confirm.click()
            except:
                time.sleep(3)
                confirm = driver.find_element_by_xpath(
                    "//*[@id='win1']/div[1]/div/div/div/div/div/div[3]/div[2]/div[2]/div/div/button[1]")
                confirm.click()
            time.sleep(3)
            close = util.wait_classname(driver, "close")
            close.click()
            driver.switch_to.default_content()
            print("Autopayment off/onn succesfull")
    time.sleep(1)


def test_security_change_password():
    try:
        util.wait_xpath(driver, util.xpath_contains("span", "Security")).click()
        time.sleep(3)
    except TimeoutException:
        time.sleep(3)
        util.wait_xpath(driver, util.xpath_contains("span", "Security")).click()
    try:
        time.sleep(3)
        inputs = driver.find_elements_by_xpath("//input[@type='password']")
        inputs[0].send_keys("12345678")
        inputs[1].send_keys("23456789")
        inputs[2].send_keys("23456789")
        driver.find_element_by_xpath(util.xpath_contains("button", "Save Changes")).click()
    except:
        time.sleep(3)
        inputs = driver.find_elements_by_xpath("//input[@type='password']")
        inputs[0].send_keys("12345678")
        inputs[1].send_keys("23456789")
        inputs[2].send_keys("23456789")
        driver.find_element_by_xpath(util.xpath_contains("button", "Save Changes")).click()
    try:
        util.wait_xpath(driver, util.xpath_contains("span", "Log out")).click()
        util.wait_xpath(driver, util.xpath_contains("button", "Confirm")).click()
    except (TimeoutException, ElementClickInterceptedException):
        driver.refresh()
        time.sleep(1)
        util.wait_classname(driver, "name").click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("span", "Log out")).click()
        util.wait_xpath(driver, util.xpath_contains("button", "Confirm")).click()
    try:
        user = util.wait_xpath(driver, "//input[@placeholder='Enter email']")
        user.send_keys(util.user_name)
        password = util.wait_xpath(driver, "//input[@placeholder='Enter password']")
        password.send_keys("23456789")
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        util.wait_classname(driver, "name").click()
    except TimeoutException:
        print("Error trying to login ")
        driver.refresh()
        user = util.wait_xpath(driver, "//input[@placeholder='Enter email']")
        user.clear()
        user.send_keys(util.user_name)
        password = util.wait_xpath(driver, "//input[@placeholder='Enter password']")
        password.clear()
        password.send_keys("12345678")
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        util.wait_classname(driver, "name").click()
    try:
        util.wait_xpath(driver, util.xpath_contains("span", "Security")).click()
        time.sleep(3)
        inputs = driver.find_elements_by_xpath("//input[@type='password']")
        inputs[0].send_keys("23456789")
        inputs[1].send_keys("12345678")
        inputs[2].send_keys("12345678")
        driver.find_element_by_xpath(util.xpath_contains("button", "Save Changes")).click()
        time.sleep(2)
        print("Change password successful")
    except:
        print("Error on changing to old password")
        raise


def test_notifications_toggles():
    try:
        util.wait_xpath(driver, util.xpath_contains("span", "Notifications")).click()
    except (TimeoutException, ElementClickInterceptedException):
        time.sleep(3)
        util.wait_xpath(driver, util.xpath_contains("span", "Notifications")).click()
    try:
        time.sleep(3)
        toggles = driver.find_elements_by_class_name("switch-body")
        toggles[0].click()
        time.sleep(1)
        toggles[0].click()
        time.sleep(1)
        toggles[1].click()
        time.sleep(1)
        toggles[1].click()
        time.sleep(1)
        toggles[2].click()
        time.sleep(1)
        toggles[2].click()
        time.sleep(1)
        print("Notifications toggles OK")
    except:
        print("Error on clicking toggle button")
        raise


def test_preferences_language():
    try:
        util.wait_xpath(driver, util.xpath_contains("span", "Preferences")).click()
        time.sleep(1)
        util.wait_classname(driver, "ng-input").click()
        util.wait_classname(driver, "ng-arrow-wrapper").click()
        time.sleep(2)
        print("Pending to add different language")
    except:
        print("Error on changing language")
        raise


def test_change_picture():
    try:
        dirpath = os.getcwd()
        time.sleep(2)
        upload_image = driver.find_element_by_name("newImage")
        upload_image.send_keys(dirpath + "/photo4.jpeg")
        driver.find_element_by_class_name("mat-icon").click()
        time.sleep(3)
        dirpath = os.getcwd()
        time.sleep(1)
        upload_image = driver.find_element_by_name("newImage")
        upload_image.send_keys(dirpath + "/photo5.jpeg")
        driver.find_element_by_class_name("mat-icon").click()
        time.sleep(3)
        print("Change picture successful")
    except:
        print("Error changing picture")
        raise


def test_teardown():
    driver.close()
    driver.quit()
