import pytest
from selenium import webdriver
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators as L

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def prepared_driver(driver):
    # 1) открываем главную
    main = MainPage(driver)
    main.open_main()

    # 2) закрываем cookies (если есть)
    main.close_cookies_if_present(L.COOKIE_ACCEPT)

    return driver