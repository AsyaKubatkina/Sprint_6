import pytest
from selenium import webdriver
from config import BASE_URL
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators as L
from pages.base_page import BasePage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def prepared_driver(driver):
    # открыть сайт
    driver.get(BASE_URL)

    # закрыть cookies
    base = BasePage(driver)
    base.close_cookies_if_present(L.COOKIE_ACCEPT)

    return driver