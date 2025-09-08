import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Заполнить первую страницу заказа: {user}')
    def fill_first_page(self, user):
        # Заполняем основные поля
        self.set_value(OrderPageLocators.NAME_FIELD, user['name'])
        self.set_value(OrderPageLocators.SURNAME_FIELD, user['surname'])
        self.set_value(OrderPageLocators.ADDRESS_FIELD, user['address'])

        # Выбор станции метро
        self.click_element(OrderPageLocators.METRO_STATION_FIELD)
        station_locator = (By.XPATH, f"//div[text()='{user['metro_station']}']")
        self.click_element(station_locator)

        self.set_value(OrderPageLocators.PHONE_FIELD, user['phone'])
        self.click_element(OrderPageLocators.NEXT_BUTTON)

        # Ждем загрузки второй страницы
        self.wait_for_element(OrderPageLocators.DATE_FIELD, timeout=10)

    @allure.step('Заполнить вторую страницу заказа: {user}')
    def fill_second_page(self, user):
        # Установка даты
        date_field = self.wait_for_element(OrderPageLocators.DATE_FIELD)
        date_field.send_keys(Keys.CONTROL + "a")
        date_field.send_keys(Keys.DELETE)
        date_field.send_keys(user['date'])
        date_field.send_keys(Keys.ENTER)

        # Выбор срока аренды
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)

        period_mapping = {
            'сутки': OrderPageLocators.RENT_PERIOD_1_DAY,
            'двое суток': OrderPageLocators.RENT_PERIOD_2_DAYS,
            'трое суток': OrderPageLocators.RENT_PERIOD_3_DAYS,
            'четверо суток': OrderPageLocators.RENT_PERIOD_4_DAYS,
            'пятеро суток': OrderPageLocators.RENT_PERIOD_5_DAYS,
            'шестеро суток': OrderPageLocators.RENT_PERIOD_6_DAYS,
            'семеро суток': OrderPageLocators.RENT_PERIOD_7_DAYS
        }

        self.click_element(period_mapping[user['period']])

        #Выбор цвета
        color = user.get('color')
        if color == 'black':
            self.click_element(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        elif color == 'grey':
            self.click_element(OrderPageLocators.GREY_COLOR_CHECKBOX)

        # Ввод комментария
        if user.get('comment'):
            self.set_value(OrderPageLocators.COMMENT_FIELD, user['comment'])

        # Нажимаем кнопку Заказать
        self.click_element(OrderPageLocators.ORDER_BUTTON)

        # Ждем появления модального окна подтверждения
        self.wait_for_element(OrderPageLocators.MODAL_WINDOW, timeout=10)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        # Ждем и кликаем кнопку подтверждения (убрали неиспользуемую переменную)
        self.wait_for_element(OrderPageLocators.CONFIRM_BUTTON, timeout=10)
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Проверить сообщение об успешном заказе')
    def check_success_message(self):
        return self.is_element_present(OrderPageLocators.SUCCESS_MESSAGE, timeout=10)