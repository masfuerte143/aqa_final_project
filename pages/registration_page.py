import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    region_text = ""
    # Геттеры
    def get_first_name_filed(self):
        return self.driver.find_element(By.XPATH, "//input[@id='register_firstname']")

    def get_last_name_filed(self):
        return self.driver.find_element(By.XPATH, "//input[@id='register_lastname']")

    def get_email_filed(self):
        return self.driver.find_element(By.XPATH, "//input[@id='register_email']")

    def get_phone_filed(self):
        return self.driver.find_element(By.XPATH, "//input[@id='register_telephone']")

    def get_password_filed(self):
        return self.driver.find_element(By.XPATH, "//input[@id='register_password']")

    def get_confirm_password_filed(self):
        return self.driver.find_element(By.XPATH, "//input[@id='register_confirm_password']")

    def get_region_selector(self):
        return self.driver.find_element(By.XPATH, "//select[@id='register_zone_id']")

    def get_region_moscow(self):
        return self.driver.find_element(By.XPATH, "//option[@value='2761']")

    def get_city_field(self):
        return self.driver.find_element(By.XPATH, "//input[@id='register_city']")

    def get_subscription_no(self):
        return self.driver.find_element(By.XPATH, "//input[@id='register_newsletter_1']")

    def get_registration_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#simpleregister_button_confirm")

    def get_registration_successful_h1(self):
        return WebDriverWait(self.driver, 60).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='content']/p")))

    # Действия!!!!!!!!!!!!!!!!!!!!
    def fill_required_fields(self):
        """Заполнить обязательные поля"""
        global region_text
        self.get_first_name_filed().send_keys(BasePage.first_name)
        self.get_last_name_filed().send_keys(BasePage.last_name)
        self.get_email_filed().send_keys(BasePage.email)
        self.get_phone_filed().send_keys(BasePage.phone)
        self.get_password_filed().send_keys(BasePage.password)
        self.get_confirm_password_filed().send_keys(BasePage.password)
        self.get_region_selector().click()
        self.get_region_moscow().click()
        region_text = self.get_region_moscow().text
        self.get_city_field().send_keys(BasePage.city_text)
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
