

#####
##//input[@data-testid='royal-email']     or //*[@data-testid='royal-email']


##//input[@data-testid='royal-pass']   or  //*[@data-testid='royal-pass']


"""
pip install selenium
"""
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
driver.get("https://www.facebook.com")

driver.find_element(By.XPATH, "//*[@data-testid='royal-email']").send_keys("user1@gmail.com")
driver.find_element(By.XPATH, "//*[@data-testid='royal-pass']").send_keys("user@123456")
#driver.find_element(By.XPATH, "//*[@data-testid='royal-login-button']").click()

# click on create new account button
driver.find_element(By.XPATH, "//*[@data-testid='open-registration-form-button']").click()

#  Signup First Name
driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Pradeep")

# Signup Last Name
driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Hubballi")
##//input[@name="firstname"]
##//input[@name="lastname"]
##//*[@name="birthday_day"]


#
driver.find_element(By.XPATH, "//*[@name='birthday_day']").send_keys("06")
##birthday_month
driver.find_element(By.XPATH, "//*[@name='birthday_month']").send_keys("JUNE")

driver.find_element(By.XPATH, "//*[@name='birthday_year']").send_keys("1987")

driver.find_element(By.XPATH, "//input[@ value='2']").click()
#//input[@ value="2"]

driver.find_element(By.XPATH, "//*[@name='reg_email__']").send_keys("Pradeep.h147@gmail.com")


driver.find_element(By.XPATH, "//*[@data-type='password']").send_keys("4564564oip")
##//*[@name='reg_email__']
#//*[@data-type="password"]


# static wait as 10 sec
time.sleep(10)

# close browser
driver.close()