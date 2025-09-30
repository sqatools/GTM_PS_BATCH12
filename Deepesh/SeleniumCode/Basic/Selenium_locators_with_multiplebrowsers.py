"""
pip install selenium
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initiate chrome driver and launch the Chrome browser
Browser = "Chrome"
driver = None
if Browser.lower() == "chrome":
    driver = webdriver.Chrome()
elif Browser.lower() == "firefox":
    driver = webdriver.Firefox()
elif Browser.lower() == "edge":
    webdriver = webdriver.Edge()


driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.facebook.com")
"""
   Selenium Locators:
   
    -> ID = "id"
    XPATH = "xpath"
    -> LINK_TEXT = "link text"
    -> PARTIAL_LINK_TEXT = "partial link text"
    -> NAME = "name"
    -> TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
"""

# Get Element with ID and NAME locator
driver.find_element(By.ID, "email").send_keys("user1@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("user@12345")

# Get element with LINK text locator
driver.find_element(By.LINK_TEXT, "Create new account").click()

# Get element with the help PARTIAL LINK text locator
driver.find_element(By.PARTIAL_LINK_TEXT, "Already have").click()

# Get element with the help TAGNAME locator
elem = driver.find_element(By.TAG_NAME, "img")
print("Image attribute value :", elem.get_attribute("alt"))



time.sleep(10)
driver.close()

# Home work
# Automate facebook login page and signup.












time.sleep(5)