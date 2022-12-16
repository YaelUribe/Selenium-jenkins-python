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
        events = util.wait_xpath(driver, util.xpath_contains("span", "Chat"))
        events.click()
        time.sleep(2)
    except:
        driver.refresh()
        time.sleep(1)
        chat = util.wait_xpath(driver, util.xpath_contains("span", "Chat"))
        chat.click()
        time.sleep(2)
    # if rate appear
    try:
        skip = driver.find_element_by_xpath("//img[@src='/assets/icons/thumbUp.svg']")
    except:
        pass
    if skip is not None:
        skip = driver.find_elements_by_xpath("//img[@src='/assets/icons/thumbUp.svg']")
        time.sleep(1)
        for i in range(len(skip)):
            try:
                time.sleep(0.5)
                skip[i].click()
                break
            except ElementNotInteractableException:
                pass


def test_send_message():
    try:
        text = util.wait_xpath(driver, "//textarea")
        text.send_keys("Test message")
        driver.find_element_by_xpath(util.xpath_contains("span", "Send")).click()
        time.sleep(1)
        message = util.wait_xpath(driver, util.xpath_contains("div", "Test message"))
        assert message.is_displayed()
        print("Send message OK")
    except ElementNotInteractableException:
        time.sleep(2)
        text = util.wait_xpath(driver, "//textarea")
        text.send_keys("Test message")
        driver.find_element_by_xpath(util.xpath_contains("span", "Send")).click()
        time.sleep(1)
        message = util.wait_xpath(driver, util.xpath_contains("div", "Test message"))
        assert message.is_displayed()
        print("Send message OK")
    except:
        print("Error on sending message")
        raise


def test_skip_rate():
    time.sleep(1)
    try:
        manger_tab = driver.execute_script('''window.open("_blank");''')
        driver.switch_to.window(driver.window_handles[1])
        util.wait_xpath(driver, util.xpath_contains("span", "Log out")).click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("button", "Confirm")).click()
        time.sleep(3)
        util.wait_xpath(driver, "//input[@placeholder='Enter email']").send_keys(util.manager_name)
        util.wait_xpath(driver, "//input[@placeholder='Enter password']").send_keys(util.password)
        util.wait_xpath(driver, util.xpath_contains("button", "Login")).click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("span", "Chat")).click()
        time.sleep(1)
        util.wait_classname(driver, "avatar-name").click()
        time.sleep(1)
        text = util.wait_xpath(driver, "//textarea")
        text.send_keys("Ok")
        driver.find_element_by_xpath(util.xpath_contains("span", "Send")).click()
        time.sleep(1)
    except:
        # driver.close()
        driver.switch_to.window(driver.window_handles[0])
        raise
    try:
        util.wait_xpath(driver, "//div[@class='ng-select-container']//span[@class='ng-arrow-wrapper']").click()
        time.sleep(1.5)
        elements = driver.find_elements_by_xpath("//div[@role='option']")
        num = random.choice(range(len(elements)))
        elements[num].location_once_scrolled_into_view
        elements[num].click()
        time.sleep(1)
        button = util.wait_xpath(driver, "//button[@class='mt-2 button is-primary ng-star-inserted']")
        button.location_once_scrolled_into_view
        button.click()
        time.sleep(1)
    except:
        pass
    try:
        util.wait_xpath(driver, util.xpath_contains("button", "Resolve ✓")).click()
        time.sleep(2)
    except (TimeoutException, ElementClickInterceptedException):
        time.sleep(3)
        util.wait_xpath(driver, util.xpath_contains("button", "Resolve ✓")).click()
        time.sleep(2)
    try:
        util.wait_xpath(driver, util.xpath_contains("button", "Confirm")).click()
    except TimeoutException:
        time.sleep(3)
        util.wait_xpath(driver, util.xpath_contains("button", "Resolve ✓")).click()
        util.wait_xpath(driver, util.xpath_contains("button", "Confirm")).click()
    time.sleep(3)
    try:
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.refresh()
        util.wait_xpath(driver, util.xpath_contains("span", "Logout")).click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("button", "Confirm")).click()
        time.sleep(1)
        util.wait_xpath(driver, "//input[@placeholder='Enter email']").send_keys(util.user_name)
        util.wait_xpath(driver, "//input[@placeholder='Enter password']").send_keys(util.password)
        util.wait_xpath(driver, util.xpath_contains("button", "Login")).click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("span", "Chat")).click()
        time.sleep(1)
    except:
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.refresh()
        util.wait_xpath(driver, util.xpath_contains("span", "Logout")).click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("button", "Confirm")).click()
        time.sleep(1)
        util.wait_xpath(driver, "//input[@placeholder='Enter email']").send_keys(util.user_name)
        util.wait_xpath(driver, "//input[@placeholder='Enter password']").send_keys(util.password)
        util.wait_xpath(driver, util.xpath_contains("button", "Login")).click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("span", "Chat")).click()
        time.sleep(1)
    try:
        skip = util.wait_xpath(driver,
                          "//div[@class='rating-box waiting ng-star-inserted']//span[@class='ng-star-inserted'][contains(text(),'Skip')]")
        skip.click()
        time.sleep(1)
        print("Skip rate Ok")
    except:
        print("Error on skip")
        raise


