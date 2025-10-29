import time
import os
import pytest
from ...page_objects.open_hrm_login.openhrm_login_page import OpenHRMPage
from ...page_objects.open_hrm_admin.openhrm_admin_page import AdminPage
from ...page_objects.open_hrm_login.openhrm_data import *
from ...utilities.utils_tools import Utils


@pytest.mark.usefixtures("get_driver_instance")
class TestOpenHRM:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.hrm = OpenHRMPage(self.driver)
        self.ad = AdminPage(self.driver)
        self.util = Utils()
        file_path = os.path.join(os.getcwd(), "page_objects/open_hrm_admin/admin_data.json")
        self.admin_data = self.util.read_json_file(file_path)

    @pytest.mark.smoke
    def test_login_functionality_and_verify(self, request):
        self.hrm.log.info(f"---------- Test Name : {request.node.name} -----------")
        self.hrm.launch_url(url=url)
        self.hrm.login_on_openhrm(user=username, pass_word=password)
        time.sleep(5)

    # def test_add_user_in_admin(self):
    #     self.ad.navigate_admin_page()
    #     self.ad.add_new_user(user_role="Admin", status="Enabled", password="user123", conf_pass="user123",
    #                          username="Rahul MG", emp_name="Ravi M B")

    @pytest.mark.sanity
    def test_add_user_in_admin(self, request):
        self.hrm.log.info(f"---------- Test Name : {request.node.name} -----------")
        self.ad.navigate_admin_page()
        self.ad.add_new_user(user_role=self.admin_data['add_users']['user_role'],
                             status=self.admin_data['add_users']['user_status'],
                             password=self.admin_data['add_users']['password'],
                             conf_pass=self.admin_data['add_users']['conf_pass'],
                             username=self.admin_data['add_users']['username'],
                             emp_name=self.admin_data['add_users']['emp_name'])
        time.sleep(5)


