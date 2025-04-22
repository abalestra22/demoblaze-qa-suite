BASE_URL = "https://demoblaze.com"

import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def home(driver):
    return HomePage(driver)

@pytest.fixture
def product(driver):
    return ProductPage(driver)

@pytest.fixture
def cart(driver):
    return CartPage(driver)

@pytest.mark.mandatory
def test_scrape_products(driver, home):
    """Extracts product info from the first 2 pages and writes to products.txt."""
    driver.get(BASE_URL)
    all_products = []

    for _ in range(2):
        all_products.extend(home.get_products_info_from_current_page())
        home.go_to_next_page()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "footc"))
    )

    with open("products.txt", "w", encoding="utf-8", errors="replace") as f:
        for item in all_products:
            f.write(f"{item['name']} - ${item['price']} - {item['link']}\n")

@pytest.mark.mandatory
def test_purchase_flow_add_to_cart(driver, home, product, cart):
    """Completes an end-to-end purchase: select -> add to cart -> confirm order."""
    driver.get(BASE_URL)
    home.click_first_product()

    selected_name = product.get_product_title()
    product.add_to_cart()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert "Product added" in alert.text
    alert.accept()

    cart.go_to_cart()

    cart_product_names = cart.get_cart_product_names()
    assert selected_name in cart_product_names

    cart.place_order()
    cart.fill_order_form("Andrea", "Argentina", "Santa Fe", "1234567890123456", "04", "2025")
    cart.confirm_purchase()

    confirmation = cart.get_confirmation_text()
    assert "Thank you for your purchase!" in confirmation

@pytest.mark.optional
def test_cancel_order_modal(driver, home, product, cart):
    """Opens the order modal and closes it without confirming the purchase."""
    driver.get(BASE_URL)
    home.click_first_product()

    product.add_to_cart()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    cart.go_to_cart()
    cart.place_order()
    cart.cancel_purchase()

    WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.ID, "orderModal")))

@pytest.mark.optional
def test_multiple_products_cart_total(driver, home, product, cart):
    """Adds two products to the cart and validates both appear in the cart."""
    driver.get(BASE_URL)
    home.click_first_product()
    product_1 = product.get_product_title()
    product.add_to_cart()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

    driver.get(BASE_URL)
    home.click_first_product()
    product_2 = product.get_product_title()
    product.add_to_cart()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

    cart.go_to_cart()

    cart_product_names = cart.get_cart_product_names()

    assert product_1 in cart_product_names
    assert product_2 in cart_product_names
    assert len(cart_product_names) >= 2
