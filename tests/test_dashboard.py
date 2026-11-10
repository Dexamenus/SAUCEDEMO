from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.data_reader import read_json


def test_add_to_cart_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    user = read_json("users.json")["valid_user"]
    login_page.open()
    login_page.login(user["username"], user["password"])
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    assert cart_page.get_item_name() == "Sauce Labs Backpack"
    assert cart_page.get_item_quantity() == "1"


def test_logout_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    user = read_json("users.json")["valid_user"]
    login_page.open()
    login_page.login(user["username"], user["password"])
    inventory_page.logout()

    assert login_page.is_login_form_displayed()
