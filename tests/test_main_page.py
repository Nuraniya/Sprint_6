import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from data import faq_data
from urls import Urls

@pytest.mark.usefixtures('driver')
@allure.feature('Главная страница')
class TestMainPage:

    @allure.title('Проверка ответов в разделе "Вопросы о важном"')
    @pytest.mark.parametrize('index, expected_answer', [(i, data[1]) for i, data in enumerate(faq_data)])
    def test_faq_section(self, driver, index, expected_answer):
        main_page = MainPage(driver)
        main_page.accept_cookies()

        with allure.step(f'Кликаем на вопрос с индексом {index}'):
            main_page.click_question(index)

        with allure.step('Проверяем текст ответа'):
            actual_answer = main_page.get_answer_text(index)
            actual_clean = ' '.join(actual_answer.split())
            expected_clean = ' '.join(expected_answer.split())
            assert actual_clean == expected_clean, f"Ожидался ответ: '{expected_clean}', получен: '{actual_clean}'"

    @allure.title('Проверка перехода на главную страницу по логотипу Самоката')
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_scooter_logo()
        urls = Urls()
        assert driver.current_url == urls.MAIN_PAGE

    @allure.title('Проверка перехода на Дзен по логотипу Яндекса')
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        original_window = driver.current_window_handle

        with allure.step('Кликаем на логотип Яндекса'):
            main_page.click_yandex_logo()

        with allure.step('Ждем открытия новой вкладки и переключаемся на нее'):
            main_page.wait_for_new_window(original_window, timeout=10)
            new_window = [window for window in driver.window_handles if window != original_window][0]
            driver.switch_to.window(new_window)

        with allure.step('Ждем загрузки страницы Dzen'):
            # Ждем, пока URL сменится с about:blank на нужный
            urls = Urls()
            WebDriverWait(driver, 15).until(
                EC.url_contains('dzen.ru')
            )

        with allure.step('Проверяем переход на Dzen'):
            current_url = driver.current_url
            assert 'dzen.ru' in current_url, f"Ожидался переход на Dzen, но текущий URL: {current_url}"

        with allure.step('Закрываем вкладку Дзена и возвращаемся обратно'):
            driver.close()
            driver.switch_to.window(original_window)