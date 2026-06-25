"""
CartPage: encapsula la página del carrito de compras.
"""
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = ".cart_item"
    CHECKOUT_BUTTON = "#checkout"
    ITEM_NAME = ".inventory_item_name"
    REMOVE_BUTTON = "button.cart_button"

    def get_items_count(self) -> int:
        return self.page.locator(self.CART_ITEMS).count()

    def get_item_names(self) -> list[str]:
        return self.page.locator(self.ITEM_NAME).all_inner_texts()

    def remove_first_item(self):
        self.page.locator(self.REMOVE_BUTTON).first.click()

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
