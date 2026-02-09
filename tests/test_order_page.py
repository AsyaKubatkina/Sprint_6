import pytest
import allure
from pages.order_page import OrderPage
from data import ORDER_DATA

@allure.title("Создание заказа через: {entry_point}")
@pytest.mark.parametrize("entry_point, client_data, rent_data", ORDER_DATA)
def test_create_order(prepared_driver, entry_point, client_data, rent_data):
    order = OrderPage(prepared_driver)

    if entry_point == "top":
        order.click_order_top()
    else:
        order.click_order_bottom()

    order.check_fields_about_client_opened()

    order.fill_data_about_client(client_data)
    order.check_fields_about_rent_opened()

    order.fill_data_about_rent(rent_data)
    order.submit_order()
    order.check_order_success()

    order.wait_order_number_in_popup()
    order.click_view_status()

    order.click_scooter_logo()
    order.check_main_header_visible()

    order.click_yandex_logo()
    order.check_yandex_search_visible()