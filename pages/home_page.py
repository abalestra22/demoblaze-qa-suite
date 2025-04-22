from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.home_page_locators import HomePageLocators

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_products_info_from_current_page(self):
        """Extracts name, price, and URL of all products listed on the current page."""
        titles = self.wait.until(EC.presence_of_all_elements_located(HomePageLocators.PRODUCT_TITLES))
        prices = self.driver.find_elements(*HomePageLocators.PRODUCT_PRICES)
        links = self.driver.find_elements(*HomePageLocators.PRODUCT_TITLES)

        product_info = []
        for i in range(len(titles)):
            product_info.append({
                "name": titles[i].text,
                "price": prices[i].text.replace("$", ""),
                "link": links[i].get_attribute("href")
            })
        return product_info

    def go_to_next_page(self):
        """Clicks the 'Next' button to navigate to the next page of products."""
        next_button = self.wait.until(EC.element_to_be_clickable(HomePageLocators.NEXT_BUTTON))
        next_button.click()

    def click_first_product(self):
        """Clicks the first visible product on the current page."""
        first_product = self.wait.until(EC.element_to_be_clickable(HomePageLocators.PRODUCT_TITLES))
        self.wait.until(lambda driver: first_product.text.strip() != "")
        product_name = first_product.text.strip()
        first_product.click()
        return product_name