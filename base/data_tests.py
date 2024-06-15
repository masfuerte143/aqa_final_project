import os


class Links:
    """Ссылки"""
    base_url = "https://f-fishing.ru/"


class DataTests:
    """Тестовые данные"""
    first_name = "Евгений"
    last_name = "Марков"
    email = "masfuerte666@mail.ru"
    password = "HYH$9$pki~nC"
    phone = "+79161886677"
    region = "Москва"
    city = "Москва"
    search_ask = "Катушка Shimano"
    search_result = "SHIMANO"


class ProjectPaths:
    """Пути"""
    current_dir = os.path.dirname(__file__)
    screens_path = os.path.join(current_dir, "screens")