def test_rate_positive():
    time.sleep(1)
    try:
        text = util.wait_xpath(driver, "//textarea")
        text.send_keys("Test message")
        driver.find_element_by_xpath(util.xpath_contains("span", "Send")).click()
        time.sleep(3)
    except:
        time.sleep(3)
        text = util.wait_xpath(driver, "//textarea")
        text.send_keys("Test message")
        driver.find_element_by_xpath(util.xpath_contains("span", "Send")).click()
        time.sleep(3)
    try:
        driver.switch_to.window(driver.window_handles[1])
        util.wait_xpath(driver, "//tr[@class='clickable ng-star-inserted']").click()
        time.sleep(1)
        text = util.wait_xpath(driver, "//textarea")
        text.send_keys("Ok")
        driver.find_element_by_xpath(util.xpath_contains("span", "Send")).click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[@class='ng-select-container']//span[@class='ng-arrow-wrapper']").click()
        time.sleep(1.5)
        elements = driver.find_elements_by_xpath("//div[@role='option']")
        num = random.choice(range(len(elements)))
        elements[num].location_once_scrolled_into_view
        elements[num].click()
        time.sleep(1)
        button = util.wait_xpath(driver, "//button[@class='mt-2 button is-primary ng-star-inserted']")
        button.location_once_scrolled_into_view
        button.click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("button", "Resolve ✓")).click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("button", "Confirm")).click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        up = driver.find_element_by_xpath(
            "//div[@class='rating-box waiting ng-star-inserted']//div[@class='r-action positive ng-star-inserted']//img[@class='ng-star-inserted']")
        up.click()
        time.sleep(1)
    except:
        # driver.close()
        driver.switch_to.window(driver.window_handles[0])
        raise
    try:
        assert driver.find_element_by_xpath("//div[@class='rating-box waiting ng-star-inserted']").is_displayed()
        # print("thank you for your feedback message displayed")
    except AssertionError:
        print("error rate feedback message")
    print("Rate positive Ok")


def test_rate_negative_choose_other():
    try:
        text = util.wait_xpath(driver, "//textarea")
        text.send_keys("Test message")
        driver.find_element_by_xpath(util.xpath_contains("span", "Send")).click()
        time.sleep(3)
    except:
        time.sleep(3)
        text = util.wait_xpath(driver, "//textarea")
        text.send_keys("Test message")
        driver.find_element_by_xpath(util.xpath_contains("span", "Send")).click()
        time.sleep(3)
    try:
        driver.switch_to.window(driver.window_handles[1])
        util.wait_xpath(driver, "//tr[@class='clickable ng-star-inserted']").click()
        time.sleep(1)
        text = util.wait_xpath(driver, "//textarea")
        text.send_keys("Ok")
        driver.find_element_by_xpath(util.xpath_contains("span", "Send")).click()
        time.sleep(1)
        util.wait_xpath(driver, "//div[@class='ng-select-container']//span[@class='ng-arrow-wrapper']").click()
        time.sleep(1.5)
        elements = driver.find_elements_by_xpath("//div[@role='option']")
        num = random.choice(range(len(elements)))
        elements[num].location_once_scrolled_into_view
        elements[num].click()
        time.sleep(1)
        button = util.wait_xpath(driver, "//button[@class='mt-2 button is-primary ng-star-inserted']")
        button.location_once_scrolled_into_view
        button.click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("button", "Resolve ✓")).click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("button", "Confirm")).click()
        time.sleep(3)
    except:
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
    try:
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
    except:
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
    try:
        down = driver.find_element_by_xpath(
            "//div[@class='rating-box waiting ng-star-inserted']//div[@class='r-action negative ng-star-inserted']//img[@class='ng-star-inserted']")
        down.click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'Other')]").click()
        util.wait_xpath(driver, "//textarea[@placeholder='(Optional)']").send_keys("Test message")
        driver.find_element_by_xpath("//span[contains(text(),'Not now')]").click()
        assert driver.find_element_by_xpath("//div[@class='rating-box waiting ng-star-inserted']").is_displayed()
        # print("thank you for your feedback message displayed")
    except AssertionError:
        print("error rate feedback message")
    print("Rate negative choose other Ok")


