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

URL = driver.execute_script("return document.URL;")
print("URL :", URL)

title = driver.execute_script("return document.title")
print("Title value :", title)

dob_elem = driver.execute_script("return document.getElementById('birthday');")
dob_elem.send_keys("02/01/2025")


one_way_elem = driver.execute_script("return document.getElementById('oneway');")
one_way_elem.click()

time.sleep(5)

driver.close()
