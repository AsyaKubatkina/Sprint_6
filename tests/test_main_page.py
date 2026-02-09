import pytest
import allure

from pages.main_page import MainPage
from data import FAQ_DATA


@allure.feature("Главная страница")
@allure.story("Вопросы о важном (FAQ)")
class TestMainPageFAQ:


    @allure.title("FAQ: при клике на вопрос #{num} открывается правильный ответ")
    @pytest.mark.parametrize("num, expected_text", FAQ_DATA)
    def test_faq_answer_opens_correct_text(self, driver, num, expected_text, prepared_driver):
        page = MainPage(prepared_driver)

        page.open_faq_answer(num)
        actual_text = page.get_faq_answer_text(num)

        assert actual_text == expected_text