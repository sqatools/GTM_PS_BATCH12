import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# It will maximize the browser window.
driver.maximize_window()

# set implicit wait for each web element
driver.implicitly_wait(10)

# launch facebook on browser
driver.get("https://www.facebook.com")

driver.implicitly_wait(10)

driver.find_element(By.XPATH,'//a[@href="/r.php?entry_point=login"]').click()

driver.find_element(By.XPATH, '//input[@aria-label="First name"]').send_keys("Sourbabh")

driver.find_element(By.XPATH,'//input[@aria-label="Last name"]').send_keys("savadat")

driver.find_element(By.XPATH,'//select[@name="birthday_month"]').send_keys("Oct")

driver.find_element(By.XPATH,'//select[@title="Day"]').send_keys("17")

driver.find_element(By.XPATH,'//select[@name="birthday_year"]').send_keys("1999")

driver.find_element(By.XPATH,'//input[@value="2"]').click()

driver.find_element(By.XPATH,'//input[@aria-label="Mobile number or email"]').send_keys("9892838469")

driver.find_element(By.XPATH,'//input[@autocomplete="new-password"]').send_keys("AbcXyz@123")

driver.find_element(By.XPATH,'//button[@name="websubmit"]').click()


time.sleep(10)
print(driver.title)
driver.close()
