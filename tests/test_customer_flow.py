from selenium import webdriver

from base.data_tests import Links
from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage
from pages.match_rods_page import MatchRodsPage
from pages.registration_page import RegistrationPage
from tests.contest import setup


def test_customer_flow(setup):
    setup.get(Links.base_url)
    base_page = BasePage(setup)
    registration_page = RegistrationPage(setup)
    match_rods_page = MatchRodsPage(setup)
    checkout_page = CheckoutPage(setup)
    registration_page.click_login_button()  # Регистрируемся
    registration_page.click_registration()
    registration_page.fill_required_fields()
    registration_page.click_registration_button()
    registration_page.check_registration_successful()
    base_page.open_catalog_in_header()  # Переходим из шапки в раздел с товарами
    base_page.go_to_match_rods_section()
    match_rods_page.choose_price()  # Дергаем фильтры
    match_rods_page.choose_manufacturer()
    match_rods_page.choose_presence_true()
    match_rods_page.expand_hidden_filters()
    match_rods_page.choose_rods()
    match_rods_page.click_pop_up_submit_search()
    match_rods_page.check_submitting_filters()
    match_rods_page.add_rods_in_basket()  # Добавляем в корзину
    base_page.go_to_checkout()  # Переходим к оформлению
    checkout_page.checkout_assertion()
    checkout_page.check_correct_user_info()  # Сверяем информацию
    checkout_page.change_delivery()  # Выбираем способ доставки
    checkout_page.change_payment()  # Выбираем способ оплаты
    checkout_page.input_comment()  # Пишем коммент
    # checkout_page.submit_order() # Подтверждаем заказ
