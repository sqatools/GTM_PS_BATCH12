import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Initiate chrome driver and launch the Chrome browser
driver = webdriver.Chrome()
# It will maximize the browser window.
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")


# click on any link
driver.find_element(By.LINK_TEXT, "Software Testing Principles").click()

# get list of browsers tabs
browser_tabs = driver.window_handles

# navigate to new tab
driver.switch_to.window(browser_tabs[1])

# get all the sub topics heading.
print(driver.title)
topics_heading = driver.find_elements(By.XPATH, "//h3/span")

for topic in topics_heading:
    print(topic.text)


time.sleep(5)
# close new tab
driver.close()
time.sleep(5)


# switch to original tab
driver.switch_to.window(browser_tabs[0])

# Go to new page
driver.find_element(By.LINK_TEXT, "Robot Framework").click()

driver.save_screenshot("robotframework_page.png")




