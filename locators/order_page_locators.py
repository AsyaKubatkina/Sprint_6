from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Кнопка "Заказать" на главной странице Самоката
    ORDER_TOP = (By.XPATH, "//div[contains(@class,'Header_Nav')]/button[text()='Заказать']")
    ORDER_BOTTOM = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']")

    # Шаг 1: Данные клиента
    FOR_WHO_HEADER = (By.XPATH, "//div[contains(@class,'Order_Header') and text()='Для кого самокат']")
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME  = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS    = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO      = (By.CSS_SELECTOR, "input.select-search__input[placeholder='* Станция метро']")
    PHONE      = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BTN   = (By.XPATH, "//div[contains(@class,'Order_NextButton')]//button[text()='Далее']")

    METRO_OPTION_NUM = (
        By.XPATH,
        "//div[contains(@class,'select-search__select')]"
        "//button[contains(@class,'select-search__option')][.//div[text()='{}']]"
    )

    # Шаг 2: Данные аренды
    PRO_RENT_HEADER = (By.XPATH, "//div[contains(@class,'Order_Header') and text()='Про аренду']")
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    RENT_DROPDOWN = (By.XPATH, "//div[contains(@class,'Dropdown-placeholder') and contains(text(),'Срок аренды')]/..")
    RENT_OPTION_NUM = (By.XPATH, "//div[contains(@class,'Dropdown-option') and text()='{}']")

    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY  = (By.ID, "grey")

    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    ORDER_BTN = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']")

    # Модалка подтверждения / успеха
    CONFIRM_TITLE = (By.XPATH, "//div[contains(@class,'Order_ModalHeader') and contains(.,'Хотите оформить заказ')]")
    YES_BTN = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[text()='Да']")
    SUCCESS_TITLE = (By.XPATH, "//div[contains(@class,'Order_ModalHeader') and contains(.,'Заказ оформлен')]")
    SUCCESS_TEXT = (By.XPATH, "//div[contains(@class,'Order_Text')]")
    VIEW_STATUS_BTN = (By.XPATH, "//div[contains(@class,'Order_NextButton')]//button[contains(.,'Посмотреть статус')]")

    # Страница статуса
    TRACK_INPUT = (By.XPATH, "//input[contains(@class,'Track_Input')]")

    # Логотипы
    SCOOTER_LOGO = (By.CSS_SELECTOR, "a[href='/'] img[alt='Scooter']")
    YANDEX_LOGO = (By.CSS_SELECTOR, "a[href='//yandex.ru']")

    # Яндекс/Дзен: поле поиска
    YANDEX_SEARCH = (By.ID, "text")

    # Заголовок на странице Самоката
    MAIN_HEADER = (By.XPATH, "//div[contains(@class,'Home_Header') and contains(.,'Самокат')]")
