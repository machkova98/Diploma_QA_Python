from pages.home_page import HomePage
from selenium.webdriver.common.by import By


new_in_txt = (By.CSS_SELECTOR, 'h1[class="b-header_plp-title"]')
colour_button = (By.ID, 'searchRefineBarAccordionItemBtn-colour')
black_select = (By.ID, 'refinementAttributesListItem-colour-black')
trousers_image = (By.CSS_SELECTOR, 'a[data-pid="BGG10835"]')
clear_all_button = (By.CSS_SELECTOR, 'button[class="b-applied_filters-clear_all"]')
showing_number = (By.CSS_SELECTOR, 'span[class="b-load_progress-value"]')
sort = (By.ID, 'plp-sort-desktop')
brush = (By.LINK_TEXT, 'Nasty Gal Beauty Crease Brush')
read_more = (By.CSS_SELECTOR, 'span[class="b-more-button_text"]')
shop_by_fit = (By.ID, 'searchRefineBarAccordionItemBtn-shop-by-fit')
plus_size = (By.ID, 'refinementAttributesListItem-shop-by-fit-plus_size')
underwear = (By.CSS_SELECTOR, 'a[data-pid="BGG01090"]')
jeans = (By.CSS_SELECTOR, 'a[data-pid="AGG14092"]')


class ClothesPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def new_in_txt(self):
        return self.find_element(new_in_txt)

    @property
    def colour_button(self):
        return self.find_element(colour_button)

    @property
    def black_select(self):
        return self.find_element(black_select)

    @property
    def trousers_image(self):
        return self.find_element(trousers_image)

    @property
    def clear_all(self):
        return self.find_element(clear_all_button)

    @property
    def showing_number_of_orders(self):
        return self.find_element(showing_number)

    @property
    def sort(self):
        return self.find_element(sort)

    @property
    def brush(self):
        return self.find_element(brush)

    @property
    def read_more(self):
        return self.find_element(read_more)

    @property
    def shop_by_fit(self):
        return self.find_element(shop_by_fit)

    @property
    def plus_size(self):
        return self.find_element(plus_size)

    @property
    def underwear(self):
        return self.find_element(underwear)

    @property
    def jeans(self):
        return self.find_element(jeans)

