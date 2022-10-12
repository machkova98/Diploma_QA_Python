import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep


EMAIL = 'nastya.machkova98@gmail.com'
PASSWORD = '1234567'
SEARCH = 'laptop'
SEARCH_JS = 'jeans'
BLACK_SHOES = 'black shoes'


@allure.feature("Home Page")
@allure.story("Check discount")
def test_check_discount(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Show discount"):
        home_page.check_discount.is_displayed()
        assert home_page.check_discount.text == "30% OFF EVERYTHING*"


@allure.feature("Home Page")
@allure.story("Open login page")
def test_login_page_open(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
        driver.execute_script("window.scrollTo(1000, 2000)")
        sleep(2)
    with allure.step("Click"):
        home_page.account_button.click()
    with allure.step("Open login page"):
        login_page = LoginPage(driver)
        assert login_page.log_in_text.is_displayed()


@allure.feature("Home Page")
@allure.story("Button log is enabled")
def test_log_in_enabled(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
        driver.execute_script("window.scrollTo(1000, 2000)")
        sleep(2)
    with allure.step("Click"):
        home_page.account_button.click()
    with allure.step("Open login page"):
        login_page = LoginPage(driver)
    with allure.step("Insert values"):
        login_page.email_field.send_keys(EMAIL)
        login_page.passwd_field.send_keys(PASSWORD)
    with allure.step("Check the button is enabled"):
        login_page.log_in_button.click()
        assert login_page.log_in_button.is_enabled()


@allure.feature("Home Page")
@allure.story("Error should appear when fields empty")
def test_error_when_empty_fields(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
        driver.execute_script("window.scrollTo(0, 2500)")
        sleep(2)
    with allure.step("Click"):
        home_page.account_button.click()
    with allure.step("Open login page"):
        login_page = LoginPage(driver)
    with allure.step("Do not insert values"):
        login_page.log_in_button.click()
    with allure.step("Error appears"):
        login_page.error.is_displayed()
        assert login_page.error.text == 'This field is required.'


@allure.feature("Home Page")
@allure.story("Error color appears")
def test_error_color(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
        driver.execute_script("window.scrollTo(0, 2500)")
        sleep(2)
    with allure.step("Click"):
        home_page.account_button.click()
    with allure.step("Open login page"):
        login_page = LoginPage(driver)
    with allure.step("Click the login button"):
        login_page.log_in_button.click()
    with allure.step("Check color of the error"):
        error_color = login_page.error.value_of_css_property('background-color')
        assert error_color == 'rgba(253, 232, 231, 1)'


@allure.feature("Home Page")
@allure.story("Search button")
def test_search_button_is_clickable(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Search button is enabled"):
        home_page.search_button.click()
        assert home_page.search_button.is_enabled()


@allure.feature("Home Page")
@allure.story("Search not exist items")
def test_search_soap(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click search button"):
        home_page.search_button.click()
    with allure.step("Insert values of not existed item"):
        home_page.search_field.send_keys(SEARCH)
        home_page.search_field.send_keys(Keys.ENTER)
    with allure.step("Check the text"):
        home_page.no_result.is_displayed()
        assert home_page.no_result.text == 'It looks like we haven’t found anything for that search term.\n'\
                                       'Try browsing some of the categories below'


@allure.feature("Home Page")
@allure.story("Number of jeans in the page")
def test_amount_of_results_jeans(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click search button"):
        home_page.search_button.click()
    with allure.step("Insert values"):
        home_page.search_field.send_keys(SEARCH_JS)
        home_page.search_field.send_keys(Keys.ENTER)
    with allure.step("The amount of jeans displayed"):
        home_page.jeans_result.is_displayed()
        print(home_page.jeans_result.text)
        assert home_page.jeans_result.text > '450'


@allure.feature("Home Page")
@allure.story("Add to the wishlist")
def test_favorite(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click search button"):
        home_page.search_button.click()
    with allure.step("Insert values"):
        home_page.search_field.send_keys(SEARCH_JS)
        home_page.search_field.send_keys(Keys.ENTER)
        driver.execute_script("window.scrollTo(0, 500)")
        sleep(2)
    with allure.step("Add the item to wishlist"):
        home_page.add_to_wishlist.click()
        driver.execute_script("window.scrollTo(500, 0)")
        sleep(2)
    with allure.step("Go to the wishlist"):
        home_page.wish_list.click()
    with allure.step("Item is displayed in the wishlist"):
        home_page.jeans_in_wishlist.is_displayed()
        assert "Straight Talking High-Waisted Jeans" in home_page.jeans_in_wishlist.text


@allure.feature("Home Page")
@allure.story("Select button is enabled in wishlist")
def test_button_select_is_enabled_in_wishlist(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click search button"):
        home_page.search_button.click()
    with allure.step("Insert values"):
        home_page.search_field.send_keys(SEARCH_JS)
        home_page.search_field.send_keys(Keys.ENTER)
        driver.execute_script("window.scrollTo(0, 500)")
        sleep(2)
    with allure.step("Add the item to wishlist"):
        home_page.add_to_wishlist.click()
        driver.execute_script("window.scrollTo(500, 0)")
        sleep(2)
    with allure.step("Button select in wishlist is enabled"):
        home_page.wish_list.click()
        driver.execute_script("window.scrollTo(0, 500)")
        sleep(2)
        size = Select(home_page.select_size_in_wishlist)
        size.select_by_value('16')
        assert home_page.button_select.is_displayed()


@allure.feature("Home Page")
@allure.story("Dialog is displayed when deleting items")
def test_remove_from_wishlist_dialog_displayed(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click search button"):
        home_page.search_button.click()
    with allure.step("Insert values"):
        home_page.search_field.send_keys(SEARCH_JS)
        home_page.search_field.send_keys(Keys.ENTER)
        driver.execute_script("window.scrollTo(0, 500)")
        sleep(2)
    with allure.step("Add the item to wishlist"):
        home_page.add_to_wishlist.click()
        driver.execute_script("window.scrollTo(500, 0)")
        sleep(2)
    with allure.step("Go to the wishlist"):
        home_page.wish_list.click()
        driver.execute_script("window.scrollTo(0, 500)")
        sleep(2)
    with allure.step("Try removing the item, dialogue is displayed"):
        home_page.remove.click()
        assert home_page.dialog.is_displayed()


@allure.feature("Home Page")
@allure.story("Delete items from the wishlist")
def test_remove_from_the_wishlist(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click search button"):
        home_page.search_button.click()
    with allure.step("Insert values"):
        home_page.search_field.send_keys(SEARCH_JS)
        home_page.search_field.send_keys(Keys.ENTER)
        driver.execute_script("window.scrollTo(0, 500)")
        sleep(2)
    with allure.step("Add the item to wishlist"):
        home_page.add_to_wishlist.click()
        driver.execute_script("window.scrollTo(500, 0)")
        sleep(2)
    with allure.step("Go to the wishlist"):
        home_page.wish_list.click()
        driver.execute_script("window.scrollTo(0, 500)")
        sleep(2)
    with allure.step("Delete the item from the wishlist"):
        home_page.remove.click()
        home_page.button_delete.click()
        assert home_page.show_items_in_wishlist.text == "'Showing 2 of 2 products"


@allure.feature("Home Page")
@allure.story("Add shoes to the wishlist")
def test_add_2_shoes_to_wl(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click search button"):
        home_page.search_button.click()
    with allure.step("Insert values"):
        home_page.search_field.send_keys(BLACK_SHOES)
        home_page.search_field.send_keys(Keys.ENTER)
        driver.execute_script("window.scrollTo(0, 500)")
        sleep(2)
    with allure.step("Add items to the wishlist"):
        home_page.shoes_add_to_wl.click()
        home_page.shoes_add_to_wl_2.click()
        driver.execute_script("window.scrollTo(500, 0)")
        sleep(2)
    with allure.step("The amount of items in the wishlist"):
        home_page.wish_list.click()
        home_page.amount_of_shoes.is_displayed()
        assert "3" in home_page.amount_of_shoes.text


@allure.feature("Home Page")
@allure.story("Check discount in wishlist")
def test_price_color_discount(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click search button"):
        home_page.search_button.click()
    with allure.step("Insert values"):
        home_page.search_field.send_keys(BLACK_SHOES)
        home_page.search_field.send_keys(Keys.ENTER)
        driver.execute_script("window.scrollTo(0, 500)")
        sleep(2)
    with allure.step("Price of the items"):
        home_page.discount_color_type = home_page.discount_color.get_attribute('content')
        assert home_page.discount_color_type == '55.30'


@allure.feature("Home Page")
@allure.story("Amount of items in a row")
def test_images_decrease(driver):
    with allure.step("Open Home Page"):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Click search button"):
        home_page.search_button.click()
    with allure.step("Insert values"):
        home_page.search_field.send_keys(SEARCH_JS)
        home_page.search_field.send_keys(Keys.ENTER)
    with allure.step("Click 4 items should be displayed on the page"):
        home_page.button_four.click()
        images_decrease = home_page.images_decrease.get_attribute('data-col-count')
        assert images_decrease == "4"
