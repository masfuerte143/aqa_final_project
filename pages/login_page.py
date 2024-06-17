import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.data_tests import DataTests
from base.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Getters
    def get_email_field(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD))

    def get_pass_filed(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(LoginPageLocators.PASS_FIELD))

    def get_submit_button(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(LoginPageLocators.SUBMIT_BUTTON))

    # Actions and Methods
    def fill_email(self):
        """Заполнить имейл"""
        self.get_email_field().send_keys(DataTests.email)

    def fill_pass(self):
        """Заполнить пароль"""
        self.get_pass_filed().send_keys(DataTests.password)

    def submit_click(self):
        """Кликнуть войти"""
        self.get_submit_button().click()
        self.driver.refresh()

    @allure.step("Авторизоваться в личном кабинете")
    def login(self):
        """Залогиниться по тестовым данным"""
        self.go_to_login()
        self.fill_email()
        self.fill_pass()
        self.submit_click()
        self.check_login_successfully()
