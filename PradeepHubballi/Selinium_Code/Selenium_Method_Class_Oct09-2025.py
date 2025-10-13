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
driver.get ("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# get title of the website
print(driver.title)

# get current url

print("current",driver.current_url)

##username_field = driver.find_element(By.NAME, "username")
username_field = driver.find_element(By.NAME, "username")
print("Check element is displayed :",username_field.is_displayed())
print("check is element enabled:",username_field.is_enabled())

# clear existing data if something is available
username_field.clear()
# enter username value to the field
username_field.send_keys ("Admin")
# enter password value to password field
driver.find_element(By.NAME,"password").send_keys("admin123")
# click in login button
driver.find_element(By.XPATH, " //button[normalize-space()='Login']").click()

time.sleep(10)

# Get list of anchor tag value
list_of_links = driver.find_elements(By.XPATH, "//a")

# get each link value from list of links
for link in list_of_links:
    print(link.get_attribute("href"))
