from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")
    ITEM_NAME = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    ITEM_QUANTITY = (By.CSS_SELECTOR, ".cart_item .cart_quantity")

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def get_item_name(self):
        return self.get_text(self.ITEM_NAME)

    def get_item_quantity(self):
        return self.get_text(self.ITEM_QUANTITY)
