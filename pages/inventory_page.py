from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITLE_HEADER = (By.XPATH, "//span[@class='title']") # Ditambahkan kembali
    ADD_TO_CART_BTN = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    CART_ICON = (By.XPATH, "//a[@class='shopping_cart_link']")
    
    def get_title(self):
        return self.get_text(self.TITLE_HEADER) # Ditambahkan kembali

    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def go_to_cart(self):
        self.click(self.CART_ICON)