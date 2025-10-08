import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# class css selector
heading = driver.find_element(By.CSS_SELECTOR, ".post-title.entry-title")
print(heading.text)

# ID css selector
driver.find_element(By.CSS_SELECTOR, "#birthday").send_keys("10/8/2025")
driver.find_element(By.CSS_SELECTOR, "#male").click()

# Attribute CSS selector
driver.find_element(By.CSS_SELECTOR, "input[id='oneway']").click()
driver.find_element(By.CSS_SELECTOR, "div>input[id='billing_name']").send_keys("Mumbai, Boriwali")




time.sleep(10)
driver.close()
