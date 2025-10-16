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


#perform_hover_operation()

def drag_and_drop_operation():
    frame_elem = driver.find_element(By.XPATH, "//iframe[contains(@src, 'photo-manager')]")
    driver.switch_to.frame(frame_elem)

    image1_elem = driver.find_element(By.XPATH, "//h5[text()='High Tatras']//parent::li")
    trash_elem = driver.find_element(By.ID, "trash")
    action.drag_and_drop(image1_elem,  trash_elem).perform()

    time.sleep(5)
    # get list of images and perform drag and drop operation one by one
    images_list = driver.find_elements(By.XPATH, "//h5[contains(text(), 'High Tatras')]//parent::li")
    for image_ele in images_list:
        trash_elem = driver.find_element(By.ID, "trash")
        action.drag_and_drop(image_ele, trash_elem).perform()
        time.sleep(2)


#drag_and_drop_operation()

def scroll_to_element():
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    home_link_element = driver.find_element(By.XPATH, "//a[@class='home-link']")
    action.scroll_to_element(home_link_element).perform()
    time.sleep(5)
    home_link_element.screenshot("home_link.png")
    action.click(home_link_element).perform()

scroll_to_element()




