from selenium.webdriver.common.by import By


class BasePageLocators:
    """Локаторы BasePage"""
    LOGIN_BUTTON = (By.XPATH, "(//button[@data-toggle='dropdown'])[2]")
    LOGIN_LINK = (By.XPATH, "//a[@id='login-popup']")
    CATALOG_BUTTON = (By.XPATH, "(//div[@class='container']//button)[7]")
    FLOAT_SECTION = (By.XPATH, "//ul[@id='menu-vertical-list']/li[5]")
    FLOAT_RODS_SECTION = (By.LINK_TEXT, "Поплавочные удилища")
    MATCH_RODS_SECTION = (By.LINK_TEXT, "Матчевые удилища")
    MATCH_RODS_SECTION_TITLE = (By.XPATH, "//h1")
    CART_DROPDOWN = (By.XPATH, "//div[@id='cart']")
    CHECKOUT_BUTTON = (By.XPATH, "//a[@class='btn btn-shopping']")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(text(),'Выход')]")
    SEARCH_FIELD = (By.XPATH, "//input[@name='search']")
    SEARCH_BUTTON = (By.XPATH, "//button[@class='btn btn-search']")
    FOOTER_PROMO_TEXT_1 = (By.XPATH, "//div[contains(text(),'Хотите быть в курсе всех акций и скидок?')]")
    FOOTER_PROMO_TEXT_2 = (By.XPATH, "//div[contains(text(),'Подпишитесь на нашу рассылку')]")
    WORK_TIME_TEXT = (By.XPATH, "//li[contains(text(), '10:00-19:00 Пн.-Вс')]")
    WITHOUT_HOLIDAYS_TEXT = (By.XPATH, "//li[contains(text(), 'Без выходных!')]")
    COPYRIGHT = (By.XPATH, "//div[@class='col-sm-12']/p")


class CheckoutPageLocators:
    """Локаторы CheckoutPage"""
    CHECKOUT_H1 = (By.XPATH, "//h1")
    SHIP_FIRST_NAME = (By.XPATH, "//input[@id='shipping_address_firstname']")
    SHIP_LAST_NAME = (By.XPATH, "//input[@id='shipping_address_lastname']")
    SHIP_REGION = (By.XPATH, "(//option[@selected='selected'])[2]")
    SHIP_CITY = (By.XPATH, "//input[@id='shipping_address_city']")
    MSK_DELIVERY = (By.XPATH, "//input[@id='dostavkaplus.sh7']")
    FACT_PAY = (By.XPATH, "//input[@id='cod']")
    COMMENT_FIELD = (By.XPATH, "//textarea[@id='comment']")
    SUBMIT_ORDER_BUTTON = (By.XPATH, "//a[@id='simplecheckout_button_confirm']")
    SHIP_ADDRESS = (By.XPATH, "//input[@id='shipping_address_address_1']")


class MatchRodsPageLocators:
    """Локаторы MatchRodsPage"""
    SLIDER_MIN = (By.XPATH, "(//div[@role='slider'])[1]")
    SLIDER_MAX = (By.XPATH, "(//div[@role='slider'])[2]")
    MANUFACTURER_CHECKBOX = (By.XPATH, "//span[contains(text(), 'Flagman')]")
    MANUFACTURER_CHECKBOX_SELECTED = (By.XPATH, "//button[@data-value-id='36']")
    PRESENCE_TRUE_RADIO = (By.XPATH, "//span[contains(text(), 'Есть в наличии')]")
    PRESENCE_TRUE_RADIO_SELECTED = (By.XPATH, "//button[@id='ocf-v-3-0-2-1']")
    EXPAND_BUTTON = (By.XPATH, "//span[contains(text(), 'Показать еще 14 фильтров ')]")
    MATCH_RODS_CHECKBOX = (By.XPATH, "//span[contains(text(), 'Матчевое')]")
    MATCH_RODS_CHECKBOX_SELECTED = (By.XPATH, "//button[@id='ocf-v-3-0-2-1']")
    SUBMIT_SEARCH_BUTTON = (By.XPATH, "(//button[contains(text(), 'Показать')])[2]")
    MANUFACTURER_TITLE_AFTER_SEARCH = (By.XPATH, "(//div[@class='ocf-selected-card ocf-desktop']//button)[1]/span")
    PRICE_AFTER_SEARCH = (By.XPATH, "(//div[@class='ocf-selected-card ocf-desktop']//button)[2]/span")
    PRESENCE_AFTER_SEARCH = (By.XPATH, "(//div[@class='ocf-selected-card ocf-desktop']//button)[3]/span")
    RODS_TYPE_AFTER_SEARCH = (By.XPATH, "(//div[@class='ocf-selected-card ocf-desktop']//button)[4]/span")
    FIRST_SEARCH_RESULT_ADD_BUTTON = (By.XPATH, "(//div[@class='cart']/button)[1]")
    FIRST_SEARCH_RESULT_PRICE = (By.XPATH, "(//div[@class='price'])[1]")
    CONTINUE_BUTTON = (By.XPATH, "//button[@class='btn-shopping']")
    PRICE_IN_BASKET = (By.XPATH, "(//td[@class='text-right'])[2]")


class LoginPageLocators:
    """Локаторы LoginPage"""
    EMAIL_FIELD = (By.XPATH, "//input[@id='input-email-popup']")
    PASS_FIELD = (By.XPATH, "//input[@id='input-password-popup']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='button-login-popup']")


class SearchResultPageLocators:
    """Локаторы SearchResultPage"""
    FIRST_RESULT_TITLE = (By.XPATH, "(//div[@class='product-name'])[1]")


class MainPageLocators:
    """Локаторы MainPage"""
    BIG_SLIDER_FIRST_ITEM = (By.XPATH, "//div[@id='slick-slide00']")
    BIG_SLIDER_SECOND_ITEM = (By.XPATH, "//div[@id='slick-slide01']")
    BIG_SLIDER_NEXT_BUTTON = (By.XPATH, "(//div[contains(@class,'next-prod')])[1]")
    BIG_SLIDER_PREV_BUTTON = (By.XPATH, "(//div[contains(@class,'prev-prod')])[1]")
    SMALL_SLIDER_FIRST_ITEM = (By.XPATH, "//div[@id='slick-slide10']")
    SMALL_SLIDER_SECOND_ITEM = (By.XPATH, "//div[@id='slick-slide11']")
    SMALL_SLIDER_NEXT_BUTTON = (By.XPATH, "(//div[contains(@class,'next-prod')])[2]")
    SMALL_SLIDER_PREV_BUTTON = (By.XPATH, "(//div[contains(@class,'prev-prod')])[2]")
