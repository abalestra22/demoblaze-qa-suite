from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.cart_page_locators import CartPageLocators

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_cart(self):
        """Navigates to the cart page by clicking on the cart link."""
        cart_link = self.wait.until(EC.element_to_be_clickable(CartPageLocators.CART_LINK))
        cart_link.click()

    def place_order(self):
        """Opens the 'Place Order' modal from the cart page."""
        place_order_btn = self.wait.until(EC.element_to_be_clickable(CartPageLocators.PLACE_ORDER_BUTTON))
        place_order_btn.click()

    def fill_order_form(self, name, country, city, card, month, year):
        """Fills in the order form with user details in the modal."""
        self.wait.until(EC.visibility_of_element_located(CartPageLocators.ORDER_MODAL))
        self.wait.until(EC.element_to_be_clickable(CartPageLocators.NAME_FIELD)).send_keys(name)
        self.driver.find_element(*CartPageLocators.COUNTRY_FIELD).send_keys(country)
        self.driver.find_element(*CartPageLocators.CITY_FIELD).send_keys(city)
        self.driver.find_element(*CartPageLocators.CARD_FIELD).send_keys(card)
        self.driver.find_element(*CartPageLocators.MONTH_FIELD).send_keys(month)
        self.driver.find_element(*CartPageLocators.YEAR_FIELD).send_keys(year)

    def confirm_purchase(self):
        """Clicks the 'Purchase' button to complete the transaction."""
        purchase_btn = self.wait.until(EC.element_to_be_clickable(CartPageLocators.PURCHASE_BUTTON))
        purchase_btn.click()

    def get_confirmation_text(self):
        """Returns the confirmation text shown after a successful purchase."""
        confirmation = self.wait.until(EC.visibility_of_element_located(CartPageLocators.CONFIRMATION_TITLE))
        return confirmation.text

    def cancel_purchase(self):
        """Closes the order modal without confirming the purchase."""
        self.wait.until(EC.visibility_of_element_located(CartPageLocators.ORDER_MODAL))
        cancel_btn = self.wait.until(EC.element_to_be_clickable(CartPageLocators.CLOSE_BUTTON))
        cancel_btn.click()

    def get_cart_product_names(self):
        """Returns a list of product names currently in the cart."""
        self.wait.until(lambda driver: len(driver.find_elements(*CartPageLocators.CART_PRODUCT_ROWS)) > 0)
        rows = self.driver.find_elements(*CartPageLocators.CART_PRODUCT_ROWS)
        return [row.text.strip() for row in rows]