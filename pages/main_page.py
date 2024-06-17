import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.data_tests import ProjectPaths
from base.locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    # Getters
    def get_big_slider_first_item(self):
        return WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.BIG_SLIDER_FIRST_ITEM))

    def get_big_slider_second_item(self):
        return WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.BIG_SLIDER_SECOND_ITEM))

    def get_big_slider_next_button(self):
        return self.driver.find_element(*MainPageLocators.BIG_SLIDER_NEXT_BUTTON)

    def get_big_slider_prev_button(self):
        return self.driver.find_element(*MainPageLocators.BIG_SLIDER_PREV_BUTTON)

    def get_small_slider_first_item(self):
        return WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.SMALL_SLIDER_FIRST_ITEM))

    def get_small_slider_second_item(self):
        return WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.SMALL_SLIDER_SECOND_ITEM))

    def get_small_slider_next_button(self):
        return self.driver.find_element(*MainPageLocators.SMALL_SLIDER_NEXT_BUTTON)

    def get_small_slider_prev_button(self):
        return self.driver.find_element(*MainPageLocators.SMALL_SLIDER_PREV_BUTTON)

    # Actions and Methods

    @allure.step("В большом слайдере отображается первый элемент")
    def check_visibility_of_big_slider_first_item(self):
        """Проверить видимость 1 элемента в большом слайдере"""
        self.get_big_slider_first_item().is_displayed()

    @allure.step("В большом слайдере отображается второй элемент")
    def check_visibility_of_big_slider_second_item(self):
        """Проверить видимость 2 элемента в большом слайдере"""
        self.get_big_slider_second_item().is_displayed()

    @allure.step("Пролистать большой слайдер вправо")
    def click_big_slider_next_button(self):
        """Пролистать вправо большой слайдер"""
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_big_slider_next_button()).perform()
        self.get_big_slider_next_button().click()

    @allure.step("Пролистать большой слайдер влево")
    def click_big_slider_prev_button(self):
        """Пролистать влево большой слайдер"""
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_big_slider_prev_button()).perform()
        self.get_big_slider_prev_button().click()

    @allure.step("В маленьком слайдере отображается первый элемент")
    def check_visibility_of_small_slider_first_item(self):
        """Проверить видимость 1 элемента в маленьком слайдере"""
        self.get_small_slider_first_item().is_displayed()
        BasePage.take_screenshot(self, ProjectPaths.screens_path, action_name="SmallSlider1item-OK")

    @allure.step("В маленьком слайдере отображается второй элемент")
    def check_visibility_of_small_slider_second_item(self):
        """Проверить видимость 2 элемента в маленьком слайдере"""
        self.get_small_slider_second_item().is_displayed()

    @allure.step("Пролистать маленький слайдер вправо")
    def click_small_slider_next_button(self):
        """Пролистать вправо маленький слайдер"""
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_small_slider_next_button()).perform()
        self.get_small_slider_next_button().click()

    @allure.step("Пролистать маленький слайдер влево")
    def click_small_slider_prev_button(self):
        """Пролистать влево маленький слайдер"""
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_small_slider_prev_button()).perform()
        self.get_small_slider_prev_button().click()
