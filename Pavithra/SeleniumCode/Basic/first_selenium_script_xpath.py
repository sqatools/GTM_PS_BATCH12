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

driver.find_element(By.XPATH, "//*[@data-testid='royal-email']").send_keys("user1@gmail.com")
driver.find_element(By.XPATH, "//*[@data-testid='royal-pass']").send_keys("user@123456")
#driver.find_element(By.XPATH, "//*[@data-testid='royal-login-button']").click()

# click on create new account button
driver.find_element(By.XPATH, "//*[@data-testid='open-registration-form-button']").click()


# static wait as 10 sec
time.sleep(10)

# close browser
driver.close()
