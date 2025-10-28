from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class SeleniumBase:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def get_element(self, locator, cond=ec.presence_of_element_located):
        element = self.wait.until(cond(locator))
        return element

    def click_element(self, locator, **kwargs):
        element = self.get_element(locator, **kwargs)
        element.click()

    def enter_text(self, locator, value, **kwargs):
        element = self.get_element(locator, **kwargs)
        element.send_keys(value)

    def get_text(self, locator, **kwargs):
        element = self.get_element(locator, **kwargs)
        return element.text

    def select_dropdown_value(self,  locator, value, **kwargs):
        element = self.get_element(locator, **kwargs)
        select = Select(element)
        select.select_by_visible_text(value)

    def get_elements_list(self, locator, cond=ec.presence_of_all_elements_located):
        elem_list = self.wait.until(cond(locator))
        return elem_list





