import pytest
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.clothes_page import ClothesPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep


CARDIGAN = 'cardigan'
BLACK_SHOES = 'black shoes'


@pytest.mark.skip
def test_check_open_cart_empty_page(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.all_cookies.click()
    home_page.cart_button.click()
    cart_page = CartPage(driver)
    cart_page.cart_empty.is_displayed()
    assert cart_page.cart_empty.text == "Your cart is currently empty"


@pytest.mark.skip
def test_blazer_and_skirt_width(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.cart_button.click()
    cart_page = CartPage(driver)
    blazer = cart_page.blazer_and_skirt_width.value_of_css_property('width')
    assert blazer == '235.167px'


@pytest.mark.skip
def test_go_to_clothes_from_cart(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.all_cookies.click()
    home_page.cart_button.click()
    cart_page = CartPage(driver)
    driver.execute_script("window.scrollTo(0, 300)")
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(cart_page.shop_new_in))
    cart_page.shop_new_in.click()
    clothes_page = ClothesPage(driver)
    clothes_page.new_in_txt.is_displayed()
    assert clothes_page.new_in_txt.text == "NEW IN"


# test_19
@pytest.mark.skip
def test_add_to_cart(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.all_cookies.click()
    home_page.search_button.click()
    home_page.search_field.send_keys(CARDIGAN)
    home_page.search_field.send_keys(Keys.ENTER)
    home_page.cardigan.click()
    home_page.choose_size_s.click()
    home_page.add_to_cart.click()
    home_page.view_bag.click()
    cart_page = CartPage(driver)
    cart_page.cardigan_in_cart.is_displayed()
    assert "Over Knit Button-Down Ribbed Cardigan" in cart_page.cardigan_in_cart.text


# test_20
@pytest.mark.skip
def test_edit_cart(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.all_cookies.click()
    home_page.search_button.click()
    home_page.search_field.send_keys(CARDIGAN)
    home_page.search_field.send_keys(Keys.ENTER)
    home_page.cardigan.click()
    home_page.choose_size_s.click()
    home_page.add_to_cart.click()
    home_page.view_bag.click()
    cart_page = CartPage(driver)
    cart_page.cardigan_in_cart.is_displayed()
    cart_page.edit_in_cart.click()
    rose_cardigan = Select(cart_page.select_rose_cardigan)
    rose_cardigan.select_by_value('158')
    sleep(2)
    cart_page.update_cart.click()
    assert cart_page.rose_color.text == "rose"


# test_25
@pytest.mark.skip
def test_secure_checkout_cart_page(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.all_cookies.click()
    home_page.search_button.click()
    home_page.search_field.send_keys(BLACK_SHOES)
    home_page.search_field.send_keys(Keys.ENTER)
    home_page.black_shoes.click()
    home_page.shoes_size.click()
    home_page.add_to_cart.click()
    home_page.view_bag.click()
    cart_page = CartPage(driver)
    cart_page.checkout.click()
    assert cart_page.secure.text == "Secure checkout"


# test_26
@pytest.mark.skip
def test_delete_in_cart(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.all_cookies.click()
    home_page.search_button.click()
    home_page.search_field.send_keys(BLACK_SHOES)
    home_page.search_field.send_keys(Keys.ENTER)
    home_page.black_shoes.click()
    home_page.shoes_size.click()
    home_page.add_to_cart.click()
    home_page.view_bag.click()
    cart_page = CartPage(driver)
    cart_page.remove_button.click()
    assert cart_page.cart_empty_after_remove.text != "Cart(1)"