def test_rate_negative_my_issue_not_resolved():
    try:
        time.sleep(1)
        text = util.wait_xpath(driver, "//textarea")
        time.sleep(1)
        text.send_keys("Test message")
        driver.find_element_by_xpath(util.xpath_contains("span", "Send")).click()
    except ElementNotInteractableException:
        time.sleep(2)
        text = util.wait_xpath(driver, "//textarea")
        text.send_keys("Test message")
        driver.find_element_by_xpath(util.xpath_contains("span", "Send")).click()
    try:
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
    except:
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
    try:
        util.wait_xpath(driver, "//tr[@class='clickable ng-star-inserted']").click()
        time.sleep(1)
        text = util.wait_xpath(driver, "//textarea")
        text.send_keys("Ok")
        driver.find_element_by_xpath(util.xpath_contains("span", "Send")).click()
        time.sleep(1)
    except:
        driver.refresh()
        chat = util.wait_xpath(driver, util.xpath_contains("span", "Chat"))
        chat.click()
        util.wait_xpath(driver, "//tr[@class='clickable ng-star-inserted']").click()
        time.sleep(1)
        text = util.wait_xpath(driver, "//textarea")
        text.send_keys("Ok")
        driver.find_element_by_xpath(util.xpath_contains("span", "Send")).click()
        time.sleep(1)
    try:
        util.wait_xpath(driver, "//div[@class='ng-select-container']//span[@class='ng-arrow-wrapper']").click()
        time.sleep(1.5)
        elements = driver.find_elements_by_xpath("//div[@role='option']")
        num = random.choice(range(len(elements)))
        elements[num].location_once_scrolled_into_view
        elements[num].click()
        time.sleep(1)
        button = util.wait_xpath(driver, "//button[@class='mt-2 button is-primary ng-star-inserted']")
        button.location_once_scrolled_into_view
        button.click()
        time.sleep(1)
    except:
        pass
    try:
        util.wait_xpath(driver, util.xpath_contains("button", "Resolve ✓")).click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("button", "Confirm")).click()
        time.sleep(3)
    except TimeoutException:
        time.sleep(2)
        util.wait_xpath(driver, util.xpath_contains("button", "Resolve ✓")).click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("button", "Confirm")).click()
        time.sleep(3)
    try:
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
    except:
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
    try:
        down = driver.find_element_by_xpath(
            "//div[@class='rating-box waiting ng-star-inserted']//div[@class='r-action negative ng-star-inserted']//img[@class='ng-star-inserted']")
        down.click()
        time.sleep(1)
        util.wait_xpath(driver, "//span[contains(text(),'My issue was not resolved!')]").click()
        assert driver.find_element_by_xpath("//div[@class='rating-box waiting ng-star-inserted']").is_displayed()
        # print("thank you for your feedback message displayed")
    except AssertionError:
        print("error rate feedback message")
    print("Rate negative my issue was not resolved Ok")


def test_rate_negative_second_time():
    driver.switch_to.window(driver.window_handles[1])
    try:
        assert util.wait_xpath(driver, "//span[3]//mat-icon[1]")
        print("Red flag rate issue not resolved is displayed")
    except:
        print("Red flag not displayed")
        raise
    try:
        util.wait_xpath(driver, "//tr[@class='clickable ng-star-inserted']").click()
        time.sleep(1)
        text = util.wait_xpath(driver, "//textarea")
        text.send_keys("Ok")
        driver.find_element_by_xpath(util.xpath_contains("span", "Send")).click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("button", "Resolve ✓")).click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("button", "Confirm")).click()
        time.sleep(3)
    except:
        driver.refresh()
        chat = util.wait_xpath(driver, util.xpath_contains("span", "Chat"))
        chat.click()
        util.wait_xpath(driver, "//tr[@class='clickable ng-star-inserted']").click()
        time.sleep(1)
        text = util.wait_xpath(driver, "//textarea")
        text.send_keys("Ok")
        driver.find_element_by_xpath(util.xpath_contains("span", "Send")).click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("button", "Resolve ✓")).click()
        time.sleep(1)
        util.wait_xpath(driver, util.xpath_contains("button", "Confirm")).click()
        time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    try:
        down = driver.find_element_by_xpath(
            "//div[@class='rating-box reopen ng-star-inserted']//div[@class='r-action negative ng-star-inserted']//img[@class='ng-star-inserted']")
        down.click()
        time.sleep(2)
        # wait_xpath(driver, "//span[contains(text(),'My issue was not resolved!')]").click()
        util.wait_xpath(driver, "//textarea[@placeholder='(Optional)']").send_keys("Test message")
        driver.find_element_by_xpath("//button[@class='button is-primary']//span[contains(text(),'Send')]").click()
        time.sleep(1)
        assert driver.find_element_by_xpath("//div[@class='rating-box reopen ng-star-inserted']").is_displayed()
        # print("thank you for your feedback message displayed")
    except AssertionError:
        print("error rate feedback message")
    print("Rate negative second time Ok")


def test_teardown():
    driver.close()
    driver.quit()

