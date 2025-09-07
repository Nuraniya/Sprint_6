import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from urls import Urls


@pytest.fixture(scope='function')
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    urls = Urls()
    driver.get(urls.MAIN_PAGE)
    driver.maximize_window()
    yield driver
    driver.quit()