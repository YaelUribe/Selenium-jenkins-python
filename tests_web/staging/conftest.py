import pytest
from selenium import webdriver
import time
import os


@pytest.fixture(scope='class')
def init_driver(request):
    time.sleep(5)
    web_driver = webdriver.Chrome(executable_path=os.getcwd()+"/chromedriver")
    web_driver.maximize_window()
    request.cls.driver = web_driver
    yield
    web_driver.close()
    web_driver.quit()
