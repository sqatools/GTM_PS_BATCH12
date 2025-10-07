
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

driver.find_element(By.XPATH, '//input[@aria-label="First name"]').send_keys("vivek")

driver.find_element(By.XPATH,'//input[@aria-label="Surname"]').send_keys("gowda")

driver.find_element(By.XPATH,'//select[@name="birthday_month"]').send_keys("apr")

driver.find_element(By.XPATH,'//select[@title="Day"]').send_keys("25")

driver.find_element(By.XPATH,'//select[@name="birthday_year"]').send_keys("1995")

driver.find_element(By.XPATH,'//input[@value="2"]').click()

driver.find_element(By.XPATH,'//input[@aria-label="Mobile number or email address"]').send_keys("9741326742")

driver.find_element(By.XPATH,'//input[@aria-label="New password"]').send_keys("Vivek@123")

driver.find_element(By.XPATH,'//button[@name="websubmit"]').click()


time.sleep(10)
print(driver.title)
driver.close()
