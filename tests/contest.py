import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup():
    """Открывать браузер при выполнении теста и закрывать в завершение"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
