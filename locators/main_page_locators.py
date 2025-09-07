from selenium.webdriver.common.by import By

class MainPageLocators:
    #Кнопки "Заказать"
    ORDER_BUTTON_HEADER = (By.XPATH, "//button[contains(text(), 'Заказать') and @class='Button_Button__ra12g']")
    ORDER_BUTTON_FOOTER = (By.XPATH, "//button[contains(text(), 'Заказать') and @class='Button_Button__ra12g Button_Middle__1CSJM']")

    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//a[@href='/']")
    YANDEX_LOGO = (By.XPATH, "//a[@href='//yandex.ru']")

    # Вопросы о важном
    QUESTION_LOCATOR_TEMPLATE = "//div[@id='accordion__heading-{}']"
    ANSWER_LOCATOR_TEMPLATE = "//div[@id='accordion__panel-{}']/p"

    # Кнопка принятия куки
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")