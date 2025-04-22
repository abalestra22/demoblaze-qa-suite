from selenium.webdriver.common.by import By

class CartPageLocators:
    CART_LINK = (By.ID, "cartur")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Place Order']")
    PURCHASE_BUTTON = (By.XPATH, "//button[text()='Purchase']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "#orderModal .modal-footer button.btn.btn-secondary")
    ORDER_MODAL = (By.ID, "orderModal")
    CONFIRMATION_TITLE = (By.CSS_SELECTOR, ".sweet-alert > h2")
    CART_PRODUCT_ROWS = (By.CSS_SELECTOR, "#tbodyid tr td:nth-child(2)")

    NAME_FIELD = (By.ID, "name")
    COUNTRY_FIELD = (By.ID, "country")
    CITY_FIELD = (By.ID, "city")
    CARD_FIELD = (By.ID, "card")
    MONTH_FIELD = (By.ID, "month")
    YEAR_FIELD = (By.ID, "year")
