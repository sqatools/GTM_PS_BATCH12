import time

from selenium import webdriver

from selenium.webdriver.common.by import By

Browser= "Chrome"
driver = None
if Browser.lower() == "chrome":
    driver= webdriver.Chrome()
elif Browser.lower() == "firefox":
    driver= webdriver.Firefox()
elif Browser.lower() == "edge":
    driver= webdriver.Edge()

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http:/www.facebook.com")
driver.find_element(By.NAME, "email").send_keys("user1@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("P@ssw0rd")
driver.find_element(By.NAME, "login").click()

