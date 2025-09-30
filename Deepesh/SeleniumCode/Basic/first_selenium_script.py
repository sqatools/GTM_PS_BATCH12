"""
pip install selenium
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initiate chrome driver and launch the Chrome browser
driver = webdriver.Chrome()

# It will maximize the browser window.
driver.maximize_window()

# set implicit wait for each web element
driver.implicitly_wait(10)

# launch facebook on browser
driver.get("https://www.facebook.com")

# Find element with the property as NAME and provide user email and password.
driver.find_element(By.NAME, "email").send_keys("user1@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("P@ssw0rd")

# get webelement and click on login button
driver.find_element(By.NAME, "login").click()

# static wait as 10 sec
time.sleep(10)

# close browser
driver.close()
