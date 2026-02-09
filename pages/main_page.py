import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as L

class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    @allure.step("Открыть главную страницу Самоката")
    def open_main(self):
        self.open(self.URL)

    @allure.step("Проскроллить до последнего вопроса FAQ")
    def scroll_to_last_faq(self):
        self.scroll_to(L.FAQ_LAST_QUESTION)

    @allure.step("Открыть ответ FAQ для вопроса №{num}")
    def open_faq_answer(self, num):
        self.scroll_to_last_faq()
        question = self.format_locator(L.FAQ_QUESTION_NUM, num)
        self.scroll_to(question)
        self.click(question)

    @allure.step("Получить текст ответа FAQ для вопроса №{num}")
    def get_faq_answer_text(self, num):
        answer = self.format_locator(L.FAQ_ANSWER_NUM, num)
        return self.get_text(answer)