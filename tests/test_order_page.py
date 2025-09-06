import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Users
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Заказ через верхнюю кнопку "Заказать"')
    @allure.description('Позитивный тест заказа через кнопку в хедере')
    @pytest.mark.parametrize('user_data', [
        Users.user,
        Users.user_2
    ], ids=["Набор 1", "Набор 2"])
    def test_order_via_header_button(self, driver, user_data):
        with allure.step('Инициализация страниц'):
            main_page = MainPage(driver)
            order_page = OrderPage(driver)
            wait = WebDriverWait(driver, 10)

        with allure.step('Принимаем куки'):
            main_page.accept_cookies()

        with allure.step('Кликаем на верхнюю кнопку "Заказать"'):
            main_page.click_order_button_header()

        with allure.step('Ждем загрузки страницы заказа'):
            wait.until(EC.url_contains("/order"))
            print(f"Перешли на URL: {driver.current_url}")

        with allure.step('Заполняем первую страницу заказа'):
            order_page.fill_first_page(user_data)

        with allure.step('Заполняем вторую страницу заказа'):
            order_page.fill_second_page(user_data)

        with allure.step('Подтверждаем заказ'):
            order_page.confirm_order()

        with allure.step('Проверяем успешное оформление заказа'):
            success = order_page.check_success_message()
            assert success, "Окно подтверждения заказа не отобразилось"

    @allure.title('Заказ через нижнюю кнопку "Заказать"')
    @allure.description('Позитивный тест заказа через кнопку в футере')
    @pytest.mark.parametrize('user_data', [
        Users.user,
        Users.user_2
    ], ids=["Набор 1", "Набор 2"])
    def test_order_via_footer_button(self, driver, user_data):
        with allure.step('Инициализация страниц'):
            main_page = MainPage(driver)
            order_page = OrderPage(driver)
            wait = WebDriverWait(driver, 10)

        with allure.step('Принимаем куки'):
            main_page.accept_cookies()

        with allure.step('Кликаем на нижнюю кнопку "Заказать"'):
            main_page.click_order_button_footer()

        with allure.step('Ждем загрузки страницы заказа'):
            wait.until(EC.url_contains("/order"))
            print(f"Перешли на URL: {driver.current_url}")

        with allure.step('Заполняем первую страницу заказа'):
            order_page.fill_first_page(user_data)

        with allure.step('Заполняем вторую страницу заказа'):
            order_page.fill_second_page(user_data)

        with allure.step('Подтверждаем заказ'):
            order_page.confirm_order()

        with allure.step('Проверяем успешное оформление заказа'):
            success = order_page.check_success_message()
            assert success, "Окно подтверждения заказа не отобразилось"