import time
from selenium import webdriver
from selenium.webdriver.common.by import By


Browser = "chrome"

driver = None

if Browser.lower() == "chrome":
    driver = webdriver.Chrome()
elif Browser.lower() == "firefox":
    driver = webdriver.Firefox()
elif Browser.lower() == "edge":
    driver = webdriver.Edge()

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.facebook.com")

time.sleep(5)