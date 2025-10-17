import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)


def get_element(locator, condition=ec.element_to_be_clickable):
    element = wait.until(condition(locator))
    return element


def click_element(locator, **kwargs):
    get_element(locator=locator, **kwargs).click()


def enter_text(locator, value, **kwargs):
    get_element(locator=locator, **kwargs).send_keys(value)


def get_text(locator, **kwargs):
    return get_element(locator=locator, **kwargs).text


def automate_open_source_website():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    get_element(locator=(By.NAME, "username"), condition=ec.visibility_of_element_located).send_keys("Admin")
    get_element(locator=(By.NAME, "password"), condition=ec.visibility_of_element_located).send_keys("admin123")
    get_element(locator=(By.XPATH, "//button[normalize-space()='Login'] ")).click()
    time.sleep(5)
    get_element(locator=(By.XPATH, "//span[text()='Admin']")).click()
    get_element(locator=(By.XPATH, "//button[normalize-space()='Add']")).click()

    get_element(locator=(By.XPATH, "//label[text()='User Role']//parent::div//following-sibling::div/div")).click()
    get_element(locator=(By.XPATH, "//div[@role='listbox']//*[contains(text(), 'ESS')]")).click()

    get_element(locator=(By.XPATH, "//label[text()='Status']//parent::div//following-sibling::div/div")).click()
    get_element(locator=(By.XPATH, "//div[@role='listbox']//*[contains(text(), 'Enabled')]")).click()

    get_element(locator=(By.XPATH, "(//input[@type='password'])[1]")).send_keys("user123")
    get_element(locator=(By.XPATH, "(//input[@type='password'])[2]")).send_keys("user123")
    get_element(locator=(By.XPATH, "//input[@placeholder='Type for hints...']")).send_keys("Ravi")
    get_element(locator=(By.XPATH, "//*[contains(text(), 'Ravi M B')]")).click()
    get_element(locator=(By.XPATH, "//label[text()='Username']//parent::div//following-sibling::div/input")).send_keys(
        "User2025")
    time.sleep(5)
    get_element(locator=(By.XPATH, "//button[normalize-space()='Save']")).click()
    time.sleep(5)


def automate_nse_website():
    driver.get("https://www.nseindia.com/")
    time.sleep(10)
    stock_traded = get_text(locator=(By.XPATH, "//a[contains(@href, 'stocks-traded')]"))
    print("Today's stock traded :", stock_traded)

    advance = get_text(locator=(By.XPATH, "//p[text()='Advances']//following-sibling::h3/a"))
    print("Advances :", advance)

automate_nse_website()

driver.close()
