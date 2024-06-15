from base.data_tests import Links
from pages.base_page import BasePage
from pages.search_result_page import SearchResultPage
from tests.contest import setup


def test_search_in_header(setup):
    """Тестирование поиска"""
    setup.get(Links.base_url)
    base_page = BasePage(setup)
    search_page = SearchResultPage(setup)
    base_page.do_search()
    search_page.assertion_search_result()


def test_footer_static_text(setup):
    """Проверка статического текста в подвале"""
    setup.get(Links.base_url)
    base_page = BasePage(setup)
    base_page.check_footer_promo_text()
    base_page.check_footer_work_times()
    base_page.check_footer_copyright()

