import allure
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
@allure.title("Запуск и остановка Playwright")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    yield browser
    browser.close()
    playwright.stop()
