from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def click_question(self, index):
        locator = (By.XPATH, MainPageLocators.QUESTION_LOCATOR_TEMPLATE.format(index))
        self.scroll_to_element(locator)
        self.click_element(locator)

    def get_answer_text(self, index):
        locator = (By.XPATH, MainPageLocators.ANSWER_LOCATOR_TEMPLATE.format(index))
        return self.wait_for_element(locator).text

    def accept_cookies(self):
        self.click_element(MainPageLocators.COOKIE_BUTTON)

    def click_order_button_header(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_HEADER)

    def click_order_button_footer(self):
        footer_button = self.wait.until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON_FOOTER)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer_button)
        self.driver.execute_script("arguments[0].click();", footer_button)

    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    def click_order_button_header(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_HEADER)

    def click_order_button_footer(self):
        footer_button = self.wait.until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON_FOOTER)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer_button)
        self.driver.execute_script("arguments[0].click();", footer_button)

    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    def scroll_and_click_on_the_order_button(self):
        self.click_order_button_footer()