import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# find_elements method provide list of element
element_list = driver.find_elements(By.XPATH, "//input[@value='checkbox']")
print(element_list)

for element in element_list:
    element.click()
    time.sleep(2)

# get all the city names from table
for i in range(2, 9):
    elem = driver.find_element(By.XPATH, f"//table[@id='cities']/tbody/tr[{i}]/td[3]")
    print(elem.text)
    time.sleep(1)


time.sleep(10)
driver.close()

# Automate Admin Page Action in this page
# https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser
