import allure
import pytest

from base.data_tests import Links
from pages.base_page import BasePage
from pages.search_result_page import SearchResultPage
from tests.contest import setup


@pytest.mark.smoke
@allure.parent_suite("Smoke")
@allure.suite("Поиск")
@allure.title("Поиск выполняется")
def test_search_in_header(setup):
    """Протестировать поиск"""
    setup.get(Links.base_url)
    base_page = BasePage(setup)
    search_page = SearchResultPage(setup)
    base_page.do_search()
    search_page.assertion_search_result()


@pytest.mark.smoke
@allure.parent_suite("Smoke")
@allure.suite("Подвал")
@allure.title("Статичный текст в подвале присутствует")
def test_footer_static_text(setup):
    """Протестировать Статичный текст в подвале"""
    setup.get(Links.base_url)
    base_page = BasePage(setup)
    base_page.check_footer_promo_text()
    base_page.check_footer_work_times()
    base_page.check_footer_copyright()
