"""
conftest.py: fixtures compartidos por todos los tests.
pytest los detecta automáticamente sin necesidad de importarlos.
"""
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

# Usuarios de prueba de SauceDemo
VALID_USER = "standard_user"
LOCKED_USER = "locked_out_user"
VALID_PASSWORD = "secret_sauce"


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def logged_in_page(login_page, inventory_page):
    """Fixture que entrega la página ya autenticada, lista para usar en tests
    que no necesitan probar el login en sí."""
    login_page.open()
    login_page.login(VALID_USER, VALID_PASSWORD)
    inventory_page.wait_for_selector(".inventory_list")
    return inventory_page
