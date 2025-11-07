import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("user_name, pass_word, status", [("Admin", "admin123", False),
                                                          ("Admin", "admin1234", True),
                                                          ("testuser", "admin123", True),
                                                          ("testuser", "admin1235", True)])
def test_login_hrm(user_name, pass_word, status):
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "username").send_keys(user_name)
    driver.find_element(By.NAME, "password").send_keys(pass_word)
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    try:
        error_status = driver.find_element(By.XPATH, "//p[text()='Invalid credentials']").is_displayed()
    except Exception as e:
        print(e)
        error_status = False
    assert error_status == status
    driver.close()
