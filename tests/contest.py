import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup():
    """Открывать браузер при выполнении теста"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    """Закрывать браузер при выполнении теста"""
    driver.quit()
