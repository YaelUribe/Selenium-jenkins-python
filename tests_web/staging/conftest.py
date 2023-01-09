import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os


@pytest.fixture(scope='class')
def init_driver(request):
    time.sleep(5)
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    web_driver = webdriver.Chrome(executable_path=os.getcwd()+"/chromedriver", options=options)
    request.cls.driver = web_driver
    yield
    web_driver.close()
    web_driver.quit()
