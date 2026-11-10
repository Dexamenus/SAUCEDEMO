from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BTN = (By.XPATH, "//button[@id='checkout']")
    
    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BTN)

class CheckoutInfoPage(BasePage):
    FIRST_NAME = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME = (By.XPATH, "//input[@id='last-name']")
    POSTAL_CODE = (By.XPATH, "//input[@id='postal-code']")
    CONTINUE_BTN = (By.XPATH, "//input[@id='continue']")

    def fill_information(self, first, last, zip_code):
        self.enter_text(self.FIRST_NAME, first)
        self.enter_text(self.LAST_NAME, last)
        self.enter_text(self.POSTAL_CODE, zip_code)
        self.click(self.CONTINUE_BTN)

class CheckoutOverviewPage(BasePage):
    FINISH_BTN = (By.XPATH, "//button[@id='finish']")
    
    def finish_checkout(self):
        self.click(self.FINISH_BTN)

class CheckoutCompletePage(BasePage):
    COMPLETE_HEADER = (By.XPATH, "//h2[@class='complete-header']")
    
    def get_success_message(self):
        return self.get_text(self.COMPLETE_HEADER)