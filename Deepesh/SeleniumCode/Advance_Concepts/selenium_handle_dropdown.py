import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Initiate chrome driver and launch the Chrome browser
driver = webdriver.Chrome()
# It will maximize the browser window.
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")


def select_dropdown_value_with_visible_text():
    element_select = driver.find_element(By.ID, "admorepass")
    select_var = Select(element_select)
    select_var.select_by_visible_text("Add 3 more passenger (200%)")
    time.sleep(5)

#select_dropdown_value_with_visible_text()


def select_dropdown_value_with_index_position():
    element_select = driver.find_element(By.ID, "admorepass")
    # take screenshot of the element
    element_select.screenshot("dropdown_image.png")
    select_var = Select(element_select)
    select_var.select_by_index(2)
    time.sleep(5)
    # take screenshot of entire page
    driver.save_screenshot("index_position.png")

select_dropdown_value_with_index_position()


def select_dropdown_data_with_optionn_value():
    element_select = driver.find_element(By.ID, "billing_country")
    # take screenshot of the element
    element_select.screenshot("country_dropdown_image.png")
    select_var = Select(element_select)
    select_var.select_by_value("AQ")
    time.sleep(5)
    # take screenshot of entire page
    driver.save_screenshot("country_value_position.png")

select_dropdown_data_with_optionn_value()