from pages.home_page import HomePage
from selenium.webdriver.common.by import By


log_in_text = (By.CSS_SELECTOR, 'h1[class="l-service-title"]')
email_field = (By.ID, 'dwfrm_login_email')
passwd_field = (By.ID, 'dwfrm_login_password')
log_in_button = (By.CSS_SELECTOR, 'button[type="submit"]')
error = (By.ID, 'dwfrm_login_email-error')


class LoginPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def log_in_text(self):
        return self.find_element(log_in_text)

    @property
    def email_field(self):
        return self.find_element(email_field)

    @property
    def passwd_field(self):
        return self.find_element(passwd_field)

    @property
    def log_in_button(self):
        return self.find_element(log_in_button)

    @property
    def error(self):
        return self.find_element(error)

