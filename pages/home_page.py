from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    # Локаторы для главной страницы
    HEADER_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Заказать') and @class='Button_Button__ra12g']")
    MAIN_ORDER_BUTTON = (By.XPATH, "(//button[contains(text(), 'Заказать') and @class='Button_Button__ra12g'])[2]")
    COOKIE_BANNER = (By.XPATH, "//div[contains(@class, 'App_CookieConsent')]//button")

    def accept_cookies(self):
        try:
            self.click_element(self.COOKIE_BANNER)
        except:
            print("Баннер куки не найден или уже закрыт")

    def click_header_order_button(self):
        self.click_element(self.HEADER_ORDER_BUTTON)

    def click_main_order_button(self):
        self.scroll_to_element(self.MAIN_ORDER_BUTTON)
        self.click_element(self.MAIN_ORDER_BUTTON)