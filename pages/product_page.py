from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.product_page_locators import ProductPageLocators

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self):
        """Clicks the 'Add to cart' button on the product detail page."""
        add_button = self.wait.until(EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON))
        add_button.click()

    def get_product_title(self):
        """Returns the title of the product currently being viewed."""
        title = self.wait.until(EC.presence_of_element_located(ProductPageLocators.PRODUCT_TITLE))
        return title.text.strip()
