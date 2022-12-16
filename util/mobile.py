from datetime import datetime, timedelta
import os
from allure import attachment_type
from allure_commons.types import AttachmentType
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
import sys
import warnings
from selenium.webdriver.chrome.options import Options
import allure

# Constants
now = datetime.now().strftime("%d-%m-%Y")
path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
screen_dir = os.path.join(path, "screenshot", str(now))
address = "http://localhost:8100"
event_address = "http://localhost:8100/tenant/events/upcoming"
password = "12345678"
wrong_password = "984294234"
user_name = "aakashh94@g8p3c.com"
user_name1 = "annelaure.garabedian@moc.liamg.z"
user_name_175a = "adam+175@dvoralife.zzc"
user_name_175b = "eyal+175@dvoralife.zzc"
user_name_prod = "tenant_two@dvoraliving.com"
user_name_prod1 = "tenant_three@dvoraliving.com"
manager_name = "mauricio@dvoralife.com"
manager_name_prod = "manager_one@dvoraliving.com"
lorem_ipsum = "Lorem ipsum dolor sit amet"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-application-cache')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--disable-dev-shm-usage")

# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument("--allow-insecure-localhost")
# chrome_options.add_argument("--incognito")


# Functions
def wait_xpath(driver, xpath):
    element = WebDriverWait(driver, 12).until(ec.visibility_of_element_located((By.XPATH, xpath)))
    return element


def wait_xpaths(driver, xpath):
    element = WebDriverWait(driver, 8).until(ec.presence_of_all_elements_located((By.XPATH, xpath)))
    return element


def wait_classname(driver, class_name):
    element = WebDriverWait(driver, 12).until(ec.visibility_of_element_located((By.CLASS_NAME, class_name)))
    return element


def wait_classesname(driver, class_name):
    try:
        element = WebDriverWait(driver, 8).until(ec.visibility_of_any_elements_located((By.CLASS_NAME, class_name)))
    except:
        element = WebDriverWait(driver, 8).until(ec.presence_of_all_elements_located((By.CLASS_NAME, class_name)))
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


def login(driver, url, user_name, passkey):
    driver.set_window_size(300, 1200)
    driver.get(url)
    user = wait_xpath(driver, "//input[@type='email']")
    user.send_keys(user_name)
    password = wait_xpath(driver, "//input[@type='password']")
    password.send_keys(passkey)
    password.send_keys(Keys.ENTER)
    time.sleep(1)
    #   driver.find_element_by_xpath(xpath_contains("ion-button", "LOGIN")).click()
    time.sleep(1.5)
    driver.refresh()


def xpath_contains(selector, text):
    xpath = "//" + selector + "[contains(text(),'" + text + "')]"
    return xpath


def take_picture(driver, name):
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
