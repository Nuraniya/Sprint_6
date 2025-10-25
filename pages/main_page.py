import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Кликнуть на вопрос с индексом {index}')
    def click_question(self, index):
        locator = (By.XPATH, MainPageLocators.QUESTION_LOCATOR_TEMPLATE.format(index))
        self.scroll_to_element(locator)
        self.click_element(locator)

    @allure.step('Получить текст ответа для вопроса с индексом {index}')
    def get_answer_text(self, index):
        locator = (By.XPATH, MainPageLocators.ANSWER_LOCATOR_TEMPLATE.format(index))
        return self.get_element_text(locator)

    @allure.step('Принять куки')
    def accept_cookies(self):
        self.click_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Кликнуть на кнопку "Заказать" типа {button_type}')
    def click_order_button(self, button_type):
        if button_type == 'header':
            self.click_element(MainPageLocators.ORDER_BUTTON_HEADER)
        elif button_type == 'footer':
            self.scroll_to_element(MainPageLocators.ORDER_BUTTON_FOOTER)
            self.click_element(MainPageLocators.ORDER_BUTTON_FOOTER)
        else:
            raise ValueError(f"Unknown button type: {button_type}")

    @allure.step('Кликнуть на кнопку "Заказать" в хедере')
    def click_order_button_header(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Кликнуть на кнопку "Заказать" в футере')
    def click_order_button_footer(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_FOOTER)
        self.click_element(MainPageLocators.ORDER_BUTTON_FOOTER)

    @allure.step('Кликнуть на логотип Самоката')
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Кликнуть на логотип Яндекса')
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Проверить что текущий URL содержит {url}')
    def check_url_contains(self, url):
        current_url = self.get_current_url()
        assert url in current_url, f"Ожидался URL содержащий '{url}', но получен: {current_url}"
        return True