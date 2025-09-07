import allure
import pytest
from data import Users
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import Urls

class TestOrderPage:

    @allure.title('Заказ через кнопку "Заказать" - {button_type}')
    @allure.description('Позитивный тест заказа через разные кнопки')
    @pytest.mark.parametrize('user_data', [
        Users.user,
        Users.user_2
    ], ids=["Набор 1", "Набор 2"])
    @pytest.mark.parametrize('button_type, button_func', [
        ('верхняя', 'header'),
        ('нижняя', 'footer')
    ], ids=["Верхняя кнопка", "Нижняя кнопка"])
    def test_order_via_different_buttons(self, driver, user_data, button_type, button_func):
        with allure.step('Инициализация страниц'):
            main_page = MainPage(driver)
            order_page = OrderPage(driver)
            urls = Urls()

        with allure.step('Принимаем куки'):
            main_page.accept_cookies()

        with allure.step(f'Кликаем на {button_type} кнопку "Заказать"'):
            if button_func == 'header':
                main_page.click_order_button_header()
            else:
                main_page.click_order_button_footer()

        with allure.step('Проверяем переход на страницу заказа'):
            assert urls.ORDER_PAGE in driver.current_url

        with allure.step('Заполняем первую страницу заказа'):
            order_page.fill_first_page(user_data)

        with allure.step('Заполняем вторую страницу заказа'):
            order_page.fill_second_page(user_data)

        with allure.step('Подтверждаем заказ'):
            order_page.confirm_order()

        with allure.step('Проверяем успешное оформление заказа'):
            success = order_page.check_success_message()
            assert success, "Окно подтверждения заказа не отобразилось"