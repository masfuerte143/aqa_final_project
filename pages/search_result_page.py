import allure

from base.data_tests import DataTests, ProjectPaths
from base.locators import SearchResultPageLocators
from pages.base_page import BasePage


class SearchResultPage(BasePage):
    # Getters
    def get_first_result_title(self):
        return self.driver.find_element(*SearchResultPageLocators.FIRST_RESULT_TITLE)

    # Actions and Methods
    @allure.step("В результатах поиска первый товар - Катушка Shimano")
    def assertion_search_result(self):
        """Проверка результата поиска"""
        BasePage.take_screenshot(self, ProjectPaths.screens_path, action_name="SearchDone")
        assert DataTests.search_result in self.get_first_result_title().text, "Неудовлетворительный поиск!"
