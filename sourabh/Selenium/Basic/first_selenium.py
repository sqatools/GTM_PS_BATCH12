from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.chrome()
driver.maximize_window()
driver.implicitly.wait(10)

driver.get("http://facebook.com")
driver.find_element(By.NAME)
