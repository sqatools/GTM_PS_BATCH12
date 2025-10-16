import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as chrome_option
from selenium.webdriver.firefox.options import Options as firefox_option
from selenium.webdriver.edge.options import Options as edge_option
#
browser = "chrome"
driver = None
headless = False

# Initiate chrome driver and launch the Chrome browser
if browser.lower() == "chrome":
    opt = chrome_option()
    if headless:
        opt.add_argument("--headless")
    opt.add_argument("--disable-notification")
    opt.add_argument("--windows-size=1920*1080")
    #opt.add_argument("--incognito")
    opt.add_experimental_option("detach", True)
    pref_dict = {
        "download.default_directory" : "E:\\Trainings\\GTM_PS_Batch12_July25\\GTM_PS_BATCH12\\Deepesh\\SeleniumCode\\downloadFile",
        "download.prompt_for_download" : False,
        "safebrowsering.enabled" : True
    }
    opt.add_experimental_option("prefs", pref_dict)
    driver = webdriver.Chrome(options=opt)
elif browser.lower() == "firefox":
    opt = firefox_option()
    opt.add_argument("--headless")
    driver = webdriver.Firefox(options=opt)
elif browser.lower() == "edge":
    opt = edge_option()
    opt.add_argument("--headless")
    driver = webdriver.Edge()

# It will maximize the browser window.
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.facebook.com")
driver.save_screenshot("firefox_option.png")
time.sleep(5)

driver.get("https://www.python.org/downloads/windows/")
driver.find_element(By.XPATH, "//a[contains(@href,'python-3.13.9.exe')]").click()
time.sleep(20)

driver.close()