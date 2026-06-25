"""
InventoryPage: encapsula la página de listado de productos.
"""
from pages.base_page import BasePage


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    # Locators
    PAGE_TITLE = ".title"
    INVENTORY_ITEMS = ".inventory_item"
    ADD_TO_CART_BUTTON = "button.btn_inventory"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    SORT_DROPDOWN = ".product_sort_container"
    ITEM_PRICE = ".inventory_item_price"

    def is_loaded(self) -> bool:
        return self.is_visible(self.PAGE_TITLE)

    def get_items_count(self) -> int:
        return self.page.locator(self.INVENTORY_ITEMS).count()

    def add_first_item_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BUTTON).first.click()

    def add_item_by_name(self, item_name: str):
        item = self.page.locator(".inventory_item").filter(has_text=item_name)
        item.locator("button").click()

    def get_cart_count(self) -> str:
        return self.get_text(self.CART_BADGE)

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def sort_by(self, option_value: str):
        """option_value: 'az', 'za', 'lohi', 'hilo'"""
        self.page.select_option(self.SORT_DROPDOWN, option_value)

    def get_all_prices(self) -> list[float]:
        prices_text = self.page.locator(self.ITEM_PRICE).all_inner_texts()
        return [float(p.replace("$", "")) for p in prices_text]
