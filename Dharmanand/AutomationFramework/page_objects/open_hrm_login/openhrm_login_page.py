from ...base.selenium_base import SeleniumBase
from .openhrm_login_locators import *


class OpenHRMPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_url(self, url):
        self.driver.get(url)

    def enter_username(self, username_value):
        self.enter_text(locator=username_field, value=username_value)

    def enter_password(self, password_value):
        self.enter_text(locator=password_field, value=password_value)

    def click_login_button(self):
        self.click_element(locator=login_button)

    def login_on_openhrm(self, user, pass_word):
        self.enter_username(user)
        self.enter_password(pass_word)
        self.click_login_button()
