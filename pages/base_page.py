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

    def get_promo_text_in_footer_1(self):
        return self.driver.find_element(*BasePageLocators.FOOTER_PROMO_TEXT_1)

    def get_promo_text_in_footer_2(self):
        return self.driver.find_element(*BasePageLocators.FOOTER_PROMO_TEXT_2)

    def get_work_time(self):
        return self.driver.find_element(*BasePageLocators.WORK_TIME_TEXT)

    def get_without_holidays(self):
        return self.driver.find_element(*BasePageLocators.WITHOUT_HOLIDAYS_TEXT)

    def get_footer_copyright(self):
        return self.driver.find_element(*BasePageLocators.COPYRIGHT)

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

    def assertion_footer_promo_text_1(self):
        """Сравнить первую строку промо"""
        assert self.get_promo_text_in_footer_1().text == "Хотите быть в курсе всех акций и скидок?", "Первая строка промо отсутствует или не совпадет"

    def assertion_footer_promo_text_2(self):
        """Сравнить вторую строку промо"""
        assert self.get_promo_text_in_footer_2().text == "Подпишитесь на нашу рассылку", "Вторая строка промо отсутствует или не совпадет"

    def check_footer_promo_text(self):
        """Проверить текст промо в подвале"""
        self.assertion_footer_promo_text_1()
        self.assertion_footer_promo_text_2()

    def assertion_footer_work_times_text(self):
        """Проверить часы работы"""
        assert self.get_work_time().text == "10:00-19:00 Пн.-Вс.", "Часы работы отсутствуют или не совпадют"

    def assertion_footer_holidays_text(self):
        """Проверить текст Без выходных"""
        assert self.get_without_holidays().text == "Без выходных!", "Текст отсутствует или не совпадет"

    def check_footer_work_times(self):
        """Проверить весь блок Часы работы"""
        self.assertion_footer_work_times_text()
        self.assertion_footer_holidays_text()

    def check_footer_copyright(self):
        """Проверить копирайт в подвале"""
        self.get_footer_copyright()
        assert self.get_footer_copyright().text == "F-fishing.ru © 2024", "Копирайт отсутствует или не совпадет"
