import random

from faker import Faker
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from transliterate import translit


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    # Тестовые данные
    fake = Faker("ru_RU")
    first_name = fake.first_name_male()
    last_name = fake.last_name_male()
    email = translit(first_name, "ru", reversed=True) + "_" + translit(last_name, "ru",
                                                                       reversed=True) + "@mail.ru"
    password = "HYH$9$pki~nC"
    phone = "+7916" + str(random.randint(143561, 9999999))
    city_text = "Москва"

    # Геттеры

    def get_login_button(self):
        return self.driver.find_element(By.XPATH, "(//button[@data-toggle='dropdown'])[2]")

    def get_registration_link(self):
        return self.driver.find_element(By.XPATH, "//a[@class='btn-register']")

    def get_catalog_button(self):
        return self.driver.find_element(By.XPATH, "(//div[@class='container']//button)[7]")

    def get_float_section(self):
        return self.driver.find_element(By.XPATH, "//ul[@id='menu-vertical-list']/li[5]")

    def get_float_rods_section(self):
        return self.driver.find_element(By.LINK_TEXT, "Поплавочные удилища")

    def get_match_rods_section(self):
        return self.driver.find_element(By.LINK_TEXT, "Матчевые удилища")

    def get_match_rods_section_title(self):
        return self.driver.find_element(By.XPATH, "//h1").text

    def get_cart_dropdown(self):
        return self.driver.find_element(By.XPATH, "//div[@id='cart']")

    def get_checkout_button(self):
        return self.driver.find_element(By.XPATH, "//a[@class='btn btn-shopping']")

    def get_checkout_h1(self):
        return self.driver.find_element(By.XPATH, "//h1").text

    # Действия

    def click_login_button(self):
        """Кликнуть на кнопку входа в ЛК в шапке сайта"""
        return self.get_login_button().click()

    def click_registration(self):
        """Кликнуть на ссылку регистрации в поп апе входа в ЛК"""
        return self.get_registration_link().click()

    def open_catalog_in_header(self):
        """Открыть каталог в шапке"""
        return self.get_catalog_button().click()

    def go_to_match_rods_section(self):
        """Перейти в раздел с матчевыми удилищами"""
        action = ActionChains(self.driver)
        action.move_to_element(self.get_float_section()).perform()
        action.move_to_element(self.get_float_rods_section()).perform()
        self.get_match_rods_section().click()
        assert self.get_match_rods_section_title() == "Матчевые удилища", "Неудачный переход в раздел"

    def go_to_checkout(self):
        """Перейти к оформлению"""
        self.get_cart_dropdown().click()
        self.get_checkout_button().click()
        assert self.get_checkout_h1() == "Оформление заказа", "Неудачный переход"
