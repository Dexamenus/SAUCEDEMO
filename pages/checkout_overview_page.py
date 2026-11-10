from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    FINISH_BTN = (By.ID, "finish")

    def finish_checkout(self):
        self.click(self.FINISH_BTN)
