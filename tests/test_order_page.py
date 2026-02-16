import pytest
import allure
from pages.order_page import OrderPage
from data import ORDER_DATA
from tests.helpers import get_click_method


@allure.title("Создание заказа через: {entry_point}")
@pytest.mark.parametrize("entry_point, client_data, rent_data", ORDER_DATA)
def test_create_order(prepared_driver, entry_point, client_data, rent_data):
    order = OrderPage(prepared_driver)
    click_method = get_click_method(order, entry_point)

    order.create_order(click_method, client_data, rent_data)
    order.check_order_success()


@allure.title("Логотип Самоката ведёт на главную ({entry_point})")
@pytest.mark.parametrize("entry_point, client_data, rent_data", ORDER_DATA)
def test_scooter_logo_returns_home(prepared_driver, entry_point, client_data, rent_data):
    order = OrderPage(prepared_driver)
    click_method = get_click_method(order, entry_point)

    order.create_order(click_method, client_data, rent_data)
    order.wait_order_number_in_popup()
    order.click_view_status()
    order.click_scooter_logo()

    order.check_main_header_visible()


@allure.title("Логотип Яндекса открывает Дзен ({entry_point})")
@pytest.mark.parametrize("entry_point, client_data, rent_data", ORDER_DATA)
def test_yandex_logo_opens_dzen(prepared_driver, entry_point, client_data, rent_data):
    order = OrderPage(prepared_driver)
    click_method = get_click_method(order, entry_point)

    order.create_order(click_method, client_data, rent_data)
    order.wait_order_number_in_popup()
    order.click_view_status()
    order.click_yandex_logo()

    order.check_yandex_search_visible()

    