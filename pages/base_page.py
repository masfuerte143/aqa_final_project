from selenium.webdriver import ActionChains

from base.locators import BasePageLocators


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    # Геттеры

    def get_login_button(self):
        return self.driver.find_element(*BasePageLocators.LOGIN_BUTTON)

    def get_registration_link(self):
        return self.driver.find_element(*BasePageLocators.REGISTRATION_LINK)

    def get_catalog_button(self):
        return self.driver.find_element(*BasePageLocators.CATALOG_BUTTON)

    def get_float_section(self):
        return self.driver.find_element(*BasePageLocators.FLOAT_SECTION)

    def get_float_rods_section(self):
        return self.driver.find_element(*BasePageLocators.FLOAT_RODS_SECTION)

    def get_match_rods_section(self):
        return self.driver.find_element(*BasePageLocators.MATCH_RODS_SECTION)

    def get_match_rods_section_title(self):
        return self.driver.find_element(*BasePageLocators.MATCH_RODS_SECTION_TITLE).text

    def get_cart_dropdown(self):
        return self.driver.find_element(*BasePageLocators.CART_DROPDOWN)

    def get_checkout_button(self):
        return self.driver.find_element(*BasePageLocators.CHECKOUT_BUTTON)

    # Действия

    def click_login_button(self):
        """Кликнуть на кнопку входа в ЛК в шапке сайта"""
        return self.get_login_button().click()

    def click_registration(self):
        """Кликнуть на ссылку регистрации в поп апе входа в ЛК"""
        return self.get_registration_link().click()

    def open_catalog_in_header(self):
        """Открыть каталог в шапке"""
        return self.get_catalog_button().click()

    def go_to_match_rods_section(self):
        """Перейти в раздел с матчевыми удилищами"""
        action = ActionChains(self.driver)
        action.move_to_element(self.get_float_section()).perform()
        action.move_to_element(self.get_float_rods_section()).perform()
        self.get_match_rods_section().click()
        assert self.get_match_rods_section_title() == "Матчевые удилища", "Неудачный переход в раздел"

    def go_to_checkout(self):
        """Перейти к оформлению"""
        self.get_cart_dropdown().click()
        self.get_checkout_button().click()
