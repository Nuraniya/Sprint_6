from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def click_question(self, index):
        locator = (By.XPATH, MainPageLocators.QUESTION_LOCATOR_TEMPLATE.format(index))
        self.scroll_to_element(locator)
        self.click_element(locator)

    def get_answer_text(self, index):
        locator = (By.XPATH, MainPageLocators.ANSWER_LOCATOR_TEMPLATE.format(index))
        return self.get_element_text(locator)

    def accept_cookies(self):
        self.click_element(MainPageLocators.COOKIE_BUTTON)

    def click_order_button_header(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_HEADER)

    def click_order_button_footer(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_FOOTER)
        self.click_element(MainPageLocators.ORDER_BUTTON_FOOTER)

    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)