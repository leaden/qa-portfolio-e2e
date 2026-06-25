"""
LoginPage: encapsula todos los elementos y acciones de la página de login.
"""
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com"

    # Locators
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def open(self):
        self.goto(self.URL)

    def login(self, username: str, password: str):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def has_error(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)
