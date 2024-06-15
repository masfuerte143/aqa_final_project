import datetime

from selenium.webdriver import ActionChains

from base.data_tests import ProjectPaths, DataTests
from base.locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Getters

    def get_login_button(self):
        return self.driver.find_element(*BasePageLocators.LOGIN_BUTTON)

    def get_login_link(self):
        return self.driver.find_element(*BasePageLocators.LOGIN_LINK)

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

    def get_logout_button(self):
        return self.driver.find_element(*BasePageLocators.LOGOUT_BUTTON)

    def get_search_filed(self):
        return self.driver.find_element(*BasePageLocators.SEARCH_FIELD)

    def get_search_button(self):
        return self.driver.find_element(*BasePageLocators.SEARCH_BUTTON)

    # Actions and Methods

    def click_login_button(self):
        """Нажать на Личный кабинет в шапке"""
        return self.get_login_button().click()

    def click_log_in(self):
        """Нажать Вход в дропдауне"""
        return self.get_login_link().click()

    def open_catalog_in_header(self):
        """Развернуть каталог в шапке"""
        return self.get_catalog_button().click()

    def fill_search_filed(self):
        return self.get_search_filed().send_keys(DataTests.search_ask)

    def click_search_button(self):
        return self.get_search_button().click()

    def go_to_match_rods_section(self):
        """Выбрать раздел матчевых удилищ в каталоге"""
        action = ActionChains(self.driver)
        action.move_to_element(self.get_float_section()).perform()
        action.move_to_element(self.get_float_rods_section()).perform()
        self.get_match_rods_section().click()
        assert self.get_match_rods_section_title() == "Матчевые удилища", "Неудачный переход в раздел"

    def go_to_checkout(self):
        """Перейти к оформлению"""
        self.get_cart_dropdown().click()
        self.get_checkout_button().click()

    def open_match_rods(self):
        """Перейти в раздел матчевых удилищ"""
        self.open_catalog_in_header()
        self.go_to_match_rods_section()
        BasePage.take_screenshot(self, ProjectPaths.screens_path, action_name="MatchRodsOpened")

    def take_screenshot(self, path, action_name):
        """Метод для создания скриншота"""
        screen_name = f"Screenshot_{action_name}_{datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")}.png"
        self.driver.save_screenshot(path + screen_name)

    def go_to_login(self):
        """Перейти на страницу входа"""
        self.click_login_button()
        self.click_log_in()

    def check_login_successfully(self):
        """Проверить, что вход выполнен удачно"""
        self.click_login_button()
        self.get_logout_button()

    def do_search(self):
        """Выполнить поиск"""
        self.fill_search_filed()
        self.click_search_button()
