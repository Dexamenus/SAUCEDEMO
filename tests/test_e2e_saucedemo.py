from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

def test_end_to_end_checkout(driver):
    # 1. Inisialisasi semua halaman
    login_page = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout_info = CheckoutInfoPage(driver)
    checkout_overview = CheckoutOverviewPage(driver)
    checkout_complete = CheckoutCompletePage(driver)

    # 2. Proses Login
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # 3. Pilih Produk & Masuk Keranjang
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    # 4. Proses Keranjang & Pengisian Data
    cart.proceed_to_checkout()
    checkout_info.fill_information("Muhammad", "Abdan", "52111")

    # 5. Konfirmasi Pembayaran
    checkout_overview.finish_checkout()

    # 6. Assertion: Memastikan pesanan berhasil
    success_message = checkout_complete.get_success_message()
    assert success_message == "Thank you for your order!", f"Pesan salah: {success_message}"
    