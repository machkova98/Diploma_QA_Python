from pages.base_page import BasePage
from selenium.webdriver.common.by import By


all_cookies = (By.XPATH, '//*[@class="b-notification_panel-button b-button m-large"]')
account_button = (By.XPATH, '//*[@href="https://www.nastygal.com/eu/myaccount"]')
check_discount = (By.XPATH, '//*[@class="live-text-promo-title hidden-on-mobile"]')
cart_button = (By.CSS_SELECTOR, 'a[title="View your cart"]')
search_button = (By.CSS_SELECTOR, 'span[class="b-search_toggle-icon"]')
search_field = (By.CSS_SELECTOR, 'input[id="header-search-input"]')
no_result = (By.CSS_SELECTOR, 'p[class="b-header_search-noresult_msg"]')
jeans_result = (By.CSS_SELECTOR, 'span[class="b-header_search-count"]')
cardigan = (By.CSS_SELECTOR, 'a[data-pid="AGG08275-1"]')
choose_size_s = (By.CSS_SELECTOR, 'button[id="variation-swatch-button-1-68"]')
add_to_bag = (By.CSS_SELECTOR, 'button[data-id="addToCart"]')
view_bag = (By.CSS_SELECTOR, 'a[class="b-button m-outline b-minicart-button"]')
add_to_wishlist = (By.CSS_SELECTOR, 'i[class="b-wishlist_button-icon"]')
alert_added = (By.LINK_TEXT, 'Product added to wish list')
wish_list = (By.XPATH, '//*[@id="page-head"]/div[2]/div[2]/div/div[4]')
jeans_in_wishlist = (By.CSS_SELECTOR, 'h2[class="b-product_tile-title"]')
select_size_wl = (By.CSS_SELECTOR, 'select[class="b-select-input attribute-size"')
button_select_tap = (By.CSS_SELECTOR, 'span[data-ref="container"]')
remove = (By.CSS_SELECTOR, 'a[class="b-wishlist_tile-remove"]')
dialog = (By.XPATH, '//div[@aria-labelledby="Delete item?"]')
delete_button = (By.CSS_SELECTOR, 'button[data-tau="remove_item_confirmation_confirm"]')
empty_text = (By.CSS_SELECTOR, 'p[class="b-wishlist-empty_text"]')
black_shoes = (By.CSS_SELECTOR, 'a[data-pid ="AGG44076"]')
shoes_size = (By.CSS_SELECTOR, 'button[aria-label="38"]')
shoes_to_add_to_wl = (By.XPATH, '//*[@id="product-grid"]/div[2]/section[1]/div[2]/div[1]/div[1]/button[2]/i')
shoes_to_add_to_wl_2 = (By.XPATH, '//*[@id="product-grid"]/div[2]/section[2]/div[2]/div[1]/div[1]/button[2]/i')
amount_of_shoes = (By.CSS_SELECTOR, 'span[class="b-load_progress-value"]')
discount_color = (By.CSS_SELECTOR, 'span[class="b-price-item m-new"]')
button_four = (By. CSS_SELECTOR, 'button[data-value="4"]')
images_decrease = (By.XPATH, '//div[@class="l-plp_grid"]')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://www.nastygal.com/eu/')

    @property
    def all_cookies(self):
        return self.find_element(all_cookies)

    @property
    def check_discount(self):
        return self.find_element(check_discount)

    @property
    def account_button(self):
        return self.find_element(account_button)

    @property
    def cart_button(self):
        return self.find_element(cart_button)

    @property
    def search_button(self):
        return self.find_element(search_button)

    @property
    def search_field(self):
        return self.find_element(search_field)

    @property
    def no_result(self):
        return self.find_element(no_result)

    @property
    def jeans_result(self):
        return self.find_element(jeans_result)

    @property
    def cardigan(self):
        return self.find_element(cardigan)

    @property
    def choose_size_s(self):
        return self.find_element(choose_size_s)

    @property
    def add_to_cart(self):
        return self.find_element(add_to_bag)

    @property
    def view_bag(self):
        return self.find_element(view_bag)

    @property
    def add_to_wishlist(self):
        return self.find_element(add_to_wishlist)

    @property
    def alert_added(self):
        return self.find_element(alert_added)

    @property
    def wish_list(self):
        return self.find_element(wish_list)

    @property
    def jeans_in_wishlist(self):
        return self.find_element(jeans_in_wishlist)

    @property
    def select_size_in_wishlist(self):
        return self.find_element(select_size_wl)

    @property
    def button_select(self):
        return self.find_element(button_select_tap)

    @property
    def remove(self):
        return self.find_element(remove)

    @property
    def dialog(self):
        return self.find_element(dialog)

    @property
    def button_delete(self):
        return self.find_element(delete_button)

    @property
    def empty_text_in_wishlist(self):
        return self.find_element(empty_text)

    @property
    def black_shoes(self):
        return self.find_element(black_shoes)

    @property
    def shoes_size(self):
        return self.find_element(shoes_size)

    @property
    def shoes_add_to_wl(self):
        return self.find_element(shoes_to_add_to_wl)

    @property
    def shoes_add_to_wl_2(self):
        return self.find_element(shoes_to_add_to_wl_2)

    @property
    def amount_of_shoes(self):
        return self.find_element(amount_of_shoes)

    @property
    def discount_color(self):
        return self.find_element(discount_color)

    @property
    def button_four(self):
        return self.find_element(button_four)

    @property
    def images_decrease(self):
        return self.find_element(images_decrease)
