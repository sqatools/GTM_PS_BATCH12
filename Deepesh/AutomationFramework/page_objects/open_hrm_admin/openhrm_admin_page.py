from selenium.webdriver.common.by import By
from ...base.selenium_base import SeleniumBase
from .openhrm_admin_locator import AdminPageLoc


class AdminPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_admin_page(self):
        self.log.info("Navigate to admin page")
        self.click_element(AdminPageLoc.admin_link)

    def click_add_button(self):
        self.log.info("Navigate to add button")
        self.click_element(AdminPageLoc.add_button)

    def select_user_role(self, user_role):
        self.log.info(f"select user role: {user_role}")
        self.click_element(AdminPageLoc.user_role_dropdwn)
        user_role_value = (By.XPATH, f"//div[@role='listbox']//*[contains(text(), '{user_role}')]")
        self.click_element(user_role_value)

    def select_user_status(self, user_status):
        self.log.info(f"select user status: {user_status}")
        self.click_element(AdminPageLoc.status_dropdwn)
        user_status_value = (By.XPATH, f"//div[@role='listbox']//*[contains(text(), '{user_status}')]")
        self.click_element(user_status_value)

    def enter_password(self, password):
        self.log.info(f"enter user password: {password}")
        self.enter_text(AdminPageLoc.password_field, value=password)

    def enter_confirm_password(self, confirm_pass):
        self.log.info(f"enter confirm password: {confirm_pass}")
        self.enter_text(AdminPageLoc.confirm_pass_field, value=confirm_pass)

    def enter_username(self, username):
        self.log.info(f"enter username: {username}")
        self.enter_text(AdminPageLoc.username_field, value=username)

    def select_employee_name(self, emp_name):
        self.log.info(f"select employee name: {emp_name}")
        self.enter_text(AdminPageLoc.employee_name_field, value=emp_name)
        employee_name_value = (By.XPATH, f"//div[@role='listbox']//*[contains(text(), '{emp_name}')]")
        self.click_element(employee_name_value)

    def click_save_button(self):
        self.log.info(f"click to save button")
        self.click_element(AdminPageLoc.save_button)

    def add_new_user(self, user_role, status, password, conf_pass, username, emp_name):
        self.click_add_button()
        self.select_user_role(user_role)
        self.select_user_status(status)
        self.enter_password(password)
        self.enter_confirm_password(conf_pass)
        self.enter_username(username)
        self.select_employee_name(emp_name)
        self.click_save_button()
