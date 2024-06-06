import pytest
from selenium import webdriver

from base.data_tests import Links


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()  # Открываем браузер
    driver.maximize_window()
    yield driver
    driver.quit()
