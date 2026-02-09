import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    @allure.step("Открыть страницу: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Закрыть баннер cookies (если отображается)")
    def close_cookies_if_present(self, locator, timeout=2):
        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            self.driver.execute_script("arguments[0].click();", el)
        except TimeoutException:
            pass

    @allure.step("Сформировать локатор {locator_num} с num={num}")
    def format_locator(self, locator_num, num):
        by, locator = locator_num
        return by, locator.format(num)


    @allure.step("Клик по элементу: {locator}")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()


    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text


    @allure.step("Проскроллить до элемента: {locator}")
    def scroll_to(self, locator):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
        self.wait.until(EC.visibility_of_element_located(locator))

    
    @allure.step("Найти элемент (видимый): {locator}")
    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    

    @allure.step("Кликнуть и переключиться на новую вкладку")
    def click_and_switch_to_new_tab(self, locator, timeout=10):
        old_handles = set(self.driver.window_handles)
        self.click(locator)

        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > len(old_handles)
        )

        new_handle = (set(self.driver.window_handles) - old_handles).pop()
        self.driver.switch_to.window(new_handle)
    
