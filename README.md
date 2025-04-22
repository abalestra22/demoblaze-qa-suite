# Demoblaze QA Automation Suite

This project contains automated UI tests for the [Demoblaze](https://demoblaze.com) website using **Selenium**, structured with the **Page Object Model** and powered by **Pytest**.

These tests were designed to:
- Scrape product data for use in analysis or test databases.
- Automate a full purchase flow using the shopping cart.
- Validate cart contents with one or more products.
- Demonstrate good practices: waits, fixtures, modularity.

---

## Requirements

- Python 3.9+
- Google Chrome
- ChromeDriver (auto-managed via `webdriver-manager`)

Install dependencies:
```bash
pip install -r requirements.txt
```

> If no `requirements.txt` exists, install manually:
```bash
pip install selenium pytest webdriver-manager
```

---

## How to Run

From the root of the project:

Run all tests:
```bash
pytest -v
```

Run only required tests:
```bash
pytest -v -m mandatory
```

Run only optional/bonus tests:
```bash
pytest -v -m optional
```

---

## Project Structure

```bash
.
├── pages/
│   ├── home_page.py         # Home interactions
│   ├── product_page.py      # Product detail page
│   └── cart_page.py         # Cart and checkout
│
├── tests/
│   └── test_scraper.py      # All test cases (scraping + purchase + optional)
│
├── products.txt             # Output from the scraping test
```

---

## Tests Implemented

### Mandatory:
- `test_scrape_products`: saves info from the first 2 pages to `products.txt`
- `test_purchase_flow_add_to_cart`: completes a full product purchase

### Optional:
- `test_multiple_products_cart_total`: adds 2 products to the cart and validates them

---

## ⚠ Notes & Tips

- The `--headless` mode can be disabled in `driver()` fixture to watch the tests in Chrome.
- The site is a demo and may return inconsistent results occasionally. All critical interactions use `WebDriverWait`.

---

## Author
**Andrea Balestra**

[GitHub: abalestra22](https://github.com/abalestra22)

---
