"""
Suite de pruebas para el flujo de carrito de compras.
Usa la fixture 'logged_in_page' para evitar repetir el login en cada test.
"""
import pytest


@pytest.mark.smoke
def test_agregar_producto_al_carrito(logged_in_page, cart_page):
    """Al agregar un producto, el contador del carrito debe actualizarse a 1."""
    logged_in_page.add_first_item_to_cart()

    assert logged_in_page.get_cart_count() == "1"


def test_agregar_multiples_productos(logged_in_page, cart_page):
    """El contador del carrito debe reflejar correctamente múltiples productos."""
    logged_in_page.add_item_by_name("Sauce Labs Backpack")
    logged_in_page.add_item_by_name("Sauce Labs Bike Light")

    assert logged_in_page.get_cart_count() == "2"


def test_carrito_muestra_productos_agregados(logged_in_page, cart_page):
    """Los productos agregados deben aparecer correctamente en la página del carrito."""
    logged_in_page.add_item_by_name("Sauce Labs Backpack")
    logged_in_page.go_to_cart()

    assert cart_page.get_items_count() == 1
    assert "Sauce Labs Backpack" in cart_page.get_item_names()


def test_eliminar_producto_del_carrito(logged_in_page, cart_page):
    """Un producto eliminado del carrito ya no debe aparecer en el listado."""
    logged_in_page.add_first_item_to_cart()
    logged_in_page.go_to_cart()
    cart_page.remove_first_item()

    assert cart_page.get_items_count() == 0


@pytest.mark.parametrize("sort_option,is_ascending", [
    ("lohi", True),
    ("hilo", False),
])
def test_ordenar_productos_por_precio(logged_in_page, sort_option, is_ascending):
    """Los productos deben poder ordenarse por precio ascendente y descendente."""
    logged_in_page.sort_by(sort_option)
    prices = logged_in_page.get_all_prices()

    expected = sorted(prices, reverse=not is_ascending)
    assert prices == expected, f"El orden de precios no es correcto: {prices}"
