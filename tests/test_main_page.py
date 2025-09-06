import pytest
import allure
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from data import faq_data


@pytest.mark.usefixtures('driver')
@allure.feature('Главная страница')
class TestMainPage:

    @allure.title('Проверка ответов в разделе "Вопросы о важном"')
    @pytest.mark.parametrize('index, expected_answer', [(i, data[1]) for i, data in enumerate(faq_data)])
    def test_faq_section(self, driver, index, expected_answer):
        driver.find_element(By.ID, "rcc-confirm-button").click()
        main_page = MainPage(driver)

        with allure.step(f'Кликаем на вопрос с индексом {index}'):
            main_page.click_question(index)
            time.sleep(1)

        with allure.step('Проверяем текст ответа'):
            actual_answer = main_page.get_answer_text(index)
            actual_clean = ' '.join(actual_answer.split())
            expected_clean = ' '.join(expected_answer.split())
            assert actual_clean == expected_clean, f"Ожидался ответ: '{expected_clean}', получен: '{actual_clean}'"

    @allure.title('Проверка перехода на главную страницу по логотипу Самоката')
    def test_scooter_logo_redirect(self, driver):
        driver.find_element(By.ID, "rcc-confirm-button").click()
        main_page = MainPage(driver)
        main_page.click_scooter_logo()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка перехода на Дзен по логотипу Яндекса')
    def test_yandex_logo_redirect(self, driver):
        driver.find_element(By.ID, "rcc-confirm-button").click()
        main_page = MainPage(driver)
        original_window = driver.current_window_handle

        with allure.step('Кликаем на логотип Яндекса'):
            main_page.click_yandex_logo()

        with allure.step('Ждем открытия новой вкладки и переключаемся на нее'):
            WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
            new_window = [window for window in driver.window_handles if window != original_window][0]
            driver.switch_to.window(new_window)

        with allure.step('Ждем загрузки и проверяем URL'):
            WebDriverWait(driver, 10).until(EC.url_contains('dzen.ru'))
            assert 'dzen.ru' in driver.current_url.lower()

        with allure.step('Закрываем вкладку Дзена и возвращаемся обратно'):
            driver.close()
            driver.switch_to.window(original_window)