import allure
from playwright.sync_api import expect

from src.enums.urls import Url


class BasePage:
    __BASE_URL = Url.BASE_URL.value

    def __init__(self, page):
        self.page = page
        self._endpoint = ''

    @allure.step("Получение полного URL")
    def _get_full_url(self):
        """Защищенный метод для получения полного URL."""
        return f"{self.__BASE_URL}/{self._endpoint}"

    @allure.step("Открытие указанного URL")
    def navigate_to(self):
        full_url = self._get_full_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(full_url)

    @allure.step("Клик по элементу")
    def wait_for_selector_and_click(self, selector):
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    @allure.step("Заполнение текстового поля")
    def wait_for_selector_and_fill(self, selector, value):
        self.page.wait_for_selector(selector)
        self.page.fill(selector, value)

    @allure.step("Посимвольное заполнение текстового поля")
    def wait_for_selector_and_type(self, selector, value, delay):
        self.page.wait_for_selector(selector)
        self.page.type(selector, value, delay=delay)

    @allure.step("Проверка видимости элемента")
    def assert_element_is_visible(self, selector):
        expect(self.page.locator(selector)).to_be_visible()

    @allure.step("Проверка наличия подстроки в тексте элемента")
    def assert_text_present_on_page(self, text):
        expect(self.page.locator("body")).to_contain_text(text)

    @allure.step("Проверка наличия текста внутри элемента")
    def assert_text_in_element(self, selector, text):
        expect(self.page.locator(selector)).to_have_text(text)

    @allure.step("Проверка значения атрибута элемента")
    def assert_input_value(self, selector, expected_value):
        expect(self.page.locator(selector)).to_have_value(expected_value)
