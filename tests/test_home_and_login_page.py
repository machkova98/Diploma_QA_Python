import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep


EMAIL = 'nastya.machkova98@gmail.com'
PASSWORD = '1234567'
SEARCH = 'laptop'
SEARCH_JS = 'jeans'
BLACK_SHOES = 'black shoes'


def test_check_discount(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.all_cookies.click()
    home_page.check_discount.is_displayed()
    assert home_page.check_discount.text == "30% OFF EVERYTHING*"


def test_login_page_open(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.all_cookies.click()
    driver.execute_script("window.scrollTo(1000, 2000)")
    sleep(2)
    # WebDriverWait(driver, 10).until(ec.element_to_be_clickable(home_page.account_button))
    home_page.account_button.click()
    login_page = LoginPage(driver)
    assert login_page.log_in_text.is_displayed()


def test_log_in_enabled(driver):
    home_page = HomePage(driver)
    home_page.open()
    # home_page.all_cookies.click()
    driver.execute_script("window.scrollTo(1000, 2000)")
    sleep(2)
    # WebDriverWait(driver, 10).until(ec.element_to_be_clickable(home_page.account_button))
    home_page.account_button.click()
    login_page = LoginPage(driver)
    login_page.email_field.send_keys(EMAIL)
    login_page.passwd_field.send_keys(PASSWORD)
    login_page.log_in_button.click()
    assert login_page.log_in_button.is_enabled()


def test_error_when_empty_fields(driver):
    home_page = HomePage(driver)
    home_page.open()
    # home_page.all_cookies.click()
    driver.execute_script("window.scrollTo(0, 2500)")
    # WebDriverWait(driver, 10).until(ec.element_to_be_clickable(home_page.account_button))
    sleep(2)
    home_page.account_button.click()
    login_page = LoginPage(driver)
    login_page.log_in_button.click()
    login_page.error.is_displayed()
    assert login_page.error.text == 'This field is required.'


def test_error_color(driver):
    home_page = HomePage(driver)
    home_page.open()
    # home_page.all_cookies.click()
    driver.execute_script("window.scrollTo(0, 2500)")
    # WebDriverWait(driver, 10).until(ec.element_to_be_clickable(home_page.account_button))
    sleep(2)
    home_page.account_button.click()
    login_page = LoginPage(driver)
    login_page.log_in_button.click()
    error_color = login_page.error.value_of_css_property('background-color')
    assert error_color == 'rgba(253, 232, 231, 1)'


def test_search_button_is_clickable(driver):
    home_page = HomePage(driver)
    home_page.open()
    # home_page.all_cookies.click()
    home_page.search_button.click()
    assert home_page.search_button.is_enabled()


def test_search_soap(driver):
    home_page = HomePage(driver)
    home_page.open()
    # home_page.all_cookies.click()
    home_page.search_button.click()
    home_page.search_field.send_keys(SEARCH)
    home_page.search_field.send_keys(Keys.ENTER)
    home_page.no_result.is_displayed()
    assert home_page.no_result.text == 'It looks like we haven’t found anything for that search term.\n'\
                                       'Try browsing some of the categories below'


def test_amount_of_results_jeans(driver):
    home_page = HomePage(driver)
    home_page.open()
    # home_page.all_cookies.click()
    home_page.search_button.click()
    home_page.search_field.send_keys(SEARCH_JS)
    home_page.search_field.send_keys(Keys.ENTER)
    home_page.jeans_result.is_displayed()
    print(home_page.jeans_result.text)
    assert home_page.jeans_result.text > '450'


def test_favorite(driver):
    home_page = HomePage(driver)
    home_page.open()
    # home_page.all_cookies.click()
    home_page.search_button.click()
    home_page.search_field.send_keys(SEARCH_JS)
    home_page.search_field.send_keys(Keys.ENTER)
    driver.execute_script("window.scrollTo(0, 500)")
    sleep(2)
    # WebDriverWait(driver, 10).until(ec.element_to_be_clickable(home_page.add_to_wishlist))
    home_page.add_to_wishlist.click()
    driver.execute_script("window.scrollTo(500, 0)")
    sleep(2)
    home_page.wish_list.click()
    home_page.jeans_in_wishlist.is_displayed()
    assert "Straight Talking High-Waisted Jeans" in home_page.jeans_in_wishlist.text


def test_button_select_is_enabled_in_wishlist(driver):
    home_page = HomePage(driver)
    home_page.open()
    # home_page.all_cookies.click()
    home_page.search_button.click()
    home_page.search_field.send_keys(SEARCH_JS)
    home_page.search_field.send_keys(Keys.ENTER)
    driver.execute_script("window.scrollTo(0, 500)")
    sleep(2)
    # WebDriverWait(driver, 10).until(ec.element_to_be_clickable(home_page.add_to_wishlist))
    home_page.add_to_wishlist.click()
    driver.execute_script("window.scrollTo(500, 0)")
    sleep(2)
    home_page.wish_list.click()
    driver.execute_script("window.scrollTo(0, 500)")
    sleep(2)
    size = Select(home_page.select_size_in_wishlist)
    size.select_by_value('16')
    assert home_page.button_select.is_displayed()


def test_remove_from_wishlist_dialog_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    # home_page.all_cookies.click()
    home_page.search_button.click()
    home_page.search_field.send_keys(SEARCH_JS)
    home_page.search_field.send_keys(Keys.ENTER)
    driver.execute_script("window.scrollTo(0, 500)")
    sleep(2)
    # WebDriverWait(driver, 10).until(ec.element_to_be_clickable(home_page.add_to_wishlist))
    home_page.add_to_wishlist.click()
    driver.execute_script("window.scrollTo(500, 0)")
    sleep(2)
    home_page.wish_list.click()
    driver.execute_script("window.scrollTo(0, 500)")
    sleep(2)
    home_page.remove.click()
    assert home_page.dialog.is_displayed()


def test_remove_from_the_wishlist(driver):
    home_page = HomePage(driver)
    home_page.open()
    # home_page.all_cookies.click()
    home_page.search_button.click()
    home_page.search_field.send_keys(SEARCH_JS)
    home_page.search_field.send_keys(Keys.ENTER)
    driver.execute_script("window.scrollTo(0, 500)")
    sleep(2)
    # WebDriverWait(driver, 10).until(ec.element_to_be_clickable(home_page.add_to_wishlist))
    home_page.add_to_wishlist.click()
    driver.execute_script("window.scrollTo(500, 0)")
    sleep(2)
    home_page.wish_list.click()
    driver.execute_script("window.scrollTo(0, 500)")
    sleep(2)
    home_page.remove.click()
    home_page.button_delete.click()
    assert home_page.empty_text_in_wishlist.text == "You don't have any items saved for later (yet)"


def test_add_2_shoes_to_wl(driver):
    home_page = HomePage(driver)
    home_page.open()
    # home_page.all_cookies.click()
    home_page.search_button.click()
    home_page.search_field.send_keys(BLACK_SHOES)
    home_page.search_field.send_keys(Keys.ENTER)
    driver.execute_script("window.scrollTo(0, 500)")
    sleep(2)
    home_page.shoes_add_to_wl.click()
    home_page.shoes_add_to_wl_2.click()
    driver.execute_script("window.scrollTo(500, 0)")
    sleep(2)
    home_page.wish_list.click()
    home_page.amount_of_shoes.is_displayed()
    assert "2" in home_page.amount_of_shoes.text


def test_price_color_discount(driver):
    home_page = HomePage(driver)
    home_page.open()
    # home_page.all_cookies.click()
    home_page.search_button.click()
    home_page.search_field.send_keys(BLACK_SHOES)
    home_page.search_field.send_keys(Keys.ENTER)
    driver.execute_script("window.scrollTo(0, 500)")
    sleep(2)
    home_page.discount_color_type = home_page.discount_color.get_attribute('content')
    assert home_page.discount_color_type == '55.30'


def test_images_decrease(driver):
    home_page = HomePage(driver)
    home_page.open()
    # home_page.all_cookies.click()
    home_page.search_button.click()
    home_page.search_field.send_keys(SEARCH_JS)
    home_page.search_field.send_keys(Keys.ENTER)
    home_page.button_four.click()
    images_decrease = home_page.images_decrease.get_attribute('data-col-count')
    assert images_decrease == "4"
