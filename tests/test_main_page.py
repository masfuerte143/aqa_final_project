import pytest

from base.data_tests import Links
from pages.main_page import MainPage
from tests.contest import setup


@pytest.mark.regress
def test_big_slider(setup):
    """Протестировать большой слайдер"""
    setup.get(Links.base_url)
    main_page = MainPage(setup)
    main_page.check_visibility_of_big_slider_first_item()
    main_page.click_big_slider_next_button()
    main_page.check_visibility_of_big_slider_second_item()
    main_page.click_big_slider_prev_button()
    main_page.check_visibility_of_big_slider_first_item()


@pytest.mark.regress
def test_small_slider(setup):
    """Протестировать маленький слайдер"""
    setup.get(Links.base_url)
    main_page = MainPage(setup)
    main_page.check_visibility_of_small_slider_first_item()
    main_page.click_small_slider_next_button()
    main_page.check_visibility_of_small_slider_second_item()
    main_page.click_small_slider_prev_button()
    main_page.check_visibility_of_small_slider_first_item()
