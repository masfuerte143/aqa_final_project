import random

from faker import Faker
from transliterate import translit


class Links():
    """Ссылки"""
    base_url = "https://f-fishing.ru/"


class DataTests():
    """Тестовые данные"""
    fake = Faker("ru_RU")
    first_name = fake.first_name_male()
    last_name = fake.last_name_male()
    email = translit(first_name, "ru", reversed=True) + "_" + translit(last_name, "ru",
                                                                       reversed=True) + "@mail.ru"
    password = "HYH$9$pki~nC"
    phone = "+7916" + str(random.randint(143561, 9999999))
    city_text = "Москва"


class ProjectPaths():
    registration_screens_path = "C:\\Users\\MasFuerte\\PycharmProjects\\aqa_final_project\\screens\\registaration_screens\\"
    other_screens_path = "C:\\Users\\MasFuerte\\PycharmProjects\\aqa_final_project\\screens\\"
