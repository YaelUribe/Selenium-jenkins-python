import datetime
import os
import string
import time
import unittest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, \
    ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException

import time
import os
from datetime import datetime, timedelta

# Constants
from selenium.webdriver.support.wait import WebDriverWait

now = datetime.now().strftime("%d-%m-%Y")
path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
screen_dir = os.path.join(path, "screenshot", str(now))
address = "http://app.dvoraliving.com/"
password = "12345678"
wrong_password = "984294234"
user_name = "annelaure.garabedian@moc.liamg.z"
manager_name = "mauricio@dvoralife.com"
lorem_ipsum = "Lorem ipsum dolor sit amet"

# Locators
username_locator = "username"
password_locator = "password"
login_button = "//input[@value='Log in']"
user_menu = ".usermenu"
error = '.error'


# Functions

def screen_path():
    global screen_dir
    if not os.path.exists(screen_dir):
        os.makedirs(screen_dir)
        os.chmod(screen_dir, 0o755)
    return screen_dir


def save_screenshot(driver, name):
    _name = remove_special_characters(name)
    driver.get_screenshot_as_file(os.path.join(screen_path(), _name + '-' + now + ".png"))


def remove_special_characters(text):
    return text.translate(string.maketrans('', ''), '\\ / : * ? " < > |')


def wait_xpath(driver, xpath):
    element = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, xpath)))
    return element


def wait_id(driver, i_d):
    element = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, i_d)))
    return element


def wait_xpath_click(driver, xpath):
    element = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, xpath)))
    return element


def wait_xpath_present(driver, xpath):
    try:
        element = WebDriverWait(driver, 12).until(ec.presence_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        print("Waiting longer than expected")
        element = WebDriverWait(driver, 120).until(ec.presence_of_element_located((By.XPATH, xpath)))
    return element


def wait_classname(driver, class_name):
    element = WebDriverWait(driver, 12).until(ec.visibility_of_element_located((By.CLASS_NAME, class_name)))
    return element


def wait_css(driver, css):
    element = WebDriverWait(driver, 12).until(ec.visibility_of_element_located((By.CSS_SELECTOR, css)))
    return element


def wait_css_all(driver, css):
    element = WebDriverWait(driver, 12).until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, css)))
    return element


def wait_link_text(driver, text):
    element = WebDriverWait(driver, 12).until(ec.visibility_of_element_located((By.LINK_TEXT, text)))
    return element


def wait_name(driver, name):
    element = WebDriverWait(driver, 12).until(ec.visibility_of_element_located((By.NAME, name)))
    return element


def login(driver, url, user, passkey):
    # driver.set_window_size(300, 800)
    driver.get(url)
    time.sleep(2)
    user = wait_xpath(driver, "//input[@placeholder='Enter email']")
    user.clear()
    user.send_keys(user_name)
    passkey = wait_xpath(driver, "//input[@placeholder='Enter password']")
    passkey.clear()
    passkey.send_keys(passkey)
    passkey.send_keys(Keys.ENTER)


def xpath_contains(selector, text):
    xpath = "//" + selector + "[contains(text(),'" + text + "')]"
    return xpath


def autopay_off(driver):
    my_account = WebDriverWait(driver, 8).until(ec.visibility_of_element_located((By.XPATH,
                                                                                  "/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div[3]/div/p")))
    my_account.click()
    time.sleep(3)
    settings = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div[1]/a[1]/div")
    settings.click()
    time.sleep(2)
    payments = wait_xpath(driver, '//*[@id="settings-nav-section"]/div/a[2]')
    payments.click()
    time.sleep(2)
    toggle = wait_xpath_present(driver, "//*[@id='main-container']/div/div[2]/div/div[2]/div/div[2]/input")
    status = toggle.get_attribute("checked")
    if status is not None and status == "true":
        toggle.click()
        time.sleep(2)
        try:
            driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/button").click()
            time.sleep(4)
        except NoSuchElementException:
            pass
        try:
            driver.find_element_by_xpath("//*[@id='my-account-container']/div[2]/div/div[2]/button[2]").click()
            time.sleep(4)
        except NoSuchElementException:
            pass
        frame = wait_xpath(driver, "/html/body/iframe")
        driver.switch_to.frame(frame)
        time.sleep(4)
        try:
            time.sleep(2)
            card = wait_css(driver, "button.dropdown_list_button.rounded_corners.jtk_btn")
            time.sleep(2)
            card.click()
            time.sleep(2)
            card.click()
        except:
            time.sleep(2)
            card = wait_css(driver, "button.dropdown_list_button.rounded_corners.jtk_btn")
            time.sleep(2)
            card.click()
            time.sleep(2)
            card.click()
        time.sleep(2)
        try:
            toggle = driver.find_element_by_name("_enable_autopay")
            toggle.click()
        except (NoSuchElementException, TimeoutException):
            toggle = wait_css(driver, ".ha_right.float_right")
            toggle.click()
        time.sleep(4)
        close = wait_classname(driver, "close")
        close.click()
        driver.switch_to.default_content()
        print("Autopayment off")
        return True
    else:
        return False


def autopay_on(driver):
    my_account = WebDriverWait(driver, 8).until(ec.visibility_of_element_located((By.XPATH,
                                                                                  "/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div[3]/div/p")))
    my_account.click()
    time.sleep(3)
    settings = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div[1]/a[1]/div")
    settings.click()
    time.sleep(2)
    payments = wait_xpath(driver, '//*[@id="settings-nav-section"]/div/a[2]')
    payments.click()
    time.sleep(2)
    toggle = wait_xpath_present(driver, "//*[@id='main-container']/div/div[2]/div/div[2]/div/div[2]/input")
    status = toggle.get_attribute("checked")
    if status is None:
        toggle.click()
        time.sleep(3)
        frame = wait_xpath(driver, "/html/body/iframe")
        driver.switch_to.frame(frame)
        time.sleep(4)
        try:
            time.sleep(2)
            card = wait_css(driver, "button.dropdown_list_button.rounded_corners.jtk_btn")
            time.sleep(2)
            card.click()
            time.sleep(2)
            card.click()
        except:
            time.sleep(2)
            card = wait_css(driver, "button.dropdown_list_button.rounded_corners.jtk_btn")
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
            toggle = wait_xpath(driver, "//*[@id='win1']/div[1]/div/div/div/div/div/div[1]/div[5]/div[2]/label/input")
            toggle.click()
        time.sleep(2)
        confirm = driver.find_element_by_xpath(
            "//*[@id='win1']/div[1]/div/div/div/div/div/div[3]/div[2]/div[2]/div/div/button[1]")
        confirm.click()
        time.sleep(3)
        close = wait_classname(driver, "close")
        close.click()
        driver.switch_to.default_content()
        print("Autopayment on succesfull")
    else:
        pass


def autopay_verify(driver, link):
    my_account = WebDriverWait(driver, 8).until(ec.visibility_of_element_located((By.XPATH,
                                                                                  "/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div[3]/div/p")))
    my_account.click()
    time.sleep(3)
    settings = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div[1]/a[1]/div")
    settings.click()
    time.sleep(2)
    payments = wait_xpath(driver, '//*[@id="settings-nav-section"]/div/a[2]')
    payments.click()
    time.sleep(2)
    toggle = wait_xpath_present(driver, "//*[@id='main-container']/div/div[2]/div/div[2]/div/div[2]/input")
    status = toggle.get_attribute("checked")
    time.sleep(4)
    if status is not None and status == "true":
        return True
    else:
        return False

def take_picture(driver, name):
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
