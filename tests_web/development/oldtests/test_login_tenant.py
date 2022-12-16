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


def test_open_app():
    global driver
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(util.address)
    driver.maximize_window()


def test_wrong_email():
    try:
        user = util.wait_xpath(driver, "//input[@placeholder='Enter email']")
        user.send_keys("wrongemail@mail.com")
        password = util.wait_xpath(driver, "//input[@placeholder='Enter password']")
        password.send_keys("12345678")
        password.send_keys(Keys.ENTER)
        time.sleep(1)
    except ElementNotInteractableException:
        time.sleep(3)
        user = driver.find_element_by_xpath("//input[@placeholder='Enter email']")
        user.send_keys("wrongemail@mail.com")
        password = util.wait_xpath(driver, "//input[@placeholder='Enter password']")
        password.send_keys("12345678")
        password.send_keys(Keys.ENTER)
        time.sleep(1)
    try:
        assert util.wait_xpath(driver, util.xpath_contains("span", "Invalid email address or password"))
        print("Invalid email or password banner is displayed")
    except AssertionError:
        print("Error invalid email banner not displayed")


def test_wrong_password():
    time.sleep(1)
    try:
        driver.find_element_by_class_name("delete").click()
        user = util.wait_xpath(driver, "//input[@placeholder='Enter email']")
        user.clear()
        user.send_keys(util.user_name)
        password = util.wait_xpath(driver, "//input[@placeholder='Enter password']")
        password.clear()
        password.send_keys("wrongpass")
        password.send_keys(Keys.ENTER)
        time.sleep(1)
    except ElementNotInteractableException:
        time.sleep(3)
        user = driver.find_element_by_xpath("//input[@placeholder='Enter email']")
        user.clear()
        user.send_keys("wrongemail@mail.com")
        password = util.wait_xpath(driver, "//input[@placeholder='Enter password']")
        password.clear()
        password.send_keys("wrongpass")
        password.send_keys(Keys.ENTER)
        time.sleep(1)
    try:
        assert util.wait_xpath(driver, util.xpath_contains("span", "Invalid email address or password"))
        print("Invalid email or password banner is displayed")
    except AssertionError:
        print("Error invalid email banner not displayed")
    driver.find_element_by_class_name("delete").click()


def test_frequently_asked_questions():
    time.sleep(1)
    try:
        frequently_asked = driver.find_element_by_xpath(util.xpath_contains("a", "Frequently Asked Questions"))
        frequently_asked.click()
        time.sleep(1)
        faq = util.wait_xpath(driver, util.xpath_contains("div", "Frequently Asked Questions"))
        print(faq.text + " page loaded")
        time.sleep(1)
        driver.find_element_by_id("back_icon").click()
        time.sleep(1)
    except (NoSuchElementException, ElementClickInterceptedException):
        print("Error on clicking frequently asked question")
        raise
    except TimeoutException:
        print("Error page didnt load")
        time.sleep(1)
        driver.find_element_by_id("back_icon").click()
        time.sleep(1)
        raise


def test_terms_conditions():
    try:
        terms = util.wait_xpath(driver, util.xpath_contains("a", "Terms & Conditions"))
        terms.location_once_scrolled_into_view
        terms.click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
        assert util.wait_xpath(driver, util.xpath_contains("span", "DVORA LIFE™ RESIDENT COMMUNITY MEMBER TERMS"))
        print("Terms of conditions page displayed")
        time.sleep(1)
        driver.close()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
    except (NoSuchElementException, TimeoutException):
        print("Terms of conditions page not loaded ")
        time.sleep(1)
        driver.close()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        raise


def privacy_policy():
    try:
        util.wait_xpath(driver, util.xpath_contains("a", "Privacy Policy")).click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("span", "DVORA LIFE™ PRIVACY POLICY"))
        print("Privacy Policy page loaded")
    except (NoSuchElementException, TimeoutException):
        print("Privacy policy not page displayed ")
        raise
    finally:
        time.sleep(1)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)


def test_forgot_password_wrong_mail():
    util.wait_xpath(driver, util.xpath_contains("a", "Forgot password?")).click()
    time.sleep(1)
    try:
        email = util.wait_xpath(driver, "//input[@placeholder='Enter email']")
        email.send_keys("wrong@email.com")
        submit = driver.find_element_by_xpath(util.xpath_contains("button", "Submit"))
        submit.click()
        text = util.wait_xpath(driver, util.xpath_contains("span", "Invalid Email"))
        print(text.text + " message error is displayed")
    except (NoSuchElementException, TimeoutException):
        print("Invalid email adress error not displayed ")
        raise
    finally:
        time.sleep(1)
        driver.find_element_by_class_name("delete").click()


def test_forgot_password_correct_mail():
    try:
        email = util.wait_xpath(driver, "//input[@placeholder='Enter email']")
        email.clear()
        email.send_keys(util.user_name)
        submit = driver.find_element_by_xpath(util.xpath_contains("button", "Submit"))
        submit.click()
        time.sleep(1)
        text = util.wait_xpath(driver, util.xpath_contains("span", "Password reset email has been sent"))
        print(text.text + " message is displayed")
    except (NoSuchElementException, TimeoutException):
        print("Error on forgot password put correct email")
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("a", "Back to Login")).click()
        time.sleep(1)
        raise
    time.sleep(1)
    util.wait_xpath(driver, util.xpath_contains("a", "Back to Login")).click()
    time.sleep(1)


def test_login_successful():
    time.sleep(2)
    try:
        user = util.wait_xpath(driver, "//input[@placeholder='Enter email']")
        user.send_keys(util.user_name)
        password = util.wait_xpath(driver, "//input[@placeholder='Enter password']")
        password.send_keys("12345678")
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        util.wait_classname(driver, "unit")
        print("login succesful OK")
    except TimeoutException:
        print("Error trying to login ")
        raise


def test_teardown():
    driver.close()
    driver.quit()
