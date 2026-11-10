from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_positive(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    # Assertion: Memastikan berhasil masuk dan ada di halaman produk
    assert inventory_page.get_title() == "Products"

def test_login_negative_empty_password(driver):
    login_page = LoginPage(driver)
    
    login_page.open()
    # Mengosongkan field password untuk memicu error
    login_page.login("standard_user", "")
    
    # Assertion: Memastikan error message yang muncul sesuai
    assert login_page.get_error_message() == "Epic sadface: Password is required"