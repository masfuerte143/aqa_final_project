import allure

from base.data_tests import DataTests, ProjectPaths
from base.locators import CheckoutPageLocators
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    # Getters
    def get_checkout_h1(self):
        return self.driver.find_element(*CheckoutPageLocators.CHECKOUT_H1).text

    def get_ship_first_name(self):
        return self.driver.find_element(*CheckoutPageLocators.SHIP_FIRST_NAME).get_attribute(
            "value")

    def get_ship_last_name(self):
        return self.driver.find_element(*CheckoutPageLocators.SHIP_LAST_NAME).get_attribute(
            "value")

    def get_ship_address(self):
        return self.driver.find_element(*CheckoutPageLocators.SHIP_ADDRESS)

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

    # Actions amd Methods
    def checkout_assertion(self):
        """Проверка, что попали на нужную страницу"""
        assert self.get_checkout_h1() == "Оформление заказа", "Неудачный переход"

    @allure.step("Проверить корректность информации о пользователе")
    def check_correct_user_info(self):
        """Проверить корректность информации пльзователя"""
        self.checkout_assertion()
        assert self.get_ship_first_name() == DataTests.first_name, "Неверное имя"
        assert self.get_ship_last_name() == DataTests.last_name, "Неверная фамилия"
        assert self.get_ship_region() == DataTests.region, "Неверный регион"
        assert self.get_city() == DataTests.city, "Неверный город"

    @allure.step("Изменить способ доставки")
    def change_delivery(self):
        """Изменить способ доставки"""
        self.get_delivery_for_moscow().click()
        for_moscow_checked = self.get_delivery_for_moscow().get_attribute("checked")
        assert for_moscow_checked == "true", "Доставка не проставилась"

    @allure.step("Заполнить поле с адресом доставки")
    def fill_ship_address(self):
        """Заполнить поле с адресом доставки"""
        self.get_ship_address().send_keys(DataTests.ship_address)
        BasePage.take_screenshot(self, ProjectPaths.screens_path, action_name="AddressFilled")

    @allure.step("Изменить способ оплаты")
    def change_payment(self):
        """Изменить способ оплаты"""
        self.get_fact_pay().click()
        for_moscow_checked = self.get_fact_pay().get_attribute("checked")
        assert for_moscow_checked == "true", "Оплата не изменилась"

    @allure.step("Оставить комментарий к заказу")
    def input_comment(self):
        """Заполнить поле комментария"""
        self.get_comment_textarea().send_keys("Оставить у двери")
        BasePage.take_screenshot(self, ProjectPaths.screens_path, action_name="CommentFilled")

    @allure.step("Подтвердить заказ")
    def submit_order(self):
        """Подтвердить заказ"""
        self.get_submit_order_button().click()
