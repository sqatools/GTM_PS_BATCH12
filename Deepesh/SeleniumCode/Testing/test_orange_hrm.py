from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
import allure
import pytest

@allure.severity(allure.severity_level.NORMAL)
class TestHRM:

    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen", attachment_type=AttachmentType.PNG)
        status = self.driver.find_element(By.XPATH, "//div[@alt='company-branding']").is_displayed()
        if status:
            assert True

        else:
            assert False
        self.driver.close()

    def test_list_employee(self):
        pytest.skip('Skipping test.. Later I will implement')

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        title = self.driver.title
        if title == "OrangeHRM":
            print("This is correct title")
        else:
            pytest.fail()

        self.driver.close()

