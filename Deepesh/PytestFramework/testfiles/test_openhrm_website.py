import time

import pytest
from page_class import OpenHRMPage


@pytest.mark.usefixtures("get_driver_instance")
class TestOpenHRM:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.hrm = OpenHRMPage(self.driver)

    def test_login_functionality_and_verify(self):
        self.hrm.launch_url(url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.hrm.login_on_openhrm(user="Admin", pass_word="admin123")
        time.sleep(5)
