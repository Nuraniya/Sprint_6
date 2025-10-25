from selenium.webdriver.common.by import By


class OrderPageLocators:
    #Первая форма
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая форма
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(text(), 'Срок аренды')]")
    RENT_PERIOD_1_DAY = (By.XPATH, "//div[text()='сутки']")
    RENT_PERIOD_2_DAYS = (By.XPATH, "//div[text()='двое суток']")
    RENT_PERIOD_3_DAYS = (By.XPATH, "//div[text()='трое суток']")
    RENT_PERIOD_4_DAYS = (By.XPATH, "//div[text()='четверо суток']")
    RENT_PERIOD_5_DAYS = (By.XPATH, "//div[text()='пятеро суток']")
    RENT_PERIOD_6_DAYS = (By.XPATH, "//div[text()='шестеро суток']")
    RENT_PERIOD_7_DAYS = (By.XPATH, "//div[text()='семеро суток']")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH,
                    "//button[contains(text(), 'Заказать') and @class='Button_Button__ra12g Button_Middle__1CSJM']")

    # Цвет самоката
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")

    # Модальное окно подтверждения
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Order_Modal__')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Сообщение об успешном заказе
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")