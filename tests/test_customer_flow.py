from base.data_tests import Links
from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage
from pages.match_rods_page import MatchRodsPage
from pages.registration_page import RegistrationPage
from tests.contest import setup


def test_customer_flow(setup):
    base_page = BasePage(setup)
    registration_page = RegistrationPage(setup)
    match_rods_page = MatchRodsPage(setup)
    checkout_page = CheckoutPage(setup)
    setup.get(Links.base_url)  # Открываем браузер
    registration_page.registration()  # Регистриуемся
    base_page.open_match_rods()  # Переходимв раздел с матчевыми удилищами
    match_rods_page.search_with_filters()  # Выполняем поиск, используя фильтры
    match_rods_page.add_rods_in_basket()  # Добавляем товар в корзину
    base_page.go_to_checkout()  # Открываем браузер
    checkout_page.check_correct_user_info()  # Проверяем информацию
    checkout_page.change_delivery()  # Меняем способ доставки
    checkout_page.change_payment()  # Меняем способ оплаты
    checkout_page.input_comment()  # Оставляем комментарий
    checkout_page.submit_order()  # Подтверждаем заказ
