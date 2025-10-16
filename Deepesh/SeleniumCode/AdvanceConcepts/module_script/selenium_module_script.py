import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

def get_element(locator):
    element = wait.until(ec.element_to_be_clickable(locator))
    return element


get_element(locator=(By.NAME,"username")).send_keys("Admin")
get_element(locator=(By.NAME, "password")).send_keys("admin123")
get_element(locator=(By.XPATH, "//button[normalize-space()='Login'] ")).click()

time.sleep(10)
driver.close()