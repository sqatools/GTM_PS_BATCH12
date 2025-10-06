"""
pip install selenium
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/r.php?entry_point=login")


driver.find_element(By.NAME, "firstname").send_keys("Sourabh")
driver.find_element(By.NAME, "lastname").send_keys("Savadatti")
driver.find_element(By.NAME, "reg_email__").send_keys("sourabh@example.com")
driver.find_element(By.NAME, "reg_passwd__").send_keys("Password@123")


driver.find_element(By.ID, "month").send_keys("Jan")
driver.find_element(By.ID, "day").send_keys("1")
driver.find_element(By.ID, "year").send_keys("1995")

time.sleep(5)

driver.find_element(By.NAME, "websubmit").click()

time.sleep(10)

driver.close()
