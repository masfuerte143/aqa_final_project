import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.data_tests import DataTests
from base.locators import RegistrationPageLocators
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Геттеры
    def get_first_name_filed(self):
        return self.driver.find_element(*RegistrationPageLocators.FIRST_NAME_FIELD)

    def get_last_name_filed(self):
        return self.driver.find_element(*RegistrationPageLocators.LAST_NAME_FIELD)

    def get_email_filed(self):
        return self.driver.find_element(*RegistrationPageLocators.EMAIL_FIELD)

    def get_phone_filed(self):
        return self.driver.find_element(*RegistrationPageLocators.PHONE_FIELD)

    def get_password_filed(self):
        return self.driver.find_element(*RegistrationPageLocators.PASS_FIELD)

    def get_confirm_password_filed(self):
        return self.driver.find_element(*RegistrationPageLocators.CONFIRM_PASS_FIELD)

    def get_region_selector(self):
        return self.driver.find_element(*RegistrationPageLocators.REGION_SELECTOR)

    def get_region_moscow(self):
        return self.driver.find_element(*RegistrationPageLocators.MOSCOW_IN_SELECTOR)

    def get_city_field(self):
        return self.driver.find_element(*RegistrationPageLocators.CITY_FIELD)

    def get_subscription_no(self):
        return self.driver.find_element(*RegistrationPageLocators.NO_SUBCR_RADIO)

    def get_registration_button(self):
        return self.driver.find_element(*RegistrationPageLocators.REGISTRATION_BUTTON)

    def get_registration_successful_h1(self):
        return WebDriverWait(self.driver, 60).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_SUCCESSFUL))

    # Действия
    def fill_required_fields(self):
        """Заполнить обязательные поля"""
        global region_text
        self.get_first_name_filed().send_keys(DataTests.first_name)
        self.get_last_name_filed().send_keys(DataTests.last_name)
        self.get_email_filed().send_keys(DataTests.email)
        self.get_phone_filed().send_keys(DataTests.phone)
        self.get_password_filed().send_keys(DataTests.password)
        self.get_confirm_password_filed().send_keys(DataTests.password)
        self.get_region_selector().click()
        self.get_region_moscow().click()
        region_text = self.get_region_moscow().text
        self.get_city_field().send_keys(DataTests.city_text)
        self.get_subscription_no().click()
        return region_text

    def click_registration_button(self):
        """Нажать на кнопку регистрации"""
        self.driver.execute_script('window.scroll(0,400)')
        action = ActionChains(self.driver)
        action.move_to_element(self.get_registration_button()).perform()
        self.get_registration_button().click()

    def check_registration_successful(self):
        """Проверить, что регистрация прошла успешно"""
        assert self.get_registration_successful_h1().text == "Поздравляем! Ваш Личный Кабинет был успешно создан.", \
            "Неуспешная регистрация"
        time.sleep(15)

    def registration(self):
        """Зарегистрироваться"""
        self.click_login_button()
        self.click_registration()
        self.fill_required_fields()
        self.click_registration_button()
        self.check_registration_successful()
