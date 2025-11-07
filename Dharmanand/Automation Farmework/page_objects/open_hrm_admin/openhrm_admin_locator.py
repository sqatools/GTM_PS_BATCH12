from selenium.webdriver.common.by import By


class AdminPageLoc:
    admin_link = (By.XPATH, "//span[text()='Admin']//parent::a")
    add_button = (By.XPATH, "//button[normalize-space()='Add']")
    user_role_dropdwn = (By.XPATH, "//label[text()='User Role']//parent::div//following-sibling::div//div[text()='-- Select --']")
    user_role_value = (By.XPATH, "//div[@role='listbox']//*[contains(text(), 'Admin')]")
    status_dropdwn = (By.XPATH, "//label[text()='Status']//parent::div//following-sibling::div//div[text()='-- Select --']")
    status_value = (By.XPATH, "//div[@role='listbox']//*[contains(text(), 'Enabled')]")

    password_field = (By.XPATH, "//label[text()='Password']//parent::div//following-sibling::div//input")
    confirm_pass_field = (By.XPATH, "//label[text()='Confirm Password']//parent::div//following-sibling::div//input")

    username_field = (By.XPATH, "//label[text()='Username']//parent::div//following-sibling::div//input")
    employee_name_field = (By.XPATH, "//label[text()='Employee Name']//parent::div//following-sibling::div//input")
    employee_name_value = (By.XPATH, "//div[@role='listbox']//*[contains(text(), 'Ravi M G')]")
    save_button = (By.XPATH, "//button[normalize-space()='Save']")

