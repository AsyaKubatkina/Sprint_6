import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as L
from selenium.webdriver.support import expected_conditions as EC
from datetime import date


class OrderPage(BasePage):

    @allure.step("Нажать 'Заказать' сверху")
    def click_order_top(self):
        self.click(L.ORDER_TOP)

    @allure.step("Нажать 'Заказать' снизу")
    def click_order_bottom(self):
        self.scroll_to(L.ORDER_BOTTOM)  
        self.click(L.ORDER_BOTTOM)

    @allure.step("Проверить, что открылась форма заказа: 'Для кого самокат'")
    def check_fields_about_client_opened(self):
        assert self.find(L.FOR_WHO_HEADER).is_displayed()

    @allure.step("Шаг 1: заполнить данные клиента и нажать 'Далее'")
    def fill_data_about_client(self, data):
        self.find(L.FIRST_NAME).send_keys(data["first_name"])
        self.find(L.LAST_NAME).send_keys(data["last_name"])
        self.find(L.ADDRESS).send_keys(data["address"])

        self.click(L.METRO)
        self.find(L.METRO).send_keys(data["metro"])
        option = self.format_locator(L.METRO_OPTION_NUM, data["metro"])
        self.click(option)

        self.find(L.PHONE).send_keys(data["phone"])
        self.click(L.NEXT_BTN)

    @allure.step("Проверить, что открылся шаг 'Про аренду'")
    def check_fields_about_rent_opened(self):
        assert self.find(L.PRO_RENT_HEADER).is_displayed()

    @staticmethod
    def today_str():
        return date.today().strftime("%d.%m.%Y")

    @allure.step("Аренда: заполнить дату (сегодня)")
    def set_today_date(self):
        el = self.find(L.DATE)
        el.clear()
        el.send_keys(self.today_str())
        self.click(L.PRO_RENT_HEADER)  

    @allure.step("Аренда: Выбрать срок: {rent_period}")
    def choose_rent_period(self, rent_period):
        self.click(L.RENT_DROPDOWN)
        option = self.format_locator(L.RENT_OPTION_NUM, rent_period)
        self.click(option)

    @allure.step("Аренда: выбрать цвет: {color}")
    def choose_color(self, color):
        if color == "black":
            self.click(L.COLOR_BLACK)
        elif color == "grey":
            self.click(L.COLOR_GREY)

    @allure.step("Аренда: добавить комментарий")
    def add_comment(self, comment):
        el = self.find(L.COMMENT)
        el.clear()
        el.send_keys(comment)

    @allure.step("Аренда: заполнить данные")
    def fill_data_about_rent(self, data):
        self.set_today_date()
        self.choose_rent_period(data["rent_period"])
        self.choose_color(data["color"])
        self.add_comment(data["comment"])

    @allure.step("Оформить заказ и подтвердить (Заказать → Да)")
    def submit_order(self):
        self.click(L.ORDER_BTN)
        self.find(L.CONFIRM_TITLE)
        self.click(L.YES_BTN)

    @allure.step("Проверить, что заказ оформлен")
    def check_order_success(self):
        assert self.find(L.SUCCESS_TITLE).is_displayed()


    @allure.step("Нажать 'Посмотреть статус'")
    def click_view_status(self):
        self.click(L.VIEW_STATUS_BTN)
        
    @allure.step("Дождаться, что в попапе появился номер заказа")
    def wait_order_number_in_popup(self):
        self.wait.until(lambda d: any(ch.isdigit() for ch in self.find(L.SUCCESS_TEXT).text))
        return self.find(L.SUCCESS_TEXT).text


    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        self.click(L.SCOOTER_LOGO)


    @allure.step("Клик по логотипу Яндекса (в новую вкладку)")
    def click_yandex_logo(self):
        self.click_and_switch_to_new_tab(L.YANDEX_LOGO)


    @allure.step("Проверить, что открылась страница Яндекса/Дзена (видно поле поиска)")
    def check_yandex_search_visible(self):
        self.wait.until(EC.visibility_of_element_located(L.YANDEX_SEARCH))

    @allure.step("Страница статуса заказа > Нажатие на логотип Самокат > Проверить, что открывается главная страница ")
    def check_main_header_visible(self):
        assert self.find(L.MAIN_HEADER).is_displayed()