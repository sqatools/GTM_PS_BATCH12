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


driver.find_element(By.NAME, "firstname").send_keys("vivek")
driver.find_element(By.NAME, "lastname").send_keys("rock")
driver.find_element(By.NAME, "reg_email__").send_keys("vivekrock.com")
driver.find_element(By.NAME, "reg_passwd__").send_keys("Vivek@123")


driver.find_element(By.ID, "month").send_keys("apr")
driver.find_element(By.ID, "day").send_keys("25")
driver.find_element(By.ID, "year").send_keys("1993")

time.sleep(5)

driver.find_element(By.NAME, "websubmit").click()

time.sleep(20)

driver.close()
