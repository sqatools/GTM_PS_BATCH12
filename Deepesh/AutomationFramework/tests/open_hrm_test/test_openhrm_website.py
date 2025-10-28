import time

import pytest
from ...page_objects.open_hrm_login.openhrm_login_page import OpenHRMPage
from ...page_objects.open_hrm_admin.openhrm_admin_page import AdminPage
from ...page_objects.open_hrm_login.openhrm_data import *


@pytest.mark.usefixtures("get_driver_instance")
class TestOpenHRM:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.hrm = OpenHRMPage(self.driver)
        self.ad = AdminPage(self.driver)

    def test_login_functionality_and_verify(self):
        self.hrm.launch_url(url=url)
        self.hrm.login_on_openhrm(user=username, pass_word=password)
        time.sleep(5)

    def test_add_user_in_admin(self):
        self.ad.navigate_admin_page()
        self.ad.add_new_user(user_role="Admin", status="Enabled", password="user123", conf_pass="user123",
                             username="Rahul MG", emp_name="Ravi M B")


