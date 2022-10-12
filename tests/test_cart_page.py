import allure
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.clothes_page import ClothesPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep


CARDIGAN = 'cardigan'
BLACK_SHOES = 'black shoes'


@allure.feature("Cart Page")
@allure.story("Empty cart")
def test_check_open_cart_empty_page(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Accept cookies"):
        home_page.all_cookies.click()
    with allure.step("Click"):
        home_page.cart_button.click()
    with allure.step("Open Cart Page"):
        cart_page = CartPage(driver)
    with allure.step("Empty cart is displayed"):
        cart_page.cart_empty.is_displayed()
        assert cart_page.cart_empty.text == "Your cart is currently empty"


@allure.feature("Cart Page")
@allure.story("Clothes width")
def test_blazer_and_skirt_width(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click"):
        home_page.cart_button.click()
    with allure.step("Open Cart Page"):
        cart_page = CartPage(driver)
    with allure.step("Check the width"):
        blazer = cart_page.blazer_and_skirt_width.value_of_css_property('width')
        assert blazer == '235.167px'


@allure.feature("Cart Page")
@allure.story("Open cart from clothes page")
def test_go_to_clothes_from_cart(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click"):
        home_page.cart_button.click()
    with allure.step("Open Cart Page"):
        cart_page = CartPage(driver)
    driver.execute_script("window.scrollTo(0, 300)")
    sleep(2)
    with allure.step("Click"):
        cart_page.shop_new_in.click()
    with allure.step("Open Clothes Page"):
        clothes_page = ClothesPage(driver)
    with allure.step("Text is displayed in the Clothes Page"):
        clothes_page.new_in_txt.is_displayed()
        assert clothes_page.new_in_txt.text == "NEW IN"


@allure.feature("Cart Page")
@allure.story("Add to cart")
def test_add_to_cart(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click search button"):
        home_page.search_button.click()
    with allure.step("Insert values"):
        home_page.search_field.send_keys(CARDIGAN)
        home_page.search_field.send_keys(Keys.ENTER)
    with allure.step("Choose the item and add to the cart"):
        home_page.cardigan.click()
        home_page.choose_size_s.click()
        home_page.add_to_cart.click()
        home_page.view_bag.click()
    with allure.step("Open Cart Page"):
        cart_page = CartPage(driver)
    with allure.step("The item in the cart is displayed"):
        cart_page.cardigan_in_cart.is_displayed()
        assert "Plus Size Shoulder Detail Oversized Cardi" in cart_page.cardigan_in_cart.text


@allure.feature("Cart Page")
@allure.story("Edit cart")
def test_edit_cart(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click search button"):
        home_page.search_button.click()
    with allure.step("Insert values"):
        home_page.search_field.send_keys(CARDIGAN)
        home_page.search_field.send_keys(Keys.ENTER)
    with allure.step("Choose the item and add to the cart"):
        home_page.cardigan.click()
        home_page.choose_size_s.click()
        home_page.add_to_cart.click()
        home_page.view_bag.click()
    with allure.step("Open Cart Page"):
        cart_page = CartPage(driver)
    with allure.step("Check the item is displayed"):
        cart_page.cardigan_in_cart.is_displayed()
    with allure.step("Edit info in cart"):
        cart_page.edit_in_cart.click()
        rose_cardigan = Select(cart_page.select_bigger_cardigan)
        rose_cardigan.select_by_value('350')
    sleep(2)
    with allure.step("The info is updated"):
        cart_page.update_cart.click()
        assert cart_page.cardigan_size.text == "50"


@allure.feature("Cart Page")
@allure.story("Secure checkout")
def test_secure_checkout_cart_page(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click search button"):
        home_page.search_button.click()
    with allure.step("Insert values"):
        home_page.search_field.send_keys(BLACK_SHOES)
        home_page.search_field.send_keys(Keys.ENTER)
    with allure.step("Choose the item and add to the cart"):
        home_page.black_shoes.click()
        home_page.shoes_size.click()
        home_page.add_to_cart.click()
        home_page.view_bag.click()
    with allure.step("Open Cart Page"):
        cart_page = CartPage(driver)
    with allure.step("Check checkout page"):
        cart_page.checkout.click()
        assert cart_page.secure.text == "Secure checkout"


@allure.feature("Cart Page")
@allure.story("Delete items in cart")
def test_delete_in_cart(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click search button"):
        home_page.search_button.click()
    with allure.step("Insert values"):
        home_page.search_field.send_keys(BLACK_SHOES)
        home_page.search_field.send_keys(Keys.ENTER)
    with allure.step("Choose the item and add to the cart"):
        home_page.black_shoes.click()
        home_page.shoes_size.click()
        home_page.add_to_cart.click()
        home_page.view_bag.click()
    with allure.step("Open Cart Page"):
        cart_page = CartPage(driver)
    with allure.step("Remove from the cart"):
        cart_page.remove_button.click()
        assert cart_page.cart_empty_after_remove.text != "Cart(1)"
