import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание элемента {locator}')
    def wait_for_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Ожидание что URL содержит {url_part}')
    def wait_for_url_contains(self, url_part, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_part)
        )

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Клик по элементу {locator}')
    def click_element(self, locator):
        element = self.wait_for_element(locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Скролл к элементу {locator}')
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Ввод значения "{value}" в поле {locator}')
    def set_value(self, locator, value):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(value)

    @allure.step('Получение текста элемента {locator}')
    def get_element_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step('Проверка наличия элемента {locator}')
    def is_element_present(self, locator, timeout=10):
        try:
            self.wait_for_element(locator, timeout)
            return True
        except TimeoutException:
            return False

    @allure.step('Ожидание нового окна')
    def wait_for_new_window(self, original_handle, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.window_handles) > len([original_handle])
        )

    @allure.step('Переключение на окно с handle {handle}')
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    @allure.step('Закрытие текущего окна')
    def close_current_window(self):
        self.driver.close()

    @allure.step('Получение всех handles окон')
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step('Получение текущего handle окна')
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step('Ожидание количества окон: {expected_number}')
    def wait_for_number_of_windows(self, expected_number, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.window_handles) == expected_number
        )
