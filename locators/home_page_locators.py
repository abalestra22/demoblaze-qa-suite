from selenium.webdriver.common.by import By

class HomePageLocators:
    PRODUCT_TITLES = (By.CSS_SELECTOR, ".card-title a")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".card-block .card-text")
    NEXT_BUTTON = (By.LINK_TEXT, "Next")
