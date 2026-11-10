# Referensi Relative XPath

Seluruh ekspresi di bawah menggunakan awalan `.//` agar pencarian dimulai
relatif terhadap konteks elemen Selenium, tanpa bergantung pada posisi elemen
dalam hierarki HTML. Locator runtime di page object tetap menggunakan ID atau
CSS selector; tabel ini mendokumentasikan XPath ekuivalennya.

| Halaman | Elemen / locator POM | Relative XPath | Penjelasan |
|---|---|---|---|
| Login (`LoginPage`) | Input username (`USERNAME_INPUT`) | `.//input[@id='user-name']` | Memilih field username berdasarkan ID yang unik. |
| Login (`LoginPage`) | Input password (`PASSWORD_INPUT`) | `.//input[@id='password']` | Memilih field password berdasarkan ID yang unik. |
| Login (`LoginPage`) | Tombol login (`LOGIN_BUTTON`) | `.//input[@id='login-button']` | Memilih tombol submit login berdasarkan ID. |
| Login (`LoginPage`) | Pesan error (`ERROR_MESSAGE`) | `.//*[@data-test='error']` | Memilih elemen yang membawa atribut `data-test="error"`. |
| Produk/dashboard (`InventoryPage`) | Judul halaman (`TITLE_HEADER`) | `.//*[contains(concat(' ', normalize-space(@class), ' '), ' title ')]` | Memilih elemen dengan token class `title`, tanpa bergantung pada tag HTML. |
| Produk/dashboard (`InventoryPage`) | Tombol tambah backpack (`ADD_TO_CART_BTN`) | `.//button[@id='add-to-cart-sauce-labs-backpack']` | Memilih tombol add-to-cart khusus produk Sauce Labs Backpack. |
| Produk/dashboard (`InventoryPage`) | Ikon keranjang (`CART_ICON`) | `.//a[contains(concat(' ', normalize-space(@class), ' '), ' shopping_cart_link ')]` | Memilih tautan keranjang berdasarkan token class-nya. |
| Produk/dashboard (`InventoryPage`) | Tombol menu (`MENU_BUTTON`) | `.//button[@id='react-burger-menu-btn']` | Memilih tombol pembuka menu navigasi berdasarkan ID. |
| Produk/dashboard (`InventoryPage`) | Tautan logout (`LOGOUT_LINK`) | `.//*[@id='logout_sidebar_link']` | Memilih tautan logout di menu samping berdasarkan ID. |
| Keranjang (`CartPage`) | Tombol checkout (`CHECKOUT_BTN`) | `.//button[@id='checkout']` | Memilih tombol untuk memulai checkout berdasarkan ID. |
| Keranjang (`CartPage`) | Nama produk (`ITEM_NAME`) | `.//*[contains(concat(' ', normalize-space(@class), ' '), ' cart_item ')]//*[contains(concat(' ', normalize-space(@class), ' '), ' inventory_item_name ')]` | Memilih nama produk di dalam baris item keranjang, bukan nama produk lain di halaman. |
| Keranjang (`CartPage`) | Kuantitas produk (`ITEM_QUANTITY`) | `.//*[contains(concat(' ', normalize-space(@class), ' '), ' cart_item ')]//*[contains(concat(' ', normalize-space(@class), ' '), ' cart_quantity ')]` | Memilih kuantitas di dalam baris item keranjang. |
| Informasi checkout (`CheckoutInfoPage`) | Input nama depan (`FIRST_NAME`) | `.//input[@id='first-name']` | Memilih field nama depan berdasarkan ID. |
| Informasi checkout (`CheckoutInfoPage`) | Input nama belakang (`LAST_NAME`) | `.//input[@id='last-name']` | Memilih field nama belakang berdasarkan ID. |
| Informasi checkout (`CheckoutInfoPage`) | Input kode pos (`POSTAL_CODE`) | `.//input[@id='postal-code']` | Memilih field kode pos berdasarkan ID. |
| Informasi checkout (`CheckoutInfoPage`) | Tombol continue (`CONTINUE_BTN`) | `.//input[@id='continue']` | Memilih tombol untuk melanjutkan checkout berdasarkan ID. |
| Ringkasan checkout (`CheckoutOverviewPage`) | Tombol finish (`FINISH_BTN`) | `.//button[@id='finish']` | Memilih tombol untuk menyelesaikan pesanan berdasarkan ID. |
| Checkout selesai (`CheckoutCompletePage`) | Header konfirmasi (`COMPLETE_HEADER`) | `.//*[contains(concat(' ', normalize-space(@class), ' '), ' complete-header ')]` | Memilih header konfirmasi berdasarkan token class `complete-header`. |
