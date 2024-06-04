import time

from selenium.webdriver.common.by import By

from base.locators import CheckoutPageLocators
from pages.base_page import BasePage
from pages.registration_page import RegistrationPage


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Геттеры
    def get_ship_first_name(self):
        return self.driver.find_element(*CheckoutPageLocators.SHIP_FIRST_NAME).get_attribute(
            "value")

    def get_ship_last_name(self):
        return self.driver.find_element(*CheckoutPageLocators.SHIP_LAST_NAME).get_attribute(
            "value")

    def get_ship_region(self):
        return self.driver.find_element(*CheckoutPageLocators.SHIP_REGION).text

    def get_city(self):
        return self.driver.find_element(*CheckoutPageLocators.SHIP_CITY).get_attribute("value")

    def get_delivery_for_moscow(self):
        return self.driver.find_element(*CheckoutPageLocators.MSK_DELIVERY)

    def get_fact_pay(self):
        return self.driver.find_element(*CheckoutPageLocators.FACT_PAY)

    def get_comment_textarea(self):
        return self.driver.find_element(*CheckoutPageLocators.COMMENT_FIELD)

    def get_submit_order_button(self):
        return self.driver.find_element(*CheckoutPageLocators.SUBMIT_ORDER_BUTTON)

    # Дейсвтия
    def check_correct_user_info(self):
        rp = RegistrationPage(self.driver)
        assert self.get_ship_first_name() == BasePage.first_name, "Неверное имя"
        assert self.get_ship_last_name() == BasePage.last_name, "Неверная фамилия"
        assert self.get_ship_region() == rp.get_region_moscow().text, "Неверный регион"
        assert self.get_city() == BasePage.city_text, "Неверный город"

    def change_delivery(self):
        self.get_delivery_for_moscow().click()
        for_moscow_checked = self.get_delivery_for_moscow().get_attribute("checked")
        assert for_moscow_checked == "true", "Доставка не проставилась"

    def change_payment(self):
        self.get_fact_pay().click()
        for_moscow_checked = self.get_fact_pay().get_attribute("checked")
        assert for_moscow_checked == "true", "Оплата не изменилась"

    def input_comment(self):
        self.get_comment_textarea().send_keys("Оставить у двери")

    def submit_order(self):
        self.get_submit_order_button().click()
