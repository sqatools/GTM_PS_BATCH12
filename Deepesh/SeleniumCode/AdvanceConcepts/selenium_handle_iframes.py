import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initiate chrome driver and launch the Chrome browser
driver = webdriver.Chrome()
# It will maximize the browser window.
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")


def get_heading_outside_of_iframe():
    heading = driver.find_element(By.XPATH, "//div[@class='page_heading']/h1")
    print(heading.text)  # Frames And Windows


def get_heading_inside_of_iframe():
    iframe_elem = driver.find_element(By.NAME, "globalSqa")
    # switch to iframe
    driver.switch_to.frame(iframe_elem)
    #driver.switch_to.frame(driver.find_element(By.NAME, "globalSqa"))

    # Get heading from inside the iframe
    heading = driver.find_element(By.XPATH, "//div[@class='page_heading']/h1")
    print(heading.text)


get_heading_outside_of_iframe()
get_heading_inside_of_iframe()
