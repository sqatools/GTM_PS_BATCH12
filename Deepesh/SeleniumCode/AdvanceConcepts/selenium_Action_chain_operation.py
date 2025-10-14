import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Initiate chrome driver and launch the Chrome browser
driver = webdriver.Chrome()
# It will maximize the browser window.
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

action = ActionChains(driver)


def perform_hover_operation():
    tester_element = driver.find_element(By.XPATH, "//div[@id='menu']//a[contains(text(), 'Tester')]")
    action.move_to_element(tester_element).perform()
    time.sleep(3)

    demo_site_element = driver.find_element(By.XPATH, "//div[@id='menu']//span[contains(text(), 'Demo Testing Site')]")
    action.move_to_element(demo_site_element).perform()
    time.sleep(3)

    alerts_elem = driver.find_element(By.XPATH, "//div[@id='menu']//span[contains(text(), 'AlertBox')]")
    action.click(alerts_elem).perform()
    time.sleep(3)


perform_hover_operation()

