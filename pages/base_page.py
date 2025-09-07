import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание элемента {locator}')
    def wait_for_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )


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
        except:
            return False

    @allure.step('Ожидание нового окна')
    def wait_for_new_window(self, original_handle, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.window_handles) > len([original_handle])
        )

