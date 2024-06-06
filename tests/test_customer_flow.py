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
    registration_page.registration()
    base_page.open_match_rods()
    match_rods_page.search_with_filters()
    match_rods_page.add_rods_in_basket()
    base_page.go_to_checkout()
    checkout_page.checkout_assertion()
    checkout_page.check_correct_user_info()
    checkout_page.change_delivery()
    checkout_page.change_payment()
    checkout_page.input_comment()
    checkout_page.submit_order()
