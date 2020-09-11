import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
@pytest.fixture(params=["chrome"],scope="class")
def init_driver(request):
    if request.param=="chrome":
        web_driver = webdriver.Chrome()
    elif request.param == "firefox":
        web_driver = webdriver.Firefox()
    web_driver.maximize_window()
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
