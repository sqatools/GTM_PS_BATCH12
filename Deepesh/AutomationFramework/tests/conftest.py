import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ..session_data import headless_execution


@pytest.fixture(scope="class")
def get_driver_instance(request):
    opt = Options()
    if headless_execution:
        opt.add_argument("--headless")
    driver = webdriver.Chrome(options=opt)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
