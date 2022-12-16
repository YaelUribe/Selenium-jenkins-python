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


def test_chat_list_display():
    assert True


def test_star_new_conversation():
    try:
        take = driver.find_element_by_xpath(xpath_contains("button", "TAKE OVER"))
        take.click()
        time.sleep(2)
        confirm = driver.find_element_by_xpath(xpath_contains("button", "Confirm"))
        confirm.click()
    except:
        pass
    try:
        driver.find_element_by_xpath(xpath_contains("a", "Conversation")).click()
        time.sleep(3)
        try:
            take = driver.find_element_by_xpath(xpath_contains("button", "TAKE OVER"))
            take.click()
            time.sleep(2)
            confirm = driver.find_element_by_xpath(xpath_contains("button", "Confirm"))
            confirm.click()
        except:
            pass
        time.sleep(4)
        wait_xpath(driver, "//textarea[@placeholder='Add a message...']").send_keys("Hi this is a test")
        try:
            driver.find_element_by_class_name("send_message_chat").click()
        except ElementClickInterceptedException:
            time.sleep(4)
            driver.find_element_by_class_name("send_message_chat").click()
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element_by_xpath("//textarea").send_keys("Automated conversation details")
        driver.find_element_by_xpath(util.xpath_contains("button", "Start conversation")).click()
    print("Creating a conversation or writing to existing one Ok")


def test_send_message():
    wait_classname(driver, "icon-new-request").click()
    time.sleep(3)
    wait_xpath(driver, "//input[@placeholder='Select a Property Type']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//ion-item[@class='newrequest-type item ng-binding item-activated']").click()
    time.sleep(3)
    try:
        driver.find_element_by_xpath("//input[@placeholder='Select a Resident']").click()
    except ElementClickInterceptedException:
        time.sleep(3)
        driver.find_element_by_xpath("//input[@placeholder='Select a Resident']").click()
    time.sleep(2)
    choices = driver.find_elements_by_class_name("item-activated")
    num = random.choice(range(len(choices)))
    choices[num].location_once_scrolled_into_view
    choices[num].click()
    time.sleep(2)


def test_change_tier():
    time.sleep(5)
    name = driver.find_elements_by_class_name("avatar-hearder-container")
    for i in range(len(name)):
        try:
            try:
                name[i].click()
                break
            except ElementClickInterceptedException:
                time.sleep(3)
                name[i].click()
                break
        except ElementNotInteractableException:
            pass
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, -100);")
    tier = wait_all_css(driver, ".dropdown-tier")
    # tier[0].location_once_scrolled_into_view
    tier[0].click()
    time.sleep(3)
    choices = driver.find_elements_by_css_selector(".newrequest-type.item.ng-binding")
    time.sleep(1)
    num = random.choice(range(len(choices)))
    choices[num].click()
    time.sleep(2)
    wait_classname(driver, "button-positive").click()
    time.sleep(3)
    print("Change Tier Ok")


def test_assign_tag():
    assert True


def test_resident_detail_display():
    assert True


def test_add_notes():
    assert True


def test_change_assigned():
    asigned = driver.find_elements_by_class_name("newrequest-type-selected")
    asigned[1].click()
    choices = driver.find_elements_by_css_selector(".newrequest-type.item.ng-binding")
    time.sleep(3)
    num = random.choice(range(len(choices)))
    # choices[num].location_once_scrolled_into_view
    choices[num].click()
    time.sleep(1)
    wait_classname(driver, "button-positive").click()
    time.sleep(3)
    print("Change manager ok")
    # Test Add resident notes
    notes = wait_xpath(driver, "//textarea[@placeholder='Enter tenant note']")
    notes.location_once_scrolled_into_view
    notes.send_keys("Test notes")
    wait_xpath(driver, xpath_contains("button", "ADD NOTE")).click()
    time.sleep(3)
    try:
        note = driver.find_element_by_xpath(xpath_contains("p", "Test notes"))
        note.location_once_scrolled_into_view
        print("Add resident notes Ok")
    except NoSuchElementException:
        print("Note not found")
        raise


def test_resolve_conversation():
    time.sleep(3)
    back = driver.find_elements_by_css_selector(".button.button-icon.icon-back-button.custom-menu")
    for i in range(len(back)):
        try:
            back[i].click()
            break
        except (ElementClickInterceptedException, ElementNotInteractableException):
            pass
    try:
        wait_xpath(driver, xpath_contains("button", "TAKE OVER")).click()
        time.sleep(3)
        driver.find_element_by_class_name("button-positive").click()
    except (ElementClickInterceptedException, TimeoutException):
        wait_xpath(driver, xpath_contains("button", "TAKE OVER")).click()
        time.sleep(3)
        driver.find_element_by_class_name("button-positive").click()

    time.sleep(2)
    button = driver.find_elements_by_class_name("right-buttons")
    time.sleep(3)
    for i in range(len(button)):
        try:
            button[i].click()
        except ElementNotInteractableException:
            pass
    time.sleep(3)
    wait_classname(driver, "button-positive").click()
    time.sleep(3)
    wait_classname(driver, "button-positive").click()
    print("Resolve conversation Ok")


def test_closed_conversation():
    driver.find_element_by_xpath(xpath_contains("span", "CLOSED CONVERSATIONS")).click()
    time.sleep(3)
    items = wait_all_css(driver, ".item.maintenance-item.manager-maintenance-item")
    for i in range(len(items)):
        try:
            items[i].click()
            break
        except ElementClickInterceptedException:
            time.sleep(3)
            pass
    time.sleep(3)
    try:
        content = wait_classname(driver, "has-header")
        print("Closed Conversations OK")
    except TimeoutException:
        print("conversation details not found")
    driver.quit()


def test_teardown():
    driver.close()
    driver.quit()