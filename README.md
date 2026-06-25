# 🧪 E2E Test Automation Suite — SauceDemo

![Tests](https://github.com/TU_USUARIO/qa-portfolio-e2e/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Playwright](https://img.shields.io/badge/Playwright-1.47-green)

Suite de pruebas automatizadas End-to-End para [SauceDemo](https://www.saucedemo.com), construida con **Playwright + Python**, siguiendo el patrón **Page Object Model (POM)** e integrada con **CI/CD (GitHub Actions)**.

Este proyecto forma parte de mi portafolio de QA Automation y demuestra buenas prácticas de diseño de pruebas mantenibles y escalables.

## 🎯 Qué cubre esta suite

- ✅ **Login**: casos positivos, negativos, usuario bloqueado, campos vacíos y combinaciones inválidas (parametrizadas).
- ✅ **Carrito de compras**: agregar/eliminar productos, contador del carrito, ordenamiento por precio.
- ✅ **CI/CD**: los tests corren automáticamente en cada push/PR y también una vez al día (cron), generando un reporte HTML descargable como artefacto.

## 🛠️ Stack técnico

| Herramienta | Uso |
|---|---|
| Playwright | Automatización del navegador |
| Pytest | Framework de testing y fixtures |
| pytest-html | Reportes HTML de ejecución |
| GitHub Actions | Integración continua (CI) |

## 📂 Estructura del proyecto

```
qa-portfolio-e2e/
├── pages/              # Page Object Model
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/              # Casos de prueba
│   ├── test_login.py
│   └── test_cart.py
├── conftest.py         # Fixtures compartidos
├── pytest.ini          # Configuración de pytest
├── requirements.txt
└── .github/workflows/  # Pipeline de CI
    └── tests.yml
```

## 🚀 Cómo correrlo localmente

```bash
# 1. Clonar el repositorio
git clone https://github.com/leaden/qa-portfolio-e2e.git
cd qa-portfolio-e2e

# 2. Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt
playwright install

# 4. Ejecutar todos los tests
pytest

# 5. Ejecutar solo los smoke tests
pytest -m smoke

# 6. Ver el reporte generado
open reports/report.html
```

## 📊 Resultados

Cada ejecución genera un reporte HTML con el detalle de cada caso, su estado (pass/fail) y duración. El reporte de la última ejecución en CI está disponible como artefacto descargable en la pestaña **Actions** del repositorio.

## 🧠 Decisiones de diseño

- **Page Object Model**: separa la lógica de interacción con la UI de la lógica de las aserciones, facilitando el mantenimiento si cambia el HTML del sitio.
- **Fixtures de pytest**: evitan duplicar código de login en cada test (`logged_in_page`).
- **Tests parametrizados**: permiten cubrir múltiples combinaciones de datos con un solo bloque de código.
- **Markers (`@pytest.mark.smoke`)**: permiten correr un subconjunto crítico de pruebas rápidamente, simulando un pipeline real donde el smoke test corre antes que la suite completa.

## 📌 Próximas mejoras

- [ ] Agregar pruebas de checkout completo
- [ ] Integrar reportes Allure
- [ ] Agregar pruebas de accesibilidad (axe-core)
- [ ] Ejecución en paralelo con pytest-xdist

---

**Autor:** Tu Nombre · [LinkedIn](https://linkedin.com/in/tu-perfil) · [Portafolio](https://github.com/leaden)
