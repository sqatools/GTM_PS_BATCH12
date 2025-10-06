import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://facebook.com")
#driver.find_element(By.)
input("Press Enter to close...")