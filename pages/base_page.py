"""
BasePage: clase padre con métodos reutilizables para todas las páginas.
Implementa el patrón Page Object Model (POM), estándar en automatización.
"""
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def click(self, selector: str):
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        return self.page.inner_text(selector)

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)

    def wait_for_selector(self, selector: str, timeout: int = 5000):
        self.page.wait_for_selector(selector, timeout=timeout)
