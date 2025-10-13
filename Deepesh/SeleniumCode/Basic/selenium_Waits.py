"""
1. implicit wait :  implicit wait applies on all the web element once it initialize
2. explicit wait :  explicit wait applies on specific element.
3. fluent wait :  This part of explicit wait, where web driver will set a polling frequency for any of the element
4. static wait :  This is hard coded sleep, where driver has to wait without any condition.
                  e.g.   time.sleep(20)
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Initiate chrome driver and launch the Chrome browser
driver = webdriver.Chrome()
# It will maximize the browser window.
driver.maximize_window()


def implicit_wait_example():
    # set implicit wait for each web element
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    t1 = time.time()

    try:
         element = driver.find_element(By.NAME, "username1")
         element.send_keys("Admin")
    except Exception as e:
         print(e)

    t2 = time.time()
    print("total time taken :", t2-t1)

#implicit_wait_example()



def explicit_wait_example():
    # set explicit wait
    wait = WebDriverWait(driver=driver, timeout=10, poll_frequency=2)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    t1 = time.time()
    try:
         user_name = wait.until(ec.element_to_be_clickable((By.NAME, "username1")))
         user_name.send_keys("Admin")
    except Exception as e:
         print(e)

    t2 = time.time()
    print("total time :", t2-t1)

explicit_wait_example()