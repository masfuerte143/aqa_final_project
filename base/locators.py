from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_BUTTON = (By.XPATH, "(//button[@data-toggle='dropdown'])[2]")
    REGISTRATION_LINK = (By.XPATH, "//a[@class='btn-register']")
    CATALOG_BUTTON = (By.XPATH, "(//div[@class='container']//button)[7]")
    FLOAT_SECTION = (By.XPATH, "//ul[@id='menu-vertical-list']/li[5]")
    FLOAT_RODS_SECTION = (By.LINK_TEXT, "Поплавочные удилища")
    MATCH_RODS_SECTION = (By.LINK_TEXT, "Матчевые удилища")
    MATCH_RODS_SECTION_TITLE = (By.XPATH, "//h1")
    CART_DROPDOWN = (By.XPATH, "//div[@id='cart']")
    CHECKOUT_BUTTON = (By.XPATH, "//a[@class='btn btn-shopping']")
    CHECKOUT_H1 = (By.XPATH, "//h1")


class CheckoutPageLocators():
    SHIP_FIRST_NAME = (By.XPATH, "//input[@id='shipping_address_firstname']")
    SHIP_LAST_NAME = (By.XPATH, "//input[@id='shipping_address_lastname']")
    SHIP_REGION = (By.XPATH, "(//option[@selected='selected'])[2]")
    SHIP_CITY = (By.XPATH, "//input[@id='shipping_address_city']")
    MSK_DELIVERY = (By.XPATH, "//input[@id='dostavkaplus.sh7']")
    FACT_PAY = (By.XPATH, "//input[@id='cod']")
    COMMENT_FIELD = (By.XPATH, "//textarea[@id='comment']")
    SUBMIT_ORDER_BUTTON = (By.XPATH, "//a[@id='simplecheckout_button_confirm']")


class MatchRodsPageLocators():
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
    CART_DROPDOWN = (By.XPATH, "//div[@id='cart']")
    PRICE_IN_BASKET = (By.XPATH, "(//td[@class='text-right'])[2]")


class RegistrationPageLocators():
    FIRST_NAME_FIELD = (By.XPATH, "//input[@id='register_firstname']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@id='register_lastname']")
    EMAIL_FIELD = (By.XPATH, "//input[@id='register_email']")
    PHONE_FIELD = (By.XPATH, "//input[@id='register_telephone']")
    PASS_FIELD = (By.XPATH, "//input[@id='register_password']")
    CONFIRM_PASS_FIELD = (By.XPATH, "//input[@id='register_confirm_password']")
    REGION_SELECTOR = (By.XPATH, "//select[@id='register_zone_id']")
    MOSCOW_IN_SELECTOR = (By.XPATH, "//option[@value='2761']")
    CITY_FIELD = (By.XPATH, "//input[@id='register_city']")
    NO_SUBCR_RADIO = (By.XPATH, "//input[@id='register_newsletter_1']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#simpleregister_button_confirm")