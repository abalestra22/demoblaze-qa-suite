from selenium.webdriver.common.by import By

class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.LINK_TEXT, "Add to cart")
    PRODUCT_TITLE = (By.TAG_NAME, "h2")