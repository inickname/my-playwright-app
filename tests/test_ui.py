import allure
from faker import Faker

from src.enums.data import AuthData
from src.pages.checkout_page import CheckoutPage
from src.pages.inventory_page import InventoryPage
from src.pages.login_page import LoginPage
from src.pages.logout_page import LogoutPage

faker = Faker()


class TestOrders:
    USERNAME = AuthData.username.value
    PASSWORD = AuthData.password.value

    @allure.title("Оформление заказа")
    def test_checkout_order(self, browser):
        """
        Сценарий: авторизоваться, оформить заказ и выйти из личного кабинета.
        """
        page = browser.new_page()
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)
        checkout_page = CheckoutPage(page)
        logout_page = LogoutPage(page)

        login_page.login(self.USERNAME, self.PASSWORD)
        inventory_page.add_first_item_to_cart()
        checkout_page.start_checkout()
        checkout_page.fill_checkout_form(faker.first_name(), faker.last_name(), faker.postcode())
        checkout_page.finish_checkout()
        logout_page.logout()
