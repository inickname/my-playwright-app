from src.pages.base_page import BasePage


class LogoutPage(BasePage):
    BURGER_BUTTON_SELECTOR = '[id="react-burger-menu-btn"]'
    LOGOUT_SELECTOR = '[id="logout_sidebar_link"]'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ''

    def logout(self):
        self.wait_for_selector_and_click(self.BURGER_BUTTON_SELECTOR)
        self.assert_element_is_visible(self.LOGOUT_SELECTOR)

        self.wait_for_selector_and_click(self.LOGOUT_SELECTOR)
        self.assert_text_present_on_page('Swag Labs')
