import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]').click()

Link_of_page= driver.find_elements(By.XPATH,"//a")

for link in Link_of_page:
    print(link.get_attribute("href"))

driver.find_element(By.XPATH,"//span[text()='Admin']").click()
time.sleep(3)

driver.back()
time.sleep(3)

driver.forward()
time.sleep(3)


driver.refresh()
time.sleep(3)



driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")







time.sleep(5)
driver.quit()
