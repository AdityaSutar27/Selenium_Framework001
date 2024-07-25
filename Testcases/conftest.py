
import pytest
from selenium import webdriver

@pytest.fixture
def setup(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.get("https://www.demoblaze.com/")
    request.cls.driver.maximize_window()
    yield
    request.cls.driver.quit()