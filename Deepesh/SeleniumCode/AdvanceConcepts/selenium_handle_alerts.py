import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# Initiate chrome driver and launch the Chrome browser
driver = webdriver.Chrome()
# It will maximize the browser window.
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")


def handle_alert_message():

    btn = driver.find_element(By.ID, "btnShowMsg")
    btn.click()
    time.sleep(3)
    # create object of the alert class
    var_alert = Alert(driver)
    # get alert message
    print(var_alert.text)
    var_alert.accept()
    time.sleep(5)


# handle_alert_message()

def handle_confirm_box():
    btn = driver.find_element(By.ID, "button")
    btn.click()
    time.sleep(3)
    # create object of the alert class
    var_alert = Alert(driver)
    # get alert message
    print(var_alert.text)

    # accept the alert
    var_alert.accept()

    ui_msg = driver.find_element(By.ID, "demo")
    print(ui_msg.text)
    assert ui_msg.text == "You pressed OK!"

    ###################### dismiss the alert #######################

    btn = driver.find_element(By.ID, "button")
    btn.click()
    time.sleep(3)
    # create object of the alert class
    var_alert = Alert(driver)
    # get alert message
    print(var_alert.text)

    # dismiss the alert
    var_alert.dismiss()
    ui_msg2 = driver.find_element(By.ID, "demo")
    print(ui_msg2.text)
    assert ui_msg2.text == "You pressed Cancel!"


# handle_confirm_box()

def handle_input_box():
    btn = driver.find_element(By.ID, "promptbtn")
    btn.click()
    time.sleep(3)
    # create object of the alert class
    var_alert = Alert(driver)
    # get alert message
    print(var_alert.text)

    var_alert.send_keys("SQATools")
    time.sleep(2)
    var_alert.accept()

    ui_msg = driver.find_element(By.ID, "prompt")
    print(ui_msg.text)

    assert ui_msg.text == "Hello SQATools! How are you today?"


handle_input_box()



