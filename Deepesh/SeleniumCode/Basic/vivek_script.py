import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# It will maximize the browser window.
driver.maximize_window()

# set implicit wait for each web element
driver.implicitly_wait(10)

# launch orangehrm.com on browser
driver.get("https://www.orangehrm.com/en/30-day-free-trial#")

driver.implicitly_wait(10)

#driver.find_element(By.XPATH,'//a[@href="/r.php?entry_point=login"]').click()

driver.find_element(By.XPATH, '//input[@name="subdomain"]').send_keys("vi560vek")

driver.find_element(By.XPATH,'//input[@id="Form_getForm_Name"]').send_keys("gowdavivek")

driver.find_element(By.XPATH,'//input[@class="email text"]').send_keys("viv@gmail.com")

##driver.find_element(By.XPATH,'//select[@title="Day"]').send_keys("25")

driver.find_element(By.XPATH,'//input[@placeholder="Phone Number*"]').send_keys("9741326742")
driver.find_element(By.XPATH,'//select[@name="Country"]').send_keys("India")

#driver.find_element(By.XPATH,'//label[@id="recaptcha-anchor-label"]').click()
driver.find_element(By.XPATH, '//input[name="action_submitForm")]').click()
driver.find_element(By.LINK_TEXT,'//a[@href="/en/pricing"]').click()
time.sleep(10)
print(driver.title)
driver.close()