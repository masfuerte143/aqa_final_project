from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.locators import MatchRodsPageLocators
from pages.base_page import BasePage


class MatchRodsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    manufacturer_text = ""
    min_price = ""
    max_price = ""

    # Геттеры
    def get_slider_min(self):
        return self.driver.find_element(*MatchRodsPageLocators.SLIDER_MIN)

    def get_slider_max(self):
        return self.driver.find_element(*MatchRodsPageLocators.SLIDER_MAX)

    def get_manufacturer_checkbox(self):
        return self.driver.find_element(*MatchRodsPageLocators.MANUFACTURER_CHECKBOX)

    def get_manufacturer_checkbox_selected(self):
        return self.driver.find_element(*MatchRodsPageLocators.MANUFACTURER_CHECKBOX_SELECTED).get_attribute('class')

    def get_presence_true_radio(self):
        return self.driver.find_element(*MatchRodsPageLocators.PRESENCE_TRUE_RADIO)

    def get_presence_true_radio_selected(self):
        return self.driver.find_element(*MatchRodsPageLocators.PRESENCE_TRUE_RADIO_SELECTED).get_attribute('class')

    def get_expand_button(self):
        return self.driver.find_element(*MatchRodsPageLocators.EXPAND_BUTTON)

    def get_match_rods_checkbox(self):
        return WebDriverWait(self.driver, 60).until(
            expected_conditions.element_to_be_clickable(MatchRodsPageLocators.MATCH_RODS_CHECKBOX))

    def get_match_rods_checkbox_selected(self):
        return self.driver.find_element(*MatchRodsPageLocators.MATCH_RODS_CHECKBOX_SELECTED).get_attribute('class')

    def get_submit_search_button(self):
        return WebDriverWait(self.driver, 60).until(
            expected_conditions.element_to_be_clickable(MatchRodsPageLocators.SUBMIT_SEARCH_BUTTON))

    def get_manufacturer_title_after_search(self):
        return self.driver.find_element(*MatchRodsPageLocators.MANUFACTURER_TITLE_AFTER_SEARCH).text

    def get_price_after_search(self):
        return self.driver.find_element(*MatchRodsPageLocators.PRICE_AFTER_SEARCH).text

    def get_presence_after_search(self):
        return self.driver.find_element(*MatchRodsPageLocators.PRESENCE_AFTER_SEARCH).text

    def get_type_rods_after_search(self):
        return self.driver.find_element(*MatchRodsPageLocators.RODS_TYPE_AFTER_SEARCH).text

    def get_first_rods_add_button(self):
        return self.driver.find_element(*MatchRodsPageLocators.FIRST_SEARCH_RESULT_ADD_BUTTON)

    def get_first_rods_price(self):
        return self.driver.find_element(*MatchRodsPageLocators.FIRST_SEARCH_RESULT_PRICE).text

    def get_continue_shopping_button(self):
        return WebDriverWait(self.driver, 60).until(
            expected_conditions.element_to_be_clickable(MatchRodsPageLocators.CONTINUE_BUTTON))

    def get_rods_price_in_basket(self):
        return self.driver.find_element(*MatchRodsPageLocators.PRICE_IN_BASKET).text

    # Действия
    def choose_price(self):
        """Сдвинуть ползунки селектора цены + проверка"""
        global min_price, max_price
        action = ActionChains(self.driver)
        location_before_interaction_slider_min = self.get_slider_min().location
        location_before_interaction_slider_max = self.get_slider_max().location
        action.click_and_hold(self.get_slider_min()).move_by_offset(15, 0).release().perform()
        action.click_and_hold(self.get_slider_max()).move_by_offset(-40, 0).release().perform()
        location_after_interaction_slider_min = self.get_slider_min().location
        location_after_interaction_slider_max = self.get_slider_max().location
        min_price = self.driver.find_element(By.XPATH, "//input[@name='ocf[2-0-1][min]']").get_attribute('value')
        max_price = self.driver.find_element(By.XPATH, "//input[@name='ocf[2-0-1][max]']").get_attribute('value')
        assert location_before_interaction_slider_min != location_after_interaction_slider_min, \
            "Левый ползунок не изменил положение"
        assert location_before_interaction_slider_max != location_after_interaction_slider_max, \
            "Правый ползунок не изменил положение"
        return min_price, max_price

    def choose_manufacturer(self):
        """Выбрать производителя и проверить, что чебокс проставился"""
        global manufacturer_text
        manufacturer_text = self.get_manufacturer_checkbox().text
        self.get_manufacturer_checkbox().click()
        assert "ocf-selected" in self.get_manufacturer_checkbox_selected(), "Чекбокс производителя не проставился"
        return manufacturer_text

    def choose_presence_true(self):
        """Отфильтровать по наличию"""
        self.get_presence_true_radio().click()
        assert "ocf-selected" in self.get_presence_true_radio_selected(), "В наличии не выбрано"

    def expand_hidden_filters(self):
        """Развернуть скрытые фильтры"""
        self.driver.execute_script('window.scroll(0,700)')
        self.get_expand_button().click()

    def choose_rods(self):
        """Выбрать тип удилища и проверить, что чебокс проставился"""
        self.driver.execute_script('window.scroll(0,2500)')
        self.get_match_rods_checkbox().click()
        assert "ocf-selected" in self.get_match_rods_checkbox_selected(), "Чекбокс типа удилища не проставился"

    def click_pop_up_submit_search(self):
        """Нажать кнопку Показать N, появляющуюся при проставлении параметров поиска"""
        self.get_submit_search_button().click()

    def check_submitting_filters(self):
        """Проверить, что фильтры применились"""
        assert self.get_manufacturer_title_after_search() == manufacturer_text, \
            "Неправильный или отсутствующий производитель"
        assert self.get_presence_after_search() == "Есть в наличии"
        assert self.get_price_after_search() == f"от {min_price} до {max_price} р.", "Неправильная цена"
        assert self.get_type_rods_after_search() == "Матчевое", "Неправильный тип удилища"

    def add_rods_in_basket(self):
        """Добавить товар в корзину"""
        self.get_first_rods_add_button().click()
        self.get_continue_shopping_button().click()
        BasePage.get_cart_dropdown(self).click()
        assert self.get_first_rods_price() == self.get_rods_price_in_basket(), "Товар не добавился"
        self.driver.refresh()
