from selenium.webdriver.common.by import By

class MainPageLocators:
    FAQ_QUESTION_NUM = (By.ID, "accordion__heading-{}")
    FAQ_ANSWER_NUM = (By.ID, "accordion__panel-{}")
    FAQ_LAST_QUESTION = (By.ID, "accordion__heading-7")

    COOKIE_ACCEPT = (By.ID, "rcc-confirm-button")
    
