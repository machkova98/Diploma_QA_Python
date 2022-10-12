import allure
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.clothes_page import ClothesPage
from selenium.webdriver.support.ui import Select
from time import sleep


@allure.feature("Clothes Page")
@allure.story("Colout button is enabled")
def test_colour_button(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click"):
        home_page.cart_button.click()
        home_page.delete_from_the_cart.click()
        home_page.open_clothes.click()
    with allure.step("Open Clothes Page"):
        clothes_page = ClothesPage(driver)
    with allure.step("Check the button is enabled"):
        clothes_page.colour_button.click()
        assert clothes_page.colour_button.is_enabled()


@allure.feature("Clothes Page")
@allure.story("Black color is selected")
def test_black_colour_selected(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click"):
        home_page.cart_button.click()
    with allure.step("Open Cart Page"):
        cart_page = CartPage(driver)
        driver.execute_script("window.scrollTo(0, 500)")
        sleep(2)
    with allure.step("Click"):
        cart_page.shop_new_in.click()
    with allure.step("Open Clothes Page"):
        clothes_page = ClothesPage(driver)
    with allure.step("Select black color"):
        clothes_page.colour_button.click()
        clothes_page.black_select.click()
        sleep(2)
    with allure.step("Check the item is selected"):
        assert clothes_page.colour_button.text == "Colour\n(1)"


@allure.feature("Clothes Page")
@allure.story("Black color selected, image appear")
def test_when_black_select_trousers_img_appear(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click"):
        home_page.cart_button.click()
    with allure.step("Open Cart Page"):
        cart_page = CartPage(driver)
        driver.execute_script("window.scrollTo(0, 500)")
        sleep(2)
    with allure.step("Click"):
        cart_page.shop_new_in.click()
    with allure.step("Open Clothes Page"):
        clothes_page = ClothesPage(driver)
    with allure.step("Select black color - image appears"):
        clothes_page.colour_button.click()
        clothes_page.black_select.click()
        sleep(2)
        assert clothes_page.trousers_image.is_displayed()


@allure.feature("Clothes Page")
@allure.story("Clear button choice")
def test_clear_all_button(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click"):
        home_page.cart_button.click()
    with allure.step("Open Cart Page"):
        cart_page = CartPage(driver)
        driver.execute_script("window.scrollTo(0, 500)")
        sleep(2)
    with allure.step("Click"):
        cart_page.shop_new_in.click()
    with allure.step("Open Clothes Page"):
        clothes_page = ClothesPage(driver)
    with allure.step("Select black color"):
        clothes_page.colour_button.click()
        clothes_page.black_select.click()
        sleep(2)
    with allure.step("Unselect black color"):
        clothes_page.clear_all.click()
        sleep(2)
        assert clothes_page.colour_button.text != "Colour\n(1)"


@allure.feature("Clothes Page")
@allure.story("Number of the items on the page")
def test_showing_number_on_the_page(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click"):
        home_page.cart_button.click()
    with allure.step("Open Cart Page"):
        cart_page = CartPage(driver)
        driver.execute_script("window.scrollTo(0, 500)")
        sleep(2)
    with allure.step("Click"):
        cart_page.shop_new_in.click()
    with allure.step("Open Clothes Page"):
        clothes_page = ClothesPage(driver)
        driver.execute_script("window.scrollTo(6000, 8600)")
        sleep(2)
    with allure.step("Check the amount of items in the page"):
        clothes_page.showing_number_of_orders.is_displayed()
        assert clothes_page.showing_number_of_orders.text < "65"


@allure.feature("Clothes Page")
@allure.story("Sorting items")
def test_sort_price_low_to_high(driver):
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
    with allure.step("Select price low to high items"):
        clothes_page.sort.click()
        low_to_high = Select(clothes_page.sort)
        low_to_high.select_by_value('price-low-to-high')
        sleep(2)
    with allure.step("Check the first item"):
        print(clothes_page.brush.text)
        assert clothes_page.brush.is_displayed()


@allure.feature("Clothes Page")
@allure.story("Read more text")
def test_read_more_less_text(driver):
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
    with allure.step("Show more text"):
        read_less = clothes_page.read_more.click()
        assert clothes_page.read_more.text != read_less


@allure.feature("Clothes Page")
@allure.story("Plus size clothes appear")
def test_plus_size_clothes(driver):
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
    with allure.step("Show plus size items"):
        clothes_page.shop_by_fit.click()
        clothes_page.plus_size.click()
    assert clothes_page.jeans.is_displayed()
    assert clothes_page.underwear.is_displayed()
