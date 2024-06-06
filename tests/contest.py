import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()  # Открываем браузер
    driver.maximize_window()
    yield driver
    driver.quit()