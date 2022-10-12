from pages.home_page import HomePage
from selenium.webdriver.common.by import By


cart_empty = (By.CSS_SELECTOR, 'h2[class="b-cart_empty-title"]')
blazer_and_skirt = (By.XPATH, '//*[@class="b-top_category-picture_image"]')
shop_new_in = (By.CSS_SELECTOR, 'figure[class="b-top_category-figure"]')
cardigan_in_cart = (By.CSS_SELECTOR, 'tbody[class="l-cart_product-body"]')
edit_in_cart = (By.CSS_SELECTOR, 'button[title="Edit"]')
select_bigger = (By.CSS_SELECTOR, 'select[id="attribute-f5b66cf39ae8622dda69044229-size"')
update_button = (By.CSS_SELECTOR, 'button[class="b-product_update-button_update b-button m-small"]')
rose_color = (By.CSS_SELECTOR, 'span[data-tau-size-id="50"]')
checkout = (By.XPATH, '//*[@id="maincontent"]/div/div[1]/div/div/div[4]/aside/div[1]/section[2]/div[1]/a')
secure = (By.CSS_SELECTOR, 'h1[class="l-checkout_login-title b-checkout_title m-centered"]')
remove_button = (By.CSS_SELECTOR, 'button[title="Remove"]')
cart_empty_delete = (By.CSS_SELECTOR, 'h1[class="b-header_cart-title"]')


class CartPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def cart_empty(self):
        return self.find_element(cart_empty)

    @property
    def blazer_and_skirt_width(self):
        return self.find_element(blazer_and_skirt)

    @property
    def shop_new_in(self):
        return self.find_element(shop_new_in)

    @property
    def cardigan_in_cart(self):
        return self.find_element(cardigan_in_cart)

    @property
    def edit_in_cart(self):
        return self.find_element(edit_in_cart)

    @property
    def select_bigger_cardigan(self):
        return self.find_element(select_bigger)

    @property
    def update_cart(self):
        return self.find_element(update_button)

    @property
    def cardigan_size(self):
        return self.find_element(rose_color)

    @property
    def checkout(self):
        return self.find_element(checkout)

    @property
    def secure(self):
        return self.find_element(secure)

    @property
    def remove_button(self):
        return self.find_element(remove_button)

    @property
    def cart_empty_after_remove(self):
        return self.find_element(cart_empty_delete)


