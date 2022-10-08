import pytest
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.clothes_page import ClothesPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from time import sleep


# 7_test
@pytest.mark.skip
def test_colour_button(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.all_cookies.click()
    home_page.cart_button.click()
    cart_page = CartPage(driver)
    driver.execute_script("window.scrollTo(0, 300)")
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(cart_page.shop_new_in))
    cart_page.shop_new_in.click()
    clothes_page = ClothesPage(driver)
    clothes_page.colour_button.click()
    assert clothes_page.colour_button.is_enabled()


# test_8
@pytest.mark.skip
def test_black_colour_selected(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.all_cookies.click()
    home_page.cart_button.click()
    cart_page = CartPage(driver)
    driver.execute_script("window.scrollTo(0, 300)")
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(cart_page.shop_new_in))
    cart_page.shop_new_in.click()
    clothes_page = ClothesPage(driver)
    clothes_page.colour_button.click()
    clothes_page.black_select.click()
    sleep(2)
    assert clothes_page.colour_button.text == "Colour\n(1)"


# test_9
@pytest.mark.skip
def test_when_black_select_trousers_img_appear(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.all_cookies.click()
    home_page.cart_button.click()
    cart_page = CartPage(driver)
    driver.execute_script("window.scrollTo(0, 300)")
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(cart_page.shop_new_in))
    cart_page.shop_new_in.click()
    clothes_page = ClothesPage(driver)
    clothes_page.colour_button.click()
    clothes_page.black_select.click()
    sleep(2)
    assert clothes_page.trousers_image.is_displayed()


# test_10
@pytest.mark.skip
def test_clear_all_button(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.all_cookies.click()
    home_page.cart_button.click()
    cart_page = CartPage(driver)
    driver.execute_script("window.scrollTo(0, 300)")
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(cart_page.shop_new_in))
    cart_page.shop_new_in.click()
    clothes_page = ClothesPage(driver)
    clothes_page.colour_button.click()
    clothes_page.black_select.click()
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(clothes_page.clear_all))
    clothes_page.clear_all.click()
    sleep(2)
    assert clothes_page.colour_button.text != "Colour\n(1)"


# test_11
@pytest.mark.skip
def test_showing_number_on_the_page(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.all_cookies.click()
    home_page.cart_button.click()
    cart_page = CartPage(driver)
    driver.execute_script("window.scrollTo(0, 300)")
    sleep(2)
    # WebDriverWait(driver, 10).until(ec.element_to_be_clickable(cart_page.shop_new_in))
    cart_page.shop_new_in.click()
    clothes_page = ClothesPage(driver)
    driver.execute_script("window.scrollTo(6000, 8600)")
    sleep(2)
    clothes_page.showing_number_of_orders.is_displayed()
    assert clothes_page.showing_number_of_orders.text < "65"


# test_14
@pytest.mark.skip
def test_sort_price_low_to_high(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.all_cookies.click()
    home_page.cart_button.click()
    cart_page = CartPage(driver)
    driver.execute_script("window.scrollTo(0, 300)")
    sleep(2)
    # WebDriverWait(driver, 10).until(ec.element_to_be_clickable(cart_page.shop_new_in))
    cart_page.shop_new_in.click()
    clothes_page = ClothesPage(driver)
    clothes_page.sort.click()
    low_to_high = Select(clothes_page.sort)
    low_to_high.select_by_value('price-low-to-high')
    sleep(2)
    print(clothes_page.brush.text)
    assert clothes_page.brush.is_displayed()


# test_15
@pytest.mark.skip
def test_read_more_less_text(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.all_cookies.click()
    home_page.cart_button.click()
    cart_page = CartPage(driver)
    driver.execute_script("window.scrollTo(0, 300)")
    # sleep(2)
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(cart_page.shop_new_in))
    cart_page.shop_new_in.click()
    clothes_page = ClothesPage(driver)
    read_less = clothes_page.read_more.click()
    assert clothes_page.read_more.text != read_less
