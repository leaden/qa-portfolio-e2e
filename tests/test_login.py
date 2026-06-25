"""
Suite de pruebas para el flujo de Login.
Cubre casos positivos, negativos y de validación.
"""
import pytest
from conftest import VALID_USER, VALID_PASSWORD, LOCKED_USER


@pytest.mark.smoke
def test_login_exitoso(login_page, inventory_page):
    """El usuario válido debe poder ingresar y ver la lista de productos."""
    login_page.open()
    login_page.login(VALID_USER, VALID_PASSWORD)

    assert inventory_page.is_loaded(), "No se cargó la página de inventario tras el login"


def test_login_usuario_bloqueado(login_page):
    """Un usuario bloqueado debe recibir un mensaje de error claro."""
    login_page.open()
    login_page.login(LOCKED_USER, VALID_PASSWORD)

    assert login_page.has_error()
    assert "locked out" in login_page.get_error_message().lower()


def test_login_password_incorrecta(login_page):
    """Una contraseña incorrecta debe bloquear el acceso."""
    login_page.open()
    login_page.login(VALID_USER, "password_incorrecta")

    assert login_page.has_error()
    assert "do not match" in login_page.get_error_message().lower()


def test_login_campos_vacios(login_page):
    """No se debe permitir login sin usuario."""
    login_page.open()
    login_page.login("", "")

    assert login_page.has_error()
    assert "username is required" in login_page.get_error_message().lower()


@pytest.mark.parametrize("username,password,expected_error", [
    ("standard_user", "", "Password is required"),
    ("", "secret_sauce", "Username is required"),
    ("usuario_invalido", "clave_invalida", "do not match"),
])
def test_login_combinaciones_invalidas(login_page, username, password, expected_error):
    """Prueba parametrizada: distintas combinaciones inválidas de credenciales."""
    login_page.open()
    login_page.login(username, password)

    assert login_page.has_error()
    assert expected_error.lower() in login_page.get_error_message().lower()
